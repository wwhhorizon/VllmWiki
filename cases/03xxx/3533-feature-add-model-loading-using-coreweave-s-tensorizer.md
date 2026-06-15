# vllm-project/vllm#3533: [Feature]: Add model loading using CoreWeave's `tensorizer`

| 字段 | 值 |
| --- | --- |
| Issue | [#3533](https://github.com/vllm-project/vllm/issues/3533) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add model loading using CoreWeave's `tensorizer`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch An inference service that deploys models as serverless functions is critically dependent on container startup times to ensure it is responsive to changing traffic patterns. This is difficult to manage when model tensors stored in a container image bloat its size by tens of gigabytes. vLLM can now leverage `tensorizer` for its users [in this PR](https://github.com/vllm-project/vllm/pull/3476). With [CoreWeave's `tensorizer`](https://github.com/coreweave/tensorizer), model tensors can be loaded off HTTP/HTTPS, Redis, or S3 endpoints. By not embedding the model in the container image, users can reduce the container image size and the time it takes to load the model. This allows for fast, and therefore responsive, autoscaling. `tensorizer` serializes and can additionally encrypt model tensors to be loaded and/or decrypted extremely fast during container startup. Decoupling the model from the container image also additionally allows users to be able to update models without having to rebuild the container images, saving time deploying new versions without waiting for container image builds or for container image cache to be populated. ### Alterna...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: dditionally allows users to be able to update models without having to rebuild the container images, saving time deploying new versions without waiting for container image builds or for container image cache to be popul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add model loading using CoreWeave's `tensorizer` feature request ### 🚀 The feature, motivation and pitch An inference service that deploys models as serverless functions is critically dependent on container s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Add model loading using CoreWeave's `tensorizer` feature request ### 🚀 The feature, motivation and pitch An inference service that deploys models as serverless functions is critically dependent on container s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
