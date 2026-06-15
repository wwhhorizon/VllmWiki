# vllm-project/vllm#39583: [RFC]: Migrate bitsandbytes and GGUF quantization support to OOT plugin

| 字段 | 值 |
| --- | --- |
| Issue | [#39583](https://github.com/vllm-project/vllm/issues/39583) |
| 状态 | open |
| 标签 | RFC;quantization |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe;operator;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Migrate bitsandbytes and GGUF quantization support to OOT plugin

### Issue 正文摘录

### Motivation. bitsandbytes and GGUF are two quantization/format backends in vLLM that see very low usage relative to the maintenance burden they impose (roughly 0.5% and 0.1% respectively from what I can tell). Both predate the current weight loading architecture (`weight_loader_v2`) and have not been migrated to it. They inject conditional branches throughout the critical weight-loading path in shared code (`linear.py`, `fused_moe/layer.py`, `vocab_parallel_embedding.py`) in ways that make the codebase harder to maintain and refactor. In addition, performance is not great when using these methods, with users often citing running GGUF models with llamacpp to be faster due to different priorities wrt bs=1 performance on consumer GPUs. This RFC proposes deprecating both backends and eventually removing them, to simplify the core weight loading infrastructure and unblock further cleanup. If we were to choose one over the other, I think removing GGUF would take priority due to the greater usage of BNB. Another option is to propose moving these methods to be OOT quantization plugins, but I doubt the feasibility due to the current need to modify internal structures in vLLM. ## Summary...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: quantization ### Motivation. bitsandbytes and GGUF are two quantization/format backends in vLLM that see very low usage relative to the maintenance burden they impose (roughly 0.5% and 0.1% respectively from what I can...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ion, performance is not great when using these methods, with users often citing running GGUF models with llamacpp to be faster due to different priorities wrt bs=1 performance on consumer GPUs. This RFC proposes depreca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ctively from what I can tell). Both predate the current weight loading architecture (`weight_loader_v2`) and have not been migrated to it. They inject conditional branches throughout the critical weight-loading path in...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: removing them, to simplify the core weight loading infrastructure and unblock further cleanup. If we were to choose one over the other, I think removing GGUF would take priority due to the greater usage of BNB. Another...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: out the critical weight-loading path in shared code (`linear.py`, `fused_moe/layer.py`, `vocab_parallel_embedding.py`) in ways that make the codebase harder to maintain and refactor. In addition, performance is not grea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
