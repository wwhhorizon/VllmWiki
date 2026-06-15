# vllm-project/vllm#39270: [Bug]: Qwen3.5 crashes when using suffix-decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#39270](https://github.com/vllm-project/vllm/issues/39270) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 crashes when using suffix-decoding

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.7 (main, Mar 2 2026, 18:41:32) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-5.10.134-013.5.kangaroo.al8.x86_64-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H20-3e GPU 1: NVIDIA H20-3e GPU 2: NVIDIA H20-3e GPU 3: NVIDIA H20-3e GPU 4: NVIDIA H20-3e GPU 5: NVIDIA H20-3e GPU 6: NVIDIA H20-3e GPU 7: NVIDIA H20-3e Nvidia driver version : 535.230.02 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/...

## 现有链接修复摘要

#39695 Introduce De-dup/Similarity-Check in CI Workflow for PR/Issue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.7 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3.5 crashes when using suffix-decoding bug ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.1 LTS (x86_64) GC
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.6 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Vulnerable Vul...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39695](https://github.com/vllm-project/vllm/pull/39695) | mentioned | 0.6 | Introduce De-dup/Similarity-Check in  CI Workflow for PR/Issue | \| Issue A \| Issue B \| \|---\|---\|---\|---\|---\| \| 100% \| 100% \| 100% \| [#39270](https://github.com/vllm-project/vllm/issues/39270) [Bug]: Qwen3.5 crashes when using suffix-decoding \|… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
