# vllm-project/vllm#11482: [Usage]: 关于vllm0.6.4的性能提升在qwen2.5上并没有体现

| 字段 | 值 |
| --- | --- |
| Issue | [#11482](https://github.com/vllm-project/vllm/issues/11482) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 关于vllm0.6.4的性能提升在qwen2.5上并没有体现

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` vllm/vllm-openai:v0.6.5 vllm/vllm-openai:v0.6.2 ``` ### How would you like to use vllm @DarkLight1337 Hi~ 我测试了下vllm0.6.2和0.6.5分别请求同一份数据，发现他们处理完的时间都差不多，两个都用时5小时20分钟左右，0.6.2快了7分钟。请问下自0.6.4的性能提升在qwen2.5的各种模型中是否有效，我需要考虑是否升级部署环境。谢谢 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 。谢谢 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: 关于vllm0.6.4的性能提升在qwen2.5上并没有体现 usage;stale ### Your current environment ```text The output of `python collect_env.py` vllm/vllm-openai:v0.6.5 vllm/vllm-openai:v0.6.2 ``` ### How would you like to use vllm @Dark...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: 关于vllm0.6.4的性能提升在qwen2.5上并没有体现 usage;stale ### Your current environment ```text The output of `python collect_env.py` vllm/vllm-openai:v0.6.5 vllm/vllm-openai:v0.6.2 ``` ### How would you like to use vllm @Dark...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
