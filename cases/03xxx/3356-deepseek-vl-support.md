# vllm-project/vllm#3356: DeepSeek VL support

| 字段 | 值 |
| --- | --- |
| Issue | [#3356](https://github.com/vllm-project/vllm/issues/3356) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> DeepSeek VL support

### Issue 正文摘录

Hi, it would be awesome if [DeepSeek VL](https://huggingface.co/deepseek-ai/deepseek-vl-1.3b-chat) will be supported for all the serving goodies!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: epSeek VL support stale Hi, it would be awesome if [DeepSeek VL](https://huggingface.co/deepseek-ai/deepseek-vl-1.3b-chat) will be supported for all the serving goodies!
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: DeepSeek VL support stale Hi, it would be awesome if [DeepSeek VL](https://huggingface.co/deepseek-ai/deepseek-vl-1.3b-chat) will be supported for all the serving goodies!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
