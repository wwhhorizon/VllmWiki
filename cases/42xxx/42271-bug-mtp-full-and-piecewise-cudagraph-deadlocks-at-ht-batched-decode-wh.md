# vllm-project/vllm#42271: [Bug]: MTP + FULL_AND_PIECEWISE cudagraph deadlocks at HT batched-decode when bonus-token-only forward shape is scheduled

| 字段 | 值 |
| --- | --- |
| Issue | [#42271](https://github.com/vllm-project/vllm/issues/42271) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | fp8;moe;operator |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MTP + FULL_AND_PIECEWISE cudagraph deadlocks at HT batched-decode when bonus-token-only forward shape is scheduled

### Issue 正文摘录

## Summary With vLLM v0.20.1 + `cudagraph_mode=FULL_AND_PIECEWISE` + MTP (`num_speculative_tokens=1`), the EngineCore deterministically deadlocks during batched-decode serving whenever the scheduler issues a step with ~15-18 requests all in `scheduled_spec_decode_tokens=[-1]` (MTP bonus-token-only mode). The engine hangs at `shm_broadcast.acquire_read._spin_condition.wait` (engine waiting for worker reply); the TP workers go silent (no log output, no crash). After the dequeue timeout (~4 min), `EngineDeadError` fires. The deadlock does **not** reproduce with `cudagraph_mode=FULL_DECODE_ONLY` (FDO), nor with single-user (c=1) MTP=2, nor with `vllm bench serve` as the client (which keeps all concurrent reqs hitting bonus-only at the same scheduler step). ## Environment - vLLM: `v0.20.1` (`vllm/vllm-openai:v0.20.1`) - Model: DeepSeek-V4-Flash (FP8 + MXFP4 MoE, custom `model_type=deepseek_v4`) - Hardware: 4× NVIDIA H20 (Hopper, 96 GB HBM3), TP=4 ## Reproducer **Server**: ```bash vllm serve \ --tensor-parallel-size 4 \ --kv-cache-dtype fp8 --block-size 256 \ --max-model-len 16384 --max-num-seqs 512 --max-num-batched-tokens 16384 \ --compilation-config '{"cudagraph_mode":"FULL_AND_PIECE...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: MTP + FULL_AND_PIECEWISE cudagraph deadlocks at HT batched-decode when bonus-token-only forward shape is scheduled ## Summary With vLLM v0.20.1 + `cudagraph_mode=FULL_AND_PIECEWISE` + MTP (`num_speculative_tokens...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: vLLM: `v0.20.1` (`vllm/vllm-openai:v0.20.1`) - Model: DeepSeek-V4-Flash (FP8 + MXFP4 MoE, custom `model_type=deepseek_v4`) - Hardware: 4× NVIDIA H20 (Hopper, 96 GB HBM3), TP=4 ## Reproducer **Server**: ```bash vllm serv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ative_tokens":1}' ``` **Client** (SGLang `bench_serving.py`, any recent version): ```bash python3 sglang/python/sglang/bench_serving.py \ --backend vllm --base-url http://localhost:8000 \ --model --tokenizer \ --dataset...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: e=FULL_AND_PIECEWISE` + MTP (`num_speculative_tokens=1`), the EngineCore deterministically deadlocks during batched-decode serving whenever the scheduler issues a step with ~15-18 requests all in `scheduled_spec_decode_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: MTP + FULL_AND_PIECEWISE cudagraph deadlocks at HT batched-decode when bonus-token-only forward shape is scheduled ## Summary With vLLM v0.20.1 + `cudagraph_mode=FULL_AND_PIECEWISE` + MTP (`num_speculative_tokens...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
