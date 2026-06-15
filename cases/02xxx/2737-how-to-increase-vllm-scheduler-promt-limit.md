# vllm-project/vllm#2737: How to increase vllm scheduler promt limit?

| 字段 | 值 |
| --- | --- |
| Issue | [#2737](https://github.com/vllm-project/vllm/issues/2737) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to increase vllm scheduler promt limit?

### Issue 正文摘录

Hi, I am using FastChat vicuna-7b-v1.5 model with vllm worker. When chatting with back-end, I encountered prompt limitation in scheduler.py. ![MicrosoftTeams-image (19)](https://github.com/vllm-project/vllm/assets/6904705/29f22c61-53e6-4987-86ef-22a310fde7b2) May I know how to increase the number of prompt limitation in scheduler.py?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ease vllm scheduler promt limit? Hi, I am using FastChat vicuna-7b-v1.5 model with vllm worker. When chatting with back-end, I encountered prompt limitation in scheduler.py. ![MicrosoftTeams-image (19)](https://github.c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: How to increase vllm scheduler promt limit? Hi, I am using FastChat vicuna-7b-v1.5 model with vllm worker. When chatting with back-end, I encountered prompt limitation in scheduler.py. ![MicrosoftTeams-image (19)](https...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
