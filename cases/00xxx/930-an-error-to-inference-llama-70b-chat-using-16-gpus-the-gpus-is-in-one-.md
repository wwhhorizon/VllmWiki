# vllm-project/vllm#930: An error to inference Llama-70b-chat using 16 gpus. The gpus is in one machine.

| 字段 | 值 |
| --- | --- |
| Issue | [#930](https://github.com/vllm-project/vllm/issues/930) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> An error to inference Llama-70b-chat using 16 gpus. The gpus is in one machine.

### Issue 正文摘录

I have 16 * A10,my command is : `python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-70b-hf --tensor-parallel-size 16` But it appears an error: ![image](https://github.com/vllm-project/vllm/assets/117291738/50082601-5bb8-49cd-91e5-ee77632ee55b) Can someone tell me your command to run Llama-70b-chat？

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: An error to inference Llama-70b-chat using 16 gpus. The gpus is in one machine. I have 16 * A10,my command is : `python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-70b-hf --tensor-parallel-size 16`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
