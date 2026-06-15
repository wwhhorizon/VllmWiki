# vllm-project/vllm#38700: [Bug]: vLLM fails to start with LMCache + Qwen3-Coder-Next-FP8 (nightly image)

| 字段 | 值 |
| --- | --- |
| Issue | [#38700](https://github.com/vllm-project/vllm/issues/38700) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM fails to start with LMCache + Qwen3-Coder-Next-FP8 (nightly image)

### Issue 正文摘录

### Your current environment Image: vllm/vllm-openai:0.18.0 or lmcache/vllm-openai:nightly-2026-03-31 vLLM version: 0.18.0 - 0.18.3.dev15 Model: Qwen/Qwen3-Coder-Next-FP8 Load format: runai_streamer (S3) KV cache: LMCacheConnectorV1 GPUs: 2 (tensor_parallel_size=2) ### 🐛 Describe the bug Engine fails during startup with KV cache initialization error. To Reproduce Start with this args: --model s3://vllm-models/qwen-coder --tensor-parallel-size 2 --load-format runai_streamer --gpu-memory-utilization 0.8 --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}' Expected behavior Model should start successfully with LMCache enabled. ``` (Worker_TP0 pid=1143) ERROR 04-01 07:17:10 [multiproc_executor.py:949] Traceback (most recent call last): (Worker_TP0 pid=1143) ERROR 04-01 07:17:10 [multiproc_executor.py:949] File "/opt/venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 944, in worker_busy_loop (Worker_TP0 pid=1143) ERROR 04-01 07:17:10 [multiproc_executor.py:949] output = func(*args, **kwargs) (Worker_TP0 pid=1143) ERROR 04-01 07:17:10 [multiproc_executor.py:949] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=1143) ERROR 04-01 07:17:10 [mul...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM fails to start with LMCache + Qwen3-Coder-Next-FP8 (nightly image) bug ### Your current environment Image: vllm/vllm-openai:0.18.0 or lmcache/vllm-openai:nightly-2026-03-31 vLLM version: 0.18.0 - 0.18.3.dev1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: iproc_executor.py:949] cudagraph_memory_estimate = self.model_runner.profile_cudagraph_memory() (Worker_TP0 pid=1143) ERROR 04-01 07:17:10 [multiproc_executor.py:949] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: : vllm/vllm-openai:0.18.0 or lmcache/vllm-openai:nightly-2026-03-31 vLLM version: 0.18.0 - 0.18.3.dev15 Model: Qwen/Qwen3-Coder-Next-FP8 Load format: runai_streamer (S3) KV cache: LMCacheConnectorV1 GPUs: 2 (tensor_para...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: orker_TP0 pid=1143) ERROR 04-01 07:17:10 [multiproc_executor.py:949] cudagraph_memory_estimate = self.model_runner.profile_cudagraph_memory() (Worker_TP0 pid=1143) ERROR 04-01 07:17:10 [multiproc_executor.py:949] ^^^^^^...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ug Engine fails during startup with KV cache initialization error. To Reproduce Start with this args: --model s3://vllm-models/qwen-coder --tensor-parallel-size 2 --load-format runai_streamer --gpu-memory-utilization 0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
