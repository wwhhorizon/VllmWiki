# vllm-project/vllm#28038: [Bug]:During the vllm 0.10.1 v1 benchmark test, only about 100 out of 1000 requests could be processed, and then it would get stuck.

| 字段 | 值 |
| --- | --- |
| Issue | [#28038](https://github.com/vllm-project/vllm/issues/28038) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:During the vllm 0.10.1 v1 benchmark test, only about 100 out of 1000 requests could be processed, and then it would get stuck.

### Issue 正文摘录

### Your current environment torch 2.7.1 vllm 0.10.1 ### 🐛 Describe the bug The vllm version is 0.10.1. The v0 benchmark can be successfully executed, but the v1 request will get stuck. When the client gets stuck, it will time out. The benchmark log is provided below. 3 instance & tp1 There is a situation where the usage of one graphics card can be extremely high, reaching 99%. When the usage of the graphics card reaches 99%, the request will get stuck. The usage of the V0 version graphics card is normal. benchmark reports client timeout error scheduler reports http: proxy error: context canceled ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ug]:During the vllm 0.10.1 v1 benchmark test, only about 100 out of 1000 requests could be processed, and then it would get stuck. bug;stale ### Your current environment torch 2.7.1 vllm 0.10.1 ### 🐛 Describe the bug Th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]:During the vllm 0.10.1 v1 benchmark test, only about 100 out of 1000 requests could be processed, and then it would get stuck. bug;stale ### Your current environment torch 2.7.1 vllm 0.10.1 ### 🐛 Describe the bug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t environment torch 2.7.1 vllm 0.10.1 ### 🐛 Describe the bug The vllm version is 0.10.1. The v0 benchmark can be successfully executed, but the v1 request will get stuck. When the client gets stuck, it will time out. Th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: led ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
