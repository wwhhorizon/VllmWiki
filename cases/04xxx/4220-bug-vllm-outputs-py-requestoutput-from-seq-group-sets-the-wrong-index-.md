# vllm-project/vllm#4220: [Bug]: vllm/outputs.py: RequestOutput.from_seq_group sets the wrong index for generated `CompletionOutput`s, causing IndexError in OpenAIServingChat.chat_completion_stream_generator

| 字段 | 值 |
| --- | --- |
| Issue | [#4220](https://github.com/vllm-project/vllm/issues/4220) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm/outputs.py: RequestOutput.from_seq_group sets the wrong index for generated `CompletionOutput`s, causing IndexError in OpenAIServingChat.chat_completion_stream_generator

### Issue 正文摘录

### Your current environment ```text vLLM Version: 0.4.1 ``` ### 🐛 Describe the bug The chat completion stream generator expects the `index` field to be a number in range(request.n). vllm/entrypoints/openai/serving_chat.py:177 ```python for output in res.outputs: i = output.index if finish_reason_sent[i]: continue ``` However, RequestOutput.from_seq_group sets index to seqs.index(seq). vllm/outputs.py:116 ```python outputs = [ CompletionOutput(seqs.index(seq), seq.get_output_text_to_return(text_buffer_length), seq.get_output_token_ids(), seq.get_cumulative_logprob(), seq.output_logprobs if include_logprobs else None, SequenceStatus.get_finished_reason(seq.status), seq.stop_reason) for seq in top_n_seqs ] ``` where top_n_seqs is the top scored sequences and seqs is the *unsorted* original sequence list. Thus the indexes could be out of range (requests.n). This will cause a list index out of range error in the streaming generator.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm/outputs.py: RequestOutput.from_seq_group sets the wrong index for generated `CompletionOutput`s, causing IndexError in OpenAIServingChat.chat_completion_stream_generator bug;stale ### Your current environmen...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on_stream_generator bug;stale ### Your current environment ```text vLLM Version: 0.4.1 ``` ### 🐛 Describe the bug The chat completion stream generator expects the `index` field to be a number in range(request.n). vllm/e...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ), seq.output_logprobs if include_logprobs else None, SequenceStatus.get_finished_reason(seq.status), seq.stop_reason) for seq in top_n_seqs ] ``` where top_n_seqs is the top scored sequences and s

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
