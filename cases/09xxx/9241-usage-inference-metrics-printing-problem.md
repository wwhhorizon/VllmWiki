# vllm-project/vllm#9241: [Usage]: Inference  metrics printing problem

| 字段 | 值 |
| --- | --- |
| Issue | [#9241](https://github.com/vllm-project/vllm/issues/9241) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Inference  metrics printing problem

### Issue 正文摘录

Regarding the issue of adding print statements to the generate method in async_llm_engine.py to print inference metrics. **In version 0.5.3, i can output some inference indicators by adding the following code:** ``` async def generate( self, inputs: PromptInputs, sampling_params: SamplingParams, request_id: str, lora_request: Optional[LoRARequest] = None, trace_headers: Optional[Mapping[str, str]] = None, prompt_adapter_request: Optional[PromptAdapterRequest] = None ) -> AsyncIterator[RequestOutput]: async for output in self._process_request( request_id, inputs, sampling_params, lora_request=lora_request, trace_headers=trace_headers, prompt_adapter_request=prompt_adapter_request, ): print(f"[async_llm_engine][AsyncLLMEngine][generate] output = {output}") ### i am here!!!!!!! yield LLMEngine.validate_output(output, RequestOutput) ``` **In version 0.6.2, the same code modification method does not display the relevant inference indicators on the terminal?** ``` async def generate( self, inputs: PromptInputs, sampling_params: SamplingParams, request_id: str, lora_request: Optional[LoRARequest] = None, trace_headers: Optional[Mapping[str, str]] = None, prompt_adapter_request: Optional[...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: generate method in async_llm_engine.py to print inference metrics. **In version 0.5.3, i can output some inference indicators by adding the following code:** ``` async def generate( self, inputs: PromptInputs, sampling_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Inference metrics printing problem usage;stale Regarding the issue of adding print statements to the generate method in async_llm_engine.py to print inference metrics. **In version 0.5.3, i can output some infe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: a_request: Optional[LoRARequest] = None, trace_headers: Optional[Mapping[str, str]] = None, prompt_adapter_request: Optional[PromptAdapterRequest] = None ) -> AsyncIterator[RequestOutput]: async for output in self._proc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
