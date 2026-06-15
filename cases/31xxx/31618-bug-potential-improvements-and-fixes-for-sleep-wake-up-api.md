# vllm-project/vllm#31618: [Bug]: Potential improvements and fixes for sleep/wake_up API

| 字段 | 值 |
| --- | --- |
| Issue | [#31618](https://github.com/vllm-project/vllm/issues/31618) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Potential improvements and fixes for sleep/wake_up API

### Issue 正文摘录

### Your current environment No relevant to dev env ### 🐛 Describe the bug ## Context Hi vLLM team! I’ve been building some features on top of the v1 `sleep` / `wake_up` functionality and noticed a few edge cases. I wanted to share my observations and propose a few small robustness improvements to see if they align with the project's goals. ### 1. `wake_up` aborts on invalid/awake tags (Fix Drafted) **Observation:** I noticed that `wake_up` currently aborts the *entire* operation if any requested tag is not in `sleeping_tags`. This creates issues in partial sleep states. For example, if tag "A" is already awake but "B" is sleeping, calling `wake_up(["A", "B"])` will fail, leaving "B" asleep unexpectedly. **Proposal:** It might be better to filter out invalid tags and make a "best effort" to wake up the valid ones. I’ve submitted a small PR to address this: #31613 ### 2. `sleep` behavior with in-flight requests **Observation:** `sleep` will disconnects the physical/virtual GPU memory mapping. If `sleep` is called while there are still unfinished requests processing in the engine, it causes errors/crashes. **Proposal:** It might be safer to explicitly check for in-flight requests an...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Potential improvements and fixes for sleep/wake_up API bug;stale ### Your current environment No relevant to dev env ### 🐛 Describe the bug ## Context Hi vLLM team! I’ve been building some features on top of the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: to dev env ### 🐛 Describe the bug ## Context Hi vLLM team! I’ve been building some features on top of the v1 `sleep` / `wake_up` functionality and noticed a few edge cases. I wanted to share my observations and propose...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d a few edge cases. I wanted to share my observations and propose a few small robustness improvements to see if they align with the project's goals. ### 1. `wake_up` aborts on invalid/awake tags (Fix Drafted) **Observat...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: requests **Observation:** `sleep` will disconnects the physical/virtual GPU memory mapping. If `sleep` is called while there are still unfinished requests processing in the engine, it causes errors/crashes. **Proposal:*...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: *Observation:** `sleep` will disconnects the physical/virtual GPU memory mapping. If `sleep` is called while there are still unfinished requests processing in the engine, it causes errors/crashes. **Proposal:** It might...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
