# vllm-project/vllm#21951: [Bug]: Incremental detokenization error when running `llama-3.3-70b-fp8` model

| 字段 | 值 |
| --- | --- |
| Issue | [#21951](https://github.com/vllm-project/vllm/issues/21951) |
| 状态 | closed |
| 标签 | bug;help wanted;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incremental detokenization error when running `llama-3.3-70b-fp8` model

### Issue 正文摘录

Recently reported by @npalaska: > we have been seeing the following error with vLLM 0.9.2 and transformers 4.52.4 when serving the llama-3.3-70b-fp8 and recently with maverick fp8 as well. ``` INFO: 10.131.1.21:55318 - "POST /v1/completions HTTP/1.1" 200 OK ERROR 07-24 22:01:26 [async_llm.py:419] AsyncLLM output_handler failed. ERROR 07-24 22:01:26 [async_llm.py:419] Traceback (most recent call last): ERROR 07-24 22:01:26 [async_llm.py:419] File "/opt/app-root/lib64/python3.12/site-packages/vllm/v1/engine/async_llm.py", line 396, in output_handler ERROR 07-24 22:01:26 [async_llm.py:419] processed_outputs = output_processor.process_outputs( ERROR 07-24 22:01:26 [async_llm.py:419] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 07-24 22:01:26 [async_llm.py:419] File "/opt/app-root/lib64/python3.12/site-packages/vllm/v1/engine/output_processor.py", line 398, in process_outputs ERROR 07-24 22:01:26 [async_llm.py:419] stop_string = req_state.detokenizer.update( ERROR 07-24 22:01:26 [async_llm.py:419] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 07-24 22:01:26 [async_llm.py:419] File "/opt/app-root/lib64/python3.12/site-packages/vllm/v1/engine/detokenizer.py", line 117, in update ERROR 07-24 22:01:26 [a...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: okenization error when running `llama-3.3-70b-fp8` model bug;help wanted;stale Recently reported by @npalaska: > we have been seeing the following error with vLLM 0.9.2 and transformers 4.52.4 when serving the llama-3.3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Incremental detokenization error when running `llama-3.3-70b-fp8` model bug;help wanted;stale Recently reported by @npalaska: > we have been seeing the following error with vLLM 0.9.2 and transformers 4.52.4 when...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Incremental detokenization error when running `llama-3.3-70b-fp8` model bug;help wanted;stale Recently reported by @npalaska: > we have been seeing the following error with vLLM 0.9.2 and transformers 4.52.4 when...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 22:01:26 [async_llm.py:419] OverflowError: out of range integral type conversion attempted WARNING 07-24 22:01:26 [protocol.py:58] The following fields were present in the request but ignored: {'max_completion_tokens'}...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 92 - --no-enable-prefix-caching - --disable-log-requests - --kv-cache-dtype=fp8 ``` Used the [guidellm](https://github.com/vllm-project/guidellm) to run the performance sweep: ``` guidellm benchmark --target ' ' \ --mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
