# vllm-project/vllm#20576: [Bug]: Newer rc tags are not being pushed to docker.io

| 字段 | 值 |
| --- | --- |
| Issue | [#20576](https://github.com/vllm-project/vllm/issues/20576) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Newer rc tags are not being pushed to docker.io

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug vLLM docker.io image repository is missing latest rc tags (e.g. v0.9.2rc2) https://hub.docker.com/r/vllm/vllm-openai/tags Being unavailable to build from source under an enterprise/corporate restricted environment, having access to rc tags released on docker.io/ghcr registry makes debugging/testing new images much easier.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Newer rc tags are not being pushed to docker.io bug ### Your current environment N/A ### 🐛 Describe the bug vLLM docker.io image repository is missing latest rc tags (e.g. v0.9.2rc2) https://hub.docker.com/r/vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: /A ### 🐛 Describe the bug vLLM docker.io image repository is missing latest rc tags (e.g. v0.9.2rc2) https://hub.docker.com/r/vllm/vllm-openai/tags Being unavailable to build from source under an enterprise/corporate re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
