# vllm-project/vllm#36704: [Feature]: upstream nightly rocm docker

| 字段 | 值 |
| --- | --- |
| Issue | [#36704](https://github.com/vllm-project/vllm/issues/36704) |
| 状态 | closed |
| 标签 | feature request;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: upstream nightly rocm docker

### Issue 正文摘录

### 🚀 The feature, motivation and pitch currently only cuda has nightly docker images . if rocm wants to be first class, it should have it too ### Alternatives build from source ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: upstream nightly rocm docker feature request;rocm ### 🚀 The feature, motivation and pitch currently only cuda has nightly docker images . if rocm wants to be first class, it should have it too ### Alternative...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: upstream nightly rocm docker feature request;rocm ### 🚀 The feature, motivation and pitch currently only cuda has nightly docker images . if rocm wants to be first class, it should have it too ### Alternative...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: upstream nightly rocm docker feature request;rocm ### 🚀 The feature, motivation and pitch currently only cuda has nightly docker images . if rocm wants to be first class, it should have it too ### Alternative...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting cuda build_error 🚀 The feature, mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
