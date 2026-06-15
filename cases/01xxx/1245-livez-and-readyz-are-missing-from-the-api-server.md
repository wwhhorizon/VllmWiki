# vllm-project/vllm#1245: livez and readyz are missing from the api_server

| 字段 | 值 |
| --- | --- |
| Issue | [#1245](https://github.com/vllm-project/vllm/issues/1245) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> livez and readyz are missing from the api_server

### Issue 正文摘录

Hello, I am trying to deploy an LLM model using vLLM on Kubernetes. However, for K8, the `readinessProbe` and `livenessProbe` are needed to indicate [the health of the api-server](https://kubernetes.io/docs/reference/using-api/health-checks/) and these endpoints are missing from the [api_server.py](https://github.com/vllm-project/vllm/blob/ebe4d1db3a42096cebcc2b2d289143bc0ef02d3d/vllm/entrypoints/api_server.py) For that reason I have raised a simple PR to include the needed endpoints: https://github.com/vllm-project/vllm/pull/1244 Regards, Petros Baltzis

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: dyz are missing from the api_server Hello, I am trying to deploy an LLM model using vLLM on Kubernetes. However, for K8, the `readinessProbe` and `livenessProbe` are needed to indicate [the health of the api-server](htt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
