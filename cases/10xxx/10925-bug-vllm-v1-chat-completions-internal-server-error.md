# vllm-project/vllm#10925: [Bug]: vllm  v1/chat/completions  Internal Server Error

| 字段 | 值 |
| --- | --- |
| Issue | [#10925](https://github.com/vllm-project/vllm/issues/10925) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm  v1/chat/completions  Internal Server Error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO 12-05 09:57:05 async_llm_engine.py:173] Added request chat-4656e70d011f4049913ba3b1ab64a702. ERROR 12-05 09:57:05 async_llm_engine.py:56] Engine background task failed ERROR 12-05 09:57:05 async_llm_engine.py:56] Traceback (most recent call last): ERROR 12-05 09:57:05 async_llm_engine.py:56] File "/home/spfx/miniconda3/envs/vllm4/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 46, in _log_task_completion ERROR 12-05 09:57:05 async_llm_engine.py:56] return_value = task.result() ERROR 12-05 09:57:05 async_llm_engine.py:56] File "/home/spfx/miniconda3/envs/vllm4/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 637, in run_engine_loop ERROR 12-05 09:57:05 async_llm_engine.py:56] result = task.result() ERROR 12-05 09:57:05 async_llm_engine.py:56] File "/home/spfx/miniconda3/envs/vllm4/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 580, in engine_step ERROR 12-05 09:57:05 async_llm_engine.py:56] request_outputs = await self.engine.step_async(virtual_engine) ERROR 12-05 09:57:05 async_llm_engine.py:56] File "/home/spfx/miniconda3/envs/vl...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ROR 12-05 09:57:05 async_llm_engine.py:56] attn_metadata = self.attn_backend.make_metadata( ERROR 12-05 09:57:05 async_llm_engine.py:56] File "/home/spfx/miniconda3/envs/vllm4/lib/python3.10/site-packages/vllm/attention...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm v1/chat/completions Internal Server Error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO 12-05 09:57:05 async_llm_engine.py:173] Added request chat-465...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pt' ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 09:57:05 async_llm_engine.py:56] ) = self._prepare_prompt(seq_group_metadata_list) ERROR 12-05 09:57:05 async_llm_engine.py:56] File "/home/spfx/miniconda3/envs/vllm4/lib/python3.10/site-packages/vllm/worker/cpu_model_r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ns Internal Server Error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO 12-05 09:57:05 async_llm_engine.py:173] Added request chat-4656e70d011f4049913ba3b1ab64a702...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
