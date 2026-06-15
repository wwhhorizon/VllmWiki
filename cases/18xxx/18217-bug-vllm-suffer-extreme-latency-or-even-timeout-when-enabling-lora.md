# vllm-project/vllm#18217: [Bug]: vllm suffer extreme latency or even timeout when enabling lora

| 字段 | 值 |
| --- | --- |
| Issue | [#18217](https://github.com/vllm-project/vllm/issues/18217) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm suffer extreme latency or even timeout when enabling lora

### Issue 正文摘录

### Your current environment current environment: vllm version: `0.8.5.post1` ``` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.11.11 (main, Dec 11 2024, 16:28:39) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.11.0-25-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX 5000 Ada Generation GPU 1: NVIDIA RTX 5000 Ada Generation Nvidia driver version: 550.144.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 40 On-line CPU(s) list: 0-39 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) w7-3445 CPU family: 6 Model: 143 Thread(s) per core: 2 Core(s) per socket: 20 Socket(s): 1 Stepping: 8 CPU(s) scaling...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: g lora bug;stale ### Your current environment current environment: vllm version: `0.8.5.post1` ``` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX 5000 Ada Generation GPU 1: NVIDIA RTX 5000 Ada Generation Nvidia driver version: 550.144.03 cuDNN vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: on: `0.8.5.post1` ``` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Bug]: vllm suffer extreme latency or even timeout when enabling lora bug;stale ### Your current environment current environment: vllm version: `0.8.5.post1` ``` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA us...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
