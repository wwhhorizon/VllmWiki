# vllm-project/vllm#4185: [Feature]: Request for Status Monitoring API in vLLM openai Server

| 字段 | 值 |
| --- | --- |
| Issue | [#4185](https://github.com/vllm-project/vllm/issues/4185) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Request for Status Monitoring API in vLLM openai Server

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I propose the addition of a status monitoring API to the vLLM openai server to provide real-time performance metrics. This feature would enhance visibility into the system's current state and facilitate dynamic adjustments of operational parameters based on live data. The status API could be integrated into the existing python -m vllm.entrypoints.openai.api_server command, offering a /status endpoint that returns the current operational metrics in JSON format. This would make it easy to integrate into existing monitoring systems and dashboards. Here's an example of a JSON response: ``` { "status": "success", "timestamp": "2024-04-19T17:51:39Z", "metrics": { "average_prompt_throughput": { "value": 48.3 }, "average_generation_throughput": { "value": 56.9 }, "requests": { "running": 3, "swapped": 0, "pending": 0 }, "gpu_kv_cache_usage": { "value": 40.1 }, "cpu_kv_cache_usage": { "value": 0.0 } } } ``` Adding a status monitoring API to vLLM would significantly contribute to its usability and efficiency. It would provide users like myself with the necessary tools to optimize our deployments effectively. I am eager to discuss this further and woul...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s feature would enhance visibility into the system's current state and facilitate dynamic adjustments of operational parameters based on live data. The status API could be integrated into the existing python -m vllm.ent...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: a /status endpoint that returns the current operational metrics in JSON format. This would make it easy to integrate into existing monitoring systems and dashboards. Here's an example of a JSON response: ``` { "status":...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Request for Status Monitoring API in vLLM openai Server feature request ### 🚀 The feature, motivation and pitch I propose the addition of a status monitoring API to the vLLM openai server to provide real-time...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: "timestamp": "2024-04-19T17:51:39Z", "metrics": { "average_prompt_throughput": { "value": 48.3 }, "average_generation_throughput": { "value": 56.9 }, "requests": { "running": 3, "swapped": 0, "pending": 0 }, "gpu_kv_cac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
