# vllm-project/vllm#41852: [CI Failure]:  mi300_4: RayExecutorV2 (4 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#41852](https://github.com/vllm-project/vllm/issues/41852) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi300_4: RayExecutorV2 (4 GPUs)

### Issue 正文摘录

### Name of failing test `pytest -s -v distributed/test_ray_v2_executor.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/amd-ci/builds/8248/canvas?sid=019dfbdf-4fb7-4a5e-8c8d-97dc71657965&tab=output ### 📝 History of failing test Passed in very recent nightly run: https://buildkite.com/vllm/amd-ci/builds/8193/canvas?sid=019df193-54ec-4fe8-9012-08e851828415&tab=output

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi300_4: RayExecutorV2 (4 GPUs) ci-failure ### Name of failing test `pytest -s -v distributed/test_ray_v2_executor.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by e
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t_ray_v2_executor.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/amd-ci/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: mi300_4: RayExecutorV2 (4 GPUs) ci-failure ### Name of failing test `pytest -s -v distributed/test_ray_v2_executor.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by ext...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ng test `pytest -s -v distributed/test_ray_v2_executor.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ailure]: mi300_4: RayExecutorV2 (4 GPUs) ci-failure ### Name of failing test `pytest -s -v distributed/test_ray_v2_executor.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
