# vllm-project/vllm#9022: [Performance]: Why is Llama 3.1 405B 5 times faster than 70B on benchmarks?

| 字段 | 值 |
| --- | --- |
| Issue | [#9022](https://github.com/vllm-project/vllm/issues/9022) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Why is Llama 3.1 405B 5 times faster than 70B on benchmarks?

### Issue 正文摘录

### Proposal to improve performance N/A ### Report of performance regression N/A ### Misc discussion on performance Hi I'm seeing a strange throughput disparity between Llama 3.1 405B and 70B based on the blog and nightly benchmarks. Llama 3.1 405B was benchmarked with 3100~ tokens/sec in this post. https://blog.vllm.ai/2024/07/23/llama31.html And on the nightly benchmarks, I'm seeing Llama 3.1 70B is coming in at about 700~ tokens/second. https://buildkite.com/vllm/performance-benchmark/builds/4068 The nightly bench uses 8xA100s. I know H100s have an advantage due to native FP8 support via specialized tensor cores but this is quite a large difference. I would think 405B would have less throughput if anything. What's the reason there is such a large difference? ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: Why is Llama 3.1 405B 5 times faster than 70B on benchmarks? performance;stale ### Proposal to improve performance N/A ### Report of performance regression N/A ### Misc discussion on performance Hi I'm se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ite.com/vllm/performance-benchmark/builds/4068 The nightly bench uses 8xA100s. I know H100s have an advantage due to native FP8 support via specialized tensor cores but this is quite a large difference. I would think 40...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: m seeing Llama 3.1 70B is coming in at about 700~ tokens/second. https://buildkite.com/vllm/performance-benchmark/builds/4068 The nightly bench uses 8xA100s. I know H100s have an advantage due to native FP8 support via...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ightly bench uses 8xA100s. I know H100s have an advantage due to native FP8 support via specialized tensor cores but this is quite a large difference. I would think 405B would have less throughput if anything. What's th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: Why is Llama 3.1 405B 5 times faster than 70B on benchmarks? performance;stale ### Proposal to improve performance N/A ### Report of performance regression N/A ### Misc discussion on performance Hi I'm se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
