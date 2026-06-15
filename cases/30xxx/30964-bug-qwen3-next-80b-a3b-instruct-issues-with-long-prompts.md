# vllm-project/vllm#30964: [Bug]: Qwen3-Next-80B-A3B-Instruct issues with long prompts

| 字段 | 值 |
| --- | --- |
| Issue | [#30964](https://github.com/vllm-project/vllm/issues/30964) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next-80B-A3B-Instruct issues with long prompts

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.2.0 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.13 (main, Jun 5 2025, 13:12:00) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.10.134-16.3.al8.x86_64-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20-3e GPU 1: NVIDIA H20-3e GPU 2: NVIDIA H20-3e GPU 3: NVIDIA H20-3e GPU 4: NVIDIA H20-3e GPU 5: NVIDIA H20-3e GPU 6: NVIDIA H20-3e GPU 7: NVIDIA H20-3e Nvidia driver version : 570.133.20 cuDNN version : Probably one of the following: /us...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.2.0 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.13 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-Next-80B-A3B-Instruct issues with long prompts bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.4.1 [pip3] galore-torch==1.0 [pip3] nccl-xray==2.26.2rc2+xray1.1.0 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.8.4.1 [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
