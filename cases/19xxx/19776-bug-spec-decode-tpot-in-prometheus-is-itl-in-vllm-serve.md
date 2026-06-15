# vllm-project/vllm#19776: [Bug][Spec Decode]: TPOT in prometheus is ITL in vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#19776](https://github.com/vllm-project/vllm/issues/19776) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Spec Decode]: TPOT in prometheus is ITL in vllm serve

### Issue 正文摘录

### 🐛 Describe the bug There are 2 different kinds of metrics: ITL and TPOT. They are same for non SD model but are different for SD models. As per [vLLM serve benchmark script](https://github.com/vllm-project/vllm/blob/a44b1c951df919bd6a42cb7e13104106619723ff/vllm/benchmarks/serve.py#L170), ITL measures the time to generate in 1 scheduler step whereas TPOT measures the time to generate 1 token. However, the prometheus metric measures TPOT as [this](https://github.com/vllm-project/vllm/blob/a44b1c951df919bd6a42cb7e13104106619723ff/vllm/v1/metrics/stats.py#L126) which corresponds to ITL in vLLM serve benchmark and contradicts with the behavior of TPOT. I think it should be renamed as ITL. Also, is it possible to log the correct value for TPOT on prometheus so that one can measure the Output tokens/s reliably using prometheus? cc: @markmc ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug][Spec Decode]: TPOT in prometheus is ITL in vllm serve bug;stale ### 🐛 Describe the bug There are 2 different kinds of metrics: ITL and TPOT. They are same for non SD model but are different for SD models. As per [...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug][Spec Decode]: TPOT in prometheus is ITL in vllm serve bug;stale ### 🐛 Describe the bug There are 2 different kinds of metrics: ITL and TPOT. They are same for non SD model but are different for SD models. As per [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: mc ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: are 2 different kinds of metrics: ITL and TPOT. They are same for non SD model but are different for SD models. As per [vLLM serve benchmark script](https://github.com/vllm-project/vllm/blob/a44b1c951df919bd6a42cb7e1310...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
