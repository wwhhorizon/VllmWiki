# vllm-project/vllm#8302: [Feature]: Add ray cluster start logic to vllm container for multi host inference with leaderworkerset

| 字段 | 值 |
| --- | --- |
| Issue | [#8302](https://github.com/vllm-project/vllm/issues/8302) |
| 状态 | closed |
| 标签 | feature request;ray;unstale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add ray cluster start logic to vllm container for multi host inference with leaderworkerset

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Deploying vllm for multihost with leaderworkerset requires initializing a ray cluster. [LWS example baked into custom image](https://github.com/kubernetes-sigs/lws/blob/main/docs/examples/vllm/build/ray_init.sh) [405b example with baked in script](https://cloud.google.com/kubernetes-engine/docs/tutorials/serve-multihost-gpu#deploy-vllm) [Example using in a config map mounted entrypoint](https://github.com/kubernetes-sigs/wg-serving/pull/11/files#diff-d752f4a330f1fa68b8947a5d8ca5c9012cad198b39d127ff33ff781f8684fc7b) Request is to add new container argument `--init-ray-cluster` and contianer entrypoint script that adds the ray cluster init logic similar to https://github.com/kubernetes-sigs/wg-serving/pull/11/files#diff-d752f4a330f1fa68b8947a5d8ca5c9012cad198b39d127ff33ff781f8684fc7b when specified. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: age](https://github.com/kubernetes-sigs/lws/blob/main/docs/examples/vllm/build/ray_init.sh) [405b example with baked in script](https://cloud.google.com/kubernetes-engine/docs/tutorials/serve-multihost-gpu#deploy-vllm)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: to vllm container for multi host inference with leaderworkerset feature request;ray;unstale ### 🚀 The feature, motivation and pitch Deploying vllm for multihost with leaderworkerset requires initializing a ray cluster....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: gine/docs/tutorials/serve-multihost-gpu#deploy-vllm) [Example using in a config map mounted entrypoint](https://github.com/kubernetes-sigs/wg-serving/pull/11/files#diff-d752f4a330f1fa68b8947a5d8ca5c9012cad198b39d127ff33...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
