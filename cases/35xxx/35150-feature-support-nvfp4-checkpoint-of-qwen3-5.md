# vllm-project/vllm#35150: [Feature]:  Support NVFP4 Checkpoint of Qwen3.5

| 字段 | 值 |
| --- | --- |
| Issue | [#35150](https://github.com/vllm-project/vllm/issues/35150) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  Support NVFP4 Checkpoint of Qwen3.5

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the NVFP4 checkpoint of Qwen3.5 is only supported on SGLang due to model definitions. We want the checkpoint to also work with vLLM. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Support NVFP4 Checkpoint of Qwen3.5 feature request ### 🚀 The feature, motivation and pitch Currently the NVFP4 checkpoint of Qwen3.5 is only supported on SGLang due to model definitions. We want the checkpoi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support NVFP4 Checkpoint of Qwen3.5 feature request ### 🚀 The feature, motivation and pitch Currently the NVFP4 checkpoint of Qwen3.5 is only supported on SGLang due to model definitions. We want the checkpoi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support NVFP4 Checkpoint of Qwen3.5 feature request ### 🚀 The feature, motivation and pitch Currently the NVFP4 checkpoint of Qwen3.5 is only supported on SGLang due to model definitions. We want the checkpoi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
