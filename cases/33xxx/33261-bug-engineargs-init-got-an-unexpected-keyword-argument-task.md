# vllm-project/vllm#33261: [Bug]: EngineArgs.__init__() got an unexpected keyword argument 'task'

| 字段 | 值 |
| --- | --- |
| Issue | [#33261](https://github.com/vllm-project/vllm/issues/33261) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: EngineArgs.__init__() got an unexpected keyword argument 'task'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug EngineArgs.__init__() got an unexpected keyword argument 'task' pip3 show vllm version is 0.14.1 run xinference auto install vllm how to resolve this bug ? EngineArgs.__init__() got an unexpected keyword argument 'task' change which version about vllm? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: gs.__init__() got an unexpected keyword argument 'task' pip3 show vllm version is 0.14.1 run xinference auto install vllm how to resolve this bug ? EngineArgs.__init__() got an unexpected keyword argument 'task' change...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ug]: EngineArgs.__init__() got an unexpected keyword argument 'task' bug;stale ### Your current environment ### 🐛 Describe the bug EngineArgs.__init__() got an unexpected keyword argument 'task' pip3 show vllm version i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
