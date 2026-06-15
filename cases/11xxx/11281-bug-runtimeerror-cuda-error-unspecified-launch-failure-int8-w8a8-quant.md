# vllm-project/vllm#11281: [Bug]: [RuntimeError: CUDA error: unspecified launch failure  ]int8 w8a8 quantization data set to generate model data, an error occurred when changing the specified data set

| 字段 | 值 |
| --- | --- |
| Issue | [#11281](https://github.com/vllm-project/vllm/issues/11281) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [RuntimeError: CUDA error: unspecified launch failure  ]int8 w8a8 quantization data set to generate model data, an error occurred when changing the specified data set

### Issue 正文摘录

### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40S GPU 1: NVIDIA L40S GPU 2: NVIDIA L40S GPU 3: NVIDIA L40S GPU 4: NVIDIA L40S GPU 5: NVIDIA L40S GPU 6: NVIDIA L40S GPU 7: NVIDIA L40S Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Vendor ID: GenuineIntel BIOS Vendor ID: Intel(R) Corporation Model name: Intel(R) Xeon(R) Platinum 8468V BIOS Model name: Intel(R) Xeon(R) Pl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: [RuntimeError: CUDA error: unspecified launch failure ]int8 w8a8 quantization data set to generate model data, an error occurred when changing the specified data set bug;stale ### Your current environment PyTorch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: [RuntimeError: CUDA error: unspecified launch failure ]int8 w8a8 quantization data set to generate model data, an error occurred when changing the specified data set bug;stale ### Your current environment PyTorch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: unspecified launch failure ]int8 w8a8 quantization data set to generate model data, an error occurred when changing the specified data set bug;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug bui...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: [RuntimeError: CUDA error: unspecified launch failure ]int8 w8a8 quantization data set to generate model data, an error occurred when changing the specified data set bug;stale ### Your current environment PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e model data, an error occurred when changing the specified data set bug;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
