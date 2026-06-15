# vllm-project/vllm#6150: [Performance]:  the performance with chunked-prefill-enabled is lower than default

| 字段 | 值 |
| --- | --- |
| Issue | [#6150](https://github.com/vllm-project/vllm/issues/6150) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]:  the performance with chunked-prefill-enabled is lower than default

### Issue 正文摘录

### I tested vllm benchmark_throughput.py and finded that the performance with chunked-prefill-enabled is lower than default, how can I deal this problem _No response_ ### Your current environment (if you think it is necessary) ```text export CUDA_VISIBLE_DEVICES=0 python3 ./benchmarks/benchmark_throughput.py \ --model /home/workspace/chatglm3-6b/ \ --tokenizer /home/workspace/chatglm3-6b/ \ --num-prompts 16 \ --input-len 1024 \ --output-len 256 \ --enable-chunked-prefill \ --trust-remote-code ``` Does the params set ok?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: h chunked-prefill-enabled is lower than default performance;stale ### I tested vllm benchmark_throughput.py and finded that the performance with chunked-prefill-enabled is lower than default, how can I deal this problem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: the performance with chunked-prefill-enabled is lower than default performance;stale ### I tested vllm benchmark_throughput.py and finded that the performance with chunked-prefill-enabled is lower than de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Your current environment (if you think it is necessary) ```text export CUDA_VISIBLE_DEVICES=0 python3 ./benchmarks/benchmark_throughput.py \ --model /home/workspace/chatglm3-6b/ \ --tokenizer /home/workspace/chatglm3-6b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: A_VISIBLE_DEVICES=0 python3 ./benchmarks/benchmark_throughput.py \ --model /home/workspace/chatglm3-6b/ \ --tokenizer /home/workspace/chatglm3-6b/ \ --num-prompts 16 \ --input-len 1024 \ --output-len 256 \ --enable-chun...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
