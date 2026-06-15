# vllm-project/vllm#1736: vllm+guidance

| 字段 | 值 |
| --- | --- |
| Issue | [#1736](https://github.com/vllm-project/vllm/issues/1736) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm+guidance

### Issue 正文摘录

Hello author, we are currently integrating vllm's inference engine into the guidance project, and found that its inference speed has not improved significantly, but has declined. The principle of guidance is to save the time of generating fixed tokens by the model by presetting a template. Is this related to some mechanisms of vllm?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nference speed has not improved significantly, but has declined. The principle of guidance is to save the time of generating fixed tokens by the model by presetting a template. Is this related to some mechanisms of vllm?
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns by the model by presetting a template. Is this related to some mechanisms of vllm?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nciple of guidance is to save the time of generating fixed tokens by the model by presetting a template. Is this related to some mechanisms of vllm?

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
