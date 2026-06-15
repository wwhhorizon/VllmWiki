# vllm-project/vllm#14507: [Usage]: The example of using microsoft/Phi-4-multimodal-instruct audio

| 字段 | 值 |
| --- | --- |
| Issue | [#14507](https://github.com/vllm-project/vllm/issues/14507) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: The example of using microsoft/Phi-4-multimodal-instruct audio

### Issue 正文摘录

### Your current environment How to use microsoft/Phi-4-multimodal-instruct audio by using vllm? [Here](https://github.com/vllm-project/vllm/pull/14343/files#diff-068f76c074ff2ec408347e0b9ff0b8ce78b75048a83343b71d684b68511480aa), I can see an example of using vision, but how to use audio? Please help！ ![Image](https://github.com/user-attachments/assets/2ccfe29a-535d-4857-92ac-ae0b41df8c0d) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: The example of using microsoft/Phi-4-multimodal-instruct audio usage ### Your current environment How to use microsoft/Phi-4-multimodal-instruct audio by using vllm? [Here](https://github.com/vllm-project/vllm/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
