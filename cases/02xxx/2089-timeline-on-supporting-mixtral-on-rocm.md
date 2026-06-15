# vllm-project/vllm#2089: Timeline on supporting Mixtral on ROCm?

| 字段 | 值 |
| --- | --- |
| Issue | [#2089](https://github.com/vllm-project/vllm/issues/2089) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Timeline on supporting Mixtral on ROCm?

### Issue 正文摘录

Ran into this https://github.com/vllm-project/vllm/blob/096827c2846e7a769cf20e34c46b8eada444cc1e/vllm/model_executor/models/__init__.py#L42

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Timeline on supporting Mixtral on ROCm? rocm Ran into this https://github.com/vllm-project/vllm/blob/096827c2846e7a769cf20e34c46b8eada444cc1e/vllm/model_executor/models/__init__.py#L42
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/096827c2846e7a769cf20e34c46b8eada444cc1e/vllm/model_executor/models/__init__.py#L42

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
