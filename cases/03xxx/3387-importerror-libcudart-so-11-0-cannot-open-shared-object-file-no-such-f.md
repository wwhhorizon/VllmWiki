# vllm-project/vllm#3387: ImportError: libcudart.so.11.0: cannot open shared object file: No such file or director

| 字段 | 值 |
| --- | --- |
| Issue | [#3387](https://github.com/vllm-project/vllm/issues/3387) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ImportError: libcudart.so.11.0: cannot open shared object file: No such file or director

### Issue 正文摘录

I am getting the error `ImportError: libcudart.so.11.0: cannot open shared object file: No such file or director` when using apptainer to run the docker image, I installed vllm from source today using Python 3.10.4 Details: - Installed from source today (13th March) with CUDA: cuda/12.1.1 - Using Apptainer to run: `apptainer run --nv /cmlscratch/smcleish/lm_doc/vllm-openai_latest.sif` Full Error: ``` Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/cmlscratch/smcleish/lm_doc/vllm/entrypoints/openai/api_server.py", line 250, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/cmlscratch/smcleish/lm_doc/vllm/engine/async_llm_engine.py", line 338, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/cmlscratch/smcleish/lm_doc/vllm/engine/async_llm_engine.py", line 309, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/cmlscratch/smcleish/lm_doc/vllm/engine/async_llm_engine.py", line 409, in _init_engine return engine_class(*args, **kwargs) File "/cml...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ImportError: libcudart.so.11.0: cannot open shared object file: No such file or director stale I am getting the error `ImportError: libcudart.so.11.0: cannot open shared object file: No such file or director` when using
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ImportError: libcudart.so.11.0: cannot open shared object file: No such file or director stale I am getting the error `ImportError: libcudart.so.11.0: cannot open shared object file: No such file or director` when using...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _llm_engine.py", line 338, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/cmlscratch/smcleish/lm_doc/vllm/engine/async_llm_engine.py", line 309, in __init__ self.engine = self._init_engine(*args...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cudart.so.11.0: cannot open shared object file: No such file or director stale I am getting the error `ImportError: libcudart.so.11.0: cannot open shared object file: No such file or director` when using apptainer to ru...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0.17.1 tqdm 4.66.2 transformers 4.38.2 triton 2.1.0 typing_extensions 4.9.0 urllib3 2.1.0 uvicorn 0.28.0 uvloop 0.19.0 vllm 0.3.3 /cmlscratch/smcleis

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
