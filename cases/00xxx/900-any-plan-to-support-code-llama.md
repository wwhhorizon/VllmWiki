# vllm-project/vllm#900: Any plan to support Code Llama?

| 字段 | 值 |
| --- | --- |
| Issue | [#900](https://github.com/vllm-project/vllm/issues/900) |
| 状态 | closed |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Any plan to support Code Llama?

### Issue 正文摘录

Thanks for your great work! However, the current vllm does not support Code Llama, and the output is nonsense. Do you have any plan to make such an update? I believe it will not take you much effort cause the architecture is similar to Llama.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ake such an update? I believe it will not take you much effort cause the architecture is similar to Llama.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Any plan to support Code Llama? Thanks for your great work! However, the current vllm does not support Code Llama, and the output is nonsense. Do you have any plan to make such an update? I believe it will not take you...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
