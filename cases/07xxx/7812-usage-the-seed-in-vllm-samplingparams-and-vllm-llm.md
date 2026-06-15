# vllm-project/vllm#7812: [Usage]: The seed in vllm.SamplingParams and vllm.LLM

| 字段 | 值 |
| --- | --- |
| Issue | [#7812](https://github.com/vllm-project/vllm/issues/7812) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: The seed in vllm.SamplingParams and vllm.LLM

### Issue 正文摘录

### Your current environment vllm==0.4.0 ### How would you like to use vllm I notice that there are two seeds when using vllm. The first one is in `vllm.LLM`. https://docs.vllm.ai/en/latest/_modules/vllm/entrypoints/llm.html#LLM The second one is in `vllm.SamplingParams`. https://docs.vllm.ai/en/latest/_modules/vllm/sampling_params.html#SamplingParams I am wondering what are the differences between these two.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: using vllm. The first one is in `vllm.LLM`. https://docs.vllm.ai/en/latest/_modules/vllm/entrypoints/llm.html#LLM The second one is in `vllm.SamplingParams`. https://docs.vllm.ai/en/latest/_modules/vllm/sampling_params....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
