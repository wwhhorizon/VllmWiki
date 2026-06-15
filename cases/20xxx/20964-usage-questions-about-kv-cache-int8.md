# vllm-project/vllm#20964: [Usage]: questions about kv cache int8

| 字段 | 值 |
| --- | --- |
| Issue | [#20964](https://github.com/vllm-project/vllm/issues/20964) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: questions about kv cache int8

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, i am willing to support kv cache int8 quant in vllm, including per tensor & per channel (static) and maybe per token (dynamic). Now i have successfully quanted per channel kv int8 weight using llm compressor and willing to contribute later. i wonder whether you are willing to support this new feature, so i can start to work. Besides, i am curious that there are a lot of attention ops and which should i use to support kv int8, and actually i am not sure these ops can support this feature, and i do not know the usage of these ops, do you have some docs? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ow would you like to use vllm Hi, i am willing to support kv cache int8 quant in vllm, including per tensor & per channel (static) and maybe per token (dynamic). Now i have successfully quanted per channel kv int8 weigh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cs? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: questions about kv cache int8 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, i am willing to support kv cache int8 quant in vll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: questions about kv cache int8 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, i am willing to support kv cache int8 quant in vll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
