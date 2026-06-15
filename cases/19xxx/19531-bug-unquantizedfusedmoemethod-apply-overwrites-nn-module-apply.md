# vllm-project/vllm#19531: [Bug]:`UnquantizedFusedMoeMethod.apply` overwrites `nn.Module.apply`

| 字段 | 值 |
| --- | --- |
| Issue | [#19531](https://github.com/vllm-project/vllm/issues/19531) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;moe |
| 子分类 | env_compat |
| Operator 关键词 | operator;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:`UnquantizedFusedMoeMethod.apply` overwrites `nn.Module.apply`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `nn.Module.apply` is a method to recursively apply a transformation. `CustomOp` like [`UnquantizedFusedMoeMethod`](https://github.com/vllm-project/vllm/blob/2e090bd5df974949651ad439517e0da4e981b508/vllm/model_executor/layers/fused_moe/layer.py#L549) overwrites this method to be a completely different one. This could causing an NVIDIA ModelOpt's WIP feature for vLLM to fail. I suggest vLLM should consider renaming `apply()` method to other name to avoid conflicting with pytorch's originally designed method. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;model_support;moe operator;triton env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cribe the bug `nn.Module.apply` is a method to recursively apply a transformation. `CustomOp` like [`UnquantizedFusedMoeMethod`](https://github.com/vllm-project/vllm/blob/2e090bd5df974949651ad439517e0da4e981b508/vllm/mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: quently asked questions. development ci_build;model_support;moe operator;triton env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]:`UnquantizedFusedMoeMethod.apply` overwrites `nn.Module.apply` bug;stale ### Your current environment ### 🐛 Describe the bug `nn.Module.apply` is a method to recursively apply a transformation. `CustomOp` like [`U...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: od. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
