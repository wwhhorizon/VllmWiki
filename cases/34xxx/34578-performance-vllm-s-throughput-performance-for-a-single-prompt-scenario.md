# vllm-project/vllm#34578: [Performance]: vLLM's throughput performance for a single prompt scenario

| 字段 | 值 |
| --- | --- |
| Issue | [#34578](https://github.com/vllm-project/vllm/issues/34578) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: vLLM's throughput performance for a single prompt scenario

### Issue 正文摘录

### Proposal to improve performance I am using AMD Strix Halo APU. The performance for GPT-OSS-120B model with 1. llama.cpp - 50 tok/sec (stays same with increase in number of prompts) 2. vLLM - 7.5 tok/sec (increases with increase in number of prompts) What in the architecture can be changed to fix this? The ideal scenario would be to use less than 20 concurrent prompts ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: improve performance I am using AMD Strix Halo APU. The performance for GPT-OSS-120B model with 1. llama.cpp - 50 tok/sec (stays same with increase in number of prompts) 2. vLLM - 7.5 tok/sec (increases with increase in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: vLLM's throughput performance for a single prompt scenario performance ### Proposal to improve performance I am using AMD Strix Halo APU. The performance for GPT-OSS-120B model with 1. llama.cpp - 50 tok/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 7.5 tok/sec (increases with increase in number of prompts) What in the architecture can be changed to fix this? The ideal scenario would be to use less than 20 concurrent prompts ### Report of performance regression _No...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
