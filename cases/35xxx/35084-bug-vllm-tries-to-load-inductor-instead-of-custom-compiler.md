# vllm-project/vllm#35084: [Bug]: VLLM tries to load "inductor" instead of custom compiler

| 字段 | 值 |
| --- | --- |
| Issue | [#35084](https://github.com/vllm-project/vllm/issues/35084) |
| 状态 | open |
| 标签 | bug;torch.compile;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM tries to load "inductor" instead of custom compiler

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the option to use a custom compiler backend (e.g., `vllm server my/model --cc.backend=my.Compiler`) then within this method: https://github.com/vllm-project/vllm/blob/b1c4f0b26548d36fca304b298957e4791eafa09b/vllm/compilation/backends.py#L89 It checks if it's "inductor". If not, then this code tries to load the custom compiler: https://github.com/vllm-project/vllm/blob/b1c4f0b26548d36fca304b298957e4791eafa09b/vllm/compilation/backends.py#L112 However, `current_platform.get_compile_backend()` returns "inductor", which within `resolve_obj_by_qualname` becomes `"inductor".rsplit(".", 1)` and then fails within the assertion, that checks that it got split into 2 (package + class-name). I think instead of: ```python compiler = resolve_obj_by_qualname(current_platform.get_compile_backend())() ``` It should actually be: ```python compiler = resolve_obj_by_qualname(compilation_config.backend)() ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: VLLM tries to load "inductor" instead of custom compiler bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When using the option to use a custom compiler backend (e.g., `vllm server my/m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ### 🐛 Describe the bug When using the option to use a custom compiler backend (e.g., `vllm server my/model --cc.backend=my.Compiler`) then within this method: https://github.com/vllm-project/vllm/blob/b1c4f0b26548d36fca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: using the option to use a custom compiler backend (e.g., `vllm server my/model --cc.backend=my.Compiler`) then within this method: https://github.com/vllm-project/vllm/blob/b1c4f0b26548d36fca304b298957e4791eafa09b/vllm/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
