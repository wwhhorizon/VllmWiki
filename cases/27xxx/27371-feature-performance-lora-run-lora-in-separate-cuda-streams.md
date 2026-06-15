# vllm-project/vllm#27371: [Feature][Performance][LoRA]: Run LoRA in Separate CUDA Streams

| 字段 | 值 |
| --- | --- |
| Issue | [#27371](https://github.com/vllm-project/vllm/issues/27371) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature][Performance][LoRA]: Run LoRA in Separate CUDA Streams

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Nice blog by databricks: https://www.databricks.com/blog/fast-peft-serving-scale Two key optimizations - [ ] LoRA in separate cuda stream - @dcmaddix - [x] PDL in the LoRA kernels for Shink/Expand - @jeejeelee We should implement both - @dcmaddix on LoRA in separate stream - @jeejeelee on PDL for LoRA ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#29316 lora cuda multistream

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature][Performance][LoRA]: Run LoRA in Separate CUDA Streams feature request;stale ### 🚀 The feature, motivation and pitch Nice blog by databricks: https://www.databricks.com/blog/fast-peft-serving-scale Two key opti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][Performance][LoRA]: Run LoRA in Separate CUDA Streams feature request;stale ### 🚀 The feature, motivation and pitch Nice blog by databricks: https://www.databricks.com/blog/fast-peft-serving-scale Two key opti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ce blog by databricks: https://www.databricks.com/blog/fast-peft-serving-scale Two key optimizations - [ ] LoRA in separate cuda stream - @dcmaddix - [x] PDL in the LoRA kernels for Shink/Expand - @jeejeelee We should i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance frontend_api cuda;kernel #29316 lora cuda multistream 🚀 The feature, moti...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29316](https://github.com/vllm-project/vllm/pull/29316) | closes_keyword | 0.95 | lora cuda multistream | FIX [#27371](https://github.com/vllm-project/vllm/issues/27371) Concretely: - `PunicaWrapperGPU` gets: - A dedicated `lora_stream` (using `aux_stream()`), gated by a new e |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
