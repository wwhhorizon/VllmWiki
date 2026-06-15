# vllm-project/vllm#37658: [Bug]: Frontend Abort Fails to Stop Qwen3.5-122B Generation Loop, vLLM Backend Runs Indefinitely with Near-Full GPU Memory Utilization

| 字段 | 值 |
| --- | --- |
| Issue | [#37658](https://github.com/vllm-project/vllm/issues/37658) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Frontend Abort Fails to Stop Qwen3.5-122B Generation Loop, vLLM Backend Runs Indefinitely with Near-Full GPU Memory Utilization

### Issue 正文摘录

### Your current environment - Model: Qwen/Qwen3.5-122B-A10B - Inference Framework: vLLM 0.17.1 (official stable release) - GPU Hardware: NVIDIA RTX 6000D (multi-GPU tensor parallelism enabled) - Deployment Mode: vLLM OpenAI-compatible API Server ### 🐛 Describe the bug When deploying and running the Qwen/Qwen3.5-122B-A10B model via the vLLM 0.17.1 API server, I have encountered a severe blocking issue: sending an abort or stop generation request from the frontend fails to terminate the backend inference process, and the model falls into an uncontrollable infinite generation loop instead. The detailed abnormal behavior is as follows: 1. The frontend triggers a normal generation request to the vLLM API server, and the model starts generating tokens normally. 2. During the model generation process, I click the **abort output/stop generation** button on the frontend to terminate the current request immediately. 3. The frontend stops displaying the output stream as expected, but the**backend vLLM engine does not terminate the generation task at all** — the model falls into an infinite generation loop and keeps outputting tokens non-stop. 4. The backend keeps printing real-time generati...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: encountered a severe blocking issue: sending an abort or stop generation request from the frontend fails to terminate the backend inference process, and the model falls into an uncontrollable infinite generation loop in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Framework: vLLM 0.17.1 (official stable release) - GPU Hardware: NVIDIA RTX 6000D (multi-GPU tensor parallelism enabled) - Deployment Mode: vLLM OpenAI-compatible API Server ### 🐛 Describe the bug When deploying and run...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: n3.5-122B Generation Loop, vLLM Backend Runs Indefinitely with Near-Full GPU Memory Utilization bug ### Your current environment - Model: Qwen/Qwen3.5-122B-A10B - Inference Framework: vLLM 0.17.1 (official stable releas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Frontend Abort Fails to Stop Qwen3.5-122B Generation Loop, vLLM Backend Runs Indefinitely with Near-Full GPU Memory Utilization bug ### Your current environment - Model: Qwen/Qwen3.5-122B-A10B - Inference Framewo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tinuously, showing 1 running request all the time with stable generation throughput, and the request is never cleared from the engine queue. 5. GPU memory utilization spikes to nearly 100% and remains stuck at this high...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
