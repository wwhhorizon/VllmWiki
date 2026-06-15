# vllm-project/vllm#19402: [Feature]: collective_rpc_async for the offline `LLM` class?

| 字段 | 值 |
| --- | --- |
| Issue | [#19402](https://github.com/vllm-project/vllm/issues/19402) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: collective_rpc_async for the offline `LLM` class?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, the LLM class provides the synchronous `collective_rpc` method, while the AsyncLLMEngine class provides a method of the same name via `async def`. While adapting the [offline RLHF example](https://github.com/vllm-project/vllm/blob/9368cc90b2d2aaa359398a1b97c2313fb39c8de7/examples/offline_inference/rlhf.py), we find it sometimes inconvenient to use the collective_rpc mechanism to execute blocking operations. **Therefore, how about providing an explicit `collective_rpc_async` method in the `LLM` class** to facilitate this pattern and avoid the boilerplates? I can see that some underlying LLMEngine classes already implement a method of this name, albeit perhaps for a different use case. I'd be happy to contribute a PR for this. Please let me know your thoughts and if there is already work in progress on this. Thanks! ### Alternatives The current workaround is to wrap the call with an async wrapper: ``` async def async_call(func, *args, **kwargs): return await asyncio.to_thread(func, *args, **kwargs) ... await asyncio.gather( async_call( llm.collective_rpc, ... ), ... ) ``` ### Additional context _No response_ ### Before submitting a...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .py), we find it sometimes inconvenient to use the collective_rpc mechanism to execute blocking operations. **Therefore, how about providing an explicit `collective_rpc_async` method in the `LLM` class** to facilitate t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: collective_rpc_async for the offline `LLM` class? feature request;stale ### 🚀 The feature, motivation and pitch Currently, the LLM class provides the synchronous `collective_rpc` method, while the AsyncLLMEng...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: o execute blocking operations. **Therefore, how about providing an explicit `collective_rpc_async` method in the `LLM` class** to facilitate this pattern and avoid the boilerplates? I can see that some underlying LLMEng...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: it sometimes inconvenient to use the collective_rpc mechanism to execute blocking operations. **Therefore, how about providing an explicit `collective_rpc_async` method in the `LLM` class** to facilitate this pattern an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: method of the same name via `async def`. While adapting the [offline RLHF example](https://github.com/vllm-project/vllm/blob/9368cc90b2d2aaa359398a1b97c2313fb39c8de7/examples/offline_inference/rlhf.py), we find it somet...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
