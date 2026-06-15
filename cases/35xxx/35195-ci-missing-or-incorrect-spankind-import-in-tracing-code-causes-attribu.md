# vllm-project/vllm#35195: [CI] Missing or incorrect SpanKind import in tracing code causes AttributeError

| 字段 | 值 |
| --- | --- |
| Issue | [#35195](https://github.com/vllm-project/vllm/issues/35195) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] Missing or incorrect SpanKind import in tracing code causes AttributeError

### Issue 正文摘录

## Name of failing test - `v1/tracing/test_tracing.py::test_traces` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Metrics, Tracing (2 GPUs) **Category:** test ## Describe the failing test The tracing code in output_processor.py attempts to use SpanKind.SERVER but SpanKind resolves to typing.Any instead of the OpenTelemetry SpanKind enum, indicating that SpanKind is not properly imported from opentelemetry.trace. This causes an AttributeError when trying to access the SERVER attribute during tracing instrumentation in the do_tracing() method. ``` AttributeError: type object 'Any' has no attribute 'SERVER' - SpanKind resolves to typing.Any instead of OpenTelemetry's SpanKind enum AttributeError: type object 'Any' has no attribute 'SERVER' AttributeError: type object 'Any' has no attribute 'SERVER' - SpanKind resolves to typing.Any instead of opentelemetry.trace.SpanKind enum when accessing SpanKind.SERVER in output_processor.py do_tracing() method AttributeError: type object 'Any' has no attribute 'SERVER' - SpanKind resolves to typing.Any instead of OpenTelemetry's SpanKind enum in output_processor.py:774 Att...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI] Missing or incorrect SpanKind import in tracing code causes AttributeError ci-failure ## Name of failing test - `v1/tracing/test_tracing.py::test_traces` ## Basic information - [ ] Flaky test - [ ] Can reproduce l
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: acing.py::test_traces` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Metrics, Tracing (2 GPUs) **Category:** test ## Describe the failing test Th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: (2 GPUs)](https://buildkite.com/vllm/ci/builds/52884#019c8f90-5891-48b9-b200-fbea487fe289) - ... and 4 more builds ## History of failing test - **First seen:** Build #52859 (6af03f23) - **Last pass:** Build #52851 (f918...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: of failing test - `v1/tracing/test_tracing.py::test_traces` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Metrics, Tracing (2 GPUs) **Category:**...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: port in tracing code causes AttributeError ci-failure ## Name of failing test - `v1/tracing/test_tracing.py::test_traces` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external librar...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
