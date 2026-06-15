# vllm-project/vllm#7742: [Bug]: Requesting Prompt Logprobs with an MLP Speculator Crashes the Server

| 字段 | 值 |
| --- | --- |
| Issue | [#7742](https://github.com/vllm-project/vllm/issues/7742) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Requesting Prompt Logprobs with an MLP Speculator Crashes the Server

### Issue 正文摘录

### Your current environment Using the latest vLLM off of `main`. ### 🐛 Describe the bug When running the online server with a model with an MLP speculator, sending a request that request prompt logprobs causes the server to crash with an `AssertionError`. Stacktrace: ``` Traceback (most recent call last): File "/workspace/my-vllm/lib64/python3.11/site-packages/vllm/entrypoints/openai/rpc/server.py", line 125, in generate async for request_output in results_generator: File "/workspace/my-vllm/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 1054, in generate async for output in await self.add_request( File "/workspace/my-vllm/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 114, in generator raise result File "/workspace/my-vllm/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 55, in _log_task_completion return_value = task.result() ^^^^^^^^^^^^^ File "/workspace/my-vllm/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 920, in run_engine_loop result = task.result() ^^^^^^^^^^^^^ File "/workspace/my-vllm/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 863, in engine_step reques...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Requesting Prompt Logprobs with an MLP Speculator Crashes the Server bug ### Your current environment Using the latest vLLM off of `main`. ### 🐛 Describe the bug When running the online server with a model with a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ackages/vllm/sequence.py", line 1199, in update assert len(seq_group_metadata_list) == len(hidden_states) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ AssertionError ``` ### To Reproduce Run a server with an MLP s...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ AssertionError ``` ### To Reproduce Run a server with an MLP speculator, eg. one of IBM's granite models: ``` vllm serve ibm-granite/granite-3b-code-instruct --speculative-m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: f `main`. ### 🐛 Describe the bug When running the online server with a model with an MLP speculator, sending a request that request prompt logprobs causes the server to crash with an `AssertionError`. Stacktrace: ``` Tr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: culator Crashes the Server bug ### Your current environment Using the latest vLLM off of `main`. ### 🐛 Describe the bug When running the online server with a model with an MLP speculator, sending a request that request...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
