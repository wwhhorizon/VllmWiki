# vllm-project/vllm#36748: [Bug]: In DP mode, waiting request stack in a few DP ranks.

| 字段 | 值 |
| --- | --- |
| Issue | [#36748](https://github.com/vllm-project/vllm/issues/36748) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: In DP mode, waiting request stack in a few DP ranks.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using vLLM 0.14.0 with data parallelism on 8×B200 GPUs and started the server with: ``` vllm serve --model qwen3-vl-8b-thinking --port 8000 --tensor-parallel-size 1 --data-parallel-size 8 --max-num-seqs 64 ``` On the client side, I use a thread pool of size 512 to send requests concurrently. During serving, I noticed that a large number of waiting requests are concentrated on only a few DP ranks, rather than being evenly distributed across all ranks. For example: ``` (APIServer pid=387731) INFO 03-11 06:16:52 [loggers.py:257] Engine 000: Avg prompt throughput: 16.5 tokens/s, Avg generation throughput: 1157.2 tokens/s, Running: 51 reqs, Waiting: 117 reqs, GPU KV cache usage: 100.0%, Prefix cache hit rate: 70.0%, MM cache hit rate: 0.0% (APIServer pid=387731) INFO 03-11 06:16:52 [loggers.py:257] Engine 001: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 809.3 tokens/s, Running: 31 reqs, Waiting: 108 reqs, GPU KV cache usage: 98.6%, Prefix cache hit rate: 66.0%, MM cache hit rate: 0.0% (APIServer pid=387731) INFO 03-11 06:16:52 [loggers.py:257] Engine 002: Avg prompt throughput: 0.0 tokens/s, Avg generation thr...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nt ### 🐛 Describe the bug I am using vLLM 0.14.0 with data parallelism on 8×B200 GPUs and started the server with: ``` vllm serve --model qwen3-vl-8b-thinking --port 8000 --tensor-parallel-size 1 --data-parallel-size 8...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: on throughput: 1157.2 tokens/s, Running: 51 reqs, Waiting: 117 reqs, GPU KV cache usage: 100.0%, Prefix cache hit rate: 70.0%, MM cache hit rate: 0.0% (APIServer pid=387731) INFO 03-11 06:16:52 [loggers.py:257] Engine 0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: arallelism on 8×B200 GPUs and started the server with: ``` vllm serve --model qwen3-vl-8b-thinking --port 8000 --tensor-parallel-size 1 --data-parallel-size 8 --max-num-seqs 64 ``` On the client side, I use a thread poo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: In DP mode, waiting request stack in a few DP ranks. bug ### Your current environment ### 🐛 Describe the bug I am using vLLM 0.14.0 with data parallelism on 8×B200 GPUs and started the server with: ``` vllm serve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: pid=387731) INFO 03-11 06:16:52 [loggers.py:257] Engine 000: Avg prompt throughput: 16.5 tokens/s, Avg generation throughput: 1157.2 tokens/s, Running: 51 reqs, Waiting: 117 reqs, GPU KV cache usage: 100.0%, Prefix cach...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
