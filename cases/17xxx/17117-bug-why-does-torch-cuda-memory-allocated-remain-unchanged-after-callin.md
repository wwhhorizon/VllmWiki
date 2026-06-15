# vllm-project/vllm#17117: [Bug]: Why does torch.cuda.memory_allocated() remain unchanged after calling sleep()?

| 字段 | 值 |
| --- | --- |
| Issue | [#17117](https://github.com/vllm-project/vllm/issues/17117) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 |  |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Why does torch.cuda.memory_allocated() remain unchanged after calling sleep()?

### Issue 正文摘录

### Your current environment Hi! Although the free bytes increase (as shown by torch.cuda.mem_get_info()[0]), why does torch.cuda.memory_allocated() remain unchanged after calling sleep()? ### 🐛 Describe the bug Hi! Although the free bytes increase (as shown by torch.cuda.mem_get_info()[0]), why does torch.cuda.memory_allocated() remain unchanged after calling sleep()? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. CC @youkaichao @fingertap @fabianlim

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Why does torch.cuda.memory_allocated() remain unchanged after calling sleep()? bug;stale ### Your current environment Hi! Although the free bytes increase (as shown by torch.cuda.mem_get_info()[0]), why does torc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed questions. CC @youkaichao @fingertap @fabianlim performance cuda env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: orch.cuda.memory_allocated() remain unchanged after calling sleep()? bug;stale ### Your current environment Hi! Although the free bytes increase (as shown by torch.cuda.mem_get_info()[0]), why does torch.cuda.memory_all...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. CC @youkaichao @fingertap @fabianlim performance cuda env_dependency Your current env...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
