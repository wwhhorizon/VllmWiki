# vllm-project/vllm#18037: [RFC]: Enabling Suffix Decoding, LSTM Speculator, Sequence Parallelism from Arctic Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#18037](https://github.com/vllm-project/vllm/issues/18037) |
| 状态 | open |
| 标签 | RFC;speculative-decoding;keep-open |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Enabling Suffix Decoding, LSTM Speculator, Sequence Parallelism from Arctic Inference

### Issue 正文摘录

### Motivation. Snowflake AI Research has recently released several optimizations like Suffix Decoding, LSTM Speculation, Sequence Parallelism, SwiftKV etc, improving TTFT, TPOT and throughput for vLLM via a plugin called Arctic Inference (repo: https://github.com/snowflakedb/arcticinference). **Performance Improvements** - 4x faster generation with [Suffix Decoding](https://www.snowflake.com/en/engineering-blog/fast-speculative-decoding-vllm-arctic/) for SWEBench - 2.4x faster generation with [LSTM Speculator](https://www.snowflake.com/en/engineering-blog/fast-speculative-decoding-vllm-arctic/) for ShareGPT - 2.8x faster coding with [LSTM Speculator](https://www.snowflake.com/en/engineering-blog/fast-speculative-decoding-vllm-arctic/) for HumanEval - 2x higher throughput with [SwiftKV](https://www.snowflake.com/en/engineering-blog/swiftkv-llm-compute-reduction/) - 1.4x throughput than TP=8, but same TTFT as TP=8 with [Arctic Ulysses](https://www.snowflake.com/en/engineering-blog/ulysses-low-latency-llm-inference/) These optimizations are designed to improve vLLM performance for real production workloads at Snowflake, and will continue to be expanded, maintained, and improved over...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: lugin called Arctic Inference (repo: https://github.com/snowflakedb/arcticinference). **Performance Improvements** - 4x faster generation with [Suffix Decoding](https://www.snowflake.com/en/engineering-blog/fast-specula...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ng, LSTM Speculation, Sequence Parallelism, SwiftKV etc, improving TTFT, TPOT and throughput for vLLM via a plugin called Arctic Inference (repo: https://github.com/snowflakedb/arcticinference). **Performance Improvemen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Enabling Suffix Decoding, LSTM Speculator, Sequence Parallelism from Arctic Inference RFC;speculative-decoding;keep-open ### Motivation. Snowflake AI Research has recently released several optimizations like Suff...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nstall both vLLM and Arctic Inference, and then run vLLM with additional configs like: ``` pip install vllm==v0.8.4 arctic-inference vllm serve ... \ --sequence-parallel-size ... \ --speculative-config '{"method": "suff...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ecoding, LSTM Speculator, Sequence Parallelism from Arctic Inference RFC;speculative-decoding;keep-open ### Motivation. Snowflake AI Research has recently released several optimizations like Suffix Decoding, LSTM Specul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
