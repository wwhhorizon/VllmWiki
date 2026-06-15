# vllm-project/vllm#3750: [Usage]: Is it possible to pin `LLM` to a specific CUDA device?

| 字段 | 值 |
| --- | --- |
| Issue | [#3750](https://github.com/vllm-project/vllm/issues/3750) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is it possible to pin `LLM` to a specific CUDA device?

### Issue 正文摘录

### Your current environment - ### How would you like to use vllm I'd like to use multiple vllm instances in the same python script, each on a different CUDA device. Is it possible to pin an `LLM` object to a specific device? I don't see any option to do this anywhere in `LLM` nor in `EngineArgs`. I understand it would be slightly tricky to do this with tensor parallelism over Ray, but if each LLM is using only a single GPU, it should be relatively easy to pass in a cuda `device` to be used by the model, I think? Curious if this is already possible somehow, or if the vllm team would be open to a PR on this!

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Is it possible to pin `LLM` to a specific CUDA device? usage;stale ### Your current environment - ### How would you like to use vllm I'd like to use multiple vllm instances in the same python script, each on a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: Is it possible to pin `LLM` to a specific CUDA device? usage;stale ### Your current environment - ### How would you like to use vllm I'd like to use multiple vllm instances in the same python script, each on a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t should be relatively easy to pass in a cuda `device` to be used by the model, I think? Curious if this is already possible somehow, or if the vllm team would be open to a PR on this!
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Is it possible to pin `LLM` to a specific CUDA device? usage;stale ### Your current environment - ### How would you like to use vllm I'd like to use multiple vllm instances in the same python script, each on a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
