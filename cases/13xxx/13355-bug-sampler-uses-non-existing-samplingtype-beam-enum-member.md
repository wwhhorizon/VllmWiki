# vllm-project/vllm#13355: [Bug]: Sampler uses non-existing `SamplingType.BEAM` enum member

| 字段 | 值 |
| --- | --- |
| Issue | [#13355](https://github.com/vllm-project/vllm/issues/13355) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Sampler uses non-existing `SamplingType.BEAM` enum member

### Issue 正文摘录

### Your current environment It looks that [sampler.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/sampler.py#L803) module uses removed `SamplingType.Beam` enum member. ``` elif sampling_type == SamplingType.BEAM: beam_search_logprobs = logprobs[sample_indices] ``` It is repeated in at least 2 places within module. Original Enum definition https://github.com/vllm-project/vllm/blob/main/vllm/sampling_params.py#L22 ### 🐛 Describe the bug It is impossible to reproduce now, more looks like a typo during refactoring. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: vllm/sampling_params.py#L22 ### 🐛 Describe the bug It is impossible to reproduce now, more looks like a typo during refactoring. ### Before submitting a new issue... - [x] Make sure you already searched for relevant iss...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` elif sampling_type == SamplingType.BEAM: beam_search_logprobs = logprobs[sample_indices] ``` It is repeated in at least 2 places within module. Original Enum definition https://github.com/vllm-project/vllm/blob/main...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ks that [sampler.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/sampler.py#L803) module uses removed `SamplingType.Beam` enum member. ``` elif sampling_type == SamplingType.BEAM: beam_sear...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
