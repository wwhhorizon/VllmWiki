# vllm-project/vllm#38829: [Bug]: Unsharded model cannot be loaded

| 字段 | 值 |
| --- | --- |
| Issue | [#38829](https://github.com/vllm-project/vllm/issues/38829) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unsharded model cannot be loaded

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When the model is stored without sharding, it is stored as `model.safetensors` and it seems vllm doesn't find it and instead gives an error no model found. When storing it sharded as `model-00000-of-00001.safetensors` it does seem to work. This becomes an issue when merging (with LoRA) and storing small models that don't need sharding like Qwen/Qwen3-0.6B. These are by default saved as `model.safetensors`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: seem to work. This becomes an issue when merging (with LoRA) and storing small models that don't need sharding like Qwen/Qwen3-0.6B. These are by default saved as `model.safetensors`. ### Before submitting a new issue.....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unsharded model cannot be loaded bug ### Your current environment ### 🐛 Describe the bug When the model is stored without sharding, it is stored as `model.safetensors` and it seems vllm doesn't find it and instea...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Yo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
