# vllm-project/vllm#18393: [Bug]: `vllm serve` doesn't display detailed error logs when async_llm.generate raises an exception

| 字段 | 值 |
| --- | --- |
| Issue | [#18393](https://github.com/vllm-project/vllm/issues/18393) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `vllm serve` doesn't display detailed error logs when async_llm.generate raises an exception

### Issue 正文摘录

### Your current environment This bug is not environment-dependent. ### 🐛 Describe the bug ```python async def generate( self, prompt: PromptType, sampling_params: SamplingParams, request_id: str, lora_request: Optional[LoRARequest] = None, trace_headers: Optional[Mapping[str, str]] = None, prompt_adapter_request: Optional[PromptAdapterRequest] = None, splitwise_request: Optional[SplitwiseRequest] = None, priority: int = 0, ) -> AsyncGenerator[RequestOutput, None]: try: # some codes # If the request is disconnected by the client, generate() # is cancelled. So, we abort the request if we end up here. except asyncio.CancelledError: await self.abort(request_id) if self.log_requests: logger.info("Request %s aborted.", request_id) raise # Engine is dead. Do not abort since we shut down. except EngineDeadError: if self.log_requests: logger.info("Request %s failed (engine dead).", request_id) raise # Request validation error. except ValueError: if self.log_requests: logger.info("Request %s failed (bad request).", request_id) raise # Unexpected error in the generate() task (possibly recoverable). except Exception as e: await self.abort(request_id) if self.log_requests: logger.info("Reques...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: play detailed error logs when async_llm.generate raises an exception bug;stale ### Your current environment This bug is not environment-dependent. ### 🐛 Describe the bug ```python async def generate( self, prompt: Promp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ancelled. So, we abort the request if we end up here. except asyncio.CancelledError: await self.abort(request_id) if self.log_requests: logger.info("Request %s aborted.", request_id) raise # Engine is dead. Do not abort...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: a_request: Optional[LoRARequest] = None, trace_headers: Optional[Mapping[str, str]] = None, prompt_adapter_request: Optional[PromptAdapterRequest] = None, splitwise_request: Optional[SplitwiseRequest] = None, priority:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: etions HTTP/1.1" 500 Internal Server Error` without any detailed error information. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bott...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
