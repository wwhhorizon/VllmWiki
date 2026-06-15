# vllm-project/vllm#13986: [Feature]: Update XGrammar to 0.1.14

| 字段 | 值 |
| --- | --- |
| Issue | [#13986](https://github.com/vllm-project/vllm/issues/13986) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Update XGrammar to 0.1.14

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm using XGrammar in production and I want to use more feature-rich CFG grammars. They are supported in `0.1.14` but not in `0.1.11`. Can we release a new version updating xgrammars? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: They are supported in `0.1.14` but not in `0.1.11`. Can we release a new version updating xgrammars? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make su...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Update XGrammar to 0.1.14 feature request ### 🚀 The feature, motivation and pitch I'm using XGrammar in production and I want to use more feature-rich CFG grammars. They are supported in `0.1.14` but not in `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
