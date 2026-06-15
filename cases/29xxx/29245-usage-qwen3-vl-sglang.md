# vllm-project/vllm#29245: [Usage]: 启动 qwen3 vl 超级超级超级慢，sglang 启动很快，可能的原因是什么？

| 字段 | 值 |
| --- | --- |
| Issue | [#29245](https://github.com/vllm-project/vllm/issues/29245) |
| 状态 | open |
| 标签 | usage;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: 启动 qwen3 vl 超级超级超级慢，sglang 启动很快，可能的原因是什么？

### Issue 正文摘录

### Your current environment 连执行 python collect_env.py 都很慢，环境是直接 uv 安装的 ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.2 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-5.10.134-19.100.al8.x86_64-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA L20Y GPU 1: NVIDIA L20Y GPU 2: NVIDIA L20Y GPU 3: NVIDIA L20Y GPU 4: NVIDIA L20Y GPU 5: NVIDIA L20Y GPU 6: NVIDIA L20Y GPU 7: NVIDIA L20Y Nvidia driver version : 570.148.08 cuDNN version : Pr...

## 现有链接修复摘要

#39695 Introduce De-dup/Similarity-Check in CI Workflow for PR/Issue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.2 Libc version : glibc-2.39 ==================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: 启动 qwen3 vl 超级超级超级慢，sglang 启动很快，可能的原因是什么？ usage;unstale ### Your current environment 连执行 python collect_env.py 都很慢，环境是直接 uv 安装的 ```text Collecting environment information... ============================== Syste...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Usage]: 启动 qwen3 vl 超级超级超级慢，sglang 启动很快，可能的原因是什么？ usage;unstale ### Your current environment 连执行 python collect_env.py 都很慢，环境是直接 uv 安装的 ```text Collecting environment information... ============================== Syste...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39695](https://github.com/vllm-project/vllm/pull/39695) | mentioned | 0.6 | Introduce De-dup/Similarity-Check in  CI Workflow for PR/Issue | issues/38642) [Usage]: 模型返回值reasoning_content \| \| 77% \| 92% \| 17% \| [#29245](https://github.com/vllm-project/vllm/issues/29245) [Usage]: 启动 qwen3 vl 超级超级超级慢，sglang 启动很快，可能的原因是什么？… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
