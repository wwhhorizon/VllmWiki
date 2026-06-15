# vllm-project/vllm#25401: [Bug]: Chat template cannot be set for mistral models

| 字段 | 值 |
| --- | --- |
| Issue | [#25401](https://github.com/vllm-project/vllm/issues/25401) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Chat template cannot be set for mistral models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The [vllm docs for Mistral models](https://github.com/vllm-project/vllm/blob/3d2c56b7a958aa2c92f61424e828b1d3c3c933d4/docs/features/tool_calling.md?plain=1#L157) indicate that custom chat templates can be passed, using `--chat-template `: ``` Recommended flags: `--tool-call-parser mistral --chat-template examples/tool_chat_template_mistral_parallel.jinja` ``` However when starting a vLLM server with a mistral model, any specified chat template is [completely ignored](https://github.com/vllm-project/vllm/blob/175811e3b53f8f13eb3e8ac6aae02050f6e1412f/vllm/entrypoints/chat_utils.py#L409): ``` def resolve_mistral_chat_template( chat_template: Optional[str], **kwargs: Any, ) -> Optional[str]: if chat_template is not None: logger.warning_once( "'chat_template' cannot be overridden for mistral tokenizer." ) ``` This is inconsistent. Either the [docs](https://github.com/vllm-project/vllm/blob/3d2c56b7a958aa2c92f61424e828b1d3c3c933d4/docs/features/tool_calling.md?plain=1#L157) are misleading, or you should be able to set the chat template for mistral models. Am I misunderstanding something?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: a` ``` However when starting a vLLM server with a mistral model, any specified chat template is [completely ignored](https://github.com/vllm-project/vllm/blob/175811e3b53f8f13eb3e8ac6aae02050f6e1412f/vllm/entrypoints/ch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Chat template cannot be set for mistral models bug ### Your current environment ### 🐛 Describe the bug The [vllm docs for Mistral models](https://github.com/vllm-project/vllm/blob/3d2c56b7a958aa2c92f61424e828b1d3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
