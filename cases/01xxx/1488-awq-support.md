# vllm-project/vllm#1488: AWQ Support 

| 字段 | 值 |
| --- | --- |
| Issue | [#1488](https://github.com/vllm-project/vllm/issues/1488) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AWQ Support 

### Issue 正文摘录

I got this error to run awq model with VLLM on a v100 gpu. How can i resolve this ? ``` The quantization method awq is not supported for the current GPU. Minimum capability: 75. Current capability: 70. ```

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: un awq model with VLLM on a v100 gpu. How can i resolve this ? ``` The quantization method awq is not supported for the current GPU. Minimum capability: 75. Current capability: 70. ``` development model_support;quantiza...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: he quantization method awq is not supported for the current GPU. Minimum capability: 75. Current capability: 70. ``` development model_support;quantization quantization I got this error to run awq model with VLLM on a v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: AWQ Support I got this error to run awq model with VLLM on a v100 gpu. How can i resolve this ? ``` The quantization method awq is not supported for the current GPU. Minimum capability: 75. Current capability: 70. ``` d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
