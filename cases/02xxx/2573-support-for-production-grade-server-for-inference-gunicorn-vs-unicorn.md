# vllm-project/vllm#2573: Support for production grade server for Inference [Gunicorn vs Unicorn]?

| 字段 | 值 |
| --- | --- |
| Issue | [#2573](https://github.com/vllm-project/vllm/issues/2573) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support for production grade server for Inference [Gunicorn vs Unicorn]?

### Issue 正文摘录

hey all, context : while doing model NFRs with mixtral 8x7B OOB model, the vLLM stack is using unicorn by default in api_server.py, on increasing QPS using locust, I am guessing `unicorn` is becoming a bottleneck and is not able to scale. Ideas / Views on adding gunicorn support, how do you deploy model using vLLM stack in prod for serving ? at 2QPS running on 2 A100 GPUs error rate : 3% error status code : 0 meaning connectivity issues gpu utilisation : 90% tokens per second : ~2100 at 4.1 QPS running on 4 A100 GPUs error rate : 13% error status code : 0 meaning connectivity issues gpu utilisation : 75% tokens per second : ~4100 deductions : 1. as I increase the number of concurrent users to increase model throughput, the connectivity issues start emerging a lot. 2. in number terms, on 100 - 200 users, error rate goes to ~25-35%.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ust, I am guessing `unicorn` is becoming a bottleneck and is not able to scale. Ideas / Views on adding gunicorn support, how do you deploy model using vLLM stack in prod for serving ? at 2QPS running on 2 A100 GPUs err...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: eploy model using vLLM stack in prod for serving ? at 2QPS running on 2 A100 GPUs error rate : 3% error status code : 0 meaning connectivity issues gpu utilisation : 90% tokens per second : ~2100 at 4.1 QPS running on 4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ver for Inference [Gunicorn vs Unicorn]? hey all, context : while doing model NFRs with mixtral 8x7B OOB model, the vLLM stack is using unicorn by default in api_server.py, on increasing QPS using locust, I am guessing...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ons : 1. as I increase the number of concurrent users to increase model throughput, the connectivity issues start emerging a lot. 2. in number terms, on 100 - 200 users, error rate goes to ~25-35%.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
