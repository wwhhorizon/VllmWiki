# vllm-project/vllm#41884: [Bug][V1][Hybrid] IndexError in get_temporal_copy_spec during DFlash speculative decoding + prefix caching

| 字段 | 值 |
| --- | --- |
| Issue | [#41884](https://github.com/vllm-project/vllm/issues/41884) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][V1][Hybrid] IndexError in get_temporal_copy_spec during DFlash speculative decoding + prefix caching

### Issue 正文摘录

## Environment - **vLLM version**: `0.1.dev1+gbfde49e28.d20260418` (image `ghcr.io/aeon-7/vllm-spark-omni-q36:v1.2`) - **Hardware**: NVIDIA GB10 (DGX SPARK, 128GB UMA) - **Model**: `rdtand/Qwen3.6-35B-A3B-PrismaQuant-4.75bit-vllm` (compressed-tensors / PrismaQuant 4.75-bit) - **Speculative decoding**: DFlash, 15 draft tokens, draft model `z-lab/Qwen3.6-35B-A3B-DFlash` - **Prefix caching**: enabled (default) ## Bug Description EngineCore crashes mid-inference on text-only requests with an `IndexError` in `get_temporal_copy_spec`. APIServer then shuts down cleanly. The crash is non-deterministic — triggered by a specific acceptance pattern during DFlash decode + Mamba SSM state copy. ## Stack Trace ``` File "vllm/v1/worker/gpu_model_runner.py", line 3950, in execute_model mamba_utils.preprocess_mamba(...) File "vllm/v1/worker/mamba_utils.py", line 207, in preprocess_mamba collect_mamba_copy_meta(...) File "vllm/v1/worker/mamba_utils.py", line 124, in collect_mamba_copy_meta copy_spec = state_copy_func( ^^^^^^^^^^^^^^^^ File "vllm/model_executor/layers/mamba/mamba_utils.py", line 341, in get_temporal_copy_spec src_block_id = block_ids[cur_block_idx + num_accepted_tokens - 1] ~~~~~~~~...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug][V1][Hybrid] IndexError in get_temporal_copy_spec during DFlash speculative decoding + prefix caching ## Environment - **vLLM version**: `0.1.dev1+gbfde49e28.d20260418` (image `ghcr.io/aeon-7/vllm-spark-omni-q36:v1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: get_temporal_copy_spec`. APIServer then shuts down cleanly. The crash is non-deterministic — triggered by a specific acceptance pattern during DFlash decode + Mamba SSM state copy. ## Stack Trace ``` File "vllm/v1/worke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ng DFlash speculative decoding + prefix caching ## Environment - **vLLM version**: `0.1.dev1+gbfde49e28.d20260418` (image `ghcr.io/aeon-7/vllm-spark-omni-q36:v1.2`) - **Hardware**: NVIDIA GB10 (DGX SPARK, 128GB UMA) - *...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: k-omni-q36:v1.2`) - **Hardware**: NVIDIA GB10 (DGX SPARK, 128GB UMA) - **Model**: `rdtand/Qwen3.6-35B-A3B-PrismaQuant-4.75bit-vllm` (compressed-tensors / PrismaQuant 4.75-bit) - **Speculative decoding**: DFlash, 15 draf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: temporal_copy_spec`. APIServer then shuts down cleanly. The crash is non-deterministic — triggered by a specific acceptance pattern during DFlash decode + Mamba SSM state copy. ## Stack Trace ``` File "vllm/v1/worker/gp...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
