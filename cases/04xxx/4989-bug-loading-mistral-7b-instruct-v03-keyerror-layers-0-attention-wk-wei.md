# vllm-project/vllm#4989: [Bug]: Loading mistral-7B-instruct-v03 KeyError: 'layers.0.attention.wk.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#4989](https://github.com/vllm-project/vllm/issues/4989) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Loading mistral-7B-instruct-v03 KeyError: 'layers.0.attention.wk.weight'

### Issue 正文摘录

### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.8 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-20) Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.28 Python version: 3.9.13 (main, Oct 13 2022, 21:15:33) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-513.9.1.el8_9.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 PCIe Nvidia driver version: 535.129.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 256 On-line CPU(s) list: 0-255 Thread(s) per core: 2 Core(s) per socket: 64 Socket(s): 2 NUMA node(s): 2 Vendor ID: AuthenticAMD CPU family: 25 Model: 17 Model name: AMD EPYC 9534 64-Core Processor Stepping: 1 CPU MHz: 2450.000 CPU max MHz: 3718.0659 CPU min MHz: 1500.0000 BogoMIPS: 4900.22 Virtualization: AMD-V L1d cach...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 'layers.0.attention.wk.weight' bug ### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.8 (Green Obsidian) (x...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.8 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Re...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 PCIe Nvidia driver version: 535.129.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
