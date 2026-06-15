# vllm-project/vllm#11192: [Performance]: Online serving with Pipeline Parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#11192](https://github.com/vllm-project/vllm/issues/11192) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Online serving with Pipeline Parallel

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi, when I run ./benchmarks/benchmark_serving.py on the vLLM backend with the llama-2-7b model on two A40 GPUs connected via an NVLink bridge, using pipeline parallelism, I noticed that the data transfer between the two GPUs doesn't seem to go through NVLink, and the inference throughput significantly drops vLLM version:0.6.3.post1 ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi, when I run ./benchmarks/benchmark_serving.py on the vLLM backend with the llama-2-7b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: LLM backend with the llama-2-7b model on two A40 GPUs connected via an NVLink bridge, using pipeline parallelism, I noticed that the data transfer between the two GPUs doesn't seem to go through NVLink, and the inferenc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on two A40 GPUs connected via an NVLink bridge, using pipeline parallelism, I noticed that the data transfer between the two GPUs doesn't seem to go through NVLink, and the inference throughput significantly drops vLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: hen I run ./benchmarks/benchmark_serving.py on the vLLM backend with the llama-2-7b model on two A40 GPUs connected via an NVLink bridge, using pipeline parallelism, I noticed that the data transfer between the two GPUs...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: erformance Hi, when I run ./benchmarks/benchmark_serving.py on the vLLM backend with the llama-2-7b model on two A40 GPUs connected via an NVLink bridge, using pipeline parallelism, I noticed that the data transfer betw...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
