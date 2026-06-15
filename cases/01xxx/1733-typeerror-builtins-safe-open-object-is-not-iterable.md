# vllm-project/vllm#1733: TypeError: 'builtins.safe_open' object is not iterable

| 字段 | 值 |
| --- | --- |
| Issue | [#1733](https://github.com/vllm-project/vllm/issues/1733) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: 'builtins.safe_open' object is not iterable

### Issue 正文摘录

``` /vllm/vllm/model_executor/weight_utils.py", line 243, in hf_model_weights_iterator for name in f: TypeError: 'builtins.safe_open' object is not iterable ``` I am using the main branch build. Triggers when using /openai/api_server.py and loading the model weights for the engine object (AsyncLLMEngine) Traceback: ``` Traceback (most recent call last): File "runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "runpy.py", line 86, in _run_code exec(code, run_globals) File "api_server.py", line 644, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "async_llm_engine.py", line 486, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "async_llm_engine.py", line 269, in __init__ self.engine = self._init_engine(*args, **kwargs) File "async_llm_engine.py", line 305, in _init_engine return engine_class(*args, **kwargs) File "llm_engine.py", line 110, in __init__ self._init_workers(distributed_init_method) File "llm_engine.py", line 142, in _init_workers self._run_workers( File "llm_engine.py", line 700, in _run_workers output = executor(*args, **kwargs) File "worker.py", line 70, in init_model self.model = get_model(se...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: TypeError: 'builtins.safe_open' object is not iterable ``` /vllm/vllm/model_executor/weight_utils.py", line 243, in hf_model_weights_iterator for name in f: TypeError: 'builtins.safe_open' object is not iterable ``` I a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: iltins.safe_open' object is not iterable ``` I am using the main branch build. Triggers when using /openai/api_server.py and loading the model weights for the engine object (AsyncLLMEngine) Traceback: ``` Traceback (mos...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
