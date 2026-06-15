# vllm-project/vllm#11421: [Bug]: 0.6.5 randomly closes connection/drops requests

| 字段 | 值 |
| --- | --- |
| Issue | [#11421](https://github.com/vllm-project/vllm/issues/11421) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 0.6.5 randomly closes connection/drops requests

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running v0.6.5, after a while it starts to have strange network issues like aborting/dropping client connections. We have a prometheus dashboard and when this happens, the time per output step we have disappears: avg by (job) ( rate(vllm:time_per_output_token_seconds_sum[5m]) / rate(vllm:time_per_output_token_seconds_count[5m]) ) That formula disappearing from metrics always coincides with a server breaking. We haven't identified past here on root cause. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: 0.6.5 randomly closes connection/drops requests bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running v0.6.5, after a while it starts to have strange network is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _seconds_count[5m]) ) That formula disappearing from metrics always coincides with a server breaking. We haven't identified past here on root cause. ### Before submitting a new issue... - [X] Make sure you already searc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: connection/drops requests bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running v0.6.5, after a while it starts to have strange network issues like aborting/dropping c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
