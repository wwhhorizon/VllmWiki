# vllm-project/vllm#42084: [Bug]: GDN attention `mamba_get_block_table_tensor` torch.gather index out of bounds when prefix caching + num_speculative_tokens>=10 (DFlash, DGX Spark sm_121a, Qwen3.6 hybrid)

| 字段 | 值 |
| --- | --- |
| Issue | [#42084](https://github.com/vllm-project/vllm/issues/42084) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;quantization |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: GDN attention `mamba_get_block_table_tensor` torch.gather index out of bounds when prefix caching + num_speculative_tokens>=10 (DFlash, DGX Spark sm_121a, Qwen3.6 hybrid)

### Issue 正文摘录

## Summary Running the official `docker-compose.spark-xs.yml` from [AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash](https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash) (file-byte-identical, no edits) on a DGX Spark, the container starts cleanly (autotuner + cudagraph capture + warmup all complete in ~10 min, "Application startup complete") but **the very first inference request triggers a CUDA device-side assert and crashes the engine**. Reducing `num_speculative_tokens` from 15 to 5 stabilizes it (~31 tok/s). Disabling prefix caching also works (~31 tok/s, with worse drafter utilization). The bug only manifests when **prefix caching = on AND num_speculative_tokens >= ~10**. Either fix in isolation works. ## Repro `docker-compose.spark-xs.yml` from [AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash@main](https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash) (commit on 2026-04-28), no edits. ```bash docker compose -f docker-compose.spark-xs.yml up -d # wait 10 min for startup complete curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{"model":"aeon-ultimate","messages":[{"role":"user","content":"Hello...

## 现有链接修复摘要

#26807 [V1][Hybrid] GatedDeltaNet Automatic Prefix Caching (`all`-mode) | #38020 [Optimization] Fuse mamba_get_block_table_tensor in align mode

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: (DFlash, DGX Spark sm_121a, Qwen3.6 hybrid) ## Summary Running the official `docker-compose.spark-xs.yml` from [AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash](https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Unc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: rafter","num_speculative_tokens":15}'` - `--tensor-parallel-size 1` - `--quantization modelopt` (NVFP4 + DFlash drafter) - `--attention-backend flash_attn` ## Hardware - DGX Spark, NVIDIA GB10 (sm_121a), 128 GB unified...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: table_tensor` torch.gather index out of bounds when prefix caching + num_speculative_tokens>=10 (DFlash, DGX Spark sm_121a, Qwen3.6 hybrid) ## Summary Running the official `docker-compose.spark-xs.yml` from [AEON-7/Qwen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: prefix caching + num_speculative_tokens>=10 (DFlash, DGX Spark sm_121a, Qwen3.6 hybrid) ## Summary Running the official `docker-compose.spark-xs.yml` from [AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash](https://git...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: unds when prefix caching + num_speculative_tokens>=10 (DFlash, DGX Spark sm_121a, Qwen3.6 hybrid) ## Summary Running the official `docker-compose.spark-xs.yml` from [AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash](h...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26807](https://github.com/vllm-project/vllm/pull/26807) | mentioned | 0.45 | [V1][Hybrid] GatedDeltaNet Automatic Prefix Caching (`all`-mode)  | llegaladdress. **tp=2 specific** — this issue is tp=1, distinct. - pr #26807 — gateddeltanet apc `all`-mode. switching to `--mamba-cache-mode all` may avoid the `align`-mode code… |
| [#38020](https://github.com/vllm-project/vllm/pull/38020) | mentioned | 0.45 | [Optimization] Fuse mamba_get_block_table_tensor in align mode | all` may avoid the `align`-mode code path that this issue hits. - pr #38020 — perf optimization fusing `mamba_get_block_table_tensor` in align mode — touches the exact function bu… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
