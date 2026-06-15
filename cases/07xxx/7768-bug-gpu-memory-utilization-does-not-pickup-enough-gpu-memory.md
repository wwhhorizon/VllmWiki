# vllm-project/vllm#7768: [Bug]: gpu-memory-utilization does not pickup enough GPU memory

| 字段 | 值 |
| --- | --- |
| Issue | [#7768](https://github.com/vllm-project/vllm/issues/7768) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpu-memory-utilization does not pickup enough GPU memory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash vllm serve /model --port 8000 \ --trust-remote-code \ --served-model-name internvl2-internlm2 \ --uvicorn-log-level "info" \ --enable-chunked-prefill False \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 2 ``` the model is https://huggingface.co/OpenGVLab/InternVL2-8B, after server started, the gpu memory usage is low (as I tell vllm to pickup 90% of them): ``` +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.104.05 Driver Version: 535.104.05 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA GeForce RTX 4090 On | 00000000:1E:00.0 Off | Off | | 30% 26C P8 16W / 450W | 14214MiB / 24564MiB | 0% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ | 1 NVIDIA GeForce RTX 4090 On | 00000000:52:00.0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ----------------------------+ | NVIDIA-SMI 535.104.05 Driver Version: 535.104.05 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: --------------------------------------------------------------+ | NVIDIA-SMI 535.104.05 Driver Version: 535.104.05 CUDA Version: 12.2 | |-----------------------------------------+----------------------+-----------------...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Your current environment ### 🐛 Describe the bug ```bash vllm serve /model --port 8000 \ --trust-remote-code \ --served-model-name internvl2-internlm2 \ --uvicorn-log-level "info" \ --enable-chunked-prefill False \ --gpu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: gpu-memory-utilization does not pickup enough GPU memory bug;stale ### Your current environment ### 🐛 Describe the bug ```bash vllm serve /model --port 8000 \ --trust-remote-code \ --served-model-name internvl2-i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
