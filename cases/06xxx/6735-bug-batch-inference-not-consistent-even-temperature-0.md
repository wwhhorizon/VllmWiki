# vllm-project/vllm#6735: [Bug]: batch inference not consistent (even temperature=0)

| 字段 | 值 |
| --- | --- |
| Issue | [#6735](https://github.com/vllm-project/vllm/issues/6735) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: batch inference not consistent (even temperature=0)

### Issue 正文摘录

### Your current environment ```text PyTorch version: 1.13.1 Is debug build: False CUDA used to build PyTorch: 11.6 ROCM used to build PyTorch: N/A GCC version: (GCC) 8.5.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.17 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Is CUDA available: True CUDA runtime version: 11.6.124 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.104.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 106 Model name: Intel(R) Xeon(R) Platinum 8369B CPU @ 2.90GHz Stepping: 6 CPU MHz: 3490.909 BogoMIPS: 5807.31 Virtu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t (even temperature=0) bug ### Your current environment ```text PyTorch version: 1.13.1 Is debug build: False CUDA used to build PyTorch: 11.6 ROCM used to build PyTorch: N/A GCC version: (GCC) 8.5.0 Clang version: Coul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: rrent environment ```text PyTorch version: 1.13.1 Is debug build: False CUDA used to build PyTorch: 11.6 ROCM used to build PyTorch: N/A GCC version: (GCC) 8.5.0 Clang version: Could not collect CMake version: Could not...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 11.6.124 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r current environment ```text PyTorch version: 1.13.1 Is debug build: False CUDA used to build PyTorch: 11.6 ROCM used to build PyTorch: N/A GCC version: (GCC) 8.5.0 Clang version: Could not collect CMake version: Could...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
