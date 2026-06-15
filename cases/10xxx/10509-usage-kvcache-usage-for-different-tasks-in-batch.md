# vllm-project/vllm#10509: [Usage]: KVcache usage for different tasks in batch

| 字段 | 值 |
| --- | --- |
| Issue | [#10509](https://github.com/vllm-project/vllm/issues/10509) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: KVcache usage for different tasks in batch

### Issue 正文摘录

### Your current environment ``` The output of `python collect_env.py` Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.9 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-20) Clang version: Could not collect CMake version: version 3.26.5 Libc version: glibc-2.28 Python version: 3.11.6 | packaged by conda-forge | (main, Oct 3 2023, 10:40:35) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-4.18.0-513.18.1.el8_9.x86_64-x86_64-with-glibc2.28 Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA A40 Nvidia driver version: 550.54.14 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Thread(s) per core: 1 Core(s) per socket: 48 Socket(s): 2 NUMA node(s): 2 Vendor ID: AuthenticAMD CPU family: 25 Model: 17 Model name: AMD EPYC 9454 48-Core Processor Stepping: 1 CPU MHz: 2750.000 C...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: of `python collect_env.py` Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.9 (Green Obsidian) (x86...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.9 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 202...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ment ``` The output of `python collect_env.py` Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.9 (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: KVcache usage for different tasks in batch usage;stale ### Your current environment ``` The output of `python collect_env.py` Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
