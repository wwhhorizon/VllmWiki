# vllm-project/vllm#9456: [Usage]: Regarding VLLM Structured Output Doubts

| 字段 | 值 |
| --- | --- |
| Issue | [#9456](https://github.com/vllm-project/vllm/issues/9456) |
| 状态 | closed |
| 标签 | structured-output;usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Regarding VLLM Structured Output Doubts

### Issue 正文摘录

### Your current environment ```text vllm 0.6.1.post2 vllm-flash-attn 2.6.1 ``` ### How would you like to use vllm The document describes structured output and additional parameters as follows: ```properties add_special_tokens: bool = Field( default=True, description=( "If true (the default), special tokens (e.g. BOS) will be added to " "the prompt."), ) response_format: Optional[ResponseFormat] = Field( default=None, description= ("Similar to chat completion, this parameter specifies the format of " "output. Only {'type': 'json_object'} or {'type': 'text' } is " "supported."), ) guided_json: Optional[Union[str, dict, BaseModel]] = Field( default=None, description="If specified, the output will follow the JSON schema.", ) guided_regex: Optional[str] = Field( default=None, description=( "If specified, the output will follow the regex pattern."), ) guided_choice: Optional[List[str]] = Field( default=None, description=( "If specified, the output will be exactly one of the choices."), ) guided_grammar: Optional[str] = Field( default=None, description=( "If specified, the output will follow the context free grammar."), ) guided_decoding_backend: Optional[str] = Field( default=None, des...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: . BOS) will be added to " "the prompt."), ) response_format: Optional[ResponseFormat] = Field( default=None, description= ("Similar to chat completion, this parameter specifies the format of " "output. Only {'type': 'js...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Regarding VLLM Structured Output Doubts structured-output;usage;stale ### Your current environment ```text vllm 0.6.1.post2 vllm-flash-attn 2.6.1 ``` ### How would you like to use vllm The document describes st...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: utput will follow the context free grammar."), ) guided_decoding_backend: Optional[str] = Field( default=None, description=( "If specified, will override the default guided decoding backend " "of the server for this spe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d output and additional parameters as follows: ```properties add_special_tokens: bool = Field( default=True, description=( "If true (the default), special tokens (e.g. BOS) will be added to " "the prompt."), ) response_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lt? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
