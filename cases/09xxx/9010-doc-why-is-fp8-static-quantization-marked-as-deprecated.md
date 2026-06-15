# vllm-project/vllm#9010: [Doc]: Why is FP8 static quantization marked as deprecated?

| 字段 | 值 |
| --- | --- |
| Issue | [#9010](https://github.com/vllm-project/vllm/issues/9010) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Why is FP8 static quantization marked as deprecated?

### Issue 正文摘录

### 📚 The doc issue according to the doc https://docs.vllm.ai/en/latest/quantization/fp8.html#deprecated-flow offline quantization using AutoFP8 is marked as deprecated, wondering what is the reason for this? Is there any model quality or performance issue? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Doc]: Why is FP8 static quantization marked as deprecated? documentation ### 📚 The doc issue according to the doc https://docs.vllm.ai/en/latest/quantization/fp8.html#deprecated-flow offline quantization using AutoFP8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: arked as deprecated, wondering what is the reason for this? Is there any model quality or performance issue? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tion ### 📚 The doc issue according to the doc https://docs.vllm.ai/en/latest/quantization/fp8.html#deprecated-flow offline quantization using AutoFP8 is marked as deprecated, wondering what is the reason for this? Is th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
