# vllm-project/vllm#40988: [bug/perf] V4-Pro hangs ~60 min in post-shard-load weight materialization without --safetensors-load-strategy prefetch on EXT4

| 字段 | 值 |
| --- | --- |
| Issue | [#40988](https://github.com/vllm-project/vllm/issues/40988) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8;moe;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [bug/perf] V4-Pro hangs ~60 min in post-shard-load weight materialization without --safetensors-load-strategy prefetch on EXT4

### Issue 正文摘录

# [bug/perf] V4-Pro hangs ~60 min in post-shard-load weight materialization without `--safetensors-load-strategy prefetch` on EXT4 ## Summary On an 8-Spark cluster (TP=8, 8× NVIDIA GB10 / sm_121 / 128 GiB unified memory each, EXT4 on local NVMe), serving `deepseek-ai/DeepSeek-V4-Pro` (1.6T MoE, 805 GiB checkpoint, ~102 GiB / rank shard) **deterministically stalls** in the post-shard-load weight materialization phase without `--safetensors-load-strategy prefetch`. With the flag, full cold-start completes in ~12 minutes and inference is coherent. ## Repro Image: built from `nvcr.io/nvidia/pytorch:25.11-py3` + jasl/vllm@ds4-sm120-prototype + jasl/DeepGEMM@sm120 + tonyliu312's PR #40923 sm_12x Marlin patch + `TORCH_CUDA_ARCH_LIST="12.0;12.1"`. Launch (8 nodes, TP=8, Ray distributed executor): ```bash vllm serve deepseek-ai/DeepSeek-V4-Pro \ --trust-remote-code --kv-cache-dtype fp8 --block-size 256 \ -tp 8 --pipeline-parallel-size 1 --max-model-len 1024 \ --gpu-memory-utilization 0.88 \ --tokenizer-mode deepseek_v4 --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice --reasoning-parser deepseek_v4 \ --distributed-executor-backend ray --enforce-eager # NOTE: NO --safetensors-load-...

## 现有链接修复摘要

#40899 DeepSeek V4 support on SM12x with Triton sparse MLA fallback | #40923 [Kernel] Marlin MoE: include SM 12.x in default arch list

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: llm serve deepseek-ai/DeepSeek-V4-Pro \ --trust-remote-code --kv-cache-dtype fp8 --block-size 256 \ -tp 8 --pipeline-parallel-size 1 --max-model-len 1024 \ --gpu-memory-utilization 0.88 \ --tokenizer-mode deepseek_v4 --...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: to-tool-choice --reasoning-parser deepseek_v4 \ --distributed-executor-backend ray --enforce-eager # NOTE: NO --safetensors-load-strategy ``` Observed: each rank reports `Loaded shard X/8 (XX.X GiB)` within ~3-5 minutes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: etch` on EXT4 ## Summary On an 8-Spark cluster (TP=8, 8× NVIDIA GB10 / sm_121 / 128 GiB unified memory each, EXT4 on local NVMe), serving `deepseek-ai/DeepSeek-V4-Pro` (1.6T MoE, 805 GiB checkpoint, ~102 GiB / rank shar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: he-dtype fp8 --block-size 256 \ -tp 8 --pipeline-parallel-size 1 --max-model-len 1024 \ --gpu-memory-utilization 0.88 \ --tokenizer-mode deepseek_v4 --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice --reasoning...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: y each, EXT4 on local NVMe), serving `deepseek-ai/DeepSeek-V4-Pro` (1.6T MoE, 805 GiB checkpoint, ~102 GiB / rank shard) **deterministically stalls** in the post-shard-load weight materialization phase without `--safete...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40899](https://github.com/vllm-project/vllm/pull/40899) | mentioned | 0.45 | DeepSeek V4 support on SM12x with Triton sparse MLA fallback | antization) cc @tonyliu312 (asked me to file this separately from pr #40899 thread) --- ## bonus data point from the same cluster running v4-flash (~37 gib / rank shard) on the sa… |
| [#40923](https://github.com/vllm-project/vllm/pull/40923) | mentioned | 0.45 | [Kernel] Marlin MoE: include SM 12.x in default arch list | v0.1.dev1+g1523228e6.d20260427` (jasl/vllm `ds4-sm120-prototype` + pr #40923 patch) - container: `nvcr.io/nvidia/pytorch:25.11-py3` base - model: `deepseek-ai/deepseek-v4-pro` (80… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
