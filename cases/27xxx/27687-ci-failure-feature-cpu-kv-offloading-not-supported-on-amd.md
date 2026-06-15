# vllm-project/vllm#27687: [CI Failure][Feature]: CPU KV Offloading not supported on AMD

| 字段 | 值 |
| --- | --- |
| Issue | [#27687](https://github.com/vllm-project/vllm/issues/27687) |
| 状态 | closed |
| 标签 | rocm;ci-failure;kv-connector |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure][Feature]: CPU KV Offloading not supported on AMD

### Issue 正文摘录

### Name of failing test v1/kv_offload/test_cpu_offloading.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `test_cpu_offloading` is failing on AMD CI with the exception: ``` 2025-10-27 21:28:16 PDT | (EngineCore_DP0 pid=2847) ERROR 10-28 04:28:16 [core.py:779] for src_cls, dst_cls, handler in self.spec.get_handlers(kv_caches): -- | -- | 2025-10-27 21:28:16 PDT | (EngineCore_DP0 pid=2847) ERROR 10-28 04:28:16 [core.py:779] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ | 2025-10-27 21:28:16 PDT | (EngineCore_DP0 pid=2847) ERROR 10-28 04:28:16 [core.py:779] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/kv_offload/cpu.py", line 55, in get_handlers | 2025-10-27 21:28:16 PDT | (EngineCore_DP0 pid=2847) ERROR 10-28 04:28:16 [core.py:779] raise Exception( | 2025-10-27 21:28:16 PDT | (EngineCore_DP0 pid=2847) ERROR 10-28 04:28:16 [core.py:779] Exception: CPU Offloading is currently only supported on CUDA GPUs | 2025-10-27 21:28:16 PDT | (EngineCore_DP0 pid=2847) Traceback (most recent call last): | 2025-10-27 21:28:16 PDT | (EngineCore_DP0 pid=2847) File "/usr/lib/python3.12/mu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure][Feature]: CPU KV Offloading not supported on AMD rocm;ci-failure;kv-connector ### Name of failing test v1/kv_offload/test_cpu_offloading.py ### Basic information - [ ] Flaky test - [x] Can reproduce locall
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure][Feature]: CPU KV Offloading not supported on AMD rocm;ci-failure;kv-connector ### Name of failing test v1/kv_offload/test_cpu_offloading.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: est_cpu_offloading.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `test_cpu_offloading` is failing o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [CI Failure][Feature]: CPU KV Offloading not supported on AMD rocm;ci-failure;kv-connector ### Name of failing test v1/kv_offload/test_cpu_offloading.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Name of failing test v1/kv_offload/test_cpu_offloading.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing tes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
