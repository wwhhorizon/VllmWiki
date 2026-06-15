# vllm-project/vllm#39537: [CI] test_no_sync_with_spec_decode[eagle3-llama]: unexpected GPU-CPU sync

| 字段 | 值 |
| --- | --- |
| Issue | [#39537](https://github.com/vllm-project/vllm/issues/39537) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] test_no_sync_with_spec_decode[eagle3-llama]: unexpected GPU-CPU sync

### Issue 正文摘录

### Name of failing test `tests/v1/e2e/spec_decode/test_async_spec_decode.py::test_no_sync_with_spec_decode[eagle3-llama]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test In the **2026-04-09 nightly** build ([#60697](https://buildkite.com/vllm/ci/builds/60697)), the **Spec Decode Draft Model Nightly B200** step failed with 1 test failure. **Step link:** https://buildkite.com/vllm/ci/builds/60697#019d740c-e312-46fd-b21c-4b44b3b5fd1b **Commit:** `e5de19ff9a64` ### Error details ``` FAILED test_async_spec_decode.py::test_no_sync_with_spec_decode[eagle3-llama] AssertionError: Unexpected GPU-CPU sync: seq_lens_cpu lazy init triggered 2 times. See stack traces above. assert 2 == 0 ``` The test asserts that no GPU-CPU synchronization occurs during speculative decoding with async scheduling enabled. The assertion detected 2 unexpected `seq_lens_cpu` lazy init syncs. ### Test results summary ``` 1 failed, 7 passed, 10 skipped, 37 deselected, 1 xfailed, 21 warnings in 471.68s ``` ### Potentially causal PRs - #39206 — `tests/v1/e2e/spec_decode`: assert async scheduling is used (...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [CI] test_no_sync_with_spec_decode[eagle3-llama]: unexpected GPU-CPU sync ### Name of failing test `tests/v1/e2e/spec_decode/test_async_spec_decode.py::test_no_sync_with_spec_decode[eagle3-llama]` ### Basic information...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI] test_no_sync_with_spec_decode[eagle3-llama]: unexpected GPU-CPU sync ### Name of failing test `tests/v1/e2e/spec_decode/test_async_spec_decode.py::test_no_sync_with_spec_decode[eagle3-llama]` ### Basic information
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI] test_no_sync_with_spec_decode[eagle3-llama]: unexpected GPU-CPU sync ### Name of failing test `tests/v1/e2e/spec_decode/test_async_spec_decode.py::test_no_sync_with_spec_decode[eagle3-llama]` ### Basic information...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ance]: Fully Async Spec-Decoding | Make `seq_lens_cpu` in CommonAttentionMetadata optional — the underlying issue being tracked ### Analysis PR #39206 added assertions to detect GPU-CPU syncs during spec decode. The ass...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ens_cpu` lazy initialization. This is the behavior described in #29134 — FlashInfer's plan function triggers a D2H or H2D transfer that blocks full async overlap. The test is surfacing a known limitation that hasn't bee...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
