# vllm-project/vllm#11391: Where does the default number 43328 of KV cache come from and How can I change it?

| 字段 | 值 |
| --- | --- |
| Issue | [#11391](https://github.com/vllm-project/vllm/issues/11391) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Where does the default number 43328 of KV cache come from and How can I change it?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Not an technical issue, not related to environment. ### How would you like to use vllm I have encountered "The model's max seq len (56000) is larger than the maximum number of tokens that can be stored in KV cache (43328)" numerous times. Although it can be solved by setting a smaller --max-model-len parameter, it's actually an issue when you really want to set a large --max-model-len for a large context. What makes it more complicated is that the KV cache number changes automatically when we set different --max-model-len. My question is: 1) can we change the size of KV cache? 2) how? 3) Anyway for us user to manage the KV cache issue more directly? Thanks George ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: KV cache (43328)" numerous times. Although it can be solved by setting a smaller --max-model-len parameter, it's actually an issue when you really want to set a large --max-model-len for a large context. What makes it m...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Where does the default number 43328 of KV cache come from and How can I change it? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` Not an technical issue, not related to enviro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nvironment. ### How would you like to use vllm I have encountered "The model's max seq len (56000) is larger than the maximum number of tokens that can be stored in KV cache (43328)" numerous times. Although it can be s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: efault number 43328 of KV cache come from and How can I change it? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` Not an technical issue, not related to environment. ### How w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
