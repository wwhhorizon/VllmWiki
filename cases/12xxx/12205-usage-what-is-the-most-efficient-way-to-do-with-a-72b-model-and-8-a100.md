# vllm-project/vllm#12205: [Usage]:  what is the most efficient way to do with a 72b model and 8 * A100 ?

| 字段 | 值 |
| --- | --- |
| Issue | [#12205](https://github.com/vllm-project/vllm/issues/12205) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  what is the most efficient way to do with a 72b model and 8 * A100 ?

### Issue 正文摘录

### Your current environment None ### How would you like to use vllm Hi，say my baseline ` 1 instance and TP=4` , throughput is `x ` Suppose I have 8*A100 gpu, and I want to deploy a 72b model. I have the following two ways: | method | instance | TP | throughput | | :----: | :---: | :----: | :-----: | | **baseline** | 1 | 4 | **x** | | A | 2 | 4 | 2x (apparently) | | B | 1 | 8 | _1.5x_ | I am a little confused, option B give bad throughput lesser than **2x**, is it normal ? or How can I get throughput greater than 2*x with just 8*A100 gpu? (or I can't?) thanks for helping! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: what is the most efficient way to do with a 72b model and 8 * A100 ? usage;stale ### Your current environment None ### How would you like to use vllm Hi，say my baseline ` 1 instance and TP=4` , throughput is `x...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: would you like to use vllm Hi，say my baseline ` 1 instance and TP=4` , throughput is `x ` Suppose I have 8*A100 gpu, and I want to deploy a 72b model. I have the following two ways: | method | instance | TP | throughput...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: what is the most efficient way to do with a 72b model and 8 * A100 ? usage;stale ### Your current environment None ### How would you like to use vllm Hi，say my baseline ` 1 instance and TP=4` , throughput is `x...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: what is the most efficient way to do with a 72b model and 8 * A100 ? usage;stale ### Your current environment None ### How would you like to use vllm Hi，say my baseline ` 1 instance and TP=4` , throughput is `x...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: at is the most efficient way to do with a 72b model and 8 * A100 ? usage;stale ### Your current environment None ### How would you like to use vllm Hi，say my baseline ` 1 instance and TP=4` , throughput is `x ` Suppose...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
