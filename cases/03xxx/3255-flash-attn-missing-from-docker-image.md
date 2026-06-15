# vllm-project/vllm#3255: `flash_attn` missing from Docker image 

| 字段 | 值 |
| --- | --- |
| Issue | [#3255](https://github.com/vllm-project/vllm/issues/3255) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> `flash_attn` missing from Docker image 

### Issue 正文摘录

Since merging #3005 we see the following error using the docker image: ``` Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/workspace/vllm/entrypoints/openai/api_server.py", line 250, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/workspace/vllm/engine/async_llm_engine.py", line 680, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/workspace/vllm/engine/async_llm_engine.py", line 343, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/workspace/vllm/engine/async_llm_engine.py", line 412, in _init_engine return engine_class(*args, **kwargs) File "/workspace/vllm/engine/llm_engine.py", line 142, in __init__ self._init_workers() File "/workspace/vllm/engine/llm_engine.py", line 200, in _init_workers self._run_workers("load_model") File "/workspace/vllm/engine/llm_engine.py", line 1086, in _run_workers driver_worker_output = getattr(self.driver_worker, File "/workspace/vllm/worker/worker.py", line 99, in load_model self.model_runner.load_model...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _llm_engine.py", line 680, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/workspace/vllm/engine/async_llm_engine.py", line 343, in __init__ self.engine = self._init_engine(*args, **kwargs) File...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: .py", line 37, in __init__ from vllm.model_executor.layers.attention.backends.flash_attn import FlashAttentionBackend File "/workspace/vllm/model_executor/layers/attention/backends/flash_attn.py", line 5, in from flash_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `flash_attn` missing from Docker image Since merging #3005 we see the following error using the docker image: ``` Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: /workspace/vllm/model_executor/models/llama.py", line 251, in LlamaDecoderLayer(config, linear_method) File "/workspace/vllm/model_executor/models/llama.py", line 178, in __init__ self.self_attn = LlamaAttention( File "...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
