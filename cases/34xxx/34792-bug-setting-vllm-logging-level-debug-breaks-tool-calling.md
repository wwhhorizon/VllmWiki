# vllm-project/vllm#34792: [Bug]: setting VLLM_LOGGING_LEVEL=debug breaks tool calling

| 字段 | 值 |
| --- | --- |
| Issue | [#34792](https://github.com/vllm-project/vllm/issues/34792) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;fp8;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: setting VLLM_LOGGING_LEVEL=debug breaks tool calling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While testing the fix for tool call failures (https://github.com/vllm-project/vllm/pull/34745), I encountered this issue: Starting vllm with `VLLM_LOGGING_LEVEL=debug` with a mistral model (e.g. using `mistralai/Ministral-3-14B-Instruct-2512`) in this case and tool calling enabled (`--enable-auto-tool-choice --tool-call-parser=mistral`), tool calls fail with the following traceback: The source for this are these two lines: https://github.com/vllm-project/vllm/blob/2d5be1dd5ce2e44dfea53ea03ff61143da5137eb/vllm/entrypoints/anthropic/serving.py#L241-L242 The root cause is that the `tool_calls` attribute in pydantic models is set to `Iterable`, causing a serialization (`.model_dump_json()`) to consume its values. Here's an example of its usage in `ConversationMessage`: https://github.com/vllm-project/vllm/blob/c50e105a8843907c8c89f95ee29b8cc5e3935bae/vllm/entrypoints/chat_utils.py#L322 ## Conclusion I think this issue is particularly problematic because it can cause any pydantic models using `Iterable` to be inadvertently "consumed" by either debug logging or any other operations, causing some values to be missing from the dumped mod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r (in this case tool calls serialization) performance attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory cache;cuda;fp8;quantization;sampling build_erro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory cache;cuda;fp8;quantization;sampling build_error;crash;slowdown dtype;env_dependency;shape Your curre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: orting;model_support;quantization;sampling_logits;scheduler_memory cache;cuda;fp8;quantization;sampling build_error;crash;slowdown dtype;env_dependency;shape Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: his issue: Starting vllm with `VLLM_LOGGING_LEVEL=debug` with a mistral model (e.g. using `mistralai/Ministral-3-14B-Instruct-2512`) in this case and tool calling enabled (`--enable-auto-tool-choice --tool-call-parser=m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory cache;cuda;fp8;quantization;sampling build_error;crash;slowdown dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
