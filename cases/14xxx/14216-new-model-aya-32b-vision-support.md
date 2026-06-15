# vllm-project/vllm#14216: [New Model]: aya 32b vision support

| 字段 | 值 |
| --- | --- |
| Issue | [#14216](https://github.com/vllm-project/vllm/issues/14216) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: aya 32b vision support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi Cohere just released aya vision 32b https://huggingface.co/CohereForAI/aya-vision-32b it reach to qwen vl 2.5 72B with only 32b parameters can we support this model ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: aya 32b vision support new-model ### 🚀 The feature, motivation and pitch Hi Cohere just released aya vision 32b https://huggingface.co/CohereForAI/aya-vision-32b it reach to qwen vl 2.5 72B with only 32b pa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
