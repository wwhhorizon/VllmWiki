# Bitwise 工作的验证契约

状态：reviewed seed page。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)

## 契约

bitwise/deterministic 修复必须写清验证标准。`allclose`、semantic answer match、logprob tolerance 和 bit-identical 是不同契约，不能混用。

## 验证层级

| 层级 | 适用场景 | 例子 |
| --- | --- | --- |
| Bit-identical | KV cache、slot mapping、fused write、exact deterministic path | `torch.equal`、`rtol=0, atol=0` |
| Strict numeric tolerance | backend math 允许微小误差但不得翻转 token | `assert_close` with explicit tolerance |
| Logprob/token equality | decoding 可见行为必须稳定 | `temperature=0` 输出 token 相同 |
| Semantic equivalence | 只适合非确定 sampling 或 high-level eval | 不应作为 bitwise 修复的唯一证据 |

## Curated Case

| Case | 验证意义 | 说明 |
| --- | --- | --- |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | fused RoPE + KV cache write 要求 bit-identical | test matrix 使用 `rtol=0, atol=0`，并约束 slot mapping |
| [#29086](https://github.com/vllm-project/vllm/pull/29086) | cache/layer identity 应使用 exact equality | relaxed `allclose` 可能接受语义不同的 cached artifact |
| [#33123](https://github.com/vllm-project/vllm/issues/33123) | cache miss/hit 输出不同 | deterministic prefix caching 必须比较首次请求与后续请求 |
| [#29521](https://github.com/vllm-project/vllm/issues/29521) | sequential vs concurrent beam search 输出 mismatch | candidate：需要 linked fix/test review |

## Fix Pattern

1. 先定义要保护的对象：tensor、KV block、logits、token、answer。
2. 再选择 equality contract：bit-identical、strict tolerance、token equality 或 semantic equivalence。
3. 对 cache 类问题，必须覆盖 cache miss、cache hit、cache bypass、offload/restore。
4. 对 batch 类问题，必须覆盖单请求、混 batch、并发 prefill/decode。
5. 对 backend 类问题，必须记录硬件、dtype、backend、graph/capture 状态。

## Open Review Queue

使用 [bitwise_review_queue.csv](../bitwise_review_queue.csv) 中 cluster 为 `verification_contract` 的行。
