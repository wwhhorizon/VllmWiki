# vllm-project/vllm#1537: Question: How does the Llama engine generate multiple choices?

| 字段 | 值 |
| --- | --- |
| Issue | [#1537](https://github.com/vllm-project/vllm/issues/1537) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question: How does the Llama engine generate multiple choices?

### Issue 正文摘录

Hello everybody, Inspired by this project, I am working on [`candle_vllm`](https://github.com/EricLBuehler/candle-vllm) for the [`candle`](https://github.com/huggingface/candle/tree/main) framework. I am working on adding a Llama engine first, but cannot seem to find where it is implemented in VLLM? Specifically, I see below that only the final output will be returned from the model: > https://github.com/vllm-project/vllm/blob/5687d584fe4825d59a6fd9ecc5840e1df04e380f/vllm/entrypoints/openai/api_server.py#L308 Am I mistaken? If so, how does the Llama engine generate multiple "choices"? Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Question: How does the Llama engine generate multiple choices? Hello everybody, Inspired by this project, I am working on [`candle_vllm`](https://github.com/EricLBuehler/candle-vllm) for the [`candle`](https://github.co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: gine first, but cannot seem to find where it is implemented in VLLM? Specifically, I see below that only the final output will be returned from the model: > https://github.com/vllm-project/vllm/blob/5687d584fe4825d59a6f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
