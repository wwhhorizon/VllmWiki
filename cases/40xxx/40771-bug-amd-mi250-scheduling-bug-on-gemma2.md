# vllm-project/vllm#40771: [Bug]: AMD MI250 scheduling bug on Gemma2

| 字段 | 值 |
| --- | --- |
| Issue | [#40771](https://github.com/vllm-project/vllm/issues/40771) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AMD MI250 scheduling bug on Gemma2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug AMD MI250 scheduling bug on Gemma2 This is the issue to report per the wordaound on this pr: https://github.com/vllm-project/vllm/pull/40745 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding cuda;kernel;operator;quantization;triton b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: AMD MI250 scheduling bug on Gemma2 bug;rocm ### Your current environment ### 🐛 Describe the bug AMD MI250 scheduling bug on Gemma2 This is the issue to report per the wordaound on this pr: https://github.com/vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: AMD MI250 scheduling bug on Gemma2 bug;rocm ### Your current environment ### 🐛 Describe the bug AMD MI250 scheduling bug on Gemma2 This is the issue to report per the wordaound on this pr: https://github.com/vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: opment ci_build;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding cuda;kernel;operator;quantization;triton build_error env_dependency Your current environment
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;scheduler_memory;speculative_decoding cuda;kernel;operator;quantization;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
