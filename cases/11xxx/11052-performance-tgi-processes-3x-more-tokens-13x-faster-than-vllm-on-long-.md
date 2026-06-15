# vllm-project/vllm#11052: [Performance]: TGI processes 3x more tokens, 13x faster than vLLM on long prompts. Zero config

| 字段 | 值 |
| --- | --- |
| Issue | [#11052](https://github.com/vllm-project/vllm/issues/11052) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: TGI processes 3x more tokens, 13x faster than vLLM on long prompts. Zero config

### Issue 正文摘录

### Report of performance regression ![image](https://github.com/user-attachments/assets/cf6faa42-661d-4208-bb90-d8d435fd90df) https://huggingface.co/docs/text-generation-inference/conceptual/chunking Find TGI release the v3 today and any comments?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: TGI processes 3x more tokens, 13x faster than vLLM on long prompts. Zero config performance ### Report of performance regression ![image](https://github.com/user-attachments/assets/cf6faa42-661d-4208-bb90-d8d435fd90df)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: vLLM on long prompts. Zero config performance ### Report of performance regression ![image](https://github.com/user-attachments/assets/cf6faa42-661d-4208-bb90-d8d435fd90df) https://huggingface.co/docs/text-generation-in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
