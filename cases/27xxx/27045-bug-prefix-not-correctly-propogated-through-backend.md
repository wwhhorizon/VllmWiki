# vllm-project/vllm#27045: [Bug]: `Prefix` not correctly propogated through Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#27045](https://github.com/vllm-project/vllm/issues/27045) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `Prefix` not correctly propogated through Backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While investigating an error with `set_model_tag`, I tried to use `prefix` around torch.compile to have modules written to different caching directories However, `prefix` always is set to `backbone` in https://github.com/vllm-project/vllm/blob/7bb736d00e81c6cd893007323641dd974d921715/vllm/compilation/backends.py#L520 This is because looking at callsites of `VllmBackend`, outside of `deserialize_compile_artificats`, prefix is not passed We should modify the callsites in order to forward `prefix` so that when initializing a model from cold start we respect this setting https://github.com/vllm-project/vllm/blob/7bb736d00e81c6cd893007323641dd974d921715/vllm/config/compilation.py#L664 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ting an error with `set_model_tag`, I tried to use `prefix` around torch.compile to have modules written to different caching directories However, `prefix` always is set to `backbone` in https://github.com/vllm-project/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: `Prefix` not correctly propogated through Backend bug;stale ### Your current environment ### 🐛 Describe the bug While investigating an error with `set_model_tag`, I tried to use `prefix` around torch.compile to h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 664 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nment ### 🐛 Describe the bug While investigating an error with `set_model_tag`, I tried to use `prefix` around torch.compile to have modules written to different caching directories However, `prefix` always is set to `b...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: er lots of frequently asked questions. correctness ci_build;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environme...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
