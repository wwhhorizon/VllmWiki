# vllm-project/vllm#19243: [Bug]: high cpu utilization when there is no inference task

| 字段 | 值 |
| --- | --- |
| Issue | [#19243](https://github.com/vllm-project/vllm/issues/19243) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: high cpu utilization when there is no inference task

### Issue 正文摘录

### Your current environment I deploy models with the `vllm/vllm-openai:v0.9.0.1` docker image. The command line arguments: `--tensor-parallel-size 2` and `--enforce-eager`. ### 🐛 Describe the bug The CPU utlization is high even if no tasks are running. This does not depend on models. I encountered the issue with both qwen3 and devstral models. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: en there is no inference task bug ### Your current environment I deploy models with the `vllm/vllm-openai:v0.9.0.1` docker image. The command line arguments: `--tensor-parallel-size 2` and `--enforce-eager`. ### 🐛 Descr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: urrent environment I deploy models with the `vllm/vllm-openai:v0.9.0.1` docker image. The command line arguments: `--tensor-parallel-size 2` and `--enforce-eager`. ### 🐛 Describe the bug The CPU utlization is high even...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
