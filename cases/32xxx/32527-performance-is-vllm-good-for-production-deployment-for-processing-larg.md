# vllm-project/vllm#32527: [Performance]: Is VLLM good for production deployment for processing large data in batches?

| 字段 | 值 |
| --- | --- |
| Issue | [#32527](https://github.com/vllm-project/vllm/issues/32527) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Is VLLM good for production deployment for processing large data in batches?

### Issue 正文摘录

### Question: Performance Hello! We're considering using VLLM for production deployment for some of our customers on-premise with local LLMs. We use batch processing to help LLMs access the full data to have a row-level intelligence. We would like to know if Batch Processing open source LLMs on large-scale data could use VLLM as the default backend for this. Our requirements are: - Customizable on-prem deployments - Inference in large scale data while also using distributed computing and batch processing to send parallel batches of data to be processed. Here's the project: https://github.com/vitalops/datatune

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ssing open source LLMs on large-scale data could use VLLM as the default backend for this. Our requirements are: - Customizable on-prem deployments - Inference in large scale data while also using distributed computing...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ce. We would like to know if Batch Processing open source LLMs on large-scale data could use VLLM as the default backend for this. Our requirements are: - Customizable on-prem deployments - Inference in large scale data...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: production deployment for processing large data in batches? performance;stale ### Question: Performance Hello! We're considering using VLLM for production deployment for some of our customers on-premise with local LLMs....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
