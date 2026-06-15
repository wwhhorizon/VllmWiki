# vllm-project/vllm#32889: [ROCm] MI355X CI parity is missing

| 字段 | 值 |
| --- | --- |
| Issue | [#32889](https://github.com/vllm-project/vllm/issues/32889) |
| 状态 | open |
| 标签 | feature request;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [ROCm] MI355X CI parity is missing

### Issue 正文摘录

### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd there is good amount of B200 CI tests enablement already but MI355 is extremely lack there is close to zero MI355 CI. and it is not tracked in the vllm project board either. https://github.com/orgs/vllm-project/projects/39 what is the plans around MI355 vLLM upstream enablement? Thanks in advance for ur time on this! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [ROCm] MI355X CI parity is missing feature request;rocm ### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd there is good amount of B200 CI tests enablement already but MI355 is extremely lack there is cl
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [ROCm] MI355X CI parity is missing feature request;rocm ### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd there is good amount of B200 CI tests enablement already but MI355 is extremely lack there is cl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [ROCm] MI355X CI parity is missing feature request;rocm ### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd there is good amount of B200 CI tests enablement already but MI355 is extremely lack there is cl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: n and pitch hi @powderluv @chunfangamd there is good amount of B200 CI tests enablement already but MI355 is extremely lack there is close to zero MI355 CI. and it is not tracked in the vllm project board either. https:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
