# vllm-project/vllm#8832: [CI/Build]: Version v0.6.2 lacks the whl package

| 字段 | 值 |
| --- | --- |
| Issue | [#8832](https://github.com/vllm-project/vllm/issues/8832) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI/Build]: Version v0.6.2 lacks the whl package

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The whl package is not generated in version 0.6.2, it looks like a dependency package is missing from the packaging session. See: https://github.com/vllm-project/vllm/actions/runs/11041663331/job/30672415316 for details ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI/Build]: Version v0.6.2 lacks the whl package bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The whl package is not generated in version 0.6.2, it looks like a depend
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ils ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on v0.6.2 lacks the whl package bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The whl package is not generated in version 0.6.2, it looks like a dependency package is missin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
