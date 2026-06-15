# vllm-project/vllm#4262: [Bug]: Using the latest docker image to load CohereForAIc4ai-command-r-plus Model, it crashed

| 字段 | 值 |
| --- | --- |
| Issue | [#4262](https://github.com/vllm-project/vllm/issues/4262) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using the latest docker image to load CohereForAIc4ai-command-r-plus Model, it crashed

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.1.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 7.3.0 Clang version: Could not collect CMake version: version 3.25.0-rc2 Libc version: glibc-2.17 Python version: 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.2.128 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB GPU 4: NVIDIA A100-SXM4-40GB GPU 5: NVIDIA A100-SXM4-40GB GPU 6: NVIDIA A100-SXM4-40GB GPU 7: NVIDIA A100-SXM4-40GB Nvidia driver version: 535.86.10 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Thread(s) per core: 2 Core(s) per socket: 48 Socket(s): 2 NUMA node(s): 2 Vendor ID: Au...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Using the latest docker image to load CohereForAIc4ai-command-r-plus Model, it crashed bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.1+cu121 Is debug build: F...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 7.3.0 Clang version: Could...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: g]: Using the latest docker image to load CohereForAIc4ai-command-r-plus Model, it crashed bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.1+cu121 Is debug build: Fals...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: mpydoc==1.5.0 [pip3] nvidia-nccl-cu12==2.18.1 [pip3] torch==2.1.1 [pip3] triton==2.1.0 [conda] _anaconda_depends 2023.09 py311_mkl_1 https://repo.anaconda.com/pkgs/main [conda] blas 1.0 mkl https://repo.anaconda.com/pkg...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip overflow_recov succor smca Versions of relevant libraries: [pip3] flake8==6.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
