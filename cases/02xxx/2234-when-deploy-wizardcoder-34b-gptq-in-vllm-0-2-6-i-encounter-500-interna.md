# vllm-project/vllm#2234: when deploy wizardcoder-34b-gptq in vllm 0.2.6,  I encounter "500 Internal Server Error" ,details are as follows：

| 字段 | 值 |
| --- | --- |
| Issue | [#2234](https://github.com/vllm-project/vllm/issues/2234) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> when deploy wizardcoder-34b-gptq in vllm 0.2.6,  I encounter "500 Internal Server Error" ,details are as follows：

### Issue 正文摘录

Traceback (most recent call last): File "/workspace/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/workspace/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/workspace/vllm/engine/async_llm_engine.py", line 338, in engine_step request_outputs = await self.engine.step_async() File "/workspace/vllm/engine/async_llm_engine.py", line 191, in step_async output = await self._run_workers_async( File "/workspace/vllm/engine/async_llm_engine.py", line 227, in _run_workers_async assert output == other_output AssertionError

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pace/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/workspace/vllm/engine/async_llm_engine.py", line 338, in engine_step request_outputs = await...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
