# vllm-project/vllm#20362: [Bug]: Inconsistent behavior of AsyncLLMEngine.abort between v0 and v1

| 字段 | 值 |
| --- | --- |
| Issue | [#20362](https://github.com/vllm-project/vllm/issues/20362) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Inconsistent behavior of AsyncLLMEngine.abort between v0 and v1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using vllm as inference engine for RLHF, we rely on LLMEngine.abort_request or AsyncLLMEngine.abort to stop long running requests. The usage of AsyncLLMEngine.abort can be found in test https://github.com/vllm-project/vllm/blob/v0.9.1/tests/async_engine/test_async_llm_engine.py#L350 and https://github.com/vllm-project/vllm/blob/main/tests/v1/engine/test_async_llm.py#L185. When using v0 async engine, we can abort a request from other coroutine and the generate coroutine will raise asyncio.CancelledError. When using v1 async engine, we have to cancel the generation coroutine itself and if we abort the request but not cancel the generation coroutine, it will never return which is not expected and unfriendly for programming. So, my question is, can we change the behavior of AsyncLLM.abort (i.e. abort of v1 async engine) to raise asyncio.CancelledError if request is cancelled? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked qu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a request from other coroutine and the generate coroutine will raise asyncio.CancelledError. When using v1 async engine, we have to cancel the generation coroutine itself and if we abort the request but not cancel the g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nt ### 🐛 Describe the bug When using vllm as inference engine for RLHF, we rely on LLMEngine.abort_request or AsyncLLMEngine.abort to stop long running requests. The usage of AsyncLLMEngine.abort can be found in test ht...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: When using vllm as inference engine for RLHF, we rely on LLMEngine.abort_request or AsyncLLMEngine.abort to stop long running requests. The usage of AsyncLLMEngine.abort can be found in test https://github.com/vllm-proj...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ong running requests. The usage of AsyncLLMEngine.abort can be found in test https://github.com/vllm-project/vllm/blob/v0.9.1/tests/async_engine/test_async_llm_engine.py#L350 and https://github.com/vllm-project/vllm/blo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
