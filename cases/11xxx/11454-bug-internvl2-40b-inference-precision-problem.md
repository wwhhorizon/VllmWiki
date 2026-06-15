# vllm-project/vllm#11454: [Bug]: InternVL2-40B Inference Precision Problem

| 字段 | 值 |
| --- | --- |
| Issue | [#11454](https://github.com/vllm-project/vllm/issues/11454) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: InternVL2-40B Inference Precision Problem

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I use the InternVL2-40B open source model to infer images, require the image description, evaluate and score the images based on the given questions, and finally output the inference results in JSON format. However, I find that the JSON format provided by Vllm inference results is incorrect, about 5%. Under the same conditions, LMDeploy does not have such a high error rate. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: InternVL2-40B Inference Precision Problem bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I use the InternVL2-40B open source model to infer images, require the im
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: L2-40B open source model to infer images, require the image description, evaluate and score the images based on the given questions, and finally output the inference results in JSON format. However, I find that the JSON...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: InternVL2-40B Inference Precision Problem bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I use the InternVL2-40B open source model to infer images, require the i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: InternVL2-40B Inference Precision Problem bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I use the InternVL2-40B open source model to infer images, require the i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: te. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
