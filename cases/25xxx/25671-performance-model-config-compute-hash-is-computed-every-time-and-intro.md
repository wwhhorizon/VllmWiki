# vllm-project/vllm#25671: [Performance] `model_config.compute_hash` is computed every time and introduce overhead in each new multi-modal req

| 字段 | 值 |
| --- | --- |
| Issue | [#25671](https://github.com/vllm-project/vllm/issues/25671) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance] `model_config.compute_hash` is computed every time and introduce overhead in each new multi-modal req

### Issue 正文摘录

call stack: `InputPreprocessor::_process_multimodal` -> `MultiModalRegistry::create_processor` -> `MultiModalRegistry::_get_model_cls` -> `get_model_architecture` -> `model_config.compute_hash` https://github.com/vllm-project/vllm/blob/c60e6137f0bf2034853919b3a9d705d7e06b93cf/vllm/model_executor/model_loader/utils.py#L216-L224

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance] `model_config.compute_hash` is computed every time and introduce overhead in each new multi-modal req performance call stack: `InputPreprocessor::_process_multimodal` -> `MultiModalRegistry::create_process...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: :create_processor` -> `MultiModalRegistry::_get_model_cls` -> `get_model_architecture` -> `model_config.compute_hash` https://github.com/vllm-project/vllm/blob/c60e6137f0bf2034853919b3a9d705d7e06b93cf/vllm/model_executo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
