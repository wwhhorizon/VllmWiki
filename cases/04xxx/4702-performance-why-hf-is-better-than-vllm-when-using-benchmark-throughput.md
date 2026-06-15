# vllm-project/vllm#4702: [Performance]: why hf is better than vllm when using benchmark throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#4702](https://github.com/vllm-project/vllm/issues/4702) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: why hf is better than vllm when using benchmark throughput

### Issue 正文摘录

When I run benchmark on H800, the results are confusing. Why hf is better than vllm? Is anything wrong when I run the script? ``` python benchmark_throughput.py --input-len 128 --model /home/jiekong/.cache/modelscope/hub/AI-ModelScope/opt-125 --output-len 128 --max-num-batched-tokens 2048 --trust-remote-code ``` Throughput: 59.50 requests/s, 15231.62 tokens/s ![image](https://github.com/vllm-project/vllm/assets/12995855/92d2d824-da47-43f2-aa59-78ff44ad0cd9) ``` python benchmark_throughput.py --input-len 128 --model /home/jiekong/.cache/modelscope/hub/AI-ModelScope/opt-125 --output-len 128 --backend hf --hf-max-batch-size 256 ``` Throughput: 108.34 requests/s, 27736.31 tokens/s ![image](https://github.com/vllm-project/vllm/assets/12995855/ce316880-4b7d-408d-9189-25a15731691e)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: why hf is better than vllm when using benchmark throughput performance;stale When I run benchmark on H800, the results are confusing. Why hf is better than vllm? Is anything wrong when I run the script? `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : why hf is better than vllm when using benchmark throughput performance;stale When I run benchmark on H800, the results are confusing. Why hf is better than vllm? Is anything wrong when I run the script? ``` python ben...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: why hf is better than vllm when using benchmark throughput performance;stale When I run benchmark on H800, the results are confusing. Why hf is better than vllm? Is anything wrong when I run the script? `...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e/jiekong/.cache/modelscope/hub/AI-ModelScope/opt-125 --output-len 128 --backend hf --hf-max-batch-size 256 ``` Throughput: 108.34 requests/s, 27736.31 tokens/s ![image](https://github.com/vllm-project/vllm/assets/12995...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
