# vllm-project/vllm#40937: [Bug]: profile_cudagraph_memory() ignores GPU memory clamp on sliced GPUs (HAMi/MIG/MPS) — --gpu-memory-utilization is inert with AutoRound INT4 + fp8_e5m2 KV + FlashInfer + CUDA graphs

| 字段 | 值 |
| --- | --- |
| Issue | [#40937](https://github.com/vllm-project/vllm/issues/40937) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: profile_cudagraph_memory() ignores GPU memory clamp on sliced GPUs (HAMi/MIG/MPS) — --gpu-memory-utilization is inert with AutoRound INT4 + fp8_e5m2 KV + FlashInfer + CUDA graphs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug #### Summary On a HAMi-sliced 24 GiB Ampere GPU, vLLM's `profile_cudagraph_memory()` warmup step OOMs because the memory budget computed from `init_snapshot.total_memory * gpu_memory_utilization` is derived from the physical card capacity rather than the slice's clamped visible memory. The CUDA graph profiler then tries to allocate on top of a budget that already exceeds what the slice can deliver. Lowering `--gpu-memory-utilization` has no effect on the failure (identical numbers at 0.95 / 0.92 / 0.88), so the dial that should normally mitigate this is inert at this codepath. #### Reproducer Minimal flag set that triggers the crash on a HAMi-sliced 24 GiB Ampere card running the upstream `vllm/vllm-openai:v0.19.1` image: ```bash vllm serve Intel/Qwen3.6-27B-int4-AutoRound \ --quantization auto_round \ --kv-cache-dtype fp8_e5m2 \ --attention-backend flashinfer \ --gpu-memory-utilization 0.92 \ --max-model-len 32768 ``` The same flags also reproduce with `Lorbus/Qwen3.6-27B-int4-AutoRound` (byte-identical to the Intel publish), and with `--speculative-config '{"method":"mtp", "num_speculative_tokens":3}'` appended. MTP is not requ...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: profile_cudagraph_memory() ignores GPU memory clamp on sliced GPUs (HAMi/MIG/MPS) — --gpu-memory-utilization is inert with AutoRound INT4 + fp8_e5m2 KV + FlashInfer + CUDA graphs ### Your current environment ###...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: d GPUs (HAMi/MIG/MPS) — --gpu-memory-utilization is inert with AutoRound INT4 + fp8_e5m2 KV + FlashInfer + CUDA graphs ### Your current environment ### 🐛 Describe the bug #### Summary On a HAMi-sliced 24 GiB Ampere GPU,...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: profile_cudagraph_memory() ignores GPU memory clamp on sliced GPUs (HAMi/MIG/MPS) — --gpu-memory-utilization is inert with AutoRound INT4 + fp8_e5m2 KV + FlashInfer + CUDA graphs ### Your current environment ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 6-27B-int4-AutoRound` (byte-identical to the Intel publish), and with `--speculative-config '{"method":"mtp", "num_speculative_tokens":3}'` appended. MTP is not required. `--enable-chunked-prefill` is also not required...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: l_memory * gpu_memory_utilization` is derived from the physical card capacity rather than the slice's clamped visible memory. The CUDA graph profiler then tries to allocate on top of a budget that already exceeds what t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
