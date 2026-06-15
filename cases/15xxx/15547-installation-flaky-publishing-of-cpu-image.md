# vllm-project/vllm#15547: [Installation]: flaky publishing of cpu image

| 字段 | 值 |
| --- | --- |
| Issue | [#15547](https://github.com/vllm-project/vllm/issues/15547) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: flaky publishing of cpu image

### Issue 正文摘录

### Your current environment when looking in https://gallery.ecr.aws/q9t5s3a7/vllm-cpu-release-repo to check for vllm-cpu images, I noticed some of the releases cannot be found there. for example, release v0.7.3 was not published to this registry, as well as the latest version v0.8.2. it seems there is some flakiness, in most of the releases the cpu image gets created but not always. ### How you are installing vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: flaky publishing of cpu image installation;stale ### Your current environment when looking in https://gallery.ecr.aws/q9t5s3a7/vllm-cpu-release-repo to check for vllm-cpu images, I noticed some of the rel
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: flaky publishing of cpu image installation;stale ### Your current environment when looking in https://gallery.ecr.aws/q9t5s3a7/vllm-cpu-release-repo to check for vllm-cpu images, I noticed some of the re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ple, release v0.7.3 was not published to this registry, as well as the latest version v0.8.2. it seems there is some flakiness, in most of the releases the cpu image gets created but not always. ### How you are installi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
