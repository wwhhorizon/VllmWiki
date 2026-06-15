# vllm-project/vllm#23697: [Bug]: Recycling request IDs can lead to requests leaking in the engine due to race condition in the cancellation logic

| 字段 | 值 |
| --- | --- |
| Issue | [#23697](https://github.com/vllm-project/vllm/issues/23697) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Recycling request IDs can lead to requests leaking in the engine due to race condition in the cancellation logic

### Issue 正文摘录

### Your current environment env independent (only have reproed it in offline mode) ### 🐛 Describe the bug We're seeing VLLM hangs when we recycle request ids, I am pretty certain that this is due to a race condition in the engine when aborting requests: https://github.com/vllm-project/vllm/blob/main/vllm/v1/engine/async_llm.py#L463 Given this logic, it is possible to get into a state where a request id is popped from the output processor, but not from the engine core. This is fine in most cases, except when the user reuses a request id. When an abort is in flight this can lead to the following race: [Abort] Output processor drops the request with ID X [Add Request] New request with ID X comes in [Add Request] New request with ID X is added to the engine core [Abort] Engine core aborts request with ID X, aborting the new instance as well. In this case the engine core and the output processor get out of sync and that particular request is leaked Rough repro: ``` from vllm.v1.engine.async_llm import AsyncLLM prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Yap a lot sampling_params = SamplingParams(tempe...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Recycling request IDs can lead to requests leaking in the engine due to race condition in the cancellation logic bug;stale ### Your current environment env independent (only have reproed it in offline mode) ### 🐛...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cular request is leaked Rough repro: ``` from vllm.v1.engine.async_llm import AsyncLLM prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Yap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _p=0.95) # Add a sleep in abort to make it easy to repro llm = AsyncLLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params, "request_id", None) llm.abort("request_id") outputs = llm.generate(prom...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
