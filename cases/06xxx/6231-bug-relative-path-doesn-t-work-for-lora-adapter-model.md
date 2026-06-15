# vllm-project/vllm#6231: [Bug]: relative path doesn't work for Lora adapter model

| 字段 | 值 |
| --- | --- |
| Issue | [#6231](https://github.com/vllm-project/vllm/issues/6231) |
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

> [Bug]: relative path doesn't work for Lora adapter model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is a follow up issue of https://github.com/vllm-project/vllm/issues/6229. Relative path with `~` doesn't work for lora adapter path. We should fix it Relative Path - doesn't work ![image](https://github.com/vllm-project/vllm/assets/4739316/b63a54a3-2b2d-4ea5-bf86-891a06143f76) Absolute Path - works ![image](https://github.com/vllm-project/vllm/assets/4739316/fc5aa124-83c0-4df2-8372-35d3a52671bb) I will submit a PR to expands the path to make it work.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: bb) I will submit a PR to expands the path to make it work. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: relative path doesn't work for Lora adapter model bug ### Your current environment ### 🐛 Describe the bug This is a follow up issue of https://github.com/vllm-project/vllm/issues/6229. Relative path with `~` does...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
