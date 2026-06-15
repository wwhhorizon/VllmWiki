# vllm-project/vllm#22918: [Feature][Tools]: Complete Redesign of Tool Calling

| 字段 | 值 |
| --- | --- |
| Issue | [#22918](https://github.com/vllm-project/vllm/issues/22918) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Tools]: Complete Redesign of Tool Calling

### Issue 正文摘录

### 🚀 The feature, motivation and pitch - We currently have a patchwork of support for tools in vLLM - We currently have regexes in tools which can cause noisy-neighbor issues in vLLM - We would welcome a contributor to redesign the system, improve our CI coverage, and work together with the ecosystem to ensure vLLM's support for tool calling is elite ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: LLM - We would welcome a contributor to redesign the system, improve our CI coverage, and work together with the ecosystem to ensure vLLM's support for tool calling is elite ### Alternatives _No response_ ### Additional...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature][Tools]: Complete Redesign of Tool Calling help wanted;feature request ### 🚀 The feature, motivation and pitch - We currently have a patchwork of support for tools in vLLM - We currently have regexes in tools w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
