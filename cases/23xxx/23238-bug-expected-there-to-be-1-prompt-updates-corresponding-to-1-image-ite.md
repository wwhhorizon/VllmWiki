# vllm-project/vllm#23238: [Bug]: Expected there to be 1 prompt updates corresponding to 1 image items, but instead found 0 prompt updates! This is likely because you forgot to include input plac

| 字段 | 值 |
| --- | --- |
| Issue | [#23238](https://github.com/vllm-project/vllm/issues/23238) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Expected there to be 1 prompt updates corresponding to 1 image items, but instead found 0 prompt updates! This is likely because you forgot to include input plac

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 我使用vllm的python代码连接本地的GLM4.5VFP8模型，可以连接，可以回答问题，但是在提交照片时说我没有在提示中加入占位符，可是我有 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rent environment ### 🐛 Describe the bug 我使用vllm的python代码连接本地的GLM4.5VFP8模型，可以连接，可以回答问题，但是在提交照片时说我没有在提示中加入占位符，可是我有 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 我有 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
