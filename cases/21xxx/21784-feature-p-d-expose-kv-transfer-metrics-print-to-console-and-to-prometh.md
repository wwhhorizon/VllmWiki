# vllm-project/vllm#21784: [Feature]: [P/D] Expose kv_transfer metrics (print to console, and to promethus)

| 字段 | 值 |
| --- | --- |
| Issue | [#21784](https://github.com/vllm-project/vllm/issues/21784) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [P/D] Expose kv_transfer metrics (print to console, and to promethus)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now P/D is supported in latest release, it would be great to expose metrics like kv_xfer_time, kv_xfer_bytes, kv_xfer_num_blocks etc. to both console and prometheus, for performance monitoring. I think we can break the work into several parts 1. pipe the metrics from `nixl_connector` all the way to `model_runner` , this can be further broken into a. change interface of `get_finished` to return not only ids, ideally a new class to aggregate all the infomation b. add metrics to the new class, it's worth discussion wether we want aggregated stats (avg, sum) or raw stats 2. consume the metrics from logger, in `vllm/v1/metrics/loggers.py` 3. consume the metrics from promethus logger, to be done in `vllm/v1/metrics/loggers.py` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. cc @NickLucche @robertgshaw2-redhat @kouroshHakha @ruisearch42

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Expose kv_transfer metrics (print to console, and to promethus) feature request;stale ### 🚀 The feature, motivation and pitch Now P/D is supported in latest release, it would be great to expose metrics like kv_xfer_time...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: be great to expose metrics like kv_xfer_time, kv_xfer_bytes, kv_xfer_num_blocks etc. to both console and prometheus, for performance monitoring. I think we can break the work into several parts 1. pipe the metrics from...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: several parts 1. pipe the metrics from `nixl_connector` all the way to `model_runner` , this can be further broken into a. change interface of `get_finished` to return not only ids, ideally a new class to aggregate all...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: stale ### 🚀 The feature, motivation and pitch Now P/D is supported in latest release, it would be great to expose metrics like kv_xfer_time, kv_xfer_bytes, kv_xfer_num_blocks etc. to both console and prometheus, for per...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
