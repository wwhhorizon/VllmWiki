# vllm-project/vllm#42995: [Bug]: V1 sleep/wake leaves P0 multimodal sender cache desynced from P1 → AssertionError on next image reuse

| 字段 | 值 |
| --- | --- |
| Issue | [#42995](https://github.com/vllm-project/vllm/issues/42995) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | memory |
| Operator 关键词 | cuda;gemm;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 sleep/wake leaves P0 multimodal sender cache desynced from P1 → AssertionError on next image reuse

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary On the V1 engine with sleep mode enabled and a multimodal IPC cache (`--mm-processor-cache-gb > 0` = default behaviour), a `/sleep?level=1` followed by `/wake_up` deterministically corrupts the multimodal cache state. The next `/v1/chat/completions` request that re-uses an image whose `mm_hash` was seen **before** the sleep crashes the engine's preprocessing thread with: ``` AssertionError: Expected a cached item for mm_hash='...' ``` Afterwards: `/v1/models` and `/health` keep returning 200 OK, but any endpoint that round-trips to EngineCore (`/sleep`, `/wake_up`, `/is_sleeping`, generation) **hangs**. **Launch flags** /opt/venv/bin/vllm serve google/gemma-4-26B-A4B-it \ --host 0.0.0.0 --port 11437 \ --tensor-parallel-size 1 \ --dtype auto \ --gpu-memory-utilization 0.6271517157538793 \ --kv-cache-memory-bytes 8G \ --enable-prefix-caching \ --enable-sleep-mode \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --reasoning-parser gemma4 \ --compilation-config '{"cache_dir": "..."}' \ --default-chat-template-kwargs '{"enable_thinking": true}' **Required environment** VLLM_SERVER_DEV_MODE=1 ## Minimal reproduction...

## 现有链接修复摘要

#43001 [Bugfix] Clear P0 mm sender cache on sleep/pause to fix mm_hash desync

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: V1 sleep/wake leaves P0 multimodal sender cache desynced from P1 → AssertionError on next image reuse bug ### Your current environment ### 🐛 Describe the bug ## Summary On the V1 engine with sleep mode enabled an...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm cuda;gemm;triton build_error;crash dtype;env_dependency #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: -gb > 0` = default behaviour), a `/sleep?level=1` followed by `/wake_up` deterministically corrupts the multimodal cache state. The next `/v1/chat/completions` request that re-uses an image whose `mm_hash` was seen **be...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: lel;frontend_api;hardware_porting;model_support;multimodal_vlm cuda;gemm;triton build_error;crash dtype;env_dependency #43001 [Bugfix] Clear P0 mm sender cache on sleep/pause to fix mm_hash desync Your current environme...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43001](https://github.com/vllm-project/vllm/pull/43001) | closes_keyword | 0.95 | [Bugfix] Clear P0 mm sender cache on sleep/pause to fix mm_hash desync | Fixes #42995. `/sleep?level>=1` and `/pause?clear_cache=true` go through `EngineCore` on the engine side, which only clears the **P1** multimodal receiver cache via `pause_sched |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
