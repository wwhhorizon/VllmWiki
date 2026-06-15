# vllm-project/vllm#13716: [Bug][CI/CD]: test_metrics.py made failed tests

| 字段 | 值 |
| --- | --- |
| Issue | [#13716](https://github.com/vllm-project/vllm/issues/13716) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][CI/CD]: test_metrics.py made failed tests

### Issue 正文摘录

### Your current environment vLLM v0.7.3 base https://github.com/vllm-project/vllm/pull/11966 ### 🐛 Describe the bug ``` [2025-02-23T04:29:50Z] =========================== short test summary info ============================ -- | [2025-02-23T04:29:50Z] FAILED metrics/test_metrics.py::test_metric_set_tag_model_name[None-float-distilbert/distilgpt2] - AssertionError: Metrics tag model_name is wrong! expect: 'distilbert/distilgpt2' | [2025-02-23T04:29:50Z] actual: 'distilbert/distilgpt2' | [2025-02-23T04:29:50Z] assert 'distilbert/distilgpt2' == 's3://vllm-ci...rt/distilgpt2' | [2025-02-23T04:29:50Z] | [2025-02-23T04:29:50Z] - s3://vllm-ci-model-weights/distilbert/distilgpt2 | [2025-02-23T04:29:50Z] + distilbert/distilgpt2 | [2025-02-23T04:29:50Z] FAILED metrics/test_metrics.py::test_metric_set_tag_model_name[served_model_name1-float-distilbert/distilgpt2] - AssertionError: Metrics tag model_name is wrong! expect: 'distilbert/distilgpt2' | [2025-02-23T04:29:50Z] actual: 'distilbert/distilgpt2' | [2025-02-23T04:29:50Z] assert 'distilbert/distilgpt2' == 's3://vllm-ci...rt/distilgpt2' | [2025-02-23T04:29:50Z] | [2025-02-23T04:29:50Z] - s3://vllm-ci-model-weights/distilbert/distilgpt2 |...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug][CI/CD]: test_metrics.py made failed tests bug ### Your current environment vLLM v0.7.3 base https://github.com/vllm-project/vllm/pull/11966 ### 🐛 Describe the bug ``` [2025-02-23T04:29:50Z] =======================...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug][CI/CD]: test_metrics.py made failed tests bug ### Your current environment vLLM v0.7.3 base https://github.com/vllm-project/vllm/pull/11966 ### 🐛 Describe the bug ``` [2025-02-23T04:29:50Z] ========================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0Z] FAILED metrics/test_metrics.py::test_engine_log_metrics_regression[False-4-half-distilbert/distilgpt2] - AssertionError: Metrics should be collected | [2025-02-23T04:29:50Z] assert None == 8 | [2025-02-23T04:29:50Z]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 025-02-23T04:29:50Z] FAILED metrics/test_metrics.py::test_metric_set_tag_model_name[None-float-distilbert/distilgpt2] - AssertionError: Metrics tag model_name is wrong! expect: 'distilbert/distilgpt2' | [2025-02-23T04:2...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
