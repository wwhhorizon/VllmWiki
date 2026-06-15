# vllm-project/vllm#42895: [Bug]: NIXL disagg fails for Qwen3.5 hybrid model when prefill TP4 and decode DP8 use different physical block sizes

| 字段 | 值 |
| --- | --- |
| Issue | [#42895](https://github.com/vllm-project/vllm/issues/42895) |
| 状态 | open |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NIXL disagg fails for Qwen3.5 hybrid model when prefill TP4 and decode DP8 use different physical block sizes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary Qwen3.5 NVFP4 disaggregated serving with NIXL fails when using heterogeneous prefill/decode parallelism: - Prefill: `4xTEP4` (`4` prefill workers, each `TP4 + expert parallel`, one 4xGB200 node per worker) - Decode: `1xDEP8` (`1` logical decode worker, `DP8 + expert parallel`, spanning two 4xGB200 nodes) - KV cache dtype: `bfloat16` - Prefix caching disabled - Async scheduling disabled - Hybrid KV cache manager explicitly enabled - SSM conv state layout set to `DS` The deployment becomes healthy, but decode NIXL handshakes fail at request time because the local decode block size is `16` and the remote prefill block size is `32`. The connector currently asserts `local_block_size % remote_block_size == 0`, which rejects this case even though the opposite direction is divisible. This makes the configuration unusable for correctness testing: GSM8K accuracy collapses because KV transfers fail and vLLM skips KV post-processing for affected requests. ## Environment - Hardware: 4xGB200 per node - Nodes used in failing run: 6 nodes - Model: `Qwen3.5-397B-A17B-NVFP4` - vLLM version: `0.20.2rc1.dev354+g24337fb86.precompiled` - Dy...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: hing disabled - Async scheduling disabled - Hybrid KV cache manager explicitly enabled - SSM conv state layout set to `DS` The deployment becomes healthy, but decode NIXL handshakes fail at request time because the loca...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: Your current environment ### 🐛 Describe the bug ## Summary Qwen3.5 NVFP4 disaggregated serving with NIXL fails when using heterogeneous prefill/decode parallelism: - Prefill: `4xTEP4` (`4` prefill workers, each `TP4 + e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: serving with NIXL fails when using heterogeneous prefill/decode parallelism: - Prefill: `4xTEP4` (`4` prefill workers, each `TP4 + expert parallel`, one 4xGB200 node per worker) - Decode: `1xDEP8` (`1` logical decode wo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: NIXL disagg fails for Qwen3.5 hybrid model when prefill TP4 and decode DP8 use different physical block sizes bug ### Your current environment ### 🐛 Describe the bug ## Summary Qwen3.5 NVFP4 disaggregated serving...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: al decode worker, `DP8 + expert parallel`, spanning two 4xGB200 nodes) - KV cache dtype: `bfloat16` - Prefix caching disabled - Async scheduling disabled - Hybrid KV cache manager explicitly enabled - SSM conv state lay...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
