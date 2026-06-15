# vllm-project/vllm#21977: [Usage]: Can't run W4A16 NVFP4 quantized model with MoE

| 字段 | 值 |
| --- | --- |
| Issue | [#21977](https://github.com/vllm-project/vllm/issues/21977) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can't run W4A16 NVFP4 quantized model with MoE

### Issue 正文摘录

### Your current environment Not an env issue. ### How would you like to use vllm After quantizing `Llama-4-Scout-17B-16E-Instruct` with this `llm-compressor` [example](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a4_fp4/llama4_example.py) and using `scheme=NVFP4A16`, the model cannot be run in vLLM: ``` from vllm import LLM llm = LLM( model=model_path, gpu_memory_utilization=mem_utilization, tensor_parallel_size=8, max_model_len=2048 ) ``` Results in ``` (VllmWorker rank=6 pid=1192692) ERROR 07-30 15:19:50 [multiproc_executor.py:583] WorkerProc failed to start. (VllmWorker rank=6 pid=1192692) ERROR 07-30 15:19:50 [multiproc_executor.py:583] Traceback (most recent call last): (VllmWorker rank=6 pid=1192692) ERROR 07-30 15:19:50 [multiproc_executor.py:583] File "/home/brianpulfer/vllm/vllm/v1/executor/multiproc_executor.py", line 557, in worker_main (VllmWorker rank=6 pid=1192692) ERROR 07-30 15:19:50 [multiproc_executor.py:583] worker = WorkerProc(*args, **kwargs) (VllmWorker rank=6 pid=1192692) ERROR 07-30 15:19:50 [multiproc_executor.py:583] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=6 pid=1192692) ERROR 07-30 15:19:50 [multiproc_executor.py...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: Can't run W4A16 NVFP4 quantized model with MoE usage;stale ### Your current environment Not an env issue. ### How would you like to use vllm After quantizing `Llama-4-Scout-17B-16E-Instruct` with this `llm-comp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Can't run W4A16 NVFP4 quantized model with MoE usage;stale ### Your current environment Not an env issue. ### How would you like to use vllm After quantizing `Llama-4-Scout-17B-16E-Instruct` with this `llm-comp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: OR 07-30 15:19:50 [multiproc_executor.py:583] return CompressedTensorsMoEMethod.get_moe_method(self, layer)
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Usage]: Can't run W4A16 NVFP4 quantized model with MoE usage;stale ### Your current environment Not an env issue. ### How would you like to use vllm After quantizing `Llama-4-Scout-17B-16E-Instruct` with this `llm-comp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: using `scheme=NVFP4A16`, the model cannot be run in vLLM: ``` from vllm import LLM llm = LLM( model=model_path, gpu_memory_utilization=mem_utilization, tensor_parallel_size=8, max_model_len=2048 ) ``` Results in ``` (Vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
