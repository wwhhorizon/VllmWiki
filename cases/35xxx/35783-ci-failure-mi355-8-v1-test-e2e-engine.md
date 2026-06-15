# vllm-project/vllm#35783: [CI Failure]:  mi355_8: V1 Test e2e + engine

| 字段 | 值 |
| --- | --- |
| Issue | [#35783](https://github.com/vllm-project/vllm/issues/35783) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_8: V1 Test e2e + engine

### Issue 正文摘录

### Name of failing test `pytest -s -v v1/engine/test_engine_core_client.py::test_kv_cache_events[False-inproc]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This regression happens very rarely. The log looks like this: ```log @torch.inference_mode() def determine_available_memory(self) -> int: """Profiles the peak memory usage of the model to determine how much memory can be used for KV cache without OOMs. The engine will first conduct a profiling of the existing memory usage. Then, it calculates the free memory that can be used for KV cache in bytes. Tip: You may limit the usage of GPU memory by adjusting the `gpu_memory_utilization` parameter. """ if kv_cache_memory_bytes := self.cache_config.kv_cache_memory_bytes: # still need a profile run which compiles the model for # max_num_batched_tokens self.model_runner.profile_run() msg = ( f"Initial free memory {format_gib(self.init_snapshot.free_memory)} " f"GiB, reserved {format_gib(kv_cache_memory_bytes)} GiB memory for " "KV Cache as specified by kv_cache_memory_bytes config and " "skipped memory profiling. This d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: mi355_8: V1 Test e2e + engine ci-failure ### Name of failing test `pytest -s -v v1/engine/test_engine_core_client.py::test_kv_cache_events[False-inproc]` ### Basic information - [x] Flaky test - [ ] Can
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [CI Failure]: mi355_8: V1 Test e2e + engine ci-failure ### Name of failing test `pytest -s -v v1/engine/test_engine_core_client.py::test_kv_cache_events[False-inproc]` ### Basic information - [x] Flaky test - [ ] Can re...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: usage of the model to determine how much memory can be used for KV cache without OOMs. The engine will first conduct a profiling of the existing memory usage. Then, it calculates the free memory that can be used for KV...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _engine_core_client.py::test_kv_cache_events[False-inproc]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: events[False-inproc]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This regression happens very rarel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
