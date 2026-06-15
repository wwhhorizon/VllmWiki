# vllm-project/vllm#15469: [Usage]: RuntimeError: NCCL error: invalid usage (run with NCCL_DEBUG=WARN for details)

| 字段 | 值 |
| --- | --- |
| Issue | [#15469](https://github.com/vllm-project/vllm/issues/15469) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: RuntimeError: NCCL error: invalid usage (run with NCCL_DEBUG=WARN for details)

### Issue 正文摘录

### Your current environment **env** torch 2.5.1+cu118 vllm 0.7.2 cuda 12 **termial** ``` CUDA_VISIBLE_DEVICES=0,1 VLLM_USE_V1=1 VLLM_WORKER_MULTIPROC_METHOD=spawn vllm serve /home/work/anyujie/Qwen/Qwen2.5-VL-3B-Instruct --gpu-memory-utilization 0.9 --swap-space 16 --max-model-len 4096 --tensor-parallel-size 2 --port 8091 --disable-custom-all-reduce ``` **error** ``` (VllmWorker rank=1 pid=12231) ERROR 03-25 21:13:53 multiproc_executor.py:374] WorkerProc hit an exception: %s (VllmWorker rank=1 pid=12231) ERROR 03-25 21:13:53 multiproc_executor.py:374] Traceback (most recent call last): (VllmWorker rank=1 pid=12231) ERROR 03-25 21:13:53 multiproc_executor.py:374] File "/home/work/anyujie/py39/lib/python3.9/site-packages/vllm/v1/executor/multiproc_executor.py", line 370, in worker_busy_loop (VllmWorker rank=1 pid=12231) ERROR 03-25 21:13:53 multiproc_executor.py:374] output = func(*args, **kwargs) (VllmWorker rank=1 pid=12231) ERROR 03-25 21:13:53 multiproc_executor.py:374] File "/home/work/anyujie/py39/lib/python3.9/site-packages/vllm/v1/worker/gpu_worker.py", line 223, in compile_or_warm_up_model (VllmWorker rank=1 pid=12231) ERROR 03-25 21:13:53 multiproc_executor.py:374] self.m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: /lib/python3.9/site-packages/vllm/v1/worker/gpu_worker.py", line 223, in compile_or_warm_up_model (VllmWorker rank=1 pid=12231) ERROR 03-25 21:13:53 multiproc_executor.py:374] self.model_runner.capture_model() (VllmWork...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: SE_V1=1 VLLM_WORKER_MULTIPROC_METHOD=spawn vllm serve /home/work/anyujie/Qwen/Qwen2.5-VL-3B-Instruct --gpu-memory-utilization 0.9 --swap-space 16 --max-model-len 4096 --tensor-parallel-size 2 --port 8091 --disable-custo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sage ### Your current environment **env** torch 2.5.1+cu118 vllm 0.7.2 cuda 12 **termial** ``` CUDA_VISIBLE_DEVICES=0,1 VLLM_USE_V1=1 VLLM_WORKER_MULTIPROC_METHOD=spawn vllm serve /home/work/anyujie/Qwen/Qwen2.5-VL-3B-I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: File "/home/work/anyujie/py39/lib/python3.9/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn (VllmWorker rank=1 pid=12231) ERROR 03-25 21:13:53 multiproc_executor.py:374] return fn(*args, **kwargs) (VllmWork...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: le "/home/work/anyujie/py39/lib/python3.9/site-packages/vllm/compilation/backends.py", line 842, in __call__ (VllmWorker rank=1 pid=12231) ERROR 03-25 21:13:53 multiproc_executor.py:374] output = entry.runnable(*args) (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
