# vllm-project/vllm#24211: [Bug]: Detokenizer Overflow error occurred on DeepSeek-R1/V3

| 字段 | 值 |
| --- | --- |
| Issue | [#24211](https://github.com/vllm-project/vllm/issues/24211) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Detokenizer Overflow error occurred on DeepSeek-R1/V3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am currently using the DeepSeek-R1 AWQ quantized model, but very occasionally in production, the following error occurs and the engine crashes. ``` ERROR 08-20 23:41:35 [async_llm.py:408] AsyncLLM output_handler failed. ERROR 08-20 23:41:35 [async_llm.py:408] Traceback (most recent call last): ERROR 08-20 23:41:35 [async_llm.py:408] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/async_llm.py", line 384, in output_handler ERROR 08-20 23:41:35 [async_llm.py:408] processed_outputs = output_processor.process_outputs( ERROR 08-20 23:41:35 [async_llm.py:408] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 08-20 23:41:35 [async_llm.py:408] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/output_processor.py", line 350, in process_outputs ERROR 08-20 23:41:35 [async_llm.py:408] stop_string = req_state.detokenizer.update( ERROR 08-20 23:41:35 [async_llm.py:408] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 08-20 23:41:35 [async_llm.py:408] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/detokenizer.py", line 106, in update ERROR 08-20 23:41:35 [async_llm.py:408] self.output_text += self.decode_next(new_token_id) ERR...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # 🐛 Describe the bug I am currently using the DeepSeek-R1 AWQ quantized model, but very occasionally in production, the following error occurs and the engine crashes. ``` ERROR 08-20 23:41:35 [async_llm.py:408] AsyncLLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Detokenizer Overflow error occurred on DeepSeek-R1/V3 bug;stale ### Your current environment ### 🐛 Describe the bug I am currently using the DeepSeek-R1 AWQ quantized model, but very occasionally in production, t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 23:41:35 [async_llm.py:408] OverflowError: out of range integral type conversion attempted ``` This error occurs when the generated token ID is not present in the vocabulary. To investigate why this issue occurs, I chec...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ent ### 🐛 Describe the bug I am currently using the DeepSeek-R1 AWQ quantized model, but very occasionally in production, the following error occurs and the engine crashes. ``` ERROR 08-20 23:41:35 [async_llm.py:408] As...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
