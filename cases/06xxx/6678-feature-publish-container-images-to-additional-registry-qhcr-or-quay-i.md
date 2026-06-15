# vllm-project/vllm#6678: [Feature]: Publish container images to additional registry (qhcr or quay.io)

| 字段 | 值 |
| --- | --- |
| Issue | [#6678](https://github.com/vllm-project/vllm/issues/6678) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Publish container images to additional registry (qhcr or quay.io)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently release artifacts in the form of OCI / container images are only published to DockerHub (https://hub.docker.com/r/vllm/vllm) I like to suggest publishing the images to another registry for redundancy. The [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) is an obvious choice, but also quay.io might be worth a look. In the end this is more or less a build once, retag and a push to another registry. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ature, motivation and pitch Currently release artifacts in the form of OCI / container images are only published to DockerHub (https://hub.docker.com/r/vllm/vllm) I like to suggest publishing the images to another regis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ublish container images to additional registry (qhcr or quay.io) feature request;stale ### 🚀 The feature, motivation and pitch Currently release artifacts in the form of OCI / container images are only published to Dock...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
