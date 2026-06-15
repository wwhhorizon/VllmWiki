# vllm-project/vllm#41530: [Bug]:  TP Worker hang causes EngineDeadError - RPC call to sample_tokens timed out (DeepSeek-V4-Pro, TP=8, MTP    speculative decoding)

| 字段 | 值 |
| --- | --- |
| Issue | [#41530](https://github.com/vllm-project/vllm/issues/41530) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;fp8;moe;quantization |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  TP Worker hang causes EngineDeadError - RPC call to sample_tokens timed out (DeepSeek-V4-Pro, TP=8, MTP    speculative decoding)

### Issue 正文摘录

### 🐛 Describe the bug Body: Bug Description vLLM engine crashes with EngineDeadError after TP worker processes hang for ~5 minutes. The sample_tokens RPC call times out because shared memory broadcast blocks are unavailable — workers are unresponsive. Environment - vLLM version: v0.1.dev15830+g8d599d76a - Python version: 3.12 - CUDA version: 13.0 (driver), NCCL 2.28.9 - OS: Linux - GPU: 8x NVIDIA GPU (Tensor Parallel=8) - Model: deepseek-ai/DeepSeek-V4-Pro/ - Speculative decoding: MTP (method='mtp', num_speculative_tokens=1) - Quantization: deepseek_v4_fp8 - KV cache dtype: fp8 - Tokenizer mode: deepseek_v4 - max_seq_len: 800,000 - GPU memory utilization: 0.95 - enable_expert_parallel: True - CUDAGraph mode: FULL_DECODE_ONLY Reproduction The issue occurs intermittently during normal inference serving. The engine runs fine for a period (hours), then a worker process hangs, causing a cascading failure: 1. Engine is idle or serving low traffic (0-2 concurrent requests) 2. Worker processes stop responding to shared memory broadcast 3. After ~5 minutes of repeated warnings, sample_tokens RPC times out 4. Engine crashes with EngineDeadError, all in-flight requests return 500 Error Logs...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ror - RPC call to sample_tokens timed out (DeepSeek-V4-Pro, TP=8, MTP speculative decoding) bug ### 🐛 Describe the bug Body:
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: - KV cache dtype: fp8 - Tokenizer mode: deepseek_v4
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: - vLLM version: v0.1.dev15830+g8d599d76a - Python version: 3.12 - CUDA version: 13.0 (driver), NCCL 2.28.9
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: num_speculative_tokens=1) - Quantization: deepseek_v4_fp8 - KV cache dtype: fp8
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: - Python version: 3.12 - CUDA version: 13.0 (driver), NCCL 2.28.9 - OS: Linux

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
