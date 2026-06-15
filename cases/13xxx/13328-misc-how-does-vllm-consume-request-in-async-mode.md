# vllm-project/vllm#13328: [Misc]:  How does vllm consume request in async mode？

| 字段 | 值 |
| --- | --- |
| Issue | [#13328](https://github.com/vllm-project/vllm/issues/13328) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]:  How does vllm consume request in async mode？

### Issue 正文摘录

### Anything you want to discuss about vllm. I am new to vLLM project. I wonder how vllm model consumes input request after AsyncLLMEngine.generate when you deploy in openai compatible way. I have read the [document](https://docs.vllm.ai/en/latest/design/arch_overview.html) but I did not find how these two processors communicate. Do I miss something ? ```Python try: async for output in await self.add_request( request_id, prompt, sampling_params, lora_request=lora_request, trace_headers=trace_headers, prompt_adapter_request=prompt_adapter_request, priority=priority, ): yield LLMEngine.validate_output(output, RequestOutput) except asyncio.CancelledError: await self.abort(request_id) raise ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: How does vllm consume request in async mode？ stale ### Anything you want to discuss about vllm. I am new to vLLM project. I wonder how vllm model consumes input request after AsyncLLMEngine.generate when you dep...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ield LLMEngine.validate_output(output, RequestOutput) except asyncio.CancelledError: await self.abort(request_id) raise ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le way. I have read the [document](https://docs.vllm.ai/en/latest/design/arch_overview.html) but I did not find how these two processors communicate. Do I miss something ? ```Python try: async for output in await self.a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: want to discuss about vllm. I am new to vLLM project. I wonder how vllm model consumes input request after AsyncLLMEngine.generate when you deploy in openai compatible way. I have read the [document](https://docs.vllm.a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nai compatible way. I have read the [document](https://docs.vllm.ai/en/latest/design/arch_overview.html) but I did not find how these two processors communicate. Do I miss something ? ```Python try: async for output in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
