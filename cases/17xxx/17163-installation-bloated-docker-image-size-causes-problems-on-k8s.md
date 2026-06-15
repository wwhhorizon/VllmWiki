# vllm-project/vllm#17163: [Installation]: Bloated docker image size causes problems on k8s

| 字段 | 值 |
| --- | --- |
| Issue | [#17163](https://github.com/vllm-project/vllm/issues/17163) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Bloated docker image size causes problems on k8s

### Issue 正文摘录

### Your current environment k8s(naver cloud platform) ### How you are installing vllm via the production-stack helm chart As vLLM version got bumped up, the docker image size grew quite substantially, causing the ephemeral storage to run out in 50GB SSD nodes. I understand that NVIDIA plugins can make the docker images bloated but up to 25GB is kind of ridiculous. Is there an active effort to investigate and optimize the docker image?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Bloated docker image size causes problems on k8s installation;stale ### Your current environment k8s(naver cloud platform) ### How you are installing vllm via the production-stack helm chart As vLLM ve
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: allation]: Bloated docker image size causes problems on k8s installation;stale ### Your current environment k8s(naver cloud platform) ### How you are installing vllm via the production-stack helm chart As vLLM version g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
