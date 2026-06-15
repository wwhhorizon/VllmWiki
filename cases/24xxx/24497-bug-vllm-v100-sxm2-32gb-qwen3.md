# vllm-project/vllm#24497: [Bug]: VLLM 不支持在 V100-SXM2-32GB 上部署qwen3 系列的模型

| 字段 | 值 |
| --- | --- |
| Issue | [#24497](https://github.com/vllm-project/vllm/issues/24497) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM 不支持在 V100-SXM2-32GB 上部署qwen3 系列的模型

### Issue 正文摘录

### Your current environment # 版本 VLLM 0.9.0.1 CUDA 12.8 ### 🐛 Describe the bug # 问题 可以成功部署，但是一调用就会崩掉 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -32GB 上部署qwen3 系列的模型 bug ### Your current environment # 版本 VLLM 0.9.0.1 CUDA 12.8 ### 🐛 Describe the bug # 问题 可以成功部署，但是一调用就会崩掉 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issue...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: VLLM 不支持在 V100-SXM2-32GB 上部署qwen3 系列的模型 bug ### Your current environment # 版本 VLLM 0.9.0.1 CUDA 12.8 ### 🐛 Describe the bug # 问题 可以成功部署，但是一调用就会崩掉 ### Before submitting a new issue... - [x] Make sure you already s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
