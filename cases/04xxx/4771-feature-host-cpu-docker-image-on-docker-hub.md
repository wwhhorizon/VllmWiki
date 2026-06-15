# vllm-project/vllm#4771: [Feature]: Host CPU Docker image on Docker Hub

| 字段 | 值 |
| --- | --- |
| Issue | [#4771](https://github.com/vllm-project/vllm/issues/4771) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Host CPU Docker image on Docker Hub

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently vllm has pre-built [docker images for `vllm/vllm-openai`](https://hub.docker.com/r/vllm/vllm-openai). This image requires a GPU to run. Now that CPU support is being added, it would be great if CPU images could be added too. Allowing users to pull CPU images could greatly simplify the process for users and relaxing the GPU requirement would allow more users to benefit. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Host CPU Docker image on Docker Hub feature request ### 🚀 The feature, motivation and pitch Currently vllm has pre-built [docker images for `vllm/vllm-openai`](https://hub.docker.com/r/vllm/vllm-openai). This...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Host CPU Docker image on Docker Hub feature request ### 🚀 The feature, motivation and pitch Currently vllm has pre-built [docker images for `vllm/vllm-openai`](https://hub.docker.com/r/vllm/vllm-openai). This...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
