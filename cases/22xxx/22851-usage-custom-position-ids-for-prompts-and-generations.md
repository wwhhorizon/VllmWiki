# vllm-project/vllm#22851: [Usage]: Custom position ids for prompts and generations

| 字段 | 值 |
| --- | --- |
| Issue | [#22851](https://github.com/vllm-project/vllm/issues/22851) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Custom position ids for prompts and generations

### Issue 正文摘录

### Your current environment Is there a way to pass custom position ids for the prompts? I am trying to do the following: for the input prompts, I want to have a specific tensor to be the position ids. The generations will have regular position postion ids such that it is incremented by 1 for each token starting with the max position id in the prompt's position id tensor. Thanks! ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: m trying to do the following: for the input prompts, I want to have a specific tensor to be the position ids. The generations will have regular position postion ids such that it is incremented by 1 for each token starti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Custom position ids for prompts and generations usage;stale ### Your current environment Is there a way to pass custom position ids for the prompts? I am trying to do the following: for the input prompts, I wan...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
