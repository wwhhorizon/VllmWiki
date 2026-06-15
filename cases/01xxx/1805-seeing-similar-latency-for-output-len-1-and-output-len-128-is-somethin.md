# vllm-project/vllm#1805: Seeing similar latency for output len=1 and output len=128. Is something wrong with benchmark latency script?

| 字段 | 值 |
| --- | --- |
| Issue | [#1805](https://github.com/vllm-project/vllm/issues/1805) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Seeing similar latency for output len=1 and output len=128. Is something wrong with benchmark latency script?

### Issue 正文摘录

Hi I'm trying to benchmark Llama 7B's latency using [benchmark_latency.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_latency.py) script but I'm seeing similar latency for output len=1 and output len=128 which makes no sense Within the script I changed the `model_max_len=2000` because that's the input len I want to benchmark with. Here's the commands I used with vllm 0.2.0 on g5.12xlarge (4 A10G GPUs) on AWS ``` python3 benchmark_latency.py --model "meta-llama/Llama-2-7b-hf" --input-len 2000 --output-len 128 -tp 4 --num-iters 10 --batch-size 1 ``` gives 462ms and ``` python3 benchmark_latency.py --model "meta-llama/Llama-2-7b-hf" --input-len 2000 --output-len 1 -tp 4 --num-iters 10 --batch-size 1 ``` gives 459 ms I would expect output len=1 latency to be much lower than that of output len=128. Can someone please help me understand this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: omething wrong with benchmark latency script? Hi I'm trying to benchmark Llama 7B's latency using [benchmark_latency.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_latency.py) script but I'm see...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Seeing similar latency for output len=1 and output len=128. Is something wrong with benchmark latency script? Hi I'm trying to benchmark Llama 7B's latency using [benchmark_latency.py](https://github.com/vllm-project/vl...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
