# vllm-project/vllm#2367: v2.0.7 becomed slower than v2.0.6

| 字段 | 值 |
| --- | --- |
| Issue | [#2367](https://github.com/vllm-project/vllm/issues/2367) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> v2.0.7 becomed slower than v2.0.6

### Issue 正文摘录

model: deepseek-llm-67b-chat -awq-int4 tp = 2 gpu: A100-40G x2 v2.0.7: 16tokens/s v2.0.6: 21tokens/s

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: v2.0.7 becomed slower than v2.0.6 model: deepseek-llm-67b-chat -awq-int4 tp = 2 gpu: A100-40G x2 v2.0.7: 16tokens/s v2.0.6: 21tokens/s performance distributed_parallel;model_support;quantization quantization slowdown dt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed slower than v2.0.6 model: deepseek-llm-67b-chat -awq-int4 tp = 2 gpu: A100-40G x2 v2.0.7: 16tokens/s v2.0.6: 21tokens/s performance distributed_parallel;model_support;quantization quantization slowdown dtype model: d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: v2.0.7 becomed slower than v2.0.6 model: deepseek-llm-67b-chat -awq-int4 tp = 2 gpu: A100-40G x2 v2.0.7: 16tokens/s v2.0.6: 21tokens/s performance distributed_parallel;model_support;quantization quantization slowdown dt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
