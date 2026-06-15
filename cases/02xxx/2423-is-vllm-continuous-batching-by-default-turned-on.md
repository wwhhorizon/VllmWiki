# vllm-project/vllm#2423: Is vllm continuous batching by default turned on?

| 字段 | 值 |
| --- | --- |
| Issue | [#2423](https://github.com/vllm-project/vllm/issues/2423) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is vllm continuous batching by default turned on?

### Issue 正文摘录

Hi, I'm quite newbee to vllm. I've checked the engine arguments [here](https://github.com/vllm-project/vllm/blob/4b61c6b669e368c6850531815940d9a542b9f223/vllm/engine/arg_utils.py#L11). Not sure if I'm testing correctly. I got the below testing result (benchmark_serving.py) and am not quite sure if the continuous batching is working: |Num GPU | Requet Rate | Model | Throughput | Avg Latency(s) | Latency Per token (s) | Latency Per output token (s)| Total Time(s)| |------------|--------------|---------|--------------|------------------|------------------------|-------------------------------|---------------| |1 | 10 | 7B-float16-TP1 | 5.91 | 37.62 | 0.22 | 2.57 | 169.19| |1 | 6 | 7B-float16-TP1 | 5.76 | 6.13 | 0.04 | 0.32 | 173.7| |1 | 5 | 7B-float16-TP1 | 4.93 | 3.1 | 0.02 | 0.15 | 202.93| |1 | 2 | 7B-float16-TP1 | 1.99 | 1.18 | 0.01 | 0.06 | 503.03| |2 | 10 | 7B-float16-TP2 | 6.37 | 42.84 | 0.25 | 2.62 | 157.1| |2 | 6 | 7B-float16-TP2 | 5.9 | 7.57 | 0.04 | 0.39 | 169.47| |2 | 5 | 7B-float16-TP2 | 4.94 | 2.82 | 0.01 | 0.15 | 202.49| |1 | 6 | 7B-gptq4bit-TP1 | 5.29 | 20.73 | 0.12 | 1.15 | 189.09| |1 | 5 | 7B-gptq4bit-TP1 | 4.94 | 6.26 | 0.03 | 0.31 | 202.38| |2 | 5 | 13B-float16-TP2...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: 6850531815940d9a542b9f223/vllm/engine/arg_utils.py#L11). Not sure if I'm testing correctly. I got the below testing result (benchmark_serving.py) and am not quite sure if the continuous batching is working: |Num GPU | R...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ----------|-------------------------------|---------------| |1 | 10 | 7B-float16-TP1 | 5.91 | 37.62 | 0.22 | 2.57 | 169.19| |1 | 6 | 7B-float16-TP1 | 5.76 | 6.13 | 0.04 | 0.32 | 173.7| |1 | 5 | 7B-float16-TP1 | 4.93 | 3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: te sure if the continuous batching is working: |Num GPU | Requet Rate | Model | Throughput | Avg Latency(s) | Latency Per token (s) | Latency Per output token (s)| Total Time(s)| |------------|--------------|---------|-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
