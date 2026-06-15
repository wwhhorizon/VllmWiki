# vllm-project/vllm#11173: [Installation]: XPU dependencies are missing

| 字段 | 值 |
| --- | --- |
| Issue | [#11173](https://github.com/vllm-project/vllm/issues/11173) |
| 状态 | closed |
| 标签 | installation;intel-gpu;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: XPU dependencies are missing

### Issue 正文摘录

### Your current environment ```text [W1213 12:52:10.163702538 OperatorEntry.cpp:155] Warning: Warning only once for all operators, other operators may also be overridden. Overriding a previously registered kernel for the same operator and the same dispatch key operator: aten::_cummax_helper(Tensor self, Tensor(a!) values, Tensor(b!) indices, int dim) -> () registered at /build/pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 dispatch key: XPU previous kernel: registered at /build/pytorch/build/aten/src/ATen/RegisterCPU.cpp:30476 new kernel: registered at /build/intel-pytorch-extension/build/Release/csrc/gpu/csrc/aten/generated/ATen/RegisterXPU.cpp:2971 (function operator()) Collecting environment information... PyTorch version: 2.5.1+cxx11.abi Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Arch Linux (x86_64) GCC version: (GCC) 14.2.1 20240910 Clang version: 18.1.8 CMake version: version 3.31.1 Libc version: glibc-2.40 Python version: 3.10.16 | packaged by conda-forge | (main, Dec 5 2024, 14:16:10) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-6.12.4-arch1-1-x86_64-with-glibc2.40 Is CUDA available: False CUDA runtime version: No...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: XPU dependencies are missing installation;intel-gpu;stale ### Your current environment ```text [W1213 12:52:10.163702538 OperatorEntry.cpp:155] Warning: Warning only once for all operators, other operato
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Installation]: XPU dependencies are missing installation;intel-gpu;stale ### Your current environment ```text [W1213 12:52:10.163702538 OperatorEntry.cpp:155] Warning: Warning only once for all operators, other operato...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfth...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nt information... PyTorch version: 2.5.1+cxx11.abi Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Arch Linux (x86_64) GCC version: (GCC) 14.2.1 20240910 Clang version: 18.1.8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ATen/RegisterXPU.cpp:2971 (function operator()) Collecting environment information... PyTorch version: 2.5.1+cxx11.abi Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Arch Linu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
