# vllm-project/vllm#3912: [Bug]: Cannot use FlashAttention because the package is not found. Please install it for better performance.

| 字段 | 值 |
| --- | --- |
| Issue | [#3912](https://github.com/vllm-project/vllm/issues/3912) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot use FlashAttention because the package is not found. Please install it for better performance.

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-92-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 PCIe GPU 1: NVIDIA H100 PCIe GPU 2: NVIDIA H100 PCIe GPU 3: NVIDIA H100 PCIe Nvidia driver version: 550.54.14 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 52 bits physical, 57 bits virtual CPU(s): 126 On-line CPU(s) list: 0-125 Thread(s) per core: 1 Core(s) per socket: 126 Socket(s): 1 NUMA node(s): 1 Vendor ID: AuthenticAMD CPU family: 25 Model: 17 Model name: AMD EPYC 9554 64-Core...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: Bug]: Cannot use FlashAttention because the package is not found. Please install it for better performance. bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ance. bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Cannot use FlashAttention because the package is not found. Please install it for better performance. bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx512_bf16 clzero xsaveerptr wbnoinvd arat npt lbrv nrip_save tsc_scale vmcb_clean pausefilter pfthreshold v_vmsave_vmload vgif avx512vbmi umip pku ospke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
