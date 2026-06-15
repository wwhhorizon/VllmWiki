# vllm-project/vllm#39196: [Bug]: NCCL Error: unhandled cuda error

| 字段 | 值 |
| --- | --- |
| Issue | [#39196](https://github.com/vllm-project/vllm/issues/39196) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NCCL Error: unhandled cuda error

### Issue 正文摘录

### Your current environment Can't share completely but it has 2 gpus with 40GB vram each. They run on 1 single node. When I run serve Qwen30-30B-A3B it fails and only returns this `NCCL Error: unhandled cuda error`. I have set `NCCL_DEBUG="INFO" or "TRACE"` but neither shows the error. ### 🐛 Describe the bug . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: NCCL Error: unhandled cuda error bug ### Your current environment Can't share completely but it has 2 gpus with 40GB vram each. They run on 1 single node. When I run serve Qwen30-30B-A3B it fails and only returns...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 2 gpus with 40GB vram each. They run on 1 single node. When I run serve Qwen30-30B-A3B it fails and only returns this `NCCL Error: unhandled cuda error`. I have set `NCCL_DEBUG="INFO" or "TRACE"` but neither shows the e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development distributed_parallel cuda Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
