# vllm-project/vllm#4904: [Bug]: llm_engine_example.py (more requests) get stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#4904](https://github.com/vllm-project/vllm/issues/4904) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llm_engine_example.py (more requests) get stuck

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.10.0-23-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A5000 GPU 1: NVIDIA RTX A5000 GPU 2: NVIDIA RTX A5000 GPU 3: NVIDIA RTX A5000 Nvidia driver version: 545.23.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 43 bits physical, 48 bits virtual CPU(s): 32 On-line CPU(s) list: 0-31 Thread(s) per core: 1 Core(s) per socket: 16 Socket(s): 2 NUMA node(s): 8 Vendor ID: AuthenticAMD CPU family: 23 Model: 49 Model name: AMD EPYC 7302 16-Core...

## 现有链接修复摘要

#6223 [ BugFix ] Prompt Logprobs Detokenization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: PyTorch version: 2.3.0+cu121 Is debug build: False
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ro irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbya sid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca Versions of re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: stuck bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debu
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: llm_engine_example.py (more requests) get stuck bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6223](https://github.com/vllm-project/vllm/pull/6223) | closes_keyword | 0.95 | [ BugFix ] Prompt Logprobs Detokenization | FIX #4904 FIX #4772 FIX #5334 FIX #5872 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <detai |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
