# vllm-project/vllm#16476: [Usage]: Dev instructions for implementing new LoRA features on VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16476](https://github.com/vllm-project/vllm/issues/16476) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Dev instructions for implementing new LoRA features on VLLM

### Issue 正文摘录

What is the easiest way, when implementing new LoRA features on VLLM? For example, I want to modify the forward pass of LoRA model, ref to the forward pass in PEFT, the original LoRA is: ```python result = result + lora_B(lora_A(dropout(x))) * scaling ``` While suppose new feature is: ```python result = result + lora_B(lora_A(dropout(x))) * scaling + some_linear_A @ some_linear_B + some_func() ``` then 1. do I need to modify all the RowParallelLinearWithLoRA, MergedQKVParallelLinearWithLoRA, ColumnParallelLinearWithLoRA, etc. ? 2. consider tp? 3. torch or triton or both? 4. punica? Looking for a easiest way to implement when only the forward pass of LoRA is changed.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: thLoRA, ColumnParallelLinearWithLoRA, etc. ? 2. consider tp? 3. torch or triton or both? 4. punica? Looking for a easiest way to implement when only the forward pass of LoRA is changed.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eatures on VLLM? For example, I want to modify the forward pass of LoRA model, ref to the forward pass in PEFT, the original LoRA is: ```python result = result + lora_B(lora_A(dropout(x))) * scaling ``` While suppose ne...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
