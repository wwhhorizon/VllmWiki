# vllm-project/vllm#12584: [Bug]: [V1] New v1 engine does not support n>1?

| 字段 | 值 |
| --- | --- |
| Issue | [#12584](https://github.com/vllm-project/vllm/issues/12584) |
| 状态 | closed |
| 标签 | bug;v1 |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [V1] New v1 engine does not support n>1?

### Issue 正文摘录

### Your current environment VLLM version 0.7.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using v1 engine, `LLM.generate()` only returns 1 `CompletionOutput` even when `SamplingParams` sets `n>1` Is this expected to work or is `n>1` not yet supported for v1? If so, are there plans to support it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 1 engine does not support n>1? bug;v1 ### Your current environment VLLM version 0.7.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using v1 engine, `LLM.generate()` only returns 1 `CompletionOutput` e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: upport n>1? bug;v1 ### Your current environment VLLM version 0.7.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using v1 engine, `LLM.generate()` only returns 1 `CompletionOutput` even when `SamplingP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
