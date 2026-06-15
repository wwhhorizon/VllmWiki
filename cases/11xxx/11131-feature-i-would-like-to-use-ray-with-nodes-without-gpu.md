# vllm-project/vllm#11131: [Feature]: I would like to use ray with nodes without GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#11131](https://github.com/vllm-project/vllm/issues/11131) |
| 状态 | closed |
| 标签 | feature request;ray |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: I would like to use ray with nodes without GPU

### Issue 正文摘录

### 🚀 The feature, motivation and pitch hi, I would like to use the fantastic https://docs.vllm.ai/en/stable/serving/distributed_serving.html feature. i understood it works with GPU only. I tried to modify the run_cluster.sh removing the --gpus all but it doesn't work. Could you give me details of this requested feature? Thanks a lot Mario ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: I would like to use ray with nodes without GPU feature request;ray ### 🚀 The feature, motivation and pitch hi, I would like to use the fantastic https://docs.vllm.ai/en/stable/serving/distributed_serving.html...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
