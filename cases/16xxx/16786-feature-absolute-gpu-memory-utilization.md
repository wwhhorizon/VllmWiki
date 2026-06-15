# vllm-project/vllm#16786: [Feature]: Absolute gpu_memory_utilization

| 字段 | 值 |
| --- | --- |
| Issue | [#16786](https://github.com/vllm-project/vllm/issues/16786) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Absolute gpu_memory_utilization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi there :wave: I'm currently deploying a vllm model in gpu that has multiple processes running, meaning gpu is not empty. Let's say I know, that my vllm model fits into 3gb (and it's 0.06 of my gpu). However, I don't know how much memory is occupied by other processes on my gpu. All I know is that it always has 3gb of available memory (at least I want to take care about it and not vllm to worry) So, I want model to take only 3gb gpu, so I want to set `gpu_memory_utilization` to 0.06, however because of `non_torch_allocations` [here](https://github.com/vllm-project/vllm/blob/dbe7f07001955d6ba745f297203fee0aa0fbc5cf/vllm/v1/worker/gpu_worker.py#L179C9-L179C30) I need to set it higher. It becomes a problem, since I don't know beforehand how much of my gpu is allocated by other processes (all I know, I have enough memory for my vllm model) Right now I'm solving it by ignoring these lines: ```python if non_torch_allocations > 0: peak_memory += non_torch_allocations ``` It seems to work however I don't know whether this way has pitfalls ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x]...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Absolute gpu_memory_utilization feature request;stale ### 🚀 The feature, motivation and pitch Hi there :wave: I'm currently deploying a vllm model in gpu that has multiple processes running, meaning gpu is no...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: re, motivation and pitch Hi there :wave: I'm currently deploying a vllm model in gpu that has multiple processes running, meaning gpu is not empty. Let's say I know, that my vllm model fits into 3gb (and it's 0.06 of my...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
