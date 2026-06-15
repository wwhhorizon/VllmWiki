# vllm-project/vllm#13682: [Bug]: Speculative Decoding doesn't work with Ray compiled DAG and SPMD

| 字段 | 值 |
| --- | --- |
| Issue | [#13682](https://github.com/vllm-project/vllm/issues/13682) |
| 状态 | closed |
| 标签 | feature request;ray;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Speculative Decoding doesn't work with Ray compiled DAG and SPMD

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to run DeepSeek-R1 using Ray's compiled DAG, SPMD, and enabled speculative decoding. I get an error after sending a request. ``` ERROR 02-21 02:30:26 async_llm_engine.py:68] Engine background task failed ERROR 02-21 02:30:26 async_llm_engine.py:68] Traceback (most recent call last): ERROR 02-21 02:30:26 async_llm_engine.py:68] File "/home/ray/anaconda3/lib/python3.12/site-packages/vllm/engine/async_llm_engine.py", line 58, in _log_task_completion ERROR 02-21 02:30:26 async_llm_engine.py:68] return_value = task.result() ERROR 02-21 02:30:26 async_llm_engine.py:68] ^^^^^^^^^^^^^ ERROR 02-21 02:30:26 async_llm_engine.py:68] File "/home/ray/anaconda3/lib/python3.12/site-packages/vllm/engine/async_llm_engine.py", line 825, in run_engine_loop ERROR 02-21 02:30:26 async_llm_engine.py:68] result = task.result() ERROR 02-21 02:30:26 async_llm_engine.py:68] ^^^^^^^^^^^^^ ERROR 02-21 02:30:26 async_llm_engine.py:68] File "/home/ray/anaconda3/lib/python3.12/site-packages/vllm/engine/async_llm_engine.py", line 748, in engine_step ERROR 02-21 02:30:26 async_llm_engine.py:68] request_outputs = await self.engine.step_async(virtual_eng...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Speculative Decoding doesn't work with Ray compiled DAG and SPMD feature request;ray;stale ### Your current environment ### 🐛 Describe the bug I'm trying to run DeepSeek-R1 using Ray's compiled DAG, SPMD, and ena...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Speculative Decoding doesn't work with Ray compiled DAG and SPMD feature request;ray;stale ### Your current environment ### 🐛 Describe the bug I'm trying to run DeepSeek-R1 using Ray's compiled DAG, SPMD, and ena...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .0` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _async ERROR 02-21 02:30:26 async_llm_engine.py:68] outputs = await self.model_executor.execute_model_async( ERROR 02-21 02:30:26 async_llm_engine.py:68] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-21 02:30:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
