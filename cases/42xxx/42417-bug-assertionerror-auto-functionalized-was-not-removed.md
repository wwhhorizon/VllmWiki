# vllm-project/vllm#42417: [Bug]: AssertionError: auto_functionalized was not removed

| 字段 | 值 |
| --- | --- |
| Issue | [#42417](https://github.com/vllm-project/vllm/issues/42417) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AssertionError: auto_functionalized was not removed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug run deepseek v4 on a bunch of 5090s ``` Traceback (most recent call last): File "/root/.local/share/uv/python/cpython-3.13.13-linux-x86_64-gnu/lib/python3.13/multiprocessing/process.py", line 313, in _bootstrap self.run() ~~~~~~~~^^ File "/root/.local/share/uv/python/cpython-3.13.13-linux-x86_64-gnu/lib/python3.13/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/.venv/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 1140, in run_engine_core raise e File "/root/.venv/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 1110, in run_engine_core engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) File "/root/.venv/lib/python3.13/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper return func(*args, **kwargs) File "/root/.venv/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 876, in __init__ super().__init__( ~~~~~~~~~~~~~~~~^ vllm_config, ^^^^^^^^^^^^ ... ... internal_dp_balancing, ^^^^^^^^^^^^^^^^^^^^^^ ) ^ File "/root/.venv/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 128,...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: rker.py", line 370, in determine_available_memory self.model_runner.profile_run() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^ File "/root/.venv/lib/python3.13/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5848, in profile...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ank, **kwargs) File "/root/.venv/lib/python3.13/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper return func(*args, **kwargs) File "/root/.venv/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 87...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ) File "/root/.venv/lib/python3.13/site-packages/vllm/compilation/cuda_graph.py", line 254, in __call__ return self.runnable(*args, **kwargs) ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^ File "/root/.venv/lib/python3.13/site-packages...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: in __init__ super().__init__( ~~~~~~~~~~~~~~~~^ vllm_config, ^^^^^^^^^^^^ ... ... internal_dp_balancing, ^^^^^^^^^^^^^^^^^^^^^^ ) ^ File "/root/.venv/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 128, in __...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: o/aot_compile.py", line 368, in aot_compile_fullgraph compiled_fn = backend( backend_input.graph_module, backend_input.example_inputs ) File "/root/.venv/lib/python3.13/site-packages/torch/__init__.py", line 2535, in __...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
