# vllm-project/vllm#20533: [Bug]: VLLM doesn't work on 5090s

| 字段 | 值 |
| --- | --- |
| Issue | [#20533](https://github.com/vllm-project/vllm/issues/20533) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM doesn't work on 5090s

### Issue 正文摘录

### Your current environment I'm sorry if this is duplicating information or bugs out there, but I'm having a hard time figuring out if VLLM has been updated to work with 5090s or now. I've been trying to get OCRFlux working on my 5090 for three days now and keep going through hurdle after hurdle. I see posts that claim the 5090 now works, but that doesn't match my experience. I also see posts that show a long roadmap of fixes, which implies a long road to things being supported. ### 🐛 Describe the bug CUDA Errors, several hour attempts to build locally that just fail, misery, etc. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: upported. ### 🐛 Describe the bug CUDA Errors, several hour attempts to build locally that just fail, misery, etc. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: implies a long road to things being supported. ### 🐛 Describe the bug CUDA Errors, several hour attempts to build locally that just fail, misery, etc. ### Before submitting a new issue... - [x] Make sure you already sea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g;stale ### Your current environment I'm sorry if this is duplicating information or bugs out there, but I'm having a hard time figuring out if VLLM has been updated to work with 5090s or now. I've been trying to get OC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: VLLM doesn't work on 5090s bug;stale ### Your current environment I'm sorry if this is duplicating information or bugs out there, but I'm having a hard time figuring out if VLLM has been updated to work with 5090...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
