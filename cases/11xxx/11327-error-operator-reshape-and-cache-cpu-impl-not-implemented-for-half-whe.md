# vllm-project/vllm#11327: Error: operator reshape_and_cache_cpu_impl not implemented for half when running examples/offline_inference.py on POWER10

| 字段 | 值 |
| --- | --- |
| Issue | [#11327](https://github.com/vllm-project/vllm/issues/11327) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error: operator reshape_and_cache_cpu_impl not implemented for half when running examples/offline_inference.py on POWER10

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.6.0a0+git9126110 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.5 (Plow) (ppc64le) GCC version: (GCC) 13.3.1 20240611 (Red Hat 13.3.1-2) Clang version: 18.1.8 (Red Hat, Inc. 18.1.8-3.el9) CMake version: version 3.31.1 Libc version: glibc-2.34 Python version: 3.11.11 | packaged by conda-forge | (main, Dec 5 2024, 14:07:52) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-5.14.0-503.15.1.el9_5.ppc64le-ppc64le-with-glibc2.34 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: False CPU: Architecture: ppc64le Byte Order: Little Endian CPU(s): 320 On-line CPU(s) list: 0-319 Model name: POWER10 (architected), altivec supported Model: 2.0 (pvr 0080 0200) Thread(s) per core: 8 Core(s) per socket: 10 Socket(s): 4 Hypervisor vendor: pHyp Virtualization type: para L1d cache: 2.5 MiB (80 instances)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: of `python collect_env.py` Collecting environment information... PyTorch version: 2.6.0a0+git9126110 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: information... PyTorch version: 2.6.0a0+git9126110 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.5 (Plow) (ppc64le) GCC version: (GCC) 13.3.1 20240...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ironment The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.6.0a0+git9126110 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Red Hat...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ent information... PyTorch version: 2.6.0a0+git9126110 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.5 (Plow) (ppc64le) GCC version: (GCC) 13.3.1 2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: affected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
