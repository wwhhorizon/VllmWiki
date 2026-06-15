# vllm-project/vllm#26433: [RFC]: Batching speculation

| 字段 | 值 |
| --- | --- |
| Issue | [#26433](https://github.com/vllm-project/vllm/issues/26433) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Batching speculation

### Issue 正文摘录

### Motivation. To reduce/eliminate the CPU overhead from vLLM’s scheduler and input preparation, we can 1. at the end of one decoding step, **assume** the scheduler decision for next step will have the same batch 2. so it can immediately start executing the next step, but **only the first `N` layers** 3. `N` can be easily tuned such that (a) scheduling & input preparation and (b) execution of N layers can finish at roughly the same time 4. at that point, we check if the assumption is true/false - if the batch is indeed the same, resume from `N+1`-th layer - so we save the execution time of first `N` layers - otherwise, simply re-run from the 1st layer - note there is virtually no mis-speculation penalty here because there is no clean-up/roll-back needed When I was prototyping this, I was not aware of [#6913 Asynchronous Output Processor](https://github.com/vllm-project/vllm/issues/6913), which start with the same idea of speculating that the batch for next step will be the same. *Now I do feel the [#6913](#6913) is probably cleaner, but I want to describe this approach here in case it sparks new idea or this becomes more relevant with future changes.* To complete the comparison w...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: hly the same time 4. at that point, we check if the assumption is true/false - if the batch is indeed the same, resume from `N+1`-th layer - so we save the execution time of first `N` layers - otherwise, simply re-run f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Batching speculation RFC;stale ### Motivation. To reduce/eliminate the CPU overhead from vLLM’s scheduler and input preparation, we can 1. at the end of one decoding step, **assume** the scheduler decision for ne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: am On Qwen3-8B, ISL/OSL=1024, I'm seeing ~13% improvement in token/s on Blackwell. And the trace looks like ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before su...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing_spec` which points to the slot for the +2 speculative execution - in model implementation, add `forward_spec` to run the first `N` layers and `forward_resume` to resume from the `N+1`-th layer. - in model-runner, on...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , we can 1. at the end of one decoding step, **assume** the scheduler decision for next step will have the same batch 2. so it can immediately start executing the next step, but **only the first `N` layers** 3. `N` can...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
