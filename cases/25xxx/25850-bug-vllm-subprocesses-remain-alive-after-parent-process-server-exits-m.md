# vllm-project/vllm#25850: [Bug]: vLLM subprocesses remain alive after parent process/server exits (MCP client exit → vLLM still alive)

| 字段 | 值 |
| --- | --- |
| Issue | [#25850](https://github.com/vllm-project/vllm/issues/25850) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM subprocesses remain alive after parent process/server exits (MCP client exit → vLLM still alive)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # vLLM subprocesses remain alive after parent process/server exits (MCP client exit → vLLM still alive) ## Overview I am developing a project using **MCP (Model Context Protocol)** where a **client** orchestrates multiple **servers**. One of these servers is a **generation server** that loads an LLM and performs inference. When I use **vLLM** as the backend, the client runs and terminates correctly, and the server should exit as well. However, **vLLM subprocesses remain alive after the server exits**, leading to **GPU memory not being released** and lingering `vllm` worker processes. I would like to know **how to detect the parent process termination inside vLLM’s subprocesses and gracefully clean up the instantiated `LLM` object and all worker processes**. Is there an **official graceful shutdown API** or recommended practice for this? --- ## Project and Code Links - Repository (my project): - Generation server (loads LLM): - MCP client (triggers and terminates server): In `generation.py` I use vLLM as the backend to load the model and perform inference. When the client exits (or the server itself exits), **vLLM-related processe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nstantiated `LLM` object and all worker processes**. Is there an **official graceful shutdown API** or recommended practice for this? --- ## Project and Code Links - Repository (my project): - Generation server (loads L...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ter parent process/server exits (MCP client exit → vLLM still alive) bug;stale ### Your current environment ### 🐛 Describe the bug # vLLM subprocesses remain alive after parent process/server exits (MCP client exit → vL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: * that loads an LLM and performs inference. When I use **vLLM** as the backend, the client runs and terminates correctly, and the server should exit as well. However, **vLLM subprocesses remain alive after the server ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sequence (stop scheduler → stop engine → stop workers)? 4. For MCP-based architectures where servers are spawned and terminated by a client, is there an example of vLLM being embedded and cleanly shut down in such a con...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: **vLLM subprocesses remain alive after the server exits**, leading to **GPU memory not being released** and lingering `vllm` worker processes. I would like to know **how to detect the parent process termination inside v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
