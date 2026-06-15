# vllm-project/vllm#35118: [Feature]: Support ubuntu 24.04 runtime container

| 字段 | 值 |
| --- | --- |
| Issue | [#35118](https://github.com/vllm-project/vllm/issues/35118) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support ubuntu 24.04 runtime container

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM is pinned to a older, stable OS (22.04) at present, while 24.04 is the latest LTS ubuntu. The longer the OS gap persists, the more the project drifts from its own ecosystem. Every downstream that needs 24.04 is independently forking the Dockerfile. This also prevents vllm from getting better perf and latest security patches. - This RFE is to support both OSes - 22.04 and 24.04. - The default behaviour stays the same, folks will download ubuntu 22.04 when no OS tag is specified. - New latest LTS OS i.e. ubuntu 24.04 will be an explicit opt-in with a tagged version. There is already a docker parametrization available to make our lives easier. we may want to add CI and testing to cover this new OS support. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: cosystem. Every downstream that needs 24.04 is independently forking the Dockerfile. This also prevents vllm from getting better perf and latest security patches. - This RFE is to support both OSes - 22.04 and 24.04. -...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: latest LTS ubuntu. The longer the OS gap persists, the more the project drifts from its own ecosystem. Every downstream that needs 24.04 is independently forking the Dockerfile. This also prevents vllm from getting bett...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support ubuntu 24.04 runtime container feature request ### 🚀 The feature, motivation and pitch vLLM is pinned to a older, stable OS (22.04) at present, while 24.04 is the latest LTS ubuntu. The longer the OS...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: is pinned to a older, stable OS (22.04) at present, while 24.04 is the latest LTS ubuntu. The longer the OS gap persists, the more the project drifts from its own ecosystem. Every downstream that needs 24.04 is independ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
