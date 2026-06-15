# vllm-project/vllm#32656: [Tracker]: Use `mm_features` for M-RoPE calculation for all models

| 字段 | 值 |
| --- | --- |
| Issue | [#32656](https://github.com/vllm-project/vllm/issues/32656) |
| 状态 | closed |
| 标签 | help wanted;multi-modality |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracker]: Use `mm_features` for M-RoPE calculation for all models

### Issue 正文摘录

### Purpose Follow-up to #28399, use token indices from `mm_features` instead of searching through `input_tokens` which is inefficient and does not necessarily align with the expected tokens from `mm_features`. Apply this to all models with `SupportsMRoPE` interface. - [x] https://github.com/vllm-project/vllm/pull/39753 - [x] #33039 - [x] #28367 - [x] #39869 - [x] #39888 - [x] #32126 - [x] #32772 - [x] #28730 - [x] #33010 When submitting a PR, please run correctness evaluation, compare to main branch, and put your results in the PR description. You should also trace the inputs (see https://github.com/vllm-project/vllm/pull/32126#issuecomment-3751251933 for example) to show the performance gain. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Follow-up to #28399, use token indices from `mm_features` instead of searching through `input_tokens` which is inefficient and does not necessarily align with the expected tokens from `mm_features`. Apply this to all mo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: - [x] #28730 - [x] #33010 When submitting a PR, please run correctness evaluation, compare to main branch, and put your results in the PR description. You should also trace the inputs (see https://github.com/vllm-projec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: `mm_features` instead of searching through `input_tokens` which is inefficient and does not necessarily align with the expected tokens from `mm_features`. Apply this to all models with `SupportsMRoPE` interface. - [x] h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Tracker]: Use `mm_features` for M-RoPE calculation for all models help wanted;multi-modality ### Purpose Follow-up to #28399, use token indices from `mm_features` instead of searching through `input_tokens` which is in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
