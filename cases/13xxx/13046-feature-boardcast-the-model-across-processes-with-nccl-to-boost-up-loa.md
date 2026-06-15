# vllm-project/vllm#13046: [Feature]: boardcast the model across processes with NCCL to boost up loading time for not shadered checkpoints

| 字段 | 值 |
| --- | --- |
| Issue | [#13046](https://github.com/vllm-project/vllm/issues/13046) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: boardcast the model across processes with NCCL to boost up loading time for not shadered checkpoints

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I was trying to run deepseek-r1 on 2 aws P5 instances (8xH100). The checkpoint is located either in local disk or in S3. As the checkpoint is not sharded, the model is read 16 times, which is 10TB read from S3 or local disk. Is it possible to read the model only on one process and distribute it across processes with NCCL? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion and pitch I was trying to run deepseek-r1 on 2 aws P5 instances (8xH100). The checkpoint is located either in local disk or in S3. As the checkpoint is not sharded, the model is read 16 times, which is 10TB read fr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: with NCCL to boost up loading time for not shadered checkpoints feature request;stale ### 🚀 The feature, motivation and pitch I was trying to run deepseek-r1 on 2 aws P5 instances (8xH100). The checkpoint is located eit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: boardcast the model across processes with NCCL to boost up loading time for not shadered checkpoints feature request;stale ### 🚀 The feature, motivation and pitch I was trying to run deepseek-r1 on 2 aws P5 i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
