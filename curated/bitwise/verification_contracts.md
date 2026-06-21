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
- decode/prefill 一致性测试用文本 roundtrip 重建 prefix，导致 token ids 改变。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#29086](https://github.com/vllm-project/vllm/pull/29086) | 将 `torch.allclose` revert 回 `torch.equal`，因为 draft/target model layer identity 不能用近似相等替代。 | cache/layer identity 必须 exact。 |
| [#33123](https://github.com/vllm-project/vllm/issues/33123) | `temperature=0` 下 cache miss/hit 产生不同 token。 | token equality 可作为用户可见 correctness gate。 |
| [#34874](https://github.com/vllm-project/vllm/pull/34874) | 新 regression test 不下载模型，而是构造两个共享同一 `MambaSpec` 的 metadata builder，断言 `update_block_table()` 返回的 block index tensor 指向当前 builder 的 persistent buffer，且值正确。issue 评论指出旧 tiny Bamba 测试只有单 Mamba layer，根本不会触发 metadata cache 复用。 | verification 要复现触发拓扑，而不只是覆盖 API happy path；metadata 指针身份可以用 storage sharing 断言。 |
| [#27660](https://github.com/vllm-project/vllm/pull/27660) | DeepSeek V3.1 + FlashAttention MLA 的 `test_logprobs_bitwise_batch_invariance_bs1_vs_bsN` 通过；PR body 还用多个 `max_model_len` 和 batch size 说明 Inductor reduction kernel thread layout 固定。 | compile path 的验证要同时记录模型、backend、batch/M 维矩阵、PyTorch/cuBLAS flags 和是否启用 AOT compile。 |

| [#44319](https://github.com/vllm-project/vllm/issues/44319), [#44504](https://github.com/vllm-project/vllm/pull/44504) | 用户报告请求不同数量的 top-k logprobs 时，同一 token 的 logprob 值会变化，甚至翻转 argmax。评论确认根因不是 sampling/count bug，而是 token-string collision：多个不同 token id 被渲染成同一个 string，导致 `top_logprobs` 返回的条目数少于请求数，且某个 token 的 logprob 看起来“变了”。纯 vLLM v0.22.0 + offline LLM API + `temperature=0` 下 per-token logprob 值实际稳定；行为变化可追溯到特定 PR。修复 PR `#44504` 改 `detokenizer_utils.py` 和 `test_detokenize.py`，但仍 open/unmerged。 | token id 到 string 的映射不是一对一的；多个 token id 可碰撞到同一 string，这会让 `top_logprobs` 的值看起来不稳定。验证 logprob equality 时必须按 token id 比较，而不是按 detokenized string 比较。 |

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
8. decode/prefill consistency 测试必须使用同一 token-id prefix；不能用 detokenized text 再交给 tokenizer 重编码来代表同一前缀。

## 验证契约

| 层级 | 适用场景 | 合格证据 |
| --- | --- | --- |
| Bit-identical | KV cache、slot mapping、fused write、exact deterministic path | `torch.equal`、bit-view equality、`rtol=0, atol=0` |
| Strict numeric tolerance | backend math 允许微小误差但不得翻转 token | 显式 tolerance，并说明 dtype/backend/hardware |
| Logprob/token equality | decoding 可见行为必须稳定 | `temperature=0` 输出 token 相同，必要时检查 logprob ranking |
| Metadata identity | CUDA graph persistent buffer、block table、slot mapping | storage/data pointer 指向当前生命周期对象，且逻辑值正确 |
| Token-prefix identity | decode/prefill consistency、logprob replay | `prompt_token_ids + decode_tokens[:i]` 级别相同，避免 `decode -> encode` roundtrip |
| Semantic equivalence | 非确定 sampling 或高层 eval | 不能作为 bitwise 修复的唯一证据 |

## 代表性 Verification Matrix

| Source | 保护对象 | 最小验证矩阵 | 合格契约 | 不能被什么替代 |
| --- | --- | --- | --- | --- |
| [#29086](https://github.com/vllm-project/vllm/pull/29086) | draft/target layer identity | 同一 layer、同一输入、patched/unpatched 对照；exact compare 与近似 compare 对照 | `torch.equal` / exact identity | `allclose` 或“最终回答差不多” |
| [#33123](https://github.com/vllm-project/vllm/issues/33123), [#40179](https://github.com/vllm-project/vllm/pull/40179) | prefix-cache token/logprob 等价 | no-prefix baseline、首次 cache miss、warmed cache hit、resumed request、block-aligned prompt、`fp32` 对照、`VLLM_BATCH_INVARIANT=1` 对照 | `temperature=0` token equality，必要时补 logprob ranking | 只测普通重复请求；只看 semantic output |
| [#39589](https://github.com/vllm-project/vllm/issues/39589), [#39591](https://github.com/vllm-project/vllm/pull/39591) | block-table tail / concurrent prefill KV identity | variable-length concurrent prefill、tail-zero invariant、patched/unpatched 对照、move-row correctness 对照 | token equality + metadata tail invariant | 只测 append slice；把 reviewer 的性能建议当 correctness 阻塞 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | fused RoPE + KV write correctness | layout gate、slot uniqueness、row-size guard、dtype conversion type、patched/unpatched kernel compare | fused write bit-identical 或严格数值契约 + token/logprob 不翻转 | 只凭 open PR 的 bitwise test 名称；忽略 remaining review risk |
| [#34878](https://github.com/vllm-project/vllm/pull/34878) | beam-search / ranking verification harness | ROCm-specific engine kwargs、prefix-cache on/off、skinny GEMM on/off、batch geometry 固定前后对照 | logprob ranking 稳定；beam choice 不被 `1e-5` 级 drift 翻转 | `semantic output same`；把 test-harness 固定外推成 production guarantee |

| [#44319](https://github.com/vllm-project/vllm/issues/44319), [#44504](https://github.com/vllm-project/vllm/pull/44504) | top_logprobs 的 token-id identity | 同一 prompt、同一 model、`temperature=0`、不同 `logprobs` 参数（4/10/20）、per-token-id logprob 值对照、token-string collision 检测、patched/unpatched detokenizer 对照 | 同一 token id 的 logprob 值不随请求的 top-k 数量变化 | 按 detokenized string 比较 logprob；把 token-string collision 误判为 logprob 数值漂移 |

## 适用边界

- exact identity 不能被 `allclose` 替代，尤其是 cache/layer/KV identity。
- fused op 的验证要覆盖写入顺序和 slot mapping；duplicate slot 可能引入 last-write-wins nondeterminism。
- `#43355` 的 review comments 应写成 boundary/risk，并且必须和当前 patch 对齐：HND/NHD layout gate 与 key/value size guard 已在 patch 中出现，但 FP8 `scaled_convert` 仍使用 `raw_kv_scalar_t`，所以该 PR 仍不能直接写成最终修复结论。该 PR 仍为 open/unmerged，且 2026-05-29 起多次出现 `needs-rebase`，作者在 2026-05-31、2026-06-12、2026-06-20 多次 force-push 清除后又复现，说明 patch 在持续演进但截至 2026-06-21 仍无 maintainer approval；`include` 只能覆盖“验证契约样例”，不能覆盖“landed fix”。
- `#34874` 的 test 证明了 Mamba `"all"` mode 多 cache group 下的 metadata pointer 修复，但不证明所有 Mamba prefix-cache 或 MTP/spec decode 场景都稳定。
- `#27660` 的 compile 测试证明特定模型/backend/flag 组合下 logprob batch-invariance 通过；不能把它扩展成所有 `torch.compile`、AOT compile 或所有 cuBLAS algorithm 都稳定。
- `#43317` 仍 open/unmerged，因此只能作为“现有测试可能误报”的边界记录；不进入代表证据，也不能写成 decode/prefill consistency test 已经修好。
- semantic answer match 只能作为补充，不支持 bitwise/deterministic claim。

## 仍需补证

- 继续追踪 `#43355` 是否出现 follow-up patch 或 maintainer resolution，尤其是 FP8 `qk_t` conversion。NHD layout gate 与 `key.size/value.size >= num_tokens` host guard 已在当前 patch 中出现，下一轮只需确认它们是否被 maintainer 接受或进入最终合并版本。
- 追踪 `#43317` 是否合并；若未合并，decode/prefill consistency 的失败应先检查 token-id prefix 是否被文本 roundtrip 改写。
- 后续 review ledger 时，对每条 `include` 检查是否已经写明保护对象和验证层级。
- 追踪 `#44504` 是否合并；该 PR 改 `detokenizer_utils.py` 处理 token-string collision，使 `top_logprobs` 不再因多个 token id 映射到同一 string 而丢失条目或让 logprob 值看起来变化。未合并前，logprob equality 验证应优先按 token id 比较，而不是按 detokenized string 比较。
