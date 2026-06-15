# vllm-project/vllm#20407: [Bug]: TypeError: Qwen2_5_VLProcessor.__init__() got multiple values for argument 'image_processor' with transformers 4.53

| 字段 | 值 |
| --- | --- |
| Issue | [#20407](https://github.com/vllm-project/vllm/issues/20407) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: Qwen2_5_VLProcessor.__init__() got multiple values for argument 'image_processor' with transformers 4.53

### Issue 正文摘录

### Your current environment TypeError: Qwen2_5_VLProcessor.__init__() got multiple values for argument 'image_processor' with transformers 4.53 vllm: 0.9.1 transformers: 4.53.0 torch 2.7 cuda version 12.6 ### 🐛 Describe the bug TypeError: Qwen2_5_VLProcessor.__init__() got multiple values for argument 'image_processor' with transformers 4.53 vllm: 0.9.1 transformers: 4.53.0 torch 2.7 cuda version 12.6 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ssor' with transformers 4.53 vllm: 0.9.1 transformers: 4.53.0 torch 2.7 cuda version 12.6 ### 🐛 Describe the bug TypeError: Qwen2_5_VLProcessor.__init__() got multiple values for argument 'image_processor' with transfor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: with transformers 4.53 vllm: 0.9.1 transformers: 4.53.0 torch 2.7 cuda version 12.6 ### 🐛 Describe the bug TypeError: Qwen2_5_VLProcessor.__init__() got multiple values for argument 'image_processor' with transformers 4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: TypeError: Qwen2_5_VLProcessor.__init__() got multiple values for argument 'image_processor' with transformers 4.53 bug ### Your current environment TypeError: Qwen2_5_VLProcessor.__init__() got multiple values f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
