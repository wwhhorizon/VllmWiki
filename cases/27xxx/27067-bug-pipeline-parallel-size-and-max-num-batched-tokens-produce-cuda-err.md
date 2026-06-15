# vllm-project/vllm#27067: [Bug]: `pipeline_parallel_size` and `max_num_batched_tokens` produce `CUDA error: an illegal memory access was encountered`

| 字段 | 值 |
| --- | --- |
| Issue | [#27067](https://github.com/vllm-project/vllm/issues/27067) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `pipeline_parallel_size` and `max_num_batched_tokens` produce `CUDA error: an illegal memory access was encountered`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python #!/usr/bin/env python3 """Minimal vLLM reproduction for max_num_batched_tokens issue with PP=4.""" from vllm import EngineArgs, LLMEngine model_name = "nvidia/Llama-3.1-70B-Instruct-FP8" max_model_length = 65_528 engine_args = EngineArgs( model=model_name, pipeline_parallel_size=4, tensor_parallel_size=1, max_num_batched_tokens=max_model_length, ) # This line will raise: torch.AcceleratorError: CUDA error: an illegal memory access was encountered engine = LLMEngine.from_engine_args(engine_args) ``` Fails with: ``` (EngineCore_DP0 pid=200073) (Worker_PP3 pid=200085) ERROR 10-17 02:19:27 [multiproc_executor.py:654] WorkerProc hit an exception. (EngineCore_DP0 pid=200073) (Worker_PP3 pid=200085) ERROR 10-17 02:19:27 [multiproc_executor.py:654] Traceback (most recent call last): (EngineCore_DP0 pid=200073) (Worker_PP3 pid=200085) ERROR 10-17 02:19:27 [multiproc_executor.py:654] File "/home/ubuntu/precog/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop (EngineCore_DP0 pid=200073) (Worker_PP3 pid=200085) ERROR 10-17 02:19:27 [multiproc_executor.py:654] output = func(*ar...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: M reproduction for max_num_batched_tokens issue with PP=4.""" from vllm import EngineArgs, LLMEngine model_name = "nvidia/Llama-3.1-70B-Instruct-FP8" max_model_length = 65_528 engine_args = EngineArgs( model=model_name,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: mport EngineArgs, LLMEngine model_name = "nvidia/Llama-3.1-70B-Instruct-FP8" max_model_length = 65_528 engine_args = EngineArgs( model=model_name, pipeline_parallel_size=4, tensor_parallel_size=1, max_num_batched_tokens...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: `pipeline_parallel_size` and `max_num_batched_tokens` produce `CUDA error: an illegal memory access was encountered` bug;stale ### Your current environment ### 🐛 Describe the bug ```python #!/usr/bin/env python3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ched_tokens issue with PP=4.""" from vllm import EngineArgs, LLMEngine model_name = "nvidia/Llama-3.1-70B-Instruct-FP8" max_model_length = 65_528 engine_args = EngineArgs( model=model_name, pipeline_parallel_size=4, ten...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: kens` produce `CUDA error: an illegal memory access was encountered` bug;stale ### Your current environment ### 🐛 Describe the bug ```python #!/usr/bin/env python3 """Minimal vLLM reproduction for max_num_batched_tokens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
