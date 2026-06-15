# vllm-project/vllm#7915: [Feature]: Does VLLM only support MistralModel Architecture for embedding?

| 字段 | 值 |
| --- | --- |
| Issue | [#7915](https://github.com/vllm-project/vllm/issues/7915) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Does VLLM only support MistralModel Architecture for embedding?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Does VLLM only support MistralModel Architecture for embedding? ``` _EMBEDDING_MODELS = { "MistralModel": ("llama_embedding", "LlamaEmbeddingModel"), } ``` I tried to force embedding_mode to true `model_config.embedding_mode = True,` this error raised: ``` Activating the server engine with embedding enabled. INFO 08-27 14:54:06 async_llm_engine.py:173] Added request embd-69a08211c22a4db9baa14c2da3db9dcd-0. ERROR 08-27 14:54:06 async_llm_engine.py:56] Engine background task failed ERROR 08-27 14:54:06 async_llm_engine.py:56] Traceback (most recent call last): ERROR 08-27 14:54:06 async_llm_engine.py:56] File "myenv/lib/python3.9/site-packages/vllm/engine/async_llm_engine.py", line 46, in _log_task_completion ERROR 08-27 14:54:06 async_llm_engine.py:56] return_value = task.result() ERROR 08-27 14:54:06 async_llm_engine.py:56] File "myenv/lib/python3.9/site-packages/vllm/engine/async_llm_engine.py", line 637, in run_engine_loop ERROR 08-27 14:54:06 async_llm_engine.py:56] result = task.result() ERROR 08-27 14:54:06 async_llm_engine.py:56] File "myenv/lib/python3.9/site-packages/vllm/engine/async_llm_engine.py", line 578, in engine_step ERROR 08...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Does VLLM only support MistralModel Architecture for embedding? feature request;stale ### 🚀 The feature, motivation and pitch Does VLLM only support MistralModel Architecture for embedding? ``` _EMBEDDING_MOD...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Does VLLM only support MistralModel Architecture for embedding? feature request;stale ### 🚀 The feature, motivation and pitch Does VLLM only support MistralModel Architecture for embedding? ``` _EMBEDDING_MODELS = { "Mi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Does VLLM only support MistralModel Architecture for embedding? feature request;stale ### 🚀 The feature, motivation and pitch Does VLLM only support MistralModel Architecture for embedding? ``` _EMBEDDING_MOD...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: re_model_input ERROR 08-27 14:54:06 async_llm_engine.py:56] sampling_metadata = SamplingMetadata.prepare(seq_group_metadata_list, ERROR 08-27 14:54:06 async_llm_engine.py:56] File "myenv/lib/python3.9/site-packages/vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
