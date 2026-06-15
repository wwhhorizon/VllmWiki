# vllm-project/vllm#15607: [Bug]: Failed to run deepseek v2 lite model with tp = 4

| 字段 | 值 |
| --- | --- |
| Issue | [#15607](https://github.com/vllm-project/vllm/issues/15607) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to run deepseek v2 lite model with tp = 4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run the following code: ```bash vllm serve deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct --tensor-parallel-size 4 --trust-remote-code ``` **The code works well with tp size = 8.** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency;shape Your current...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency;shape Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Failed to run deepseek v2 lite model with tp = 4 bug ### Your current environment ### 🐛 Describe the bug Run the following code: ```bash vllm serve deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct --tensor-parallel-si...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
