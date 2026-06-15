# vllm-project/vllm#1108: No support for longer context lengths.

| 字段 | 值 |
| --- | --- |
| Issue | [#1108](https://github.com/vllm-project/vllm/issues/1108) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> No support for longer context lengths.

### Issue 正文摘录

Model: Llama-2-chat-hf The current implementation of vLLM gives the finish_reason as 'length' whilst the native model supports context length of 4024(And works well with the context we've tested it with) , Is the option available to change the native context length supported by the vLLM instance? I've retried the experiments with the latest release and the issue still persists.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: No support for longer context lengths. Model: Llama-2-chat-hf The current implementation of vLLM gives the finish_reason as 'length' whilst the native model supports context length of 4024(And works well with the contex...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: el supports context length of 4024(And works well with the context we've tested it with) , Is the option available to change the native context length supported by the vLLM instance? I've retried the experiments with th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
