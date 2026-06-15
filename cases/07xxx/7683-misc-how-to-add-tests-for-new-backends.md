# vllm-project/vllm#7683: [Misc]: how to add tests for new backends?

| 字段 | 值 |
| --- | --- |
| Issue | [#7683](https://github.com/vllm-project/vllm/issues/7683) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: how to add tests for new backends?

### Issue 正文摘录

### Anything you want to discuss about vllm. I see that some backends like Intel CPU have tests, but I cannot find any such configurations in .buildkite folder. Could you please elaborate how we can add some simple scripts to check that OpenVINO backend is not broken? We have simple script for it https://github.com/vllm-project/vllm/blob/main/.buildkite/run-openvino-test.sh, but don't know how to add it to CI service. Thanks

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: like Intel CPU have tests, but I cannot find any such configurations in .buildkite folder. Could you please elaborate how we can add some simple scripts to check that OpenVINO backend is not broken? We have simple scrip...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Misc]: how to add tests for new backends? stale ### Anything you want to discuss about vllm. I see that some backends like Intel CPU have tests, but I cannot find any such configurations in .buildkite folder. Could you...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: that some backends like Intel CPU have tests, but I cannot find any such configurations in .buildkite folder. Could you please elaborate how we can add some simple scripts to check that OpenVINO backend is not broken? W...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: how to add tests for new backends? stale ### Anything you want to discuss about vllm. I see that some backends like Intel CPU have tests, but I cannot find any such configurations in .buildkite folder. Could you...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Misc]: how to add tests for new backends? stale ### Anything you want to discuss about vllm. I see that some backends like Intel CPU have tests, but I cannot find any such configurations in .buildkite folder. Could you...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
