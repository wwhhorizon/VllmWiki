# vllm-project/vllm#25253: [Bug]: 500 internal error with mistral reasoning parser and tool choice required

| 字段 | 值 |
| --- | --- |
| Issue | [#25253](https://github.com/vllm-project/vllm/issues/25253) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 500 internal error with mistral reasoning parser and tool choice required

### Issue 正文摘录

When I prompt with `tool_choice=required` (OpenAI chat completions endpoint) with `--reasoning-parser mistral` I get 500 Internal Error. There is no stack or explanation but I could nailed it down to this because without the parser or with `tool_choice=auto` it works. The model I am using is `mistralai/Magistral-Small-2509` but it reproduces with the previous versions as well. ### Your current environment ### 🐛 Describe the bug When I prompt with `tool_choice=required` (OpenAI chat completions endpoint) with `--reasoning-parser mistral` I get 500 Internal Error. There is no stack or explanation but I could nailed it down to this because without the parser or with `tool_choice=auto` it works. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: is `mistralai/Magistral-Small-2509` but it reproduces with the previous versions as well. ### Your current environment ### 🐛 Describe the bug When I prompt with `tool_choice=required` (OpenAI chat completions endpoint)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tool_choice=auto` it works. The model I am using is `mistralai/Magistral-Small-2509` but it reproduces with the previous versions as well. ### Your current environment ### 🐛 Describe the bug When I prompt with `tool_cho...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: opment ci_build;distributed_parallel;hardware_porting;model_support cuda;triton build_error env_dependency When I prompt with `tool_choice=required` (OpenAI chat completions endpoint) with `--reasoning-parser mistral` I...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t works. The model I am using is `mistralai/Magistral-Small-2509` but it reproduces with the previous versions as well. ### Your current environment ### 🐛 Describe the bug When I prompt with `tool_choice=required` (Open...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: this because without the parser or with `tool_choice=auto` it works. The model I am using is `mistralai/Magistral-Small-2509` but it reproduces with the previous versions as well. ### Your current environment ### 🐛 Desc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
