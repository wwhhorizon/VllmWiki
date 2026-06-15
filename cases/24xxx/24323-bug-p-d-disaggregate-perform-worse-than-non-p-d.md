# vllm-project/vllm#24323: [Bug]: P/D disaggregate perform worse than non-p/d

| 字段 | 值 |
| --- | --- |
| Issue | [#24323](https://github.com/vllm-project/vllm/issues/24323) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: P/D disaggregate perform worse than non-p/d

### Issue 正文摘录

### Your current environment H100 GPUs ### 🐛 Describe the bug Benchmarked llama 3 model on h100 gpu, with and without disaggregation using the lmcache connector, performance is worse than without. Input token is 2000 and output token is 2000, 10 concurrent requests for 10 mins. Anyone else facing worse performance with p/d? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: egate perform worse than non-p/d bug;stale ### Your current environment H100 GPUs ### 🐛 Describe the bug Benchmarked llama 3 model on h100 gpu, with and without disaggregation using the lmcache connector, performance is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Your current environment H100 GPUs ### 🐛 Describe the bug Benchmarked llama 3 model on h100 gpu, with and without disaggregation using the lmcache connector, performance is worse than without. Input token is 2000 and ou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: P/D disaggregate perform worse than non-p/d bug;stale ### Your current environment H100 GPUs ### 🐛 Describe the bug Benchmarked llama 3 model on h100 gpu, with and without disaggregation using the lmcache connect...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: g;stale ### Your current environment H100 GPUs ### 🐛 Describe the bug Benchmarked llama 3 model on h100 gpu, with and without disaggregation using the lmcache connector, performance is worse than without. Input token is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: output token is 2000, 10 concurrent requests for 10 mins. Anyone else facing worse performance with p/d? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatb...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
