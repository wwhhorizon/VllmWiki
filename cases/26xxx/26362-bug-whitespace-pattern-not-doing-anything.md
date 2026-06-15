# vllm-project/vllm#26362: [Bug]: whitespace_pattern not doing anything

| 字段 | 值 |
| --- | --- |
| Issue | [#26362](https://github.com/vllm-project/vllm/issues/26362) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: whitespace_pattern not doing anything

### Issue 正文摘录

### Your current environment Using ``` whitespace_pattern = r"[ ]?" StructuredOutputsParams( json=output_schema, whitespace_pattern=whitespace_pattern, ) ``` does not seem to have any effect at all. One would expect that this forces the white-space characters between the JSON structure (e.g. before/after curly brackets and `:`) would be limited to a single white-space. However, as the minimal example below shows, that is clearly not the case as it outputs: `b'{\n\n\n "sentiment":\n\n "positive"\n}'`. ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams from vllm.sampling_params import StructuredOutputsParams def main(): output_schema = { "type": "object", "properties": {"sentiment": {"type": "string", "enum": ["positive", "negative", "neutral"]}}, "required": ["sentiment"], } pipe = LLM(model="Qwen/Qwen2.5-0.5B-Instruct", max_model_len=1024) tokenizer = pipe.get_tokenizer() prompt = tokenizer.apply_chat_template( [{"role": "user", "content": "Is this text positive or negative? Text: I love this movie!"}], tokenize=False, add_generation_template=True ) structured_outputs = StructuredOutputsParams(json=output_schema, whitespace_pattern=r" ?") sampling_params = SamplingPar...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: iment":\n\n "positive"\n}'`. ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams from vllm.sampling_params import StructuredOutputsParams def main(): output_schema = { "type": "object", "properties": {"senti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ", "neutral"]}}, "required": ["sentiment"], } pipe = LLM(model="Qwen/Qwen2.5-0.5B-Instruct", max_model_len=1024) tokenizer = pipe.get_tokenizer() prompt = tokenizer.apply_chat_template( [{"role": "user", "content": "Is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: whitespace_pattern not doing anything bug;stale ### Your current environment Using ``` whitespace_pattern = r"[ ]?" StructuredOutputsParams( json=output_schema, whitespace_pattern=whitespace_pattern, ) ``` does n...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
