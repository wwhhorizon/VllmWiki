# vllm-project/vllm#29294: [CPU Backend] [Doc]: Update Installation Docs for Arm CPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#29294](https://github.com/vllm-project/vllm/issues/29294) |
| 状态 | closed |
| 标签 | documentation;cpu |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CPU Backend] [Doc]: Update Installation Docs for Arm CPUs

### Issue 正文摘录

### 📚 The doc issue This page https://docs.vllm.ai/en/stable/getting_started/installation/cpu/#arm-aarch64 is very out-dated. We now release Arm CPU wheels and images thanks to #26931 and #27331 We need to update that page to reflect that :) ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CPU Backend] [Doc]: Update Installation Docs for Arm CPUs documentation;cpu ### 📚 The doc issue This page https://docs.vllm.ai/en/stable/getting_started/installation/cpu/#arm-aarch64 is very out-dated. We now release A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [CPU Backend] [Doc]: Update Installation Docs for Arm CPUs documentation;cpu ### 📚 The doc issue This page https://docs.vllm.ai/en/stable/getting_started/installation/cpu/#arm-aarch64 is very out-dated. We now release A...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge https://docs.vllm.ai/en/stable/getting_started/installation/cpu/#arm-aarch64 is very out-dated. We now release Arm CPU wheels and images thanks to #26931 and #27331 We need to update that page to reflect that :) ###...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
