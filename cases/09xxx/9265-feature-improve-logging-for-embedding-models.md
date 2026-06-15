# vllm-project/vllm#9265: [Feature]: Improve Logging For Embedding Models

| 字段 | 值 |
| --- | --- |
| Issue | [#9265](https://github.com/vllm-project/vllm/issues/9265) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Improve Logging For Embedding Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are working to make embedding models a first-class citizen in vllm. It would be great if we had logging metrics that are more native to embedding models! e.g. current logs look like this: ```bash INFO 10-10 20:53:17 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. ``` There is no KV cache and no generation tokens when running embedding models :cry: ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Improve Logging For Embedding Models good first issue;feature request;stale ### 🚀 The feature, motivation and pitch We are working to make embedding models a first-class citizen in vllm. It would be great if...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: look like this: ```bash INFO 10-10 20:53:17 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ivation and pitch We are working to make embedding models a first-class citizen in vllm. It would be great if we had logging metrics that are more native to embedding models! e.g. current logs look like this: ```bash IN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. ``` There is no KV cache and no generation tokens when running embedding models :cry: ### Alternat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
