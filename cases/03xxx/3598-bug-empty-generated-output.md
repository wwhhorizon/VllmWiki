# vllm-project/vllm#3598: [Bug]: Empty generated output

| 字段 | 值 |
| --- | --- |
| Issue | [#3598](https://github.com/vllm-project/vllm/issues/3598) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Empty generated output

### Issue 正文摘录

### Your current environment I am testing completion and chat completion APIs, and both return empty output `''` as output from the model and on the service side, it print zeros for the number of generated tokens and kv cache. `Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% ` model is a 7b-mistral based model. ### 🐛 Describe the bug I am using the entrypoint from vllm project.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ug]: Empty generated output bug;stale ### Your current environment I am testing completion and chat completion APIs, and both return empty output `''` as output from the model and on the service side, it print zeros for...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: the service side, it print zeros for the number of generated tokens and kv cache. `Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: at completion APIs, and both return empty output `''` as output from the model and on the service side, it print zeros for the number of generated tokens and kv cache. `Avg prompt throughput: 0.0 tokens/s, Avg generatio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Empty generated output bug;stale ### Your current environment I am testing completion and chat completion APIs, and both return empty output `''` as output from the model and on the service side, it print zeros f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
