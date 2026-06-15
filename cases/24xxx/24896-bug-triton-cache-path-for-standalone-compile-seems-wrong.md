# vllm-project/vllm#24896: [Bug]: triton cache path for standalone_compile seems wrong

| 字段 | 值 |
| --- | --- |
| Issue | [#24896](https://github.com/vllm-project/vllm/issues/24896) |
| 状态 | open |
| 标签 | bug;torch.compile;unstale;needs reproduction |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: triton cache path for standalone_compile seems wrong

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/pull/24605 for more details. We should investigate some more (and attempt to repro the bug first as the first step) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: triton cache path for standalone_compile seems wrong bug;torch.compile;unstale;needs reproduction ### Your current environment n/a ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/pull/24605 for mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: triton cache path for standalone_compile seems wrong bug;torch.compile;unstale;needs reproduction ### Your current environment n/a ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/pull/24605 for mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ep) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: triton cache path for standalone_compile seems wrong bug;torch.compile;unstale;needs reproduction ### Your current environment n/a ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/pull/24605 for more deta...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
