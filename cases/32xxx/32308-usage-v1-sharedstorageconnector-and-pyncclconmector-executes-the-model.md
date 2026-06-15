# vllm-project/vllm#32308: [Usage]: v1 SharedStorageConnector and PyNcclConmector executes the model again for the input prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#32308](https://github.com/vllm-project/vllm/issues/32308) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: v1 SharedStorageConnector and PyNcclConmector executes the model again for the input prompt

### Issue 正文摘录

### Your current environment I have tried SharedStorage and PyNccl connector in v1 and they both execute the model for input prompt in decode phase. Has something changed in v1? In v0 model execution was skipped in decode phase. For four output token, model should be executed 4 times but in v1 it is executed 5 times. I also checked in multiple versions up till 13. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ted 4 times but in v1 it is executed 5 times. I also checked in multiple versions up till 13. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: and PyNcclConmector executes the model again for the input prompt usage;stale ### Your current environment I have tried SharedStorage and PyNccl connector in v1 and they both execute the model for input prompt in decode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: v1 SharedStorageConnector and PyNcclConmector executes the model again for the input prompt usage;stale ### Your current environment I have tried SharedStorage and PyNccl connector in v1 and they both execute t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
