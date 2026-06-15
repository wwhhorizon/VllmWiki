# vllm-project/vllm#37746: [Bug] prompt_logprobs causes livelock with IsHybrid models (Qwen3.5) in DP mode

| 字段 | 值 |
| --- | --- |
| Issue | [#37746](https://github.com/vllm-project/vllm/issues/37746) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;multimodal_vlm;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;moe |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] prompt_logprobs causes livelock with IsHybrid models (Qwen3.5) in DP mode

### Issue 正文摘录

## Bug: `prompt_logprobs` causes livelock with `IsHybrid` models (Qwen3.5) in DP mode ### Your current environment - vLLM version: 0.17.0 (V1 engine, default) - GPU: H100-SXM-80GB × 8 - Python: 3.11.2 - OS: Linux 5.15 - CUDA: 12.x ### Model All `IsHybrid` Qwen3.5 models reproduce this: - `Qwen3_5ForConditionalGeneration` (Qwen3.5-2B, dense hybrid) - `Qwen3_5MoeForConditionalGeneration` (Qwen3.5-35B-A3B, MoE hybrid) Both inherit `IsHybrid` (gated delta net / linear attention + full attention layers). **Does NOT reproduce** with text-only models like Qwen3-1.7B. ### Bug description When using `prompt_logprobs=1` with `IsHybrid` models in data-parallel (DP) mode (multiple independent `LLM` instances across GPUs via `multiprocessing`), one or more workers hang indefinitely inside `_get_prompt_logprobs_dict` (`gpu_model_runner.py:4597`). The hung workers' GPUs show 100% SM utilization but make zero forward progress. The hang is: - **Model-specific**: Only affects `IsHybrid` models (Qwen3.5 family). Qwen3-1.7B (pure transformer) never hangs under identical conditions. - **Scale-dependent**: Does not reproduce with <1000 prompts/worker. Triggers at ~4000-5750 prompts/worker (batch 4-6 of...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: (100, min(5000, tok.vocab_size))) random.seed(42) prompts = [tok.decode(random.choices(vocab_ids, k=500), skip_special_tokens=True) for _ in range(total_prompts)] k, m = divmod(len(prompts), num_workers) shards = [promp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ybrid` models (Qwen3.5) in DP mode ### Your current environment - vLLM version: 0.17.0 (V1 engine, default) - GPU: H100-SXM-80GB × 8 - Python: 3.11.2 - OS: Linux 5.15 - CUDA: 12.x ### Model All `IsHybrid` Qwen3.5 models...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: current environment - vLLM version: 0.17.0 (V1 engine, default) - GPU: H100-SXM-80GB × 8 - Python: 3.11.2 - OS: Linux 5.15 - CUDA: 12.x ### Model All `IsHybrid` Qwen3.5 models reproduce this: - `Qwen3_5ForConditionalGen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] prompt_logprobs causes livelock with IsHybrid models (Qwen3.5) in DP mode ## Bug: `prompt_logprobs` causes livelock with `IsHybrid` models (Qwen3.5) in DP mode ### Your current environment - vLLM version: 0.17.0 (...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: y `max_num_seqs`**: Tested with `max_num_seqs=64` — still hangs. - **Not GPU memory related**: Happens at both `gpu_memory_utilization=0.85` and `0.60`. - **Random GPU each run**: Not hardware-specific — depends on sche...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
