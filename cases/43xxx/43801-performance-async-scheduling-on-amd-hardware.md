# vllm-project/vllm#43801: [Performance]: Async scheduling on AMD hardware

| 字段 | 值 |
| --- | --- |
| Issue | [#43801](https://github.com/vllm-project/vllm/issues/43801) |
| 状态 | open |
| 标签 | performance;rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;hardware_porting;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Async scheduling on AMD hardware

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression It looks like on AMD hardware (I'm using MI350X), schedule can't properly overlap with GPU computation. Explanation from CodeX: > On CUDA, graph launch behaves like an enqueue, so vLLM overlaps CPU scheduling with GPU graph execution. On MI350X ROCm, hipGraphLaunch appears to hold the calling Python thread for nearly the full graph execution. As a result, async scheduling is enabled but cannot create useful overlap in TP=1 uni; scheduling runs after the graph/sample boundary and creates a GPU idle bubble before the next forward. Is this a known issue? Looks like it's ROCm runtime limitation. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Performance]: Async scheduling on AMD hardware performance;rocm ### Proposal to improve performance _No response_ ### Report of performance regression It looks like on AMD hardware (I'm using MI350X), schedule can't pr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tion. Explanation from CodeX: > On CUDA, graph launch behaves like an enqueue, so vLLM overlaps CPU scheduling with GPU graph execution. On MI350X ROCm, hipGraphLaunch appears to hold the calling Python thread for nearl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression It looks like on AMD hardware (I'm using MI350X), schedule can't properly overlap with GPU computation. Explanation from CodeX: > On CUDA...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: formance distributed_parallel;hardware_porting;scheduler_memory cuda env_dependency Proposal to improve performance

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
