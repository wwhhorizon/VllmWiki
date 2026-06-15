# vllm-project/vllm#19025: [Bug]: Dual a6000 pros not working. Arch 120.

| 字段 | 值 |
| --- | --- |
| Issue | [#19025](https://github.com/vllm-project/vllm/issues/19025) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dual a6000 pros not working. Arch 120.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running any model in with -tp 2 I get illegal memory access issues. I have tried a mixture of every possible combination: -kernel version -cuda version 12.8+12.9 -different drivers -nccl versions -compiled from source for all combinations and tried docker. -works in windows WSL but not ubuntu 22.04 I understand a lot of people have been experiencing similar issues but I can't tell if its the same error. Just to be sure I have gone out and rented two a6000 pros on runpod.io. I used their 12.8 template and got the same error there... so I assume it's not my hardware since it does not work with enterprise grade infra. I cannot pin point this bug and initially thought that nccl is to blame. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: issues. I have tried a mixture of every possible combination: -kernel version -cuda version 12.8+12.9 -different drivers -nccl versions -compiled from source for all combinations and tried docker. -works in windows WSL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Dual a6000 pros not working. Arch 120. bug ### Your current environment ### 🐛 Describe the bug When running any model in with -tp 2 I get illegal memory access issues. I have tried a mixture of every possible com...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ## Your current environment ### 🐛 Describe the bug When running any model in with -tp 2 I get illegal memory access issues. I have tried a mixture of every possible combination: -kernel version -cuda version 12.8+12.9 -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
