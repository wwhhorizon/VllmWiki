# vllm-project/vllm#32713: [RFC]: Unified Parser for reasoning, tool calling

| 字段 | 值 |
| --- | --- |
| Issue | [#32713](https://github.com/vllm-project/vllm/issues/32713) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Unified Parser for reasoning, tool calling

### Issue 正文摘录

### Motivation. LLMs fundamentally are token-in, token-out models. For them to be useful, we need to parse from text into tokens ("tokenization") and parse from tokens into useful responses ("detokenization", reasoning parsing, tool calling parsing). Due to legacy reasons, vLLM has separate entrypoints for reasoning parser / tool calling parser, as the need for a reasoning parser did not arise until deepseek R1 *Current State of the World* - For input tokenization, we use chat template jinja, which is defined from the model spec. - OpenAI harmony is separate - Deepseek v3.2 also has a special tool parser - For detokenization / responsesAPI parsing, we have - tokenization from the model spec, called via _preprocess_chat() - Abs_reasoning_parsers - Abstract_tool_parser OpenAI Harmony is a special case, in which tokenization / detokenization happen separately. - For tokenization, we use _make_request_with_harmony - get_encoding().render_conversation_for_completion goes from message -> tokens - For detokenization -From token IDs -> OpenAI harmony messages, [context.py](http://context.py/) HarmonyContext runs self.parser.process() - For openAI harmony messages -> responsesAPI items, _m...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: calling RFC ### Motivation. LLMs fundamentally are token-in, token-out models. For them to be useful, we need to parse from text into tokens ("tokenization") and parse from tokens into useful responses ("detokenization"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: del spec. - OpenAI harmony is separate - Deepseek v3.2 also has a special tool parser - For detokenization / responsesAPI parsing, we have - tokenization from the model spec, called via _preprocess_chat() - Abs_reasonin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ion / detokenization happen separately. - For tokenization, we use _make_request_with_harmony - get_encoding().render_conversation_for_completion goes from message -> tokens - For detokenization -From token IDs -> OpenA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. #### Updates Edit Feb 17: see comments below, this RFC will only address decode parsi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
