# vllm-project/vllm#12940: [Bug]: Qwen2_5_VL-3B :When running the multi-modal model, encountered multiple critical issues related to sequence length and context window limitations.

| 字段 | 值 |
| --- | --- |
| Issue | [#12940](https://github.com/vllm-project/vllm/issues/12940) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2_5_VL-3B :When running the multi-modal model, encountered multiple critical issues related to sequence length and context window limitations.

### Issue 正文摘录

### Your current environment Qwen2_5_VL-3B [ ](url) ### 🐛 Describe the bug The model throws three main warnings/errors: Image rescaling issues Token sequence length exceeding maximum limit Insufficient context length for multi-modal embeddings ![Image](https://github.com/user-attachments/assets/6634d3e6-fe7c-41dd-aa19-bda346cc780f) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2_5_VL-3B :When running the multi-modal model, encountered multiple critical issues related to sequence length and context window limitations. bug ### Your current environment Qwen2_5_VL-3B [ ](url) ### 🐛 Des...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ge rescaling issues Token sequence length exceeding maximum limit Insufficient context length for multi-modal embeddings ![Image](https://github.com/user-attachments/assets/6634d3e6-fe7c-41dd-aa19-bda346cc780f) ### Befo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0f) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
