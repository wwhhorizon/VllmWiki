# vllm-project/vllm#30088: [Performance]: Manual Controlled GC

| 字段 | 值 |
| --- | --- |
| Issue | [#30088](https://github.com/vllm-project/vllm/issues/30088) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Manual Controlled GC

### Issue 正文摘录

### Proposal to improve performance ## Issues By default, python GC.collect could be kicked in anytime when we allocate new objects. We believe the setup is less ideal, as - [Unnecessary for most scenarios] GC.collect is mainly used to handle cyclic dependencies, but majority of vLLM objects are NOT in the cyclic dependencies and could be deallocated by reference counting directly. - [Perf regression due to process Interruption] GC.collect would stop the world (e.g. delay kernel launches) and ultimately severely affect GPU utils and token throughputs ## Manual GC trigger Proposal We should invoke GC.collect in a more controllable way to minimize the perf impact, and we believe the best place for GC.collect would be cuda stream sync (e.g. blocking wait for D2H sync). ### Non-async-scheduling We will have a cuda stream sync in each decode step for sampled token IDs (which could be a perfect place for GC.collect, i.e. running GC.collect when GPU is hot and CPU was doing nothing but simply waiting) ### Async-scheduling Although cuda stream sync had moved out to a dedicated thread, but cuda stream sync could still served as a great indicator of whether GPU is processing data, so it sho...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: Manual Controlled GC performance;stale ### Proposal to improve performance ## Issues By default, python GC.collect could be kicked in anytime when we allocate new objects. We believe the setup is less ide...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: dencies and could be deallocated by reference counting directly. - [Perf regression due to process Interruption] GC.collect would stop the world (e.g. delay kernel launches) and ultimately severely affect GPU utils and...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: y for most scenarios] GC.collect is mainly used to handle cyclic dependencies, but majority of vLLM objects are NOT in the cyclic dependencies and could be deallocated by reference counting directly. - [Perf regression...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e the perf impact, and we believe the best place for GC.collect would be cuda stream sync (e.g. blocking wait for D2H sync). ### Non-async-scheduling We will have a cuda stream sync in each decode step for sampled token...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: we believe the best place for GC.collect would be cuda stream sync (e.g. blocking wait for D2H sync). ### Non-async-scheduling We will have a cuda stream sync in each decode step for sampled token IDs (which could be a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
