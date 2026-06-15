# vllm-project/vllm#3316: anyone tests lora's throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#3316](https://github.com/vllm-project/vllm/issues/3316) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> anyone tests lora's throughput

### Issue 正文摘录

I installed vllm from the lastest code. found it supports Qwen2 series model. I test Qwen1.8B with 16 concurrency. got the following result: I merge the lora weight to Qwen1.8B. latency(ms)： min: 222, average: 400, max:418 without merging lora weight to Qwen1.8B, using lora dynamic calling through query. min: 307, average: 780, max: 874 vllm lora way is much more slower than merging version? Is this okay?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: anyone tests lora's throughput stale I installed vllm from the lastest code. found it supports Qwen2 series model. I test Qwen1.8B with 16 concurrency. got the following result: I merge the lora weight to Qwen1.8B. late...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: anyone tests lora's throughput stale I installed vllm from the lastest code. found it supports Qwen2 series model. I test Qwen1.8B with 16 concurrency. got the following result: I merge the lora weight to Qwen1.8B. late...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oughput stale I installed vllm from the lastest code. found it supports Qwen2 series model. I test Qwen1.8B with 16 concurrency. got the following result: I merge the lora weight to Qwen1.8B. latency(ms)： min: 222, aver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: anyone tests lora's throughput stale I installed vllm from the lastest code. found it supports Qwen2 series model. I test Qwen1.8B with 16 concurrency. got the following result: I merge the lora weight to Qwen1.8B. late...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
