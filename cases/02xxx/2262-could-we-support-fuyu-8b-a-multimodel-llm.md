# vllm-project/vllm#2262: Could we support Fuyu-8B, a multimodel llm?

| 字段 | 值 |
| --- | --- |
| Issue | [#2262](https://github.com/vllm-project/vllm/issues/2262) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Could we support Fuyu-8B, a multimodel llm?

### Issue 正文摘录

Hi, Fuyu 8B is a multimodel llm model, could we support it in vllm? https://www.adept.ai/blog/fuyu-8b It seems to me current vllm only could support pure text, so for this kind of multimodel mixing with image, how could we handle it? Thx~

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Could we support Fuyu-8B, a multimodel llm? new-model Hi, Fuyu 8B is a multimodel llm model, could we support it in vllm? https://www.adept.ai/blog/fuyu-8b It seems to me current vllm only could support pure text, so fo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
