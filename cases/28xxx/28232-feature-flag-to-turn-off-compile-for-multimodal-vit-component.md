# vllm-project/vllm#28232: [Feature]: Flag to turn off compile for multimodal/vit component

| 字段 | 值 |
| --- | --- |
| Issue | [#28232](https://github.com/vllm-project/vllm/issues/28232) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Flag to turn off compile for multimodal/vit component

### Issue 正文摘录

### 🚀 The feature, motivation and pitch With the introduction of compilation for the vision backbone for some models (i.e https://github.com/vllm-project/vllm/pull/23207), we do not currently have a lever for users to turn this off other than commenting out the code. We could utilize and environment variable and conditional compilation to make this configurable by commandline ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Flag to turn off compile for multimodal/vit component feature request ### 🚀 The feature, motivation and pitch With the introduction of compilation for the vision backbone for some models (i.e https://github.c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Flag to turn off compile for multimodal/vit component feature request ### 🚀 The feature, motivation and pitch With the introduction of compilation for the vision backbone for some models (i.e https://github.c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Flag to turn off compile for multimodal/vit component feature request ### 🚀 The feature, motivation and pitch With the introduction of compilation for the vision backbone for some models (i.e https://github.c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
