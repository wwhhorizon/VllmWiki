# vllm-project/vllm#27073: [Bug]:几个大的token超限制请求之后GPU KV cache usage持续升高一直接近100%，几个小时不下降，最后重启解决

| 字段 | 值 |
| --- | --- |
| Issue | [#27073](https://github.com/vllm-project/vllm/issues/27073) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:几个大的token超限制请求之后GPU KV cache usage持续升高一直接近100%，几个小时不下降，最后重启解决

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm/vllm-openai:v0.10.2 连续几次大的token超长推理报错之后GPU KV cache usage 逐渐升高，一直接近100%，不自动降低，持续6个小时，最后重启服务解决 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]:几个大的token超限制请求之后GPU KV cache usage持续升高一直接近100%，几个小时不下降，最后重启解决 bug;stale ### Your current environment ### 🐛 Describe the bug vllm/vllm-openai:v0.10.2 连续几次大的token超长推理报错之后GPU KV cache usage 逐渐升高，一直接近100%，不自动降低，持续6个小时...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]:几个大的token超限制请求之后GPU KV cache usage持续升高一直接近100%，几个小时不下降，最后重启解决 bug;stale ### Your current environment ### 🐛 Describe the bug vllm/vllm-openai:v0.10.2 连续几次大的token超长推理报错之后GPU KV cache usage 逐渐升高，一直接近100%，不自动降低，持续6个小时...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
