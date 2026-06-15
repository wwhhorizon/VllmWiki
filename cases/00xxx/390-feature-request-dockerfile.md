# vllm-project/vllm#390: feature request: Dockerfile

| 字段 | 值 |
| --- | --- |
| Issue | [#390](https://github.com/vllm-project/vllm/issues/390) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> feature request: Dockerfile

### Issue 正文摘录

I think it would be better if we could provide dockerfile in vLLM, for distributed serving, and single-gpu serving. Then we could use it on Kubernetes or other container-based environments.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: feature request: Dockerfile I think it would be better if we could provide dockerfile in vLLM, for distributed serving, and single-gpu serving. Then we could use it on Kubernetes or other container-based environments.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: feature request: Dockerfile I think it would be better if we could provide dockerfile in vLLM, for distributed serving, and single-gpu serving. Then we could use it on Kubernetes or other container-based environments.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
