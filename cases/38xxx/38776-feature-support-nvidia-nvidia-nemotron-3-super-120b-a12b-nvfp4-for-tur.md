# vllm-project/vllm#38776: [Feature]: support nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 for turing and ampere

| 字段 | 值 |
| --- | --- |
| Issue | [#38776](https://github.com/vllm-project/vllm/issues/38776) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 for turing and ampere

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Only support sm89 or above in modelopt_mixed, and the nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 is modelopt_mixed. The modelopt_mixed need `FP8ScaledMMLinearKernel` impl. I reviewed the code and noted that Marlin FP8 already supports per-tensor FP8 matrix multiplication, implemented by extending it to a per-channel approach. Consequently, we can also leverage Marlin FP8 to implement an `FP8ScaledMMLinearKernel` to provide support for Turing and Ampere architectures. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: support nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 for turing and ampere feature request ### 🚀 The feature, motivation and pitch Only support sm89 or above in modelopt_mixed, and the nvidia/NVIDIA-Nemotro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ]: support nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 for turing and ampere feature request ### 🚀 The feature, motivation and pitch Only support sm89 or above in modelopt_mixed, and the nvidia/NVIDIA-Nemotron-3-Supe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t ### 🚀 The feature, motivation and pitch Only support sm89 or above in modelopt_mixed, and the nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 is modelopt_mixed. The modelopt_mixed need `FP8ScaledMMLinearKernel` impl. I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 for turing and ampere feature request ### 🚀 The feature, motivation and pitch Only support sm89 or above in modelopt_mixed, and the nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVF...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
