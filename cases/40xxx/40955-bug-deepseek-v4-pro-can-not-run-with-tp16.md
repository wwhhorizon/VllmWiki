# vllm-project/vllm#40955: [Bug]: DeepSeek V4 pro can not run with TP16

| 字段 | 值 |
| --- | --- |
| Issue | [#40955](https://github.com/vllm-project/vllm/issues/40955) |
| 状态 | open |
| 标签 | bug;DSv4 |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V4 pro can not run with TP16

### Issue 正文摘录

### Your current environment use this recipes: can not run with this error: V4 shape: 3072/16=192, fp8 quantization need size is 128*x ### 🐛 Describe the bug https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro?features=tool_calling%2Creasoning%2Cspec_decoding&strategy=multi_node_tep ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: this recipes: can not run with this error: V4 shape: 3072/16=192, fp8 quantization need size is 128*x ### 🐛 Describe the bug https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro?features=tool_calling%2Creasoning%2Cspec_d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: can not run with TP16 bug;DSv4 ### Your current environment use this recipes: can not run with this error: V4 shape: 3072/16=192, fp8 quantization need size is 128*x ### 🐛 Describe the bug https://recipes.vllm.ai/deepse...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tep ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
