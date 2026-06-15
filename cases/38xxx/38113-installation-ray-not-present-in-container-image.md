# vllm-project/vllm#38113: [Installation]: Ray not present in Container Image

| 字段 | 值 |
| --- | --- |
| Issue | [#38113](https://github.com/vllm-project/vllm/issues/38113) |
| 状态 | open |
| 标签 | installation |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Ray not present in Container Image

### Issue 正文摘录

### Your current environment Docker image `vllm/vllm-openai:latest` ### How you are installing vllm The latest release removed Ray as a dependency (#33445). While this is beneficial to python installations, it breaks Kubernetes deployments that use use the upstream image for Ray for multi-node inference. Can this be added back into the Dockerfile, or was it intentionally removed from there as well? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Ray not present in Container Image installation ### Your current environment Docker image `vllm/vllm-openai:latest` ### How you are installing vllm The latest release removed Ray as a dependency (#33445
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ll? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tallation ### Your current environment Docker image `vllm/vllm-openai:latest` ### How you are installing vllm The latest release removed Ray as a dependency (#33445). While this is beneficial to python installations, it...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
