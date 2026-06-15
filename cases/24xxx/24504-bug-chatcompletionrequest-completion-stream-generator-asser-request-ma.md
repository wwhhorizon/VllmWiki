# vllm-project/vllm#24504: [Bug]: ChatCompletionRequest completion_stream_generator asser request.max_tokens even though max_tokens is optional and deprecated

| 字段 | 值 |
| --- | --- |
| Issue | [#24504](https://github.com/vllm-project/vllm/issues/24504) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ChatCompletionRequest completion_stream_generator asser request.max_tokens even though max_tokens is optional and deprecated

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On ChatCompletionRequest max_tokens is optional and deprecated the default is None: ```python class ChatCompletionRequest(OpenAIBaseModel): # Ordered by official OpenAI API documentation # https://platform.openai.com/docs/api-reference/chat/create messages: list[ChatCompletionMessageParam] model: Optional[str] = None frequency_penalty: Optional[float] = 0.0 logit_bias: Optional[dict[str, float]] = None logprobs: Optional[bool] = False top_logprobs: Optional[int] = 0 max_tokens: Optional[int] = Field( default=None, deprecated= 'max_tokens is deprecated in favor of the max_completion_tokens field') ``` However in the [completion_stream_generator function](https://github.com/vllm-project/vllm/blob/6fb27881634d89c2e70e9e5fbad1b918c0d916cf/vllm/entrypoints/openai/serving_completion.py#L378) there is `assert request.max_tokens is not None`. Why is that? If it is optional shouldn't it be possible to pass request.max_tokens = None? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ython class ChatCompletionRequest(OpenAIBaseModel): # Ordered by official OpenAI API documentation # https://platform.openai.com/docs/api-reference/chat/create messages: list[ChatCompletionMessageParam] model: Optional[...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ne? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: bias: Optional[dict[str, float]] = None logprobs: Optional[bool] = False top_logprobs: Optional[int] = 0 max_tokens: Optional[int] = Field( default=None, deprecated= 'max_tokens is deprecated in favor of the max_complet...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ted the default is None: ```python class ChatCompletionRequest(OpenAIBaseModel): # Ordered by official OpenAI API documentation # https://platform.openai.com/docs/api-reference/chat/create messages: list[ChatCompletionM...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
