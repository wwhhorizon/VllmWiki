# vllm-project/vllm#20745: [Usage]: What is the best way and parameters to serve LLM/VLM ? Facing OOM in 1x8 H200

| 字段 | 值 |
| --- | --- |
| Issue | [#20745](https://github.com/vllm-project/vllm/issues/20745) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;multimodal_vlm |
| 子分类 | memory |
| Operator 关键词 | gemm |
| 症状 | crash;oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: What is the best way and parameters to serve LLM/VLM ? Facing OOM in 1x8 H200

### Issue 正文摘录

**Python 3.10 vLLM 0.9.2** Hi vLLM team, I’m trying to serve the Qwen-2.5-72B Vision-Language model using vLLM on a single node with 8× H200 GPUs. Despite having such a large amount of GPU memory, I’m still facing OOM issues when trying to launch the model **with full parameters enabled.** When trying to serve the model with full parameters enabled (default model and vllm params), the pod crashes due to OOM errors. Oddly enough, I don’t see a clear error trace. It just crashes or gets killed by the OOM killer. **If I lower parameters like max_model_len and max_seqs_len, the model can load and serve successfully.** It’s quite surprising because I have over 1TB aggregate GPU memory (8×141 GB). I would expect this to be enough for a 70B model. These are the params to cause OOM: ``` disable_log_requests: True distributed_executor_backend: mp gpu_memory_utilization: 0.95 limit-mm-per-prompt: {'image': 5, 'video': 3} ``` 1 - **What are the optimal vLLM parameters that help avoid OOM and get best performance for my hardware?** 2 - **Should I consider pipeline parallelism?** **I’m also considering running:** 1 instance (1×8 GPUs) vs. 2 separate instances (2×4 GPUs each) Each instance woul...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: What is the best way and parameters to serve LLM/VLM ? Facing OOM in 1x8 H200 usage;stale **Python 3.10 vLLM 0.9.2** Hi vLLM team, I’m trying to serve the Qwen-2.5-72B Vision-Language model using vLLM on a sing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Usage]: What is the best way and parameters to serve LLM/VLM ? Facing OOM in 1x8 H200 usage;stale **Python 3.10 vLLM 0.9.2** Hi vLLM team, I’m trying to serve the Qwen-2.5-72B Vision-Language model using vLLM on a sing...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Usage]: What is the best way and parameters to serve LLM/VLM ? Facing OOM in 1x8 H200 usage;stale **Python 3.10 vLLM 0.9.2** Hi vLLM team, I’m trying to serve the Qwen-2.5-72B Vision-Language model using vLLM on a sing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: best way and parameters to serve LLM/VLM ? Facing OOM in 1x8 H200 usage;stale **Python 3.10 vLLM 0.9.2** Hi vLLM team, I’m trying to serve the Qwen-2.5-72B Vision-Language model using vLLM on a single node with 8× H200...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: use OOM: ``` disable_log_requests: True distributed_executor_backend: mp gpu_memory_utilization: 0.95 limit-mm-per-prompt: {'image': 5, 'video': 3} ``` 1 - **What are the optimal vLLM parameters that help avoid OOM and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
