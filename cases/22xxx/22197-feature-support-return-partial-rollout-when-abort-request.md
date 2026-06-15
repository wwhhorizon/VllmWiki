# vllm-project/vllm#22197: [Feature]: Support return partial rollout when abort request

| 字段 | 值 |
| --- | --- |
| Issue | [#22197](https://github.com/vllm-project/vllm/issues/22197) |
| 状态 | closed |
| 标签 | feature request;rl |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support return partial rollout when abort request

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Partial rollout is critical to address long-tail problem in RL. For now, `AsyncLLM.abort` doesn't return the partial generated tokens: https://github.com/vllm-project/vllm/blob/main/vllm/v1/engine/async_llm.py#L435-L442 We can implement partial rollout by put each request's tokens generated so far to its output queue: ```python class AsyncLLMServer: def __init__(self): self.engine = AsyncLLM.from_vllm_config(vllm_config) async def _abort_requests(self): request_states = self.engine.output_processor.request_states request_ids = list(request_states.keys()) print(f"abort {len(request_ids)} request_ids: {request_ids}") # put each request's tokens generated so far to its output queue for req_state in request_states.values(): request_output = req_state.make_request_output([], FinishReason.ABORT, None) req_state.queue.put(request_output) # abort all unfinished generation requests self.engine.output_processor.abort_requests(request_ids) await self.engine.engine_core.abort_requests_async(request_ids) ``` It's better vLLM officially support it. cc @youkaichao ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a n...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support return partial rollout when abort request feature request;rl ### 🚀 The feature, motivation and pitch Partial rollout is critical to address long-tail problem in RL. For now, `AsyncLLM.abort` doesn't r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: engine_core.abort_requests_async(request_ids) ``` It's better vLLM officially support it. cc @youkaichao ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Mak...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Server: def __init__(self): self.engine = AsyncLLM.from_vllm_config(vllm_config) async def _abort_requests(self): request_states = self.engine.output_processor.request_states request_ids = list(request_states.keys()) pr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
