# vllm-project/vllm#38986: [Bug]: Sync EPLB rearrangement hangs indefinitely with DP8 + EP on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#38986](https://github.com/vllm-project/vllm/issues/38986) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | cuda;moe;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Sync EPLB rearrangement hangs indefinitely with DP8 + EP on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Sync EPLB rearrangement hangs indefinitely during serving with DP8 + expert parallel on 8xB200, causing all EngineCore processes to stall. **Timeline from logs:** - Steps 75-99: EPLB runs normally, balancedness ~0.46 - Step 99 (18:07:19): `Rearranging experts sync mode ...` -- rearrangement starts - 18:08:20 (+60s): All 8 EngineCore report `No available shared memory broadcast block found in 60 seconds` - This repeats every 60 seconds for ~11 minutes - 18:18:30: All EngineCore crash with `RuntimeError: cancelled` from `shm_broadcast.py:677` The rearrangement never completes -- it deadlocks on the NCCL collective inside `rearrange()`. The first rearrangement during model loading (profile mode) works fine (3.80s). The hang occurs on the first real rearrangement triggered by serving load. Note: the balancedness before the hang is very poor (~0.46). Not sure if that's related. **Server command:** ```bash vllm serve nvidia/Qwen3.5-397B-A17B-NVFP4 \ --port 8000 -tp 1 -pp 1 -dp 8 \ --enable-expert-parallel --language-model-only \ --reasoning-parser qwen3 --stream-interval 100 \ --enable-eplb \ --eplb-config '{"num_redundant_experts": 32...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: EPLB hangs in several cases) -- that issue covers async EPLB + DeepEP/specific backends. This is **sync EPLB** with standard NCCL on B200. Full server log attached as [sync_eplb_failure_log.txt](https://github.com/user-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: elated. **Server command:** ```bash vllm serve nvidia/Qwen3.5-397B-A17B-NVFP4 \ --port 8000 -tp 1 -pp 1 -dp 8 \ --enable-expert-parallel --language-model-only \ --reasoning-parser qwen3 --stream-interval 100 \ --enable-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Sync EPLB rearrangement hangs indefinitely with DP8 + EP on B200 bug ### Your current environment ### 🐛 Describe the bug Sync EPLB rearrangement hangs indefinitely during serving with DP8 + expert parallel on 8xB...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the NCCL collective inside `rearrange()`. The first rearrangement during model loading (profile mode) works fine (3.80s). The hang occurs on the first real rearrangement triggered by serving load. Note: the balancedness...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: tive inside `rearrange()`. The first rearrangement during model loading (profile mode) works fine (3.80s). The hang occurs on the first real rearrangement triggered by serving load. Note: the balancedness before the han...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
