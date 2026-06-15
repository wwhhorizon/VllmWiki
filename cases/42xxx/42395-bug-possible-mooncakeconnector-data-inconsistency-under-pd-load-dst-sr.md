# vllm-project/vllm#42395: [Bug]: Possible MooncakeConnector data inconsistency under PD load (`dst != src_post`) with `mooncake-transfer-engine-cuda13==0.3.10.post2`

| 字段 | 值 |
| --- | --- |
| Issue | [#42395](https://github.com/vllm-project/vllm/issues/42395) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Possible MooncakeConnector data inconsistency under PD load (`dst != src_post`) with `mooncake-transfer-engine-cuda13==0.3.10.post2`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Related issue This follows the startup/cleanup issue: - https://github.com/vllm-project/vllm/issues/42385 we could not use `mooncake-transfer-engine` in our environment (that path hit the startup failure from the first issue), so we switched to: - `mooncake-transfer-engine-cuda13==0.3.10.post2` With this package, startup succeeds, but we then hit this separate data-integrity problem under PD load. ## Problem summary Under PD traffic, we observe output quality regressions and descriptor-level byte mismatches. Key signal: - `src_hash_pre == src_hash_post` (sender memory stable) - but `dst_hash != src_hash_post` (receiver bytes differ) This points to transfer / destination-write inconsistency rather than sender-memory overwrite. The reproduced with a pure-vLLM PD script: - `repro_audio_in_video_002_pd_like.sh` (attached below) ## Minimal reproduction strategy (pure vLLM) 1. Launch Mooncake PD path (prefill + decode + proxy) with `Qwen3-Omni-30B-A3B-Instruct`. 2. Send concurrent streaming audio-in-video requests (batch 5, multiple rounds). 3. Enable descriptor hash probes in `mooncake_connector.py` and inspect compare logs. ## Deb...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rc_hash_post` (fallback to `src_hash_pre`) Probe data path: 1. sender `_build_transfer_params(...)` captures `src_hash_pre` into `debug_descriptor_bytes` 2. sender `_annotate_sender_post_hash(...)` fills `src_hash_post`...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ## Minimal reproduction strategy (pure vLLM) 1. Launch Mooncake PD path (prefill + decode + proxy) with `Qwen3-Omni-30B-A3B-Instruct`. 2. Send concurrent streaming audio-in-video requests (batch 5, multiple rounds). 3....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: istency under PD load (`dst != src_post`) with `mooncake-transfer-engine-cuda13==0.3.10.post2` bug ### Your current environment ### 🐛 Describe the bug ## Related issue This follows the startup/cleanup issue: - https://g...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 1 != dst_hash_round2` - `mismatches`: final `dst_hash != src_hash_post` (fallback to `src_hash_pre`) Probe data path: 1. sender `_build_transfer_params(...)` captures `src_hash_pre` into `debug_descriptor_bytes` 2. send...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: traffic, we observe output quality regressions and descriptor-level byte mismatches. Key signal: - `src_hash_pre == src_hash_post` (sender memory stable) - but `dst_hash != src_hash_post` (receiver bytes differ) This po...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
