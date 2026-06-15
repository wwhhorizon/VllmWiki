# vllm-project/vllm#1323: qwen support long chat

| 字段 | 值 |
| --- | --- |
| Issue | [#1323](https://github.com/vllm-project/vllm/issues/1323) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> qwen support long chat

### Issue 正文摘录

support long chat [Support Longchat #555](https://github.com/vllm-project/vllm/pull/555) has been merged This does not support qwen yet. If I refer to qwen's [ntk_alpha method](https://huggingface.co/Qwen/Qwen-7B-Chat/blob/main/modeling_qwen.py#L779), can vllm support qwen's long chat? thank you

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: qwen support long chat support long chat [Support Longchat #555](https://github.com/vllm-project/vllm/pull/555) has been merged This does not support qwen yet. If I refer to qwen's [ntk_alpha method](https://huggingfac

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
