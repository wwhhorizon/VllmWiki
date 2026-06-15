# vllm-project/vllm#2857: Ray workers fail to start when not connected to the Internet

| 字段 | 值 |
| --- | --- |
| Issue | [#2857](https://github.com/vllm-project/vllm/issues/2857) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Ray workers fail to start when not connected to the Internet

### Issue 正文摘录

(using the official container in an isolated network) ``` Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/workspace/vllm/entrypoints/openai/api_server.py", line 217, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/workspace/vllm/engine/async_llm_engine.py", line 623, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/workspace/vllm/engine/async_llm_engine.py", line 319, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/workspace/vllm/engine/async_llm_engine.py", line 364, in _init_engine return engine_class(*args, **kwargs) File "/workspace/vllm/engine/llm_engine.py", line 109, in __init__ self._init_workers_ray(placement_group) File "/workspace/vllm/engine/llm_engine.py", line 176, in _init_workers_ray driver_ip = get_ip() File "/workspace/vllm/utils.py", line 166, in get_ip s.connect(("8.8.8.8", 80)) # Doesn't need to be reachable OSError: [Errno 101] Network is unreachable ``` It appears that Google Public DNS needs to be reachable after...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: workers fail to start when not connected to the Internet (using the official container in an isolated network) ``` Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _llm_engine.py", line 623, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/workspace/vllm/engine/async_llm_engine.py", line 319, in __init__ self.engine = self._init_engine(*args, **kwargs) File...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
