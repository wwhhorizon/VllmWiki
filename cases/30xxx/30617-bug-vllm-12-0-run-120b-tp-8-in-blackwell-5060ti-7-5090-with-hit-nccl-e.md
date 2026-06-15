# vllm-project/vllm#30617: [Bug]: vllm 12.0 run 120b tp=8 in blackwell 5060ti*7+5090 with hit nccl error in cuda graph

| 字段 | 值 |
| --- | --- |
| Issue | [#30617](https://github.com/vllm-project/vllm/issues/30617) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 12.0 run 120b tp=8 in blackwell 5060ti*7+5090 with hit nccl error in cuda graph

### Issue 正文摘录

### Your current environment vllm 12.0 run 120b tp=8 in blackwell 5060ti*7+5090 with hit nccl error in cuda graph ### 🐛 Describe the bug vllm 12.0 run 120b tp=8 in blackwell 5060ti*7+5090 with hit nccl error in cuda graph ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vllm 12.0 run 120b tp=8 in blackwell 5060ti*7+5090 with hit nccl error in cuda graph bug;stale ### Your current environment vllm 12.0 run 120b tp=8 in blackwell 5060ti*7+5090 with hit nccl error in cuda graph ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 0b tp=8 in blackwell 5060ti*7+5090 with hit nccl error in cuda graph bug;stale ### Your current environment vllm 12.0 run 120b tp=8 in blackwell 5060ti*7+5090 with hit nccl error in cuda graph ### 🐛 Describe the bug vll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development distributed_parallel;hardware_porting cuda Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
