# vllm-project/vllm#12511: [Feature]: Support torch.distributed as the runtime for multi-node inference

| 字段 | 值 |
| --- | --- |
| Issue | [#12511](https://github.com/vllm-project/vllm/issues/12511) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support torch.distributed as the runtime for multi-node inference

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We currently support Ray-based distributed inference, which requires Ray. This issue requests multi-node support for `torch.distributed`. ### Usage Example: ```bash # Server 1 vllm serve model_tag --nnodes 2 --rank 0 --dist-init-addr 192.168.0.1:5000 # Server 2 vllm serve model_tag --nnodes 2 --rank 1 --dist-init-addr 192.168.0.2:5000 ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: upport torch.distributed as the runtime for multi-node inference feature request;stale ### 🚀 The feature, motivation and pitch We currently support Ray-based distributed inference, which requires Ray. This issue request...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: `torch.distributed`. ### Usage Example: ```bash # Server 1 vllm serve model_tag --nnodes 2 --rank 0 --dist-init-addr 192.168.0.1:5000 # Server 2 vllm serve model_tag --nnodes 2 --rank 1 --dist-init-addr 192.168.0.2:5000...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
