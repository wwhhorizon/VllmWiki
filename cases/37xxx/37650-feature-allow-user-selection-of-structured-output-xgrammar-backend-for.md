# vllm-project/vllm#37650: [Feature]: Allow user selection of structured output (xgrammar) backend for bitmask application

| 字段 | 值 |
| --- | --- |
| Issue | [#37650](https://github.com/vllm-project/vllm/issues/37650) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Allow user selection of structured output (xgrammar) backend for bitmask application

### Issue 正文摘录

### The feature, motivation and pitch ## Feature, Motivation, and Pitch ### Background In vLLM, when structured output tasks are enabled (such as using a JSON schema, grammar, or regex constraint), the backend used to apply the structured output token bitmask is an important source of both correctness and performance. The function `xgr.apply_token_bitmask_inplace` from xgrammar supports different backends (e.g., "auto", "cpu", "cuda", "triton", "torch_compile", "torch_native"), but currently in vLLM the backend is hard-coded as "auto" and not exposed to the user. ### Motivation * Users may want to explicitly choose a backend to maximize performance for their hardware or to debug incompatibility issues, e.g., forcing `cpu` or `cuda` mode if they hit issues with the triton kernel or auto selection. * Exposing this option provides more transparency and flexibility for power users. ### Pitch * Allow structured output backend selection for bitmask application by exposing a command-line flag, config file option, or Python API parameter (e.g., `--structured-outputs-config.bitmask_backend` or `StructuredOutputsConfig(bitmask_backend=...)`). * This value should be plumbed so it is finally...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nt), the backend used to apply the structured output token bitmask is an important source of both correctness and performance. The function `xgr.apply_token_bitmask_inplace` from xgrammar supports different backends (e....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Allow user selection of structured output (xgrammar) backend for bitmask application feature request ### The feature, motivation and pitch ## Feature, Motivation, and Pitch ### Background In vLLM, when struct...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nplace` from xgrammar supports different backends (e.g., "auto", "cpu", "cuda", "triton", "torch_compile", "torch_native"), but currently in vLLM the backend is hard-coded as "auto" and not exposed to the user. ### Moti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ckend selection for bitmask application by exposing a command-line flag, config file option, or Python API parameter (e.g., `--structured-outputs-config.bitmask_backend` or `StructuredOutputsConfig(bitmask_backend=...)`...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: of structured output (xgrammar) backend for bitmask application feature request ### The feature, motivation and pitch ## Feature, Motivation, and Pitch ### Background In vLLM, when structured output tasks are enabled (s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
