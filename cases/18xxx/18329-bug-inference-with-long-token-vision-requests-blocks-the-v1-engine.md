# vllm-project/vllm#18329: [Bug]: Inference with long-token vision requests blocks the V1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#18329](https://github.com/vllm-project/vllm/issues/18329) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inference with long-token vision requests blocks the V1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I try to start a api server with default args and `max-model-len=32768`. When sending small video requests, the server works well. But some big video requests stuck the server, for example a video extracted with a shape [60, 3, 504, 896]. The server says "Added request xxxxx", then hangs. From system tools I see RAM usage is increasing. Switch to V0 engine fixes the problem. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency;shape Your current envir...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t a api server with default args and `max-model-len=32768`. When sending small video requests, the server works well. But some big video requests stuck the server, for example a video extracted with a shape [60, 3, 504,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Inference with long-token vision requests blocks the V1 engine bug ### Your current environment ### 🐛 Describe the bug I try to start a api server with default args and `max-model-len=32768`. When sending small v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Describe the bug I try to start a api server with default args and `max-model-len=32768`. When sending small video requests, the server works well. But some big video requests stuck the server, for example a video extra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
