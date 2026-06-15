# vllm-project/vllm#14386: [Usage]: Clean up Engine Args & Documentation

| 字段 | 值 |
| --- | --- |
| Issue | [#14386](https://github.com/vllm-project/vllm/issues/14386) |
| 状态 | closed |
| 标签 | good first issue;usage |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Clean up Engine Args & Documentation

### Issue 正文摘录

### Your current environment Currently vLLM has a lot of engine arguments listed here https://docs.vllm.ai/en/latest/serving/engine_args.html. Over time as we add more and more features to vLLM, this list will be less maintainable and user friendly. ### How would you like to use vllm As a first step to clean up these args, they should be made **hierarchical** (for example, `--compilation-config`). The documentation should also be updated so that engine arg documentations are **arranged in sections instead of in a flatten list**. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: vllm As a first step to clean up these args, they should be made **hierarchical** (for example, `--compilation-config`). The documentation should also be updated so that engine arg documentations are **arranged in secti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: args, they should be made **hierarchical** (for example, `--compilation-config`). The documentation should also be updated so that engine arg documentations are **arranged in sections instead of in a flatten list**. ###...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: vLLM has a lot of engine arguments listed here https://docs.vllm.ai/en/latest/serving/engine_args.html. Over time as we add more and more features to vLLM, this list will be less maintainable and user friendly. ### How...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
