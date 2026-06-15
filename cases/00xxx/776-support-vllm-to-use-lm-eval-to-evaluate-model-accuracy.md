# vllm-project/vllm#776:  Support vllm to use lm-eval to evaluate model accuracy

| 字段 | 值 |
| --- | --- |
| Issue | [#776](https://github.com/vllm-project/vllm/issues/776) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

>  Support vllm to use lm-eval to evaluate model accuracy

### Issue 正文摘录

May I ask what method is currently used by vllm to evaluate the accuracy of the model? When using[ llm-eval](https://github.com/EleutherAI/lm-evaluation-harness) to test the accuracy of the llm running model, according to the evaluation method of llm-eval, prompts corresponding to logprobs need to be output at the same time for subsequent acc or ppl calculations. But at present, vllm can only output the generated sentences. Can you add options to support vllm to output results after running, output prompt words and corresponding logprobs function?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Support vllm to use lm-eval to evaluate model accuracy May I ask what method is currently used by vllm to evaluate the accuracy of the model? When using[ llm-eval](https://github.com/EleutherAI/lm-evaluation-harness) to...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Support vllm to use lm-eval to evaluate model accuracy May I ask what method is currently used by vllm to evaluate the accuracy of the model? When using[ llm-eval](https://github.com/EleutherAI/lm-evaluation-harness) to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Support vllm to use lm-eval to evaluate model accuracy May I ask what method is currently used by vllm to evaluate the accuracy of the model? When using[ llm-eval](https://github.com/EleutherAI/lm-evaluation-harness) to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
