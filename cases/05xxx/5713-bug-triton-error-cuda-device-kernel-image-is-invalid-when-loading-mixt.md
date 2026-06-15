# vllm-project/vllm#5713: [Bug]:  "Triton Error [CUDA]: device kernel image is invalid" when loading Mixtral-8x7B-Instruct-v0.1 in fused_moe.py

| 字段 | 值 |
| --- | --- |
| Issue | [#5713](https://github.com/vllm-project/vllm/issues/5713) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;moe |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;moe;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  "Triton Error [CUDA]: device kernel image is invalid" when loading Mixtral-8x7B-Instruct-v0.1 in fused_moe.py

### Issue 正文摘录

### Your current environment ```text 2024-06-19 17:30:02,514 - [Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.10.14 (main, Mar 21 2024, 16:24:04) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.231-137.341.amzn2.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB Nvidia driver version: 470.161.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Platinum 8275CL CPU @ 3.00GHz CPU family: 6 Mo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: 2024-06-19 17:30:02,514 - [Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: "Triton Error [CUDA]: device kernel image is invalid" when loading Mixtral-8x7B-Instruct-v0.1 in fused_moe.py bug;stale ### Your current environment ```text 2024-06-19 17:30:02,514 - [Collecting environment infor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: environment ```text 2024-06-19 17:30:02,514 - [Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ernel image is invalid" when loading Mixtral-8x7B-Instruct-v0.1 in fused_moe.py bug;stale ### Your current environment ```text 2024-06-19 17:30:02,514 - [Collecting environment information... PyTorch version: 2.3.0 Is d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
