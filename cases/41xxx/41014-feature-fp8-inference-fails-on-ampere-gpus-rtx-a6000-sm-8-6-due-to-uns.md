# vllm-project/vllm#41014: [Feature]: FP8 inference fails on Ampere GPUs (RTX A6000, SM 8.6) due to unsupported default fp8e4nv (E4M3FN) format

| 字段 | 值 |
| --- | --- |
| Issue | [#41014](https://github.com/vllm-project/vllm/issues/41014) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: FP8 inference fails on Ampere GPUs (RTX A6000, SM 8.6) due to unsupported default fp8e4nv (E4M3FN) format

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The RTX A6000 (NVIDIA Ampere architecture, SM 8.6) only supports fp8e4b15 (E4M3B15) and fp8e5 (E5M2) FP8 formats with extremely limited native FP8 capability. However, vLLM (along with the default configuration of DeepSeek-V4) attempts to use the fp8e4nv (E4M3FN) format by default, which is exclusive to NVIDIA Hopper architecture and unsupported on Ampere-based GPUs, leading to inference failures. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Feature]: FP8 inference fails on Ampere GPUs (RTX A6000, SM 8.6) due to unsupported default fp8e4nv (E4M3FN) format feature request ### 🚀 The feature, motivation and pitch The RTX A6000 (NVIDIA Ampere architecture, SM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: FP8 inference fails on Ampere GPUs (RTX A6000, SM 8.6) due to unsupported default fp8e4nv (E4M3FN) format feature request ### 🚀 The feature, motivation and pitch The RTX A6000 (NVIDIA Ampere architecture, SM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ere GPUs (RTX A6000, SM 8.6) due to unsupported default fp8e4nv (E4M3FN) format feature request ### 🚀 The feature, motivation and pitch The RTX A6000 (NVIDIA Ampere architecture, SM 8.6) only supports fp8e4b15 (E4M3B15)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 6000, SM 8.6) due to unsupported default fp8e4nv (E4M3FN) format feature request ### 🚀 The feature, motivation and pitch The RTX A6000 (NVIDIA Ampere architecture, SM 8.6) only supports fp8e4b15 (E4M3B15) and fp8e5 (E5M...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development frontend_api;hardware_porting;model_support;quantization fp8 dtype 🚀 The...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
