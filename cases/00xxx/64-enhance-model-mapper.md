# vllm-project/vllm#64: Enhance model mapper

| 字段 | 值 |
| --- | --- |
| Issue | [#64](https://github.com/vllm-project/vllm/issues/64) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Enhance model mapper

### Issue 正文摘录

The current model mapper is hacky; it uses string matching based on the model name or path. Let's use HF-style model mapper that uses the architecture specified in model config and lazy-loads the target model only.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Enhance model mapper The current model mapper is hacky; it uses string matching based on the model name or path. Let's use HF-style model mapper that uses the architecture specified in model config and lazy-loads the ta...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e or path. Let's use HF-style model mapper that uses the architecture specified in model config and lazy-loads the target model only.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on the model name or path. Let's use HF-style model mapper that uses the architecture specified in model config and lazy-loads the target model only.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
