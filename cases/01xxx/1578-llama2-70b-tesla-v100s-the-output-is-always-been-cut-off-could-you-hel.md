# vllm-project/vllm#1578: llama2 70b,  Tesla V100s, the output is always been cut off,could you help to check it?

| 字段 | 值 |
| --- | --- |
| Issue | [#1578](https://github.com/vllm-project/vllm/issues/1578) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | sampling |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> llama2 70b,  Tesla V100s, the output is always been cut off,could you help to check it?

### Issue 正文摘录

configuration: Tesla V100S GPU memory: 32768MiB*8 params: "n": 1, "top_k": 30, "top_p": 0.85, "use_beam_search": False, "max_tokens": 8192, "length_penalty":1.0, "ignore_eos":True, the output is always been cut off. use the stream mode, partof code as follows. if stream_flag is True: # Streaming case async def stream_results() -> AsyncGenerator[bytes, None]: completion_output = '' previous_length = 0 async for request_output in results_generator: # print('request_output:', request_output) # print('vars(request_output):', vars(request_output)) text_outputs = [ output.text for output in request_output.outputs ] completion_output = ''.join(text_outputs) logger.info(f'completion_output: {completion_output}') new_string = completion_output[previous_length:] previous_length = len(completion_output) yield new_string.encode("utf-8") end_time = get_datetime_now_obj() duration = (end_time - start_time).seconds

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llama2 70b, Tesla V100s, the output is always been cut off,could you help to check it? configuration: Tesla V100S GPU memory: 32768MiB*8 params: "n": 1, "top_k": 30, "top_p": 0.85, "use_beam_sea
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: "n": 1, "top_k": 30, "top_p": 0.85, "use_beam_search": False, "max_tokens": 8192, "length_penalty":1.0, "ignore_eos":True, the output is always been cut off. use the stream mode, partof code as follows. if stream_flag i...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ays been cut off,could you help to check it? configuration: Tesla V100S GPU memory: 32768MiB*8 params: "n": 1, "top_k": 30, "top_p": 0.85, "use_beam_search": False, "max_tokens": 8192, "length_penalty":1.0, "ignore_eos"...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ": 1, "top_k": 30, "top_p": 0.85, "use_beam_search": False, "max_tokens": 8192, "length_penalty":1.0, "ignore_eos":True, the output is always been cut off. use the stream mode, partof code as follows. if stream_flag is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: letion_output = '' previous_length = 0 async for request_output in results_generator: # print('request_output:', request_output) # print('vars(request_output):', vars(request_output)) text_outputs = [

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
