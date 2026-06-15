# vllm-project/vllm#19409: [Bug]: RuntimeError: Invalid MNK = [0, 4096, 512]  The above exception was the direct cause of the following exception:

| 字段 | 值 |
| --- | --- |
| Issue | [#19409](https://github.com/vllm-project/vllm/issues/19409) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Invalid MNK = [0, 4096, 512]  The above exception was the direct cause of the following exception:

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This should never happen! Please open an issue on GitHub. See stack trace above for the actual cause. ERROR 06-09 11:40:52 [serving_chat.py:883] Error in chat completion stream generator. ERROR 06-09 11:40:52 [serving_chat.py:883] Traceback (most recent call last): ERROR 06-09 11:40:52 [serving_chat.py:883] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_chat.py", line 485, in chat_completion_stream_generator ERROR 06-09 11:40:52 [serving_chat.py:883] async for res in result_generator: ERROR 06-09 11:40:52 [serving_chat.py:883] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/async_llm_engine.py", line 1040, in generate ERROR 06-09 11:40:52 [serving_chat.py:883] async for output in await self.add_request( ERROR 06-09 11:40:52 [serving_chat.py:883] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/async_llm_engine.py", line 116, in generator ERROR 06-09 11:40:52 [serving_chat.py:883] raise result ERROR 06-09 11:40:52 [serving_chat.py:883] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/async_llm_e...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: The above exception was the direct cause of the following exception: bug;stale ### Your current environment ### 🐛 Describe the bug vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This shou...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rd ERROR 06-09 11:40:52 [serving_chat.py:883] output_parallel = self.quant_method.apply(self, input_, bias) ERROR 06-09 11:40:52 [serving_chat.py:883] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-09 11:40:52 [se...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 83] return self.impl.forward(self, query, key, value, kv_cache, attn_metadata) ERROR 06-09 11:40:52 [serving_chat.py:883] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-09 11:40:52 [serving...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t.py:883] File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/mla/common.py", line 1413, in forward ERROR 06-09 11:40:52 [serving_chat.py:883] output[:num_prefill_tokens] = self._forward_prefill( ERROR...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: async ERROR 06-09 11:40:52 [serving_chat.py:883] results = await asyncio.gather(*tasks) ERROR 06-09 11:40:52 [serving_chat.py:883] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-09 11:40:52 [serving_chat.py:883] File "/usr/local...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
