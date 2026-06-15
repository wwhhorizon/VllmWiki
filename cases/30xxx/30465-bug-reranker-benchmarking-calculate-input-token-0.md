# vllm-project/vllm#30465: [Bug]: reranker benchmarking calculate input_token=0

| 字段 | 值 |
| --- | --- |
| Issue | [#30465](https://github.com/vllm-project/vllm/issues/30465) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: reranker benchmarking calculate input_token=0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug using vllm 0.12.0 ``` ============ Serving Benchmark Result ============ Successful requests: 360 Failed requests: 0 Maximum request concurrency: 64 Request rate configured (RPS): 10.00 Benchmark duration (s): 36.11 Total input tokens: 0 Request throughput (req/s): 9.97 Total Token throughput (tok/s): 0.00 ``` running bash ``` python -m vllm.entrypoints.cli.main bench serve \ --model /home/bge-rerank \ --host 0.0.0.0 \ --port 1000 \ --endpoint /v1/rerank \ --backend vllm-rerank \ --dataset-name random-rerank \ --random-input-len 1024 \ --random-batch-size 5 \ --num-prompts 3000 \ --metric-percentiles=50,75,90,99 \ --max-concurrency 32 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: reranker benchmarking calculate input_token=0 bug ### Your current environment ### 🐛 Describe the bug using vllm 0.12.0 ``` ============ Serving Benchmark Result ============ Successful requests: 360
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Maximum request concurrency: 64 Request rate configured (RPS): 10.00 Benchmark duration (s): 36.11 Total input tokens: 0 Request throughput (req/s): 9.97 Total Token throughput (t
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: me/bge-rerank \ --host 0.0.0.0 \ --port 1000 \ --endpoint /v1/rerank \ --backend vllm-rerank \ --dataset-name random-rerank \ --random-input-len 1024 \ --random-batch-size 5 \ --num-prompts 3000 \ --metric-percentiles=5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: .12.0 ``` ============ Serving Benchmark Result ============ Successful requests: 360 Failed requests: 0 Maximum request concurrency: 64 Request rate configured (RPS): 10.00 Benchmark duration (s):

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
