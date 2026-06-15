# vllm-project/vllm#7367: [Usage]: how to use LLM class with AsyncLLMEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#7367](https://github.com/vllm-project/vllm/issues/7367) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to use LLM class with AsyncLLMEngine

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.36 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.1.0-18-amd64-x86_64-with-glibc2.36 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A100 80GB PCIe GPU 3: NVIDIA A100 80GB PCIe GPU 4: NVIDIA A100 80GB PCIe Nvidia driver version: 550.54.14 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 256 On-line CPU(s) list: 0-255 Vendor ID: AuthenticAMD Model name: AMD EPYC 7763 64-Core Processor CPU family: 25 Model: 1 Thread(s) per...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: PyTorch version: 2.4.0+cu121 Is debug build: Fal
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: CUDA used to build PyTorch: 12.1 ROCM used t
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ine usage ### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: veerptr rdpru wbnoinvd amd_ppin brs arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in brs arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca Virtualizat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
