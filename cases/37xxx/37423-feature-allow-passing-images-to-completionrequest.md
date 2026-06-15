# vllm-project/vllm#37423: [Feature]: Allow passing `images` to CompletionRequest

| 字段 | 值 |
| --- | --- |
| Issue | [#37423](https://github.com/vllm-project/vllm/issues/37423) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow passing `images` to CompletionRequest

### Issue 正文摘录

### 🚀 The feature, motivation and pitch At the moment it is not possible to evaluate pretrained multi-modal models such as: https://huggingface.co/Qwen/Qwen3.5-9B-Base on tasks that include text as well as images because it is not possible to pass images to the CompletionRequest class: ```py class CompletionRequest(OpenAIBaseModel): # Ordered by official OpenAI API documentation # https://platform.openai.com/docs/api-reference/completions/create model: str | None = None prompt: ( list[Annotated[int, Field(ge=0)]] | list[list[Annotated[int, Field(ge=0)]]] | str | list[str] | None ) = None ``` See here: https://github.com/vllm-project/vllm/blob/17c47fb8691f2efd7948659952c44ef167462534/vllm/entrypoints/openai/completion/protocol.py#L42-L52 This significantly limits the usage of pretrained models in vLLM. **Proposal**: Let's add: `images: np.ndarray | None = None` to the `CompletionRequest` and in case this object is not None we validate that `prompt` has to be `list[int]` meaning the prompt already has to be pre-processed by the tokenizer. This way we could add this feature with minimal changes -> no need for extra pre-processing, we can just pass the images directly down into the mo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tch At the moment it is not possible to evaluate pretrained multi-modal models such as: https://huggingface.co/Qwen/Qwen3.5-9B-Base on tasks that include text as well as images because it is not possible to pass images...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the model definitions. ```py class _NDArrayPydanticAnnotation: @classmethod def __get_pydantic_core_schema__( cls, _source_type: Any, _handler: GetCoreSchemaHandler, ) -> core_schema.CoreSchema: from_serialized_schema =...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 🚀 The feature, motivation and pitch At the moment it is not possible to evaluate pretrained multi-modal models such as: https://huggingface.co/Qwen/Qwen3.5-9B-Base on tasks that include text as well as images because it...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s: ```py class CompletionRequest(OpenAIBaseModel): # Ordered by official OpenAI API documentation # https://platform.openai.com/docs/api-reference/completions/create model: str | None = None prompt: ( list[Annotated[int...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Allow passing `images` to CompletionRequest feature request ### 🚀 The feature, motivation and pitch At the moment it is not possible to evaluate pretrained multi-modal models such as: https://huggingface.co/Q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
