# vllm-project/vllm#24584: [Bug]: vLLM Runtime Fails to Honor Context Cancellation During Streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#24584](https://github.com/vllm-project/vllm/issues/24584) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support |
| 子分类 | throughput |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM Runtime Fails to Honor Context Cancellation During Streaming

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Missing Backend Request Cancellation in AsyncLLMEngine.generate() Method When asyncio.CancelledError is caught, the current implementation only calls self.abort(request_id) which handles client-side stream cleanup but does not cancel the actual backend processing. This leads to: - Resource Waste: The backend continues processing requests that are no longer needed - Memory Leaks: Accumulated abandoned requests can cause memory issues - Performance Degradation: Resources tied up with cancelled requests slow down processing for active users - Inefficient Resource Utilization: GPU/CPU cycles are wasted on computations that won't be consumed The backend engine has its own abort_request() method that should be called to immediately stop processing This issue is particularly critical in production environments where: - Users frequently disconnect from long-running requests - High request volumes can lead to resource exhaustion - Cost optimization is important for GPU-based inference workloads - Real-time applications require immediate resource cleanup To reproduce: A vllm inference server was created on geema2b model on cpu mode After r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ackend Request Cancellation in AsyncLLMEngine.generate() Method When asyncio.CancelledError is caught, the current implementation only calls self.abort(request_id) which handles client-side stream cleanup but does not c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: g;stale ### Your current environment ### 🐛 Describe the bug Missing Backend Request Cancellation in AsyncLLMEngine.generate() Method When asyncio.CancelledError is caught, the current implementation only calls self.abor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ogs ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: vLLM Runtime Fails to Honor Context Cancellation During Streaming bug;stale ### Your current environment ### 🐛 Describe the bug Missing Backend Request Cancellation in AsyncLLMEngine.generate() Method When asyncio.Ca...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: d continues showing logs like: 05:37:55: Running: 1 reqs, Avg generation throughput: 7.8 tokens/s Request finally completes at 05:40:58 (3+ minutes later) Expected Behavior When a client disconnects during streaming: HT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
