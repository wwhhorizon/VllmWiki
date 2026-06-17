# Bitwise 工作的验证契约

状态：curated。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。  
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
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | fused RoPE + KV cache write 增加 bit-identical tests，使用 `torch.testing.assert_close(..., rtol=0, atol=0)`；测试矩阵覆盖 cache dtype、MHA/GQA、NeoX layout、token count，并避免 duplicate slot mapping 的 last-write-wins nondeterminism。review comments 还指出 FP8 path 若把 `raw_kv_scalar_t` 当浮点转换会错误、FlashAttention HND layout 可能导致 silent memory corruption、key/value row 数缺少 guard。 | 性能 fusion 必须证明写入 KV 后仍 bit-identical；review comment 暴露的 dtype/layout/shape guard 是验证矩阵必须覆盖的边界。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | deterministic prefix caching e2e test 比较 cache miss 与 cache hit 输出。 | cache 状态变化必须被纳入测试矩阵。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | concurrent prefill determinism test 和 block table unit tests 共同覆盖 stale metadata。 | 并发 determinism 需要系统级和 metadata 单元测试。 |
| [#33123](https://github.com/vllm-project/vllm/issues/33123) | `temperature=0` 下 cache miss/hit 产生不同 token。 | token equality 可作为用户可见 correctness gate。 |

## 根因机制

验证契约错误会让 correctness bug 伪装成“可接受数值误差”。对于 cache identity、KV write、layer identity、metadata layout 这类语义对象，近似相等通常不够；对于 backend math drift，strict tolerance 可以作为中间证据，但还必须证明不会翻转 token 或破坏 logprob ranking。

## 修复方式

1. 先定义保护对象：tensor、KV block、metadata、logits、token、answer。
2. 再选择 equality contract：bit-identical、strict tolerance、token equality 或 semantic equivalence。
3. cache 类问题覆盖 cache miss、cache hit、cache bypass、offload/restore。
4. batch 类问题覆盖单请求、混 batch、并发 prefill/decode、first request 与 warmup 后。
5. backend 类问题记录硬件、dtype、backend、graph/capture 状态、kernel config。
6. fused KV write 类问题额外检查 dtype conversion 类型、KV cache layout、slot uniqueness、key/value tensor row 数 guard。

## 验证契约

| 层级 | 适用场景 | 合格证据 |
| --- | --- | --- |
| Bit-identical | KV cache、slot mapping、fused write、exact deterministic path | `torch.equal`、bit-view equality、`rtol=0, atol=0` |
| Strict numeric tolerance | backend math 允许微小误差但不得翻转 token | 显式 tolerance，并说明 dtype/backend/hardware |
| Logprob/token equality | decoding 可见行为必须稳定 | `temperature=0` 输出 token 相同，必要时检查 logprob ranking |
| Semantic equivalence | 非确定 sampling 或高层 eval | 不能作为 bitwise 修复的唯一证据 |

## 适用边界

- exact identity 不能被 `allclose` 替代，尤其是 cache/layer/KV identity。
- fused op 的验证要覆盖写入顺序和 slot mapping；duplicate slot 可能引入 last-write-wins nondeterminism。
- `#43355` 的 review comments 应写成 boundary/risk：它们说明测试矩阵还应覆盖 FP8 conversion、HND/NHD layout、key/value size guard，但不能在没有后续 patch 确认时直接写成最终修复结论。
- semantic answer match 只能作为补充，不支持 bitwise/deterministic claim。

## 仍需补证

- 将 `#29086/#43355/#40179/#39591` 抽成更明确的 verification matrix，并要求每条 curated claim 都声明自己的 equality contract。
- 后续 review ledger 时，对每条 `include` 检查是否已经写明保护对象和验证层级。
