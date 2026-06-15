# vllm-project/vllm#28264: [Bug]: Precompiled nightly wheel depends on non-existent xformers version

| 字段 | 值 |
| --- | --- |
| Issue | [#28264](https://github.com/vllm-project/vllm/issues/28264) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Precompiled nightly wheel depends on non-existent xformers version

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug $ VLLM_USE_PRECOMPILED=1 uv pip install --editable . × No solution found when resolving dependencies: ╰─▶ Because there is no version of xformers{platform_machine == 'x86_64' and sys_platform == 'linux'}==0.0.33+5d4b92a5.d20251029 and vllm==0.11.1rc4.dev299+g8816e375d.d20251107.precompiled depends on xformers{platform_machine == 'x86_64' and sys_platform == 'linux'}==0.0.33+5d4b92a5.d20251029, we can conclude that vllm==0.11.1rc4.dev299+g8816e375d.d20251107.precompiled cannot be used. And because only vllm==0.11.1rc4.dev299+g8816e375d.d20251107.precompiled is available and you require vllm, we can conclude that your requirements are unsatisfiable. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Precompiled nightly wheel depends on non-existent xformers version bug ### Your current environment ### 🐛 Describe the bug $ VLLM_USE_PRECOMPILED=1 uv pip install --editable . × No solution found when resolving d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
