# vllm-project/vllm#20687: [RFC]: better differentiate infos, warnings and errors from exceptions

| 字段 | 值 |
| --- | --- |
| Issue | [#20687](https://github.com/vllm-project/vllm/issues/20687) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: better differentiate infos, warnings and errors from exceptions

### Issue 正文摘录

### Motivation. First things first: this is my first vLLM RFC, bear with me 🤗 When troubleshooting vLLM, I often face logs that look like a catastrophic failure but should be warnings or informational messages. Here is an example from this morning: `ValueError: After the optional system message, conversation roles must alternate user/assistant/user/assistant/...` + 50 lines of backtrace. This make log output much less readable and thus troubleshooting more difficult. ### Proposed Change. As a starting point, I suggest to provide simple guidelines about error throwing and handling, inspired of HTTP status codes: - information message: the user provided bad input and vLLM reacted appropriately: code handled the situation and send back a detailed message to the user - warning message: the user provided good input, but vLLM failed to process it temporarily - error message + stacktrace: the user provided good input, but vLLM failed to process it permanently Enforcing clear error definitions will help developers understand what to use in which case. I have no clue how to implement this proposition within vLLM, I suppose this is a considerable amount of work to go hunting for exceptions...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: to do so. I understand there already is a differentiated logging mechanism (`logger. `) which is the right starting point. This RFC is more about generating more "fine grained" exceptions so they can be differentiated p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ser provided good input, but vLLM failed to process it permanently Enforcing clear error definitions will help developers understand what to use in which case. I have no clue how to implement this proposition within vLL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e logs that look like a catastrophic failure but should be warnings or informational messages. Here is an example from this morning: `ValueError: After the optional system message, conversation roles must alternate user...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: FC]: better differentiate infos, warnings and errors from exceptions RFC;stale ### Motivation. First things first: this is my first vLLM RFC, bear with me 🤗 When troubleshooting vLLM, I often face logs that look like a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
