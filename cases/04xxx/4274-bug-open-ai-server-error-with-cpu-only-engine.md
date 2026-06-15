# vllm-project/vllm#4274: [Bug]: Open AI server error with CPU only engine

| 字段 | 值 |
| --- | --- |
| Issue | [#4274](https://github.com/vllm-project/vllm/issues/4274) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Open AI server error with CPU only engine

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.36 Python version: 3.10.13 (main, Dec 19 2023, 20:49:50) [GCC 12.2.0] (64-bit runtime) Python platform: Linux-5.16.0-rc8-intel-next-01534-g53cb5f883cf7-x86_64-with-glibc2.36 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 224 On-line CPU(s) list: 0-223 Vendor ID: GenuineIntel Model name: Genuine Intel(R) CPU 0000%@ CPU family: 6 Model: 143 Thread(s) per core: 2 Core(s) per socket: 56 Socket(s): 2 Stepping: 3 CPU(s) scaling MHz: 100% CPU max MHz: 1900.0000 CPU min MHz: 800.0000 BogoMIPS:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Open AI server error with CPU only engine bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: None ROC...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req hfi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ironment information... PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: environment information... PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
