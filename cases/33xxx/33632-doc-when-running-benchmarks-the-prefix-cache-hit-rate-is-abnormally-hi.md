# vllm-project/vllm#33632: [Doc]: When running benchmarks, the prefix cache hit rate is abnormally high (not consistent with the production environment).

| 字段 | 值 |
| --- | --- |
| Issue | [#33632](https://github.com/vllm-project/vllm/issues/33632) |
| 状态 | open |
| 标签 | documentation;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: When running benchmarks, the prefix cache hit rate is abnormally high (not consistent with the production environment).

### Issue 正文摘录

### 📚 The doc issue During benchmarks, the prefix cache hit rate is abnormally high (not consistent with the production environment). This is the case for both the Sonnet dataset and the prefix_repetition dataset. 我的压测相关数据： request_rates = [7, 8.5, 11.5, 12] input_lens = [5200] prefix_len = 4500 output_lens = [10] num_prompts = 300 dataset_name = "sonnet" # sonnet prefix_repetition testing benchmarks，prefix cache hit rate：从86% 增加到 99.8% production environment，prefix cache hit rate：从86% 增加到 91% vllm版本是0.11.2 ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lly high (not consistent with the production environment). documentation;stale ### 📚 The doc issue During benchmarks, the prefix cache hit rate is abnormally high (not consistent with the production environment). This i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Doc]: When running benchmarks, the prefix cache hit rate is abnormally high (not consistent with the production environment). documentation;stale ### 📚 The doc issue During benchmarks, the prefix cache hit rate is abno...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Doc]: When running benchmarks, the prefix cache hit rate is abnormally high (not consistent with the production environment). documentation;stale ### 📚 The doc issue During benchmarks, the prefix cache hit rate is abno...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Doc]: When running benchmarks, the prefix cache hit rate is abnormally high (not consistent with the production environment). documentation;stale ### 📚 The doc issue During benchmarks, the prefix cache hit rate is abno...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
