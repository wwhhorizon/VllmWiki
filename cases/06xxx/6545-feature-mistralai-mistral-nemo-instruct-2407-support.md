# vllm-project/vllm#6545: [Feature]: mistralai/Mistral-Nemo-Instruct-2407 support

| 字段 | 值 |
| --- | --- |
| Issue | [#6545](https://github.com/vllm-project/vllm/issues/6545) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: mistralai/Mistral-Nemo-Instruct-2407 support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Apparently outperforms Mixtral at a smaller size. Longer context length and multilingual. https://github.com/mistralai/mistral-inference/#deployment for Dockerfile (requires updating transformers). Currently doesn't run with `--tensor-parallel-size=2`on `vllm/vllm-openai:latest`: ``` [rank0]: Traceback (most recent call last): [rank0]: File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main [rank0]: return _run_code(code, main_globals, None, [rank0]: File "/usr/lib/python3.10/runpy.py", line 86, in _run_code [rank0]: exec(code, run_globals) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 216, in [rank0]: engine = AsyncLLMEngine.from_engine_args( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 431, in from_engine_args [rank0]: engine = cls( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 360, in __init__ [rank0]: self.engine = self._init_engine(*args, **kwargs) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 507, in _init_engine [rank0]: retu...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ages/vllm/engine/llm_engine.py", line 243, in __init__ [rank0]: self.model_executor = executor_class( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/executor/multiproc_gpu_executor.py", line 153, in __init_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ilingual. https://github.com/mistralai/mistral-inference/#deployment for Dockerfile (requires updating transformers). Currently doesn't run with `--tensor-parallel-size=2`on `vllm/vllm-openai:latest`: ``` [rank0]: Trace...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 🚀 The feature, motivation and pitch Apparently outperforms Mixtral at a smaller size. Longer context length and multilingual. https://github.com/mistralai/mistral-inference/#deployment for Dockerfile (requires updating...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: mistralai/Mistral-Nemo-Instruct-2407 support feature request ### 🚀 The feature, motivation and pitch Apparently outperforms Mixtral at a smaller size. Longer context length and multilingual. https://github.co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rently doesn't run with `--tensor-parallel-size=2`on `vllm/vllm-openai:latest`: ``` [rank0]: Traceback (most recent call last): [rank0]: File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main [rank0]: ret...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
