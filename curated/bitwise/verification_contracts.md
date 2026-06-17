# Bitwise 工作的验证契约

状态：curated。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。

## 契约

bitwise/deterministic 修复必须写清验证标准。`torch.equal`、bit-view equality、`allclose`、strict numeric tolerance、logprob/token equality 和 semantic answer match 是不同契约，不能混用。

## 验证层级

| 层级 | 适用场景 | 例子 |
| --- | --- | --- |
| Bit-identical | KV cache、slot mapping、fused write、exact deterministic path | `torch.equal`、`rtol=0, atol=0` |
| Strict numeric tolerance | backend math 允许微小误差但不得翻转 token | `assert_close` with explicit tolerance |
| Logprob/token equality | decoding 可见行为必须稳定 | `temperature=0` 输出 token 相同 |
| Semantic equivalence | 非确定 sampling 或高层 eval | 不应作为 bitwise 修复的唯一证据 |

## Source Evidence

| Source | 验证意义 | 炼化结论 |
| --- | --- | --- |
| [#29086](https://github.com/vllm-project/vllm/pull/29086) | 将 `torch.allclose` revert 回 `torch.equal`，因为 draft/target model layer identity 不能用近似相等替代。 | cache/layer identity 必须 exact。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | fused RoPE + KV cache write 增加 bit-identical tests，使用 `rtol=0, atol=0` 并约束 slot mapping。 | 性能 fusion 必须证明写入 KV 后仍 bit-identical。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | deterministic prefix caching e2e test 比较 cache miss 与 cache hit 输出。 | cache 状态变化必须被纳入测试矩阵。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | concurrent prefill determinism test 和 block table unit tests 共同覆盖 stale metadata。 | 并发 determinism 需要系统级和 metadata 单元测试。 |
| [#33123](https://github.com/vllm-project/vllm/issues/33123) | `temperature=0` 下 cache miss/hit 产生不同 token。 | token equality 可作为用户可见 correctness gate。 |

## Fix Pattern

1. 先定义保护对象：tensor、KV block、metadata、logits、token、answer。
2. 再选择 equality contract：bit-identical、strict tolerance、token equality 或 semantic equivalence。
3. cache 类问题必须覆盖 cache miss、cache hit、cache bypass、offload/restore。
4. batch 类问题必须覆盖单请求、混 batch、并发 prefill/decode、first request 与 warmup 后。
5. backend 类问题必须记录硬件、dtype、backend、graph/capture 状态、kernel config。

## Open Review Queue

下一轮把 `#29086/#43355/#40179/#39591` 抽成 verification matrix，要求每条 curated claim 都声明自己的 equality contract。
