# vllm-project/vllm#27406: [Bug]: MM performance regression from upgrading to torch 2.9

| 字段 | 值 |
| --- | --- |
| Issue | [#27406](https://github.com/vllm-project/vllm/issues/27406) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MM performance regression from upgrading to torch 2.9

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There's a significant performance regression on `nn.Conv3d` which affects all multimodal models that use this module (Qwen3-VL, GLM4.1V, etc). This was caught by the unusually long multimodal profiling time in the latest nightly build, and a similar issue can be found at https://github.com/pytorch/pytorch/issues/166122 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 's a significant performance regression on `nn.Conv3d` which affects all multimodal models that use this module (Qwen3-VL, GLM4.1V, etc). This was caught by the unusually long multimodal profiling time in the latest nig...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: MM performance regression from upgrading to torch 2.9 bug ### Your current environment ### 🐛 Describe the bug There's a significant performance regression on `nn.Conv3d` which affects all multimodal models that u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ht by the unusually long multimodal profiling time in the latest nightly build, and a similar issue can be found at https://github.com/pytorch/pytorch/issues/166122 ### Before submitting a new issue... - [x] Make sure y...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 122 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
