# vllm-project/vllm#22987: [Usage]: How to suppress the 10 % output drift between speculative and non-speculative modes?

| 字段 | 值 |
| --- | --- |
| Issue | [#22987](https://github.com/vllm-project/vllm/issues/22987) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to suppress the 10 % output drift between speculative and non-speculative modes?

### Issue 正文摘录

### How would you like to use vllm vLLM version: 0.10.0 I launch the same fixed model twice: **Service A**: speculative decoding ON (custom logic inside ngram_proposer.py, plus utils.py patched so repetition_penalty ≠ 1 still enters the ngram path) **Service B**: speculative decoding OFF For the same request batch, about 10 % of the outputs differ, while two independent launches of A (or of B) stay within 1 %. **Call parameters (unchanged):** stream=False, temperature=0.1, top_p=0.1, repetition_penalty=1.05 I already tried adding "seed": 42 to every request, but the 10 % gap between A and B remains. What additional flags or code changes are required so that a fixed seed, model weights, and parameters yield ≤ 1 % drift between the two services? Thank you for your guidance. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to suppress the 10 % output drift between speculative and non-speculative modes? usage;stale ### How would you like to use vllm vLLM version: 0.10.0 I launch the same fixed model twice: **Service A**: specu...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Usage]: How to suppress the 10 % output drift between speculative and non-speculative modes? usage;stale ### How would you like to use vllm vLLM version: 0.10.0 I launch the same fixed model twice: **Service A**: specu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -speculative modes? usage;stale ### How would you like to use vllm vLLM version: 0.10.0 I launch the same fixed model twice: **Service A**: speculative decoding ON (custom logic inside ngram_proposer.py, plus utils.py p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: A (or of B) stay within 1 %. **Call parameters (unchanged):** stream=False, temperature=0.1, top_p=0.1, repetition_penalty=1.05 I already tried adding "seed": 42 to every request, but the 10 % gap between A and B remain...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
