# vllm-project/vllm#12747: [Bug]: Using Ray with compiled DAG throws the "The compiled graph can't have more than 10 in-flight executions" error

| 字段 | 值 |
| --- | --- |
| Issue | [#12747](https://github.com/vllm-project/vllm/issues/12747) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Using Ray with compiled DAG throws the "The compiled graph can't have more than 10 in-flight executions" error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to run DeepSeek R1 using vLLM with Ray and aDAG. As soon as I send the first request I get the following error: ``` File "/home/ray/anaconda3/lib/python3.12/site-packages/vllm/engine/async_llm_engine.py", line 825, in run_engine_loop result = task.result() ^^^^^^^^^^^^^ File "/home/ray/anaconda3/lib/python3.12/site-packages/vllm/engine/async_llm_engine.py", line 748, in engine_step request_outputs = await self.engine.step_async(virtual_engine) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ray/anaconda3/lib/python3.12/site-packages/vllm/engine/async_llm_engine.py", line 353, in step_async outputs = await self.model_executor.execute_model_async( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ray/anaconda3/lib/python3.12/site-packages/vllm/executor/ray_distributed_executor.py", line 575, in execute_model_async dag_future = await self.forward_dag.execute_async(serialized_data) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ray/anaconda3/lib/python3.12/site-packages/ray/dag/compiled_dag_node.py", line 2186, in execute_async self._raise_if_too_many_inflight_executions() File "/home/r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Using Ray with compiled DAG throws the "The compiled graph can't have more than 10 in-flight executions" error bug;ray ### Your current environment ### 🐛 Describe the bug I'm trying to run DeepSeek R1 using vLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ngine/async_llm_engine.py", line 353, in step_async outputs = await self.model_executor.execute_model_async( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ray/anaconda3/lib/python3.12/site-packages/vllm/exe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: un DeepSeek R1 using vLLM with Ray and aDAG. As soon as I send the first request I get the following error: ``` File "/home/ray/anaconda3/lib/python3.12/site-packages/vllm/engine/async_llm_engine.py", line 825, in run_e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
