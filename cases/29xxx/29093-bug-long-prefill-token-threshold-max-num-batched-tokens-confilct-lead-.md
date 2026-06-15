# vllm-project/vllm#29093: [Bug]: --long-prefill-token-threshold & --max-num-batched-tokens Confilct：lead to OOM!

| 字段 | 值 |
| --- | --- |
| Issue | [#29093](https://github.com/vllm-project/vllm/issues/29093) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --long-prefill-token-threshold & --max-num-batched-tokens Confilct：lead to OOM!

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug python3 benchmark_serving.py --backend deepseek --model dpsk \ --tokenizer /workspace/app/deepseek-r1-tokenizer/ \ --base-url http://127.0.0.1:8000 --endpoint /v1/chat/completions \ --metric-percentiles 50,90,95,99 --adt-output-len 1 \ --adt-max-input-len 75000 --max-concurrency 32 \ --num-prompts 2000 --burstiness 999999 \ --request-rate 30 --dataset-name adt --dataset-path ./v12.ndjson ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: --long-prefill-token-threshold & --max-num-batched-tokens Confilct：lead to OOM! bug;stale ### Your current environment ### 🐛 Describe the bug python3 benchmark_serving.py --backend deepseek --model dpsk \ --toke
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: g;stale ### Your current environment ### 🐛 Describe the bug python3 benchmark_serving.py --backend deepseek --model dpsk \ --tokenizer /workspace/app/deepseek-r1-tokenizer/ \ --base-url http://127.0.0.1:8000 --endpoint...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: environment ### 🐛 Describe the bug python3 benchmark_serving.py --backend deepseek --model dpsk \ --tokenizer /workspace/app/deepseek-r1-tokenizer/ \ --base-url http://127.0.0.1:8000 --endpoint /v1/chat/completions \ --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: son ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: long-prefill-token-threshold & --max-num-batched-tokens Confilct：lead to OOM! bug;stale ### Your current environment ### 🐛 Describe the bug python3 benchmark_serving.py --backend deepseek --model dpsk \ --tokenizer /wor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
