# vllm-project/vllm#3222: cupy_backends.cuda.libs.nccl.NcclError: NCCL_ERROR_INTERNAL_ERROR: internal error

| 字段 | 值 |
| --- | --- |
| Issue | [#3222](https://github.com/vllm-project/vllm/issues/3222) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> cupy_backends.cuda.libs.nccl.NcclError: NCCL_ERROR_INTERNAL_ERROR: internal error

### Issue 正文摘录

Hi Im getting the following error with vllm 0.3.2 on A100 engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 625, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 321, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 366, in _init_engine return engine_class(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 118, in __init__ self._init_workers_ray(placement_group) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 286, in _init_workers_ray self._run_workers("init_model", cupy_port=get_open_port()) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 1014, in _run_workers driver_worker_output = getattr(self.driver_worker, File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker.py", line 94, in init_model init_distributed_environment(self.parallel_config, self.rank, File "/usr/local/lib/python3.10...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ----------------------------+ | NVIDIA-SMI 535.154.05 Driver Version: 535.154.05 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: cupy_backends.cuda.libs.nccl.NcclError: NCCL_ERROR_INTERNAL_ERROR: internal error Hi Im getting the following error with vllm 0.3.2 on A100 engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/pyth...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _llm_engine.py", line 625, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 321, in __init__ self.engine = self._init_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: s.py", line 90, in init_process_group _NCCL_BACKEND = NCCLBackendWithBFloat16(world_size, rank, host, port) File "/usr/local/lib/python3.10/dist-packages/cupyx/distributed/_nccl_comm.py", line 70, in __init__ self._init...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: cupy_backends.cuda.libs.nccl.NcclError: NCCL_ERROR_INTERNAL_ERROR: internal error Hi Im getting the following error with vllm 0.3.2 on A100 engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/pyth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
