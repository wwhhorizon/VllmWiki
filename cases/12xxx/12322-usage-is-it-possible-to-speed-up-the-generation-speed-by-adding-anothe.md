# vllm-project/vllm#12322: [Usage]: Is it possible to speed up the generation speed by adding another video card?

| 字段 | 值 |
| --- | --- |
| Issue | [#12322](https://github.com/vllm-project/vllm/issues/12322) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is it possible to speed up the generation speed by adding another video card?

### Issue 正文摘录

### Your current environment - Docker I have a fairly small reasoning model (deepseek r1 for qwen 14b/7b) that I want to use in production. To do this, I have to speed up the inference so that the thinking doesn’t take so long. I set pipeline-parallel-size=2 (I have two rtx3070 video cards). When running llm on 2 video cards in pipeline-parallel-size mode, there is an increase in max concurrency, but there is no increase in generation speed. Is there a way to use a second video card to speed up the generation speed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: card? usage;stale ### Your current environment - Docker I have a fairly small reasoning model (deepseek r1 for qwen 14b/7b) that I want to use in production. To do this, I have to speed up the inference so that the thin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e ### Your current environment - Docker I have a fairly small reasoning model (deepseek r1 for qwen 14b/7b) that I want to use in production. To do this, I have to speed up the inference so that the thinking doesn’t tak...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: by adding another video card? usage;stale ### Your current environment - Docker I have a fairly small reasoning model (deepseek r1 for qwen 14b/7b) that I want to use in production. To do this, I have to speed up the in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ble to speed up the generation speed by adding another video card? usage;stale ### Your current environment - Docker I have a fairly small reasoning model (deepseek r1 for qwen 14b/7b) that I want to use in production....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
