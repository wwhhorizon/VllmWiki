# vllm-project/vllm#8954: [Bug]: minicpmv crash on 1x1 image

| 字段 | 值 |
| --- | --- |
| Issue | [#8954](https://github.com/vllm-project/vllm/issues/8954) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: minicpmv crash on 1x1 image

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```text The channel dimension is ambiguous. Got image shape (1, 1, 3). Assuming channels are the first dimension. ERROR 09-29 21:38:19 image.py:48] Failed to process image ([ , , ]) ERROR 09-29 21:38:19 async_llm_engine.py:58] Engine background task failed ERROR 09-29 21:38:19 async_llm_engine.py:58] Traceback (most recent call last): ERROR 09-29 21:38:19 async_llm_engine.py:58] File "/usr/local/python3/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 48, in _log_task_completion ERROR 09-29 21:38:19 async_llm_engine.py:58] return_value = task.result() ERROR 09-29 21:38:19 async_llm_engine.py:58] File "/usr/local/python3/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 733, in run_engine_loop ERROR 09-29 21:38:19 async_llm_engine.py:58] result = task.result() ERROR 09-29 21:38:19 async_llm_engine.py:58] File "/usr/local/python3/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 673, in engine_step ERROR 09-29 21:38:19 async_llm_engine.py:58] request_outputs = await self.engine.step_async(virtual_engine) ERROR 09-29 21:38:19 async_llm_engine....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nicpmv crash on 1x1 image bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```text The channel dimension is ambiguous. Got image shape (1, 1, 3). Assuming channels are th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: minicpmv crash on 1x1 image bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```text The channel dimension is ambiguous. Got image shape (1, 1, 3). Assuming channe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: are_model_input_tensors ERROR 09-29 21:38:19 async_llm_engine.py:58] builder.add_seq_group(seq_group_metadata) ERROR 09-29 21:38:19 async_llm_engine.py:58] File "/usr/local/python3/lib/python3.10/site-packages/vllm/work...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: -29 21:38:19 async_llm_engine.py:58] builder.add_seq_group(seq_group_metadata) ERROR 09-29 21:38:19 async_llm_engine.py:58] File "/usr/local/python3/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 720, i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
