# vllm-project/vllm#5244: [Usage]: Running Phi-3-small-128k-instruct with v0.4.3 without --trust-remote-code

| 字段 | 值 |
| --- | --- |
| Issue | [#5244](https://github.com/vllm-project/vllm/issues/5244) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Running Phi-3-small-128k-instruct with v0.4.3 without --trust-remote-code

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.9.2 (default, Feb 28 2021, 17:03:44) [GCC 10.2.1 20210110] (64-bit runtime) Python platform: Linux-5.16.0-0.bpo.4-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 PCIe GPU 1: NVIDIA H100 PCIe GPU 2: NVIDIA H100 PCIe GPU 3: NVIDIA H100 PCIe GPU 4: NVIDIA H100 PCIe GPU 5: NVIDIA H100 PCIe GPU 6: NVIDIA H100 PCIe GPU 7: NVIDIA H100 PCIe Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 52 bits physical, 57 bits virtual CPU(s): 256 On-line CPU(s) lis...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: Running Phi-3-small-128k-instruct with v0.4.3 without --trust-remote-code usage ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch versi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: `text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Li...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.3 vLLM Build Flags: CUDA Archs: N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
