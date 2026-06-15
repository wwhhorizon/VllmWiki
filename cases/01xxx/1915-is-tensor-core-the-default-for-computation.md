# vllm-project/vllm#1915: Is tensor core the default for computation ？

| 字段 | 值 |
| --- | --- |
| Issue | [#1915](https://github.com/vllm-project/vllm/issues/1915) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is tensor core the default for computation ？

### Issue 正文摘录

Hi Dear: I have two questions: (1) If compiling and reasoning on the A100, the default is to use tensor core for reasoning, Not cuda core, right ? (2) If using the int4 quantized model for inference, need to de-quantize the inference calculation? thank you!

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: o use tensor core for reasoning, Not cuda core, right ? (2) If using the int4 quantized model for inference, need to de-quantize the inference calculation? thank you!
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n ？ Hi Dear: I have two questions: (1) If compiling and reasoning on the A100, the default is to use tensor core for reasoning, Not cuda core, right ? (2) If using the int4 quantized model for inference, need to de-quan...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: re for reasoning, Not cuda core, right ? (2) If using the int4 quantized model for inference, need to de-quantize the inference calculation? thank you!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
