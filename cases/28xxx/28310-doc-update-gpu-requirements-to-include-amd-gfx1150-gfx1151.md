# vllm-project/vllm#28310: [Doc]: Update GPU requirements to include AMD gfx1150/gfx1151

| 字段 | 值 |
| --- | --- |
| Issue | [#28310](https://github.com/vllm-project/vllm/issues/28310) |
| 状态 | closed |
| 标签 | documentation;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Update GPU requirements to include AMD gfx1150/gfx1151

### Issue 正文摘录

### 📚 The doc issue Summary: The documentation for GPU requirements does not list AMD gfx1150 and gfx1151 architectures, which are now supported. Background: Support for AMD gfx1150 and gfx1151 GPUs was added in https://github.com/vllm-project/vllm/pull/25908. The GPU requirements page should be updated to reflect this. Affected page: https://docs.vllm.ai/en/latest/getting_started/installation/gpu/index.html#requirements Expected behavior: The GPU requirements page lists AMD gfx1150 and gfx1151 as supported architectures. ### Suggest a potential alternative/fix Proposed fix: https://github.com/vllm-project/vllm/pull/28308 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: c]: Update GPU requirements to include AMD gfx1150/gfx1151 documentation;rocm ### 📚 The doc issue Summary: The documentation for GPU requirements does not list AMD gfx1150 and gfx1151 architectures, which are now suppor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ect this. Affected page: https://docs.vllm.ai/en/latest/getting_started/installation/gpu/index.html#requirements Expected behavior: The GPU requirements page lists AMD gfx1150 and gfx1151 as supported architectures. ###...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ld be updated to reflect this. Affected page: https://docs.vllm.ai/en/latest/getting_started/installation/gpu/index.html#requirements Expected behavior: The GPU requirements page lists AMD gfx1150 and gfx1151 as support...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
