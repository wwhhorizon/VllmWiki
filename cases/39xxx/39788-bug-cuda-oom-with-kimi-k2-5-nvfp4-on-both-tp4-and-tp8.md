# vllm-project/vllm#39788: [Bug]: CUDA OOM with Kimi-K2.5 NVFP4 on both TP4 and TP8

| 字段 | 值 |
| --- | --- |
| Issue | [#39788](https://github.com/vllm-project/vllm/issues/39788) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA OOM with Kimi-K2.5 NVFP4 on both TP4 and TP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to serve Kimi-K2.5 (NVFP4) with vLLM with TP4/TP8, we sporadically run into the following CUDA OOM (this being from a TP4 run): ```text (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949] WorkerProc hit an exception. (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949] Traceback (most recent call last): (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 944, in worker_busy_loop (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949] output = func(*args, **kwargs) (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949] return func(*args, **kwargs) (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: executor.py:949] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949] return func(*args, **kwargs) (Worker_T...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: CUDA OOM with Kimi-K2.5 NVFP4 on both TP4 and TP8 bug ### Your current environment ### 🐛 Describe the bug When trying to serve Kimi-K2.5 (NVFP4) with vLLM with TP4/TP8, we sporadically run into the following CUDA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA OOM with Kimi-K2.5 NVFP4 on both TP4 and TP8 bug ### Your current environment ### 🐛 Describe the bug When trying to serve Kimi-K2.5 (NVFP4) with vLLM with TP4/TP8, we sporadically run into the following CUDA...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: CUDA OOM with Kimi-K2.5 NVFP4 on both TP4 and TP8 bug ### Your current environment ### 🐛 Describe the bug When trying to serve Kimi-K2.5 (NVFP4) with vLLM with TP4/TP8, we sporadically run into the following CUDA...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 0 [multiproc_executor.py:949] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 (Worker_TP2 pid=99) ERROR 04-09 20:31:10 [multiproc_executor.py:949] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
