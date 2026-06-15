# vllm-project/vllm#39065: [Bug]: Gemma4 e2b and e4b models report 'Unsupported CPU attention configuration: head_dim=512 isa=1' error under vllm-cpu 0.19.0

| 字段 | 值 |
| --- | --- |
| Issue | [#39065](https://github.com/vllm-project/vllm/issues/39065) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma4 e2b and e4b models report 'Unsupported CPU attention configuration: head_dim=512 isa=1' error under vllm-cpu 0.19.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Starts up normally, but errors occur during inference service: (EngineCore pid=148) Traceback (most recent call last): (EngineCore pid=148) File "/opt/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore pid=148) self.run() (EngineCore pid=148) File "/opt/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore pid=148) self._target(*self._args, **self._kwargs) (EngineCore pid=148) File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1112, in run_engine_core (EngineCore pid=148) raise e (EngineCore pid=148) File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1101, in run_engine_core (EngineCore pid=148) engine_core.run_busy_loop() (EngineCore pid=148) File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1142, in run_busy_loop (EngineCore pid=148) self._process_engine_step() (EngineCore pid=148) File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1181, in _process_engine_step (EngineCore pid=148) outputs, model_exec...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma4 e2b and e4b models report 'Unsupported CPU attention configuration: head_dim=512 isa=1' error under vllm-cpu 0.19.0 bug ### Your current environment ### 🐛 Describe the bug Starts up normally, but errors oc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 48) future = self.model_executor.execute_model(scheduler_output, non_block=True) (EngineCore pid=148) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=148) File "/opt/venv/lib/python3....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: id=148) File "/opt/venv/lib/python3.12/site-packages/vllm/v1/attention/backends/cpu_attn.py", line 173, in build (EngineCore pid=148) scheduler_metadata = ops.cpu_attn_get_scheduler_metadata( (EngineCore pid=148) ^^^^^^...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l_runner.py", line 3970, in execute_model (EngineCore pid=148) self._build_attention_metadata( (EngineCore pid=148) File "/opt/venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 2319, in _build_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: a=1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
