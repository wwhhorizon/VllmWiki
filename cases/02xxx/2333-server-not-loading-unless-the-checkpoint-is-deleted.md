# vllm-project/vllm#2333: Server not loading unless the checkpoint is deleted

| 字段 | 值 |
| --- | --- |
| Issue | [#2333](https://github.com/vllm-project/vllm/issues/2333) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Server not loading unless the checkpoint is deleted

### Issue 正文摘录

I was trying to load the openai based server for llama2 70b when I saw that the server load doesn't complete and just pauses after the log statement `For some LLaMA V1 models, initializing the fast tokenizer may take a long time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer.` When I deleted the pre-downloaded llama2 70b from the `.cache`, it was able to redownload the checkpoints and then the deployment went through. Is there any intuition behind this observation? Thank you for any help.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e checkpoint is deleted I was trying to load the openai based server for llama2 70b when I saw that the server load doesn't complete and just pauses after the log statement `For some LLaMA V1 models, initializing the fa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ong time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer.` When I deleted the pre-downloaded llama2 70b from the `.cache`, it was able to redown...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
