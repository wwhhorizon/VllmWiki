# vllm-project/vllm#14674: [Usage]: Supports int2 quantized models

| 字段 | 值 |
| --- | --- |
| Issue | [#14674](https://github.com/vllm-project/vllm/issues/14674) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Supports int2 quantized models

### Issue 正文摘录

### Your current environment Does VLLM inference support mixed-precision models where some layers are quantized to int4 and others to int2 or int3? If not, what parts of the source code would need to be modified to support this feature? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: stale ### Your current environment Does VLLM inference support mixed-precision models where some layers are quantized to int4 and others to int2 or int3? If not, what parts of the source code would need to be modified t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Usage]: Supports int2 quantized models usage;stale ### Your current environment Does VLLM inference support mixed-precision models where some layers are quantized to int4 and others to int2 or int3? If not, what parts...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ge;stale ### Your current environment Does VLLM inference support mixed-precision models where some layers are quantized to int4 and others to int2 or int3? If not, what parts of the source code would need to be modifie...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Supports int2 quantized models usage;stale ### Your current environment Does VLLM inference support mixed-precision models where some layers are quantized to int4 and others to int2 or int3? If not, what parts...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
