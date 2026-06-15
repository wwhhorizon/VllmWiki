# vllm-project/vllm#28800: [Bug]: Build vllm on Apple silicon: libc++abi error

| 字段 | 值 |
| --- | --- |
| Issue | [#28800](https://github.com/vllm-project/vllm/issues/28800) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Build vllm on Apple silicon: libc++abi error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After followed the vllm build instruction on official page, and successfully built the dependency. And tried to run gemma3-4b model with vllm-cli (easy to setup vllm) on apple silicon. then the terminal show below error: Is there anyone facing the issue like me? --- [Full crash log](https://logpasta.com/paste/064a192c-5593-4a3b-b348-79b64ef3a21a) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Build vllm on Apple silicon: libc++abi error bug;stale ### Your current environment ### 🐛 Describe the bug After followed the vllm build instruction on official page, and successfully built the dependency. And tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1a) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: official page, and successfully built the dependency. And tried to run gemma3-4b model with vllm-cli (easy to setup vllm) on apple silicon. then the terminal show below error: Is there anyone facing the issue like me? -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: official page, and successfully built the dependency. And tried to run gemma3-4b model with vllm-cli (easy to setup vllm) on apple silicon. then the terminal show below error: Is there anyone facing the issue like me? -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Build vllm on Apple silicon: libc++abi error bug;stale ### Your current environment ### 🐛 Describe the bug After followed the vllm build instruction on official page, and successfully built the dependency. And tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
