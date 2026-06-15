# vllm-project/vllm#19639: [Bug]: Crash during OpenAI API server usage

| 字段 | 值 |
| --- | --- |
| Issue | [#19639](https://github.com/vllm-project/vllm/issues/19639) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash during OpenAI API server usage

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After this crash the server goes down which is also unexpected `vllm serve "hf-100/Jamba-1.6-large-Spellbound-StoryWriter-398B94A-instruct-0.1-chkpt-468" --host 0.0.0.0 --port 8000 --gpu-memory-utilization .95 86 --max-model-len 20000 --pipeline-parallel-size 8 --quantization experts_int8 ` ``` ERROR 06-14 04:44:54 [serving_chat.py:911] raise result ERROR 06-14 04:44:54 [serving_chat.py:911] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/entrypoints/openai/serving_chat.py", line 481, in chat_completion_stream_generator ERROR 06-14 04:44:54 [serving_chat.py:911] async for res in result_generator: ERROR 06-14 04:44:54 [serving_chat.py:911] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 976, in generate ERROR 06-14 04:44:54 [serving_chat.py:911] async for output in await self.add_request( ERROR 06-14 04:44:54 [serving_chat.py:911] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 115, in generator ERROR 06-14 04:44:54 [serving_chat.py:911] raise result ERROR 06-14 04:44:54 [serving_chat.py:911] File "/home/ubuntu/.local/lib/python...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: async ERROR 06-14 04:44:54 [serving_chat.py:911] results = await asyncio.gather(*tasks) ERROR 06-14 04:44:54 [serving_chat.py:911] File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/utils.py", line 1672, in _ru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Crash during OpenAI API server usage bug;stale ### Your current environment ### 🐛 Describe the bug After this crash the server goes down which is also unexpected `vllm serve "hf-100/Jamba-1.6-large-Spellbound-Sto...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r this crash the server goes down which is also unexpected `vllm serve "hf-100/Jamba-1.6-large-Spellbound-StoryWriter-398B94A-instruct-0.1-chkpt-468" --host 0.0.0.0 --port 8000 --gpu-memory-utilization .95 86 --max-mode...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
