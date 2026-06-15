# vllm-project/vllm#39536: [CI] test_moe_layer: all modelopt_fp4 subtests failing on 2 B200s

| 字段 | 值 |
| --- | --- |
| Issue | [#39536](https://github.com/vllm-project/vllm/issues/39536) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] test_moe_layer: all modelopt_fp4 subtests failing on 2 B200s

### Issue 正文摘录

### Name of failing test `tests/kernels/moe/test_moe_layer.py::test_moe_layer` — all `modelopt_fp4` parameterized subtests ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test In the **2026-04-09 nightly** build ([#60697](https://buildkite.com/vllm/ci/builds/60697)), the **Kernels FusedMoE Layer Test (2 B200s)** step failed with **26 subtests** failing. All failing subtests involve `modelopt_fp4` quantization format, across three different communication backends: - `flashinfer_nvlink_two_sided` — 20 failed subtests - `flashinfer_nvlink_one_sided` — 20 failed subtests - `deepep_high_throughput` — 12 failed subtests + 1 SIGABRT **Step link:** https://buildkite.com/vllm/ci/builds/60697#019d740c-e286-4513-b9dd-7d6dc04ab473 **Commit:** `e5de19ff9a64` ### Error details All failures raise `RuntimeError` from `_parallel_worker` (line 1629) with a list of failed subtests. The `deepep_high_throughput-2-1-True` variant also terminated with `SIGABRT`. Example failed subtest parameter sets: ``` [1-128-256-8-2-bfloat16-modelopt_fp4-False-False-False-False-False-flashinfer_nvlink_two_sid...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [CI] test_moe_layer: all modelopt_fp4 subtests failing on 2 B200s ### Name of failing test `tests/kernels/moe/test_moe_layer.py::test_moe_layer` — all `modelopt_fp4` parameterized subtests ### Basic information - [ ] Fl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI] test_moe_layer: all modelopt_fp4 subtests failing on 2 B200s ### Name of failing test `tests/kernels/moe/test_moe_layer.py::test_moe_layer` — all `modelopt_fp4` parameterized subtests ### Basic information - [ ] F
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI] test_moe_layer: all modelopt_fp4 subtests failing on 2 B200s ### Name of failing test `tests/kernels/moe/test_moe_layer.py::test_moe_layer` — all `modelopt_fp4` parameterized subtests ### Basic information - [ ] Fl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI] test_moe_layer: all modelopt_fp4 subtests failing on 2 B200s ### Name of failing test `tests/kernels/moe/test_moe_layer.py::test_moe_layer` — all `modelopt_fp4` parameterized subtests ### Basic information - [ ] Fl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: `modelopt_fp4` quantization format, across three different communication backends: - `flashinfer_nvlink_two_sided` — 20 failed subtests - `flashinfer_nvlink_one_sided` — 20 failed subtests - `deepep_high_throughput` — 1...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
