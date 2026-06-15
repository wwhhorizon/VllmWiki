# vllm-project/vllm#4074: [Bug]: RuntimeError: Unknown layout

| 字段 | 值 |
| --- | --- |
| Issue | [#4074](https://github.com/vllm-project/vllm/issues/4074) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Unknown layout

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.2.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.27 Python version: 3.10.12 (main, Jul 5 2023, 18:54:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-150-generic-x86_64-with-glibc2.27 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 GPU 2: NVIDIA GeForce RTX 4090 GPU 3: NVIDIA GeForce RTX 4090 Nvidia driver version: 535.146.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: 架构： x86_64 CPU 运行模式： 32-bit, 64-bit 字节序： Little Endian CPU: 32 在线 CPU 列表： 0-31 每个核的线程数： 2 每个座的核数： 16 座： 1 NUMA 节点： 4 厂商 ID： AuthenticAMD CPU 系列： 23 型号： 49 型号名称： AMD EPYC 7302 16-Core Processor 步进： 0 CPU MHz： 1486.662 CPU 最大 MHz： 3000.0000 CPU 最小 MHz： 1500.0000 BogoMIPS： 5988.92 虚拟化： AMD-V L1d 缓存： 32K L1i 缓存： 32K L2 缓存： 512K L3 缓存： 1638...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Unknown layout bug;stale ### Your current environment ```text PyTorch version: 2.2.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: RuntimeError: Unknown layout bug;stale ### Your current environment ```text PyTorch version: 2.2.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.2.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 Cl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: s of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.2.2 [pip3] triton==2.2.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.2.2 pypi_0 pypi [conda] triton 2.2.0
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: l clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca Versions of rel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
