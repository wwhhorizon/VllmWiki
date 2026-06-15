# vllm-project/vllm#42260: [Tracking] Logprobs/Logits semantics stabilization across the vLLM ecosystem

| 字段 | 值 |
| --- | --- |
| Issue | [#42260](https://github.com/vllm-project/vllm/issues/42260) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking] Logprobs/Logits semantics stabilization across the vLLM ecosystem

### Issue 正文摘录

## Purpose Track execution of the RFC for logprobs/logits semantics and determinism across vLLM, vLLM-Ascend, and VERL. ## Main RFC - [#42259](https://github.com/vllm-project/vllm/issues/42259) ## Todo List ### vLLM - [ ] [#35832](https://github.com/vllm-project/vllm/issues/35832) / [#36539](https://github.com/vllm-project/vllm/pull/36539) - [ ] [#42019](https://github.com/vllm-project/vllm/issues/42019) / [#42245](https://github.com/vllm-project/vllm/pull/42245) - [ ] [#36660](https://github.com/vllm-project/vllm/issues/36660) / [#36746](https://github.com/vllm-project/vllm/pull/36746) ### vLLM-Ascend - [ ] [#7218](https://github.com/vllm-project/vllm-ascend/issues/7218) / [#8643](https://github.com/vllm-project/vllm-ascend/pull/8643) ### VERL - [ ] [#2996](https://github.com/verl-project/verl/issues/2996) - [ ] [#6240](https://github.com/verl-project/verl/issues/6240) - [ ] [#6280](https://github.com/verl-project/verl/issues/6280) ## Exit Criteria - Core semantic contract is explicit and documented. - Prompt-side and decode-side logprob values are mode-aware and deterministic. - `top_logprobs` never duplicates the sampled token. - vLLM-Ascend follows the same mode semantics. - V...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: umented. - Prompt-side and decode-side logprob values are mode-aware and deterministic. - `top_logprobs` never duplicates the sampled token. - vLLM-Ascend follows the same mode semantics. - VERL rollout/trainer logprob...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ct/verl/issues/6280) ## Exit Criteria - Core semantic contract is explicit and documented. - Prompt-side and decode-side logprob values are mode-aware and deterministic. - `top_logprobs` never duplicates the sampled tok...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e Track execution of the RFC for logprobs/logits semantics and determinism across vLLM, vLLM-Ascend, and VERL. ## Main RFC - [#42259](https://github.com/vllm-project/vllm/issues/42259) ## Todo List ### vLLM - [ ] [#3583...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: - Core semantic contract is explicit and documented. - Prompt-side and decode-side logprob values are mode-aware and deterministic. - `top_logprobs` never duplicates the sampled token. - vLLM-Ascend follows the same mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: umented. - Prompt-side and decode-side logprob values are mode-aware and deterministic. - `top_logprobs` never duplicates the sampled token. - vLLM-Ascend follows the same mode semantics. - VERL rollout/trainer logprob...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
