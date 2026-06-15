# vllm-project/vllm#38905: [Usage]: max-model-len set to 'auto'，didn't work. Why?

| 字段 | 值 |
| --- | --- |
| Issue | [#38905](https://github.com/vllm-project/vllm/issues/38905) |
| 状态 | open |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: max-model-len set to 'auto'，didn't work. Why?

### Issue 正文摘录

### Your current environment ```text from release vLLM 0.14.0, the max-model-len parameter is support to set 'auto', it means that vLLM will automatically fill based on the current available memory capacity. But On the Qwen 3.5-27B model, setting max-model-len to 128k, vLLM server was successful, setting it to auto failed to work. It seems that this parameter does not automatically select the available max-model-len. Why? ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t vLLM will automatically fill based on the current available memory capacity. But On the Qwen 3.5-27B model, setting max-model-len to 128k, vLLM server was successful, setting it to auto failed to work. It seems that t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: max-model-len set to 'auto'，didn't work. Why? usage ### Your current environment ```text from release vLLM 0.14.0, the max-model-len parameter is support to set 'auto', it means that vLLM will automatically fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
