# vllm-project/vllm#6866: [Bug]: index out of bound for logits_processors cause vllm.engine.async_llm_engine.AsyncEngineDeadError

| 字段 | 值 |
| --- | --- |
| Issue | [#6866](https://github.com/vllm-project/vllm/issues/6866) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: index out of bound for logits_processors cause vllm.engine.async_llm_engine.AsyncEngineDeadError

### Issue 正文摘录

### Your current environment use the Vllm with phi3 model "microsoft/Phi-3-mini-128k-instruct" ### 🐛 Describe the bug The issue I think is user could give a token id which exceed the vocab size. And then this error cause the vllm.engine.async_llm_engine.AsyncEngineDeadError. The following sample actually not well decribe the issue. please check this call stack" 0] File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/logits_processor.py", line 59, in forward 0] logits = _apply_logits_processors(logits, sampling_metadata) 0] File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/logits_processor.py", line 116, in _apply_logits_processors 0] logits_row = logits_processor(past_tokens_ids, 0] File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/protocol.py", line 245, in logit_bias_logits_processor 0] logits[int(token_id)] += bias 0] IndexError: index 55434 is out of bounds for dimension 0 with size 32064 0] The above exception was the direct cause of the following exception: 0] Traceback (most recent call last): 0] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 54, in _log_task_completion 0] r...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ine 59, in forward 0] logits = _apply_logits_processors(logits, sampling_metadata) 0] File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/logits_processor.py", line 116, in _apply_logits_processors...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: EngineDeadError bug ### Your current environment use the Vllm with phi3 model "microsoft/Phi-3-mini-128k-instruct" ### 🐛 Describe the bug The issue I think is user could give a token id which exceed the vocab size. And...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
