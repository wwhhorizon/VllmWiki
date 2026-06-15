# vllm-project/vllm#9288: [Bug]: Quantization example outdated (Ammo -> ModelOpt)

| 字段 | 值 |
| --- | --- |
| Issue | [#9288](https://github.com/vllm-project/vllm/issues/9288) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Quantization example outdated (Ammo -> ModelOpt)

### Issue 正文摘录

### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug FP8 Quantization example https://github.com/vllm-project/vllm/tree/main/examples/other/fp8 uses very old version Ammo which has now been rebranded as Nvidia TensorRT Model Optimizer (ModelOpt). Here is the repository: https://github.com/NVIDIA/TensorRT-Model-Optimizer and the documentation: https://nvidia.github.io/TensorRT-Model-Optimizer/ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Quantization example outdated (Ammo -> ModelOpt) bug;stale ### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug FP8 Quantization example https://github.com/vllm-project/vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /github.com/vllm-project/vllm/tree/main/examples/other/fp8 uses very old version Ammo which has now been rebranded as Nvidia TensorRT Model Optimizer (ModelOpt). Here is the repository: https://github.com/NVIDIA/TensorR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er/ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Quantization example outdated (Ammo -> ModelOpt) bug;stale ### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug FP8 Quantization example https://github.com/vllm-project/vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Quantization example outdated (Ammo -> ModelOpt) bug;stale ### Your current environment N/A ### Model Input Dumps _No response_ ### 🐛 Describe the bug FP8 Quantization example https://github.com/vllm-project/vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
