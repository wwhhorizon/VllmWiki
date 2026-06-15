# vllm-project/vllm#24858: [Bug]: Warmup flashinfer attention is broken in v0.10.2

| 字段 | 值 |
| --- | --- |
| Issue | [#24858](https://github.com/vllm-project/vllm/issues/24858) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Warmup flashinfer attention is broken in v0.10.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Inference with GLM-4.5-Air-GPTQ is broken in version v0.10.2, while it works for commit hash few days before release: e041314184e3b1c4d797b2b025a5a9f54ade5a00 The error log (from v0.10.2): ``` (Worker_TP2 pid=78025) ERROR 09-15 02:35:32 [multiproc_executor.py:674] WorkerProc hit an exception. (Worker_TP2 pid=78025) ERROR 09-15 02:35:32 [multiproc_executor.py:674] Traceback (most recent call last): (Worker_TP2 pid=78025) ERROR 09-15 02:35:32 [multiproc_executor.py:674] File "/home/ubuntu/git/avtc/vllm/vllm/v1/executor/multiproc_executor.py", line 669, in worker_busy_loop (Worker_TP2 pid=78025) ERROR 09-15 02:35:32 [multiproc_executor.py:674] output = func(*args, **kwargs) (Worker_TP2 pid=78025) ERROR 09-15 02:35:32 [multiproc_executor.py:674] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP2 pid=78025) ERROR 09-15 02:35:32 [multiproc_executor.py:674] File "/home/ubuntu/git/avtc/vllm/vllm/v1/worker/gpu_worker.py", line 340, in compile_or_warm_up_model (Worker_TP2 pid=78025) ERROR 09-15 02:35:32 [multiproc_executor.py:674] kernel_warmup(self) (Worker_TP2 pid=78025) ERROR 09-15 02:35:32 [multiproc_executor.py:674] File "/home/ubuntu/git/avtc/vllm/vl...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: LEEP_WHEN_IDLE=1 export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve QuantTrio/GLM-4.5-Air-GPTQ-Int4-Int8Mix \ -tp 8 \ --port 8000 \ --host 0.0.0.0 \ --uvicorn-log-level info \ --trust-remote-code \ --gpu-memory-util...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Warmup flashinfer attention is broken in v0.10.2 bug ### Your current environment ### 🐛 Describe the bug Inference with GLM-4.5-Air-GPTQ is broken in version v0.10.2, while it works for commit hash few days befor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### 🐛 Describe the bug Inference with GLM-4.5-Air-GPTQ is broken in version v0.10.2, while it works for commit hash few days before release: e041314184e3b1c4d797b2b025a5a9f54ade5a00 The error log (from v0.10.2): ``` (Wo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 090 run with ``` export VLLM_ATTENTION_BACKEND="FLASHINFER" export TORCH_CUDA_ARCH_LIST="8.6" export VLLM_SLEEP_WHEN_IDLE=1 export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve QuantTrio/GLM-4.5-Air-GPTQ-Int4-Int8Mix...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: avtc/vllm/vllm/v1/worker/gpu_worker.py", line 340, in compile_or_warm_up_model (Worker_TP2 pid=78025) ERROR 09-15 02:35:32 [multiproc_executor.py:674] kernel_warmup(self) (Worker_TP2 pid=78025) ERROR 09-15 02:35:32 [mul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
