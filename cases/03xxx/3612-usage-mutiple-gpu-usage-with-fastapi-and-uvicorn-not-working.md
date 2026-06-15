# vllm-project/vllm#3612: [Usage]: Mutiple-GPU usage with Fastapi and uvicorn not working

| 字段 | 值 |
| --- | --- |
| Issue | [#3612](https://github.com/vllm-project/vllm/issues/3612) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Mutiple-GPU usage with Fastapi and uvicorn not working

### Issue 正文摘录

I am facing an error when attempting to utilize multiple GPUs with a FastAPI backend. The error arises during the integration of the multiple GPU code into the FastAPI backend API. Interestingly, the same code functions correctly when executed independently for multiple GPUs. I am simply loading model after loading libraries. ` LLM(model=model, max_model_len=16000, tensor_parallel_size=4) ` TypeError: cannot pickle '_thread.lock' object Error Traceback ``` self.llm = LLM(model=model, max_model_len=16000, tensor_parallel_size=4) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/llm.py", line 109, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 391, in from_engine_args engine = cls(*engine_configs, File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 126, in __init__ self._init_workers_ray(placement_group) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 304, in _init_workers_ray self._run_workers("init_model", File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 1041, in _run_workers driver_wor...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: s.py", line 90, in init_process_group _NCCL_BACKEND = NCCLBackendWithBFloat16(world_size, rank, host, port) File "/usr/local/lib/python3.8/dist-packages/cupyx/distributed/_nccl_comm.py", line 70, in __init__ self._init_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ectly when executed independently for multiple GPUs. I am simply loading model after loading libraries. ` LLM(model=model, max_model_len=16000, tensor_parallel_size=4) ` TypeError: cannot pickle '_thread.lock' object Er...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: facing an error when attempting to utilize multiple GPUs with a FastAPI backend. The error arises during the integration of the multiple GPU code into the FastAPI backend API. Interestingly, the same code functions corr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ge]: Mutiple-GPU usage with Fastapi and uvicorn not working usage I am facing an error when attempting to utilize multiple GPUs with a FastAPI backend. The error arises during the integration of the multiple GPU code in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
