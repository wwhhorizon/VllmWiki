# vllm-project/vllm#10605: [Usage]: Why `use_beam_search` is eliminated in `vllm.SamplingParams` from v0.6.3?

| 字段 | 值 |
| --- | --- |
| Issue | [#10605](https://github.com/vllm-project/vllm/issues/10605) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why `use_beam_search` is eliminated in `vllm.SamplingParams` from v0.6.3?

### Issue 正文摘录

### Your current environment I am asking a general API question regarding `vllm`, therefore, env info is not needed. ### How would you like to use vllm I want to ask why `use_beam_search` is eliminated in `vllm.SamplingParams` from v0.6.3 (https://docs.vllm.ai/en/v0.6.3/dev/sampling_params.html)? How can we control the usage of beam search from v0.6.3 onwards? To the best of my knowledge, `use_beam_search` is supported in all versions from [v0.4.0.post1](https://docs.vllm.ai/en/v0.4.0.post1/dev/sampling_params.html) to [v0.6.2](https://docs.vllm.ai/en/v0.6.2/dev/sampling_params.html). ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rds? To the best of my knowledge, `use_beam_search` is supported in all versions from [v0.4.0.post1](https://docs.vllm.ai/en/v0.4.0.post1/dev/sampling_params.html) to [v0.6.2](https://docs.vllm.ai/en/v0.6.2/dev/sampling...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: Why `use_beam_search` is eliminated in `vllm.SamplingParams` from v0.6.3? usage ### Your current environment I am asking a general API question regarding `vllm`, therefore, env info is not needed. ### How would...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
