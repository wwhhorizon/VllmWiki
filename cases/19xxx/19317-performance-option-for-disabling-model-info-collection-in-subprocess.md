# vllm-project/vllm#19317: [Performance]: Option for disabling model info collection in subprocess

| 字段 | 值 |
| --- | --- |
| Issue | [#19317](https://github.com/vllm-project/vllm/issues/19317) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Option for disabling model info collection in subprocess

### Issue 正文摘录

### Proposal to improve performance By default vLLM collects model support info in a single sub process per model (added in in https://github.com/vllm-project/vllm/pull/9233). Specifically, this https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/registry.py#L336 `_run_in_subprocess` call. This adds ~4s when running against local ssd and can easily be double or more against a network filesystem in some environments. Collecting the info in-process does not seem to have adverse effects, at least based on my limited manual testing, but I lack context on why this was done in the first place. Can we make this behaviour configurable via a boolean flag or env var? That way users could opt out. `collect_model_info_via_subprocess = True` Something like ``` if self.model_config.collect_model_info_via_subprocess: return _run_in_subprocess( lambda: _ModelInfo.from_model_cls(self.load_model_cls())) return _ModelInfo.from_model_cls(self.load_model_cls()) ``` ![Image](https://github.com/user-attachments/assets/5426bbd0-5c35-472a-b430-b800ce5d1a58) Show the latency in "inspect-model" span based on my local wip otel tracing of start up CC @DarkLight1337 ### Report of performa...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: es not seem to have adverse effects, at least based on my limited manual testing, but I lack context on why this was done in the first place. Can we make this behaviour configurable via a boolean flag or env var? That w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Option for disabling model info collection in subprocess performance;stale ### Proposal to improve performance By default vLLM collects model support info in a single sub process per model (added in in ht...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r model (added in in https://github.com/vllm-project/vllm/pull/9233). Specifically, this https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/registry.py#L336 `_run_in_subprocess` call. This adds ~4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ry) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e]: Option for disabling model info collection in subprocess performance;stale ### Proposal to improve performance By default vLLM collects model support info in a single sub process per model (added in in https://githu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
