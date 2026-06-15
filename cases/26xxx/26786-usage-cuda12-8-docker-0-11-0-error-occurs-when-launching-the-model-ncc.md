# vllm-project/vllm#26786: [Usage]: cuda12.8 docker 0.11.0 Error occurs when launching the model, NCCL error: unhandled cuda error.

| 字段 | 值 |
| --- | --- |
| Issue | [#26786](https://github.com/vllm-project/vllm/issues/26786) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: cuda12.8 docker 0.11.0 Error occurs when launching the model, NCCL error: unhandled cuda error.

### Issue 正文摘录

When I use only a single graphics card, the system can start up normally. Below are Docker configuration files, logs, and environment information. I encountered this issue when upgrading from version 10.1.1 to 10.2. [The system generates an error when using dual graphics cards; version 10.1.1 functions correctly, but version 10.2 triggers an error upon execution.](https://github.com/vllm-project/vllm/issues/25813) ### Your current environment ```text # vllm collect-env INFO 10-14 19:07:58 [__init__.py:216] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Usage]: cuda12.8 docker 0.11.0 Error occurs when launching the model, NCCL error: unhandled cuda error. usage When I use only a single graphics card, the system can start up normally. Below are Docker configuration fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: cuda12.8 docker 0.11.0 Error occurs when launching the model, NCCL error: unhandled cuda error. usage When I use only a single graphics card, the system can start up normally. Below are Docker configuration fil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: cuda12.8 docker 0.11.0 Error occurs when launching the model, NCCL error: unhandled cuda error. usage When I use only a single graphics card, the system can start up normally. Below are Docker configuration fil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT Host state unknown Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Mitigation; IBRS Vu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.3.1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
