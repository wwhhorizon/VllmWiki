# Bitwise 工作的验证契约

状态：curated。  
父页：[Bitwise 确定性与数值等价](README.md)。
范围：bit-identical、strict tolerance、logprob/token equality、semantic equivalence 之间的验证边界。

## 问题定义

bitwise/deterministic 修复必须写清验证标准。`torch.equal`、bit-view equality、`allclose`、strict numeric tolerance、logprob/token equality 和 semantic answer match 是不同契约，不能混用。

## 典型触发条件

- 性能优化用 `allclose` 掩盖 cache/layer identity 问题。
- fused kernel 写入 KV cache 后没有 bit-identical test。
- cache miss/hit、concurrent prefill、batch-invariant mode 只测单一路径。
- semantic answer match 被误用为 bitwise/deterministic 证据。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#29086](https://github.com/vllm-project/vllm/pull/29086) | 将 `torch.allclose` revert 回 `torch.equal`，因为 draft/target model layer identity 不能用近似相等替代。 | cache/layer identity 必须 exact。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | fused RoPE + KV cache write 增加 bit-identical tests，使用 `torch.testing.assert_close(..., rtol=0, atol=0)`；测试矩阵覆盖 cache dtype、MHA/GQA、NeoX layout、token count，并避免 duplicate slot mapping 的 last-write-wins nondeterminism。深读 patch 后，HND/NHD layout gate 已出现在 `fused_rope_kvcache_supported()`，`key.size(0)` / `value.size(0)` host guard 也已出现在 wrapper；但 FP8 path 仍在 patch 中把 `raw_kv_scalar_t` 传给 `fp8::scaled_convert`。该 PR 仍为 open / unmerged，讨论里还有 merge conflict 提醒。 | 性能 fusion 的测试不能只证明 happy path bit-identical；review risk 要和 patch 对齐。当前可认为 layout gate 与 row guard 有 patch 迹象，但 FP8 conversion type 仍是阻塞风险，不能把该 PR 当作稳定修复证据。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | deterministic prefix caching e2e test 比较 cache miss 与 cache hit 输出。 | cache 状态变化必须被纳入测试矩阵。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | concurrent prefill determinism test 和 block table unit tests 共同覆盖 stale metadata。 | 并发 determinism 需要系统级和 metadata 单元测试。 |
| [#33123](https://github.com/vllm-project/vllm/issues/33123) | `temperature=0` 下 cache miss/hit 产生不同 token。 | token equality 可作为用户可见 correctness gate。 |
| [#34874](https://github.com/vllm-project/vllm/pull/34874) | 新 regression test 不下载模型，而是构造两个共享同一 `MambaSpec` 的 metadata builder，断言 `update_block_table()` 返回的 block index tensor 指向当前 builder 的 persistent buffer，且值正确。issue 评论指出旧 tiny Bamba 测试只有单 Mamba layer，根本不会触发 metadata cache 复用。 | verification 要复现触发拓扑，而不只是覆盖 API happy path；metadata 指针身份可以用 storage sharing 断言。 |
| [#27660](https://github.com/vllm-project/vllm/pull/27660) | DeepSeek V3.1 + FlashAttention MLA 的 `test_logprobs_bitwise_batch_invariance_bs1_vs_bsN` 通过；PR body 还用多个 `max_model_len` 和 batch size 说明 Inductor reduction kernel thread layout 固定。 | compile path 的验证要同时记录模型、backend、batch/M 维矩阵、PyTorch/cuBLAS flags 和是否启用 AOT compile。 |

## 根因机制

验证契约错误会让 correctness bug 伪装成“可接受数值误差”。对于 cache identity、KV write、layer identity、metadata layout 这类语义对象，近似相等通常不够；对于 backend math drift，strict tolerance 可以作为中间证据，但还必须证明不会翻转 token 或破坏 logprob ranking。

## 修复方式

1. 先定义保护对象：tensor、KV block、metadata、logits、token、answer。
2. 再选择 equality contract：bit-identical、strict tolerance、token equality 或 semantic equivalence。
3. cache 类问题覆盖 cache miss、cache hit、cache bypass、offload/restore。
4. batch 类问题覆盖单请求、混 batch、并发 prefill/decode、first request 与 warmup 后。
5. backend 类问题记录硬件、dtype、backend、graph/capture 状态、kernel config。
6. fused KV write 类问题额外检查 dtype conversion 类型、KV cache layout、slot uniqueness、key/value tensor row 数 guard；review comment 已经被 patch 覆盖的风险要降级为边界，仍留在 patch 中的问题才阻塞 promotion。
7. metadata cache 类问题要验证 tensor 指针/地址身份，而不是只比较值；CUDA graph replay 读的是 capture 时的 persistent buffer 地址。

## 验证契约

| 层级 | 适用场景 | 合格证据 |
| --- | --- | --- |
| Bit-identical | KV cache、slot mapping、fused write、exact deterministic path | `torch.equal`、bit-view equality、`rtol=0, atol=0` |
| Strict numeric tolerance | backend math 允许微小误差但不得翻转 token | 显式 tolerance，并说明 dtype/backend/hardware |
| Logprob/token equality | decoding 可见行为必须稳定 | `temperature=0` 输出 token 相同，必要时检查 logprob ranking |
| Metadata identity | CUDA graph persistent buffer、block table、slot mapping | storage/data pointer 指向当前生命周期对象，且逻辑值正确 |
| Semantic equivalence | 非确定 sampling 或高层 eval | 不能作为 bitwise 修复的唯一证据 |

## 适用边界

- exact identity 不能被 `allclose` 替代，尤其是 cache/layer/KV identity。
- fused op 的验证要覆盖写入顺序和 slot mapping；duplicate slot 可能引入 last-write-wins nondeterminism。
- `#43355` 的 review comments 应写成 boundary/risk，并且必须和当前 patch 对齐：HND/NHD layout gate 与 key/value size guard 已在 patch 中出现，但 FP8 `scaled_convert` 仍使用 `raw_kv_scalar_t`，所以该 PR 仍不能直接写成最终修复结论。由于该 PR 在本轮证据中仍为 open/unmerged 且有 merge conflict 提醒，`include` 只能覆盖“验证契约样例”，不能覆盖“landed fix”。
- `#34874` 的 test 证明了 Mamba `"all"` mode 多 cache group 下的 metadata pointer 修复，但不证明所有 Mamba prefix-cache 或 MTP/spec decode 场景都稳定。
- `#27660` 的 compile 测试证明特定模型/backend/flag 组合下 logprob batch-invariance 通过；不能把它扩展成所有 `torch.compile`、AOT compile 或所有 cuBLAS algorithm 都稳定。
- semantic answer match 只能作为补充，不支持 bitwise/deterministic claim。

## 仍需补证

- 将 `#29086/#43355/#40179/#39591` 抽成更明确的 verification matrix，并要求每条 curated claim 都声明自己的 equality contract。
- 继续追踪 `#43355` 是否出现 follow-up patch 或 maintainer resolution，尤其是 FP8 `qk_t` conversion。NHD layout gate 与 `key.size/value.size >= num_tokens` host guard 已在当前 patch 中出现，下一轮只需确认它们是否被 maintainer 接受或进入最终合并版本。
- 后续 review ledger 时，对每条 `include` 检查是否已经写明保护对象和验证层级。
