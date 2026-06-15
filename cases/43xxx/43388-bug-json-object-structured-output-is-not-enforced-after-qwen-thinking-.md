# vllm-project/vllm#43388: [Bug]: `json_object` structured output is not enforced after Qwen thinking because reasoning end token is missed with async scheduling + spec decode

| 字段 | 值 |
| --- | --- |
| Issue | [#43388](https://github.com/vllm-project/vllm/issues/43388) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `json_object` structured output is not enforced after Qwen thinking because reasoning end token is missed with async scheduling + spec decode

### Issue 正文摘录

### Your current environment ## Summary When using a Qwen-style reasoning model with: - `chat_template_kwargs.enable_thinking: true` - `response_format: {"type": "json_object"}` - default `structured_outputs_config.enable_in_reasoning=false` - async scheduling + speculative decoding the final response `content` may contain JSON wrapped in Markdown fences, for example: ```json { ... } instead of a raw JSON object. The issue appears to be that the reasoning end token is generated, but vLLM fails to detect it in StructuredOutputRequest.should_advance(). As a result, reasoning_ended remains False, should_fill_bitmask() keeps returning False, and the JSON grammar is never applied to the post-thinking content. ### 🐛 Describe the bug Expected Behavior After the model emits the reasoning end token, vLLM should detect that reasoning has ended and enable the configured json_object structured output constraint for the final answer. The response content should be constrained as a JSON object and should not freely emit Markdown code fences before the JSON object. Actual Behavior The reasoning end token is generated, but reasoning_ended never flips to True. Observed behavior: apply=True: 0 time...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: n thinking because reasoning end token is missed with async scheduling + spec decode bug ### Your current environment ## Summary When using a Qwen-style reasoning model with: - `chat_template_kwargs.enable_thinking: tru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: `json_object` structured output is not enforced after Qwen thinking because reasoning end token is missed with async scheduling + spec decode bug ### Your current environment ## Summary When using a Qwen-style re...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uctured_output/__init__.py, should_advance() detects reasoning end by slicing request.all_token_ids: start = num_computed_tokens - num_output_placeholders delta_ids = islice(all_token_ids, start, None) However, in async...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 069 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: son_object"}` - default `structured_outputs_config.enable_in_reasoning=false` - async scheduling + speculative decoding the final response `content` may contain JSON wrapped in Markdown fences, for example: ```json { .....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
