# vllm-project/vllm#26840: [Doc]: Update AWQ Guide

| 字段 | 值 |
| --- | --- |
| Issue | [#26840](https://github.com/vllm-project/vllm/issues/26840) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Update AWQ Guide

### Issue 正文摘录

### 📚 The doc issue Situation: AutoAWQ functionality was adopted by llm-compressor but vllm [docs](https://docs.vllm.ai/en/latest/features/quantization/auto_awq.html) point to AutoAWQ which is deprecated ### Suggest a potential alternative/fix 1) Update the [AutoAWQ guide](https://github.com/vllm-project/vllm/blob/main/docs/features/quantization/auto_awq.md) to use the [llm-compressor](https://github.com/vllm-project/llm-compressor/tree/2a6a0a34c8a57b6090b5fbac9c0659edf982185c/examples/awq) apis/flow 2) Make sure to also update links in [quantization doc](https://github.com/vllm-project/vllm/blob/main/docs/features/quantization/README.md) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: fbac9c0659edf982185c/examples/awq) apis/flow 2) Make sure to also update links in [quantization doc](https://github.com/vllm-project/vllm/blob/main/docs/features/quantization/README.md) ### Before submitting a new issue...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: y llm-compressor but vllm [docs](https://docs.vllm.ai/en/latest/features/quantization/auto_awq.html) point to AutoAWQ which is deprecated ### Suggest a potential alternative/fix 1) Update the [AutoAWQ guide](https://git...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: md) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: was adopted by llm-compressor but vllm [docs](https://docs.vllm.ai/en/latest/features/quantization/auto_awq.html) point to AutoAWQ which is deprecated ### Suggest a potential alternative/fix 1) Update the [AutoAWQ guide...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
