# vllm-project/vllm#6586: [Bug]: Crash possible with Pipeline Parallel when aborting requests

| 字段 | 值 |
| --- | --- |
| Issue | [#6586](https://github.com/vllm-project/vllm/issues/6586) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Crash possible with Pipeline Parallel when aborting requests

### Issue 正文摘录

### Your current environment Test environment is running pipeline parallel on 2 A100s on a single node with vLLM v0.5.2. ### 🐛 Describe the bug When running a vLLM server with pipeline parallel, we have seen the server crash (Background loop stopped) when requests in flight are aborted. The stack trace printed in this case is: ``` Traceback (most recent call last): File "/opt/vllm/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 44, in _log_task_completion return_value = task.result() ^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 613, in run_engine_loop result = task.result() ^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 558, in engine_step request_outputs = await self.engine.step_async(virtual_engine) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 247, in step_async request_outputs = self._process_model_outputs( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.11/site-packages/vllm/engine/llm_engine.py", line 801, in _process_model_outputs self.output_processor...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _engine.py", line 247, in step_async request_outputs = self._process_model_outputs( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.11/site-packages/vllm/engine/llm_engine.py", line 801, in _process_model_out...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: llel: ```sh vllm serve meta-llama/Meta-Llama-3-8B --distributed-executor-backend=ray --tensor-parallel-size 1 --pipeline-parallel-size 2 ``` After it loads, run this script that will send some streaming requests and the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: n leads problems when processing the output into the sequence group. To reproduce: Run a model with pipeline parallel: ```sh vllm serve meta-llama/Meta-Llama-3-8B --distributed-executor-backend=ray --tensor-parallel-siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: current environment Test environment is running pipeline parallel on 2 A100s on a single node with vLLM v0.5.2. ### 🐛 Describe the bug When running a vLLM server with pipeline parallel, we have seen the server crash (Ba...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Crash possible with Pipeline Parallel when aborting requests bug ### Your current environment Test environment is running pipeline parallel on 2 A100s on a single node with vLLM v0.5.2. ### 🐛 Describe the bug Whe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
