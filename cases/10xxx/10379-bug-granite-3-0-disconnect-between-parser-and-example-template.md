# vllm-project/vllm#10379: [Bug]: Granite 3.0 disconnect between parser and example template

| 字段 | 值 |
| --- | --- |
| Issue | [#10379](https://github.com/vllm-project/vllm/issues/10379) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Granite 3.0 disconnect between parser and example template

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using the example template found at `examples/tool_chat_template_granite.jinja` will produce a different format than the parser as implemented at `vllm/entrypoints/openai/tool_parsers/granite_tool_parser.py`. The template loops over the tool calling list, thus removing any `[` characters from the input, while the parse explicitly uses the `[` symbol to determine if a response should be parsed. This has the effect of requiring a different format on input than on output, making fine-tuning a model using this format very difficult. It appears to me the only change made from the original tokenizer as found at https://huggingface.co/ibm-granite/granite-3.0-2b-instruct/blob/main/tokenizer_config.json#L188 and the one found in this repo is this looping over the tools rather than representing the entire list at once. This difference is demonstrated by the following code snippet. ```python from vllm.entrypoints.openai.tool_parsers.granite_tool_parser import GraniteToolParser from vllm.entrypoints.chat_utils import apply_hf_chat_template from transformers import AutoTokenizer from vllm.entrypoints.openai...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: een parser and example template bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using the example template found at `examples/tool_chat_template_granite.jinja` will produce a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t, thus removing any `[` characters from the input, while the parse explicitly uses the `[` symbol to determine if a response should be parsed. This has the effect of requiring a different format on input than on output...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: AutoTokenizer from vllm.entrypoints.openai.protocol import ChatCompletionRequest tokenizer = AutoTokenizer.from_pretrained("ibm-granite/granite-3.0-2b-instruct") chat_template = open("./examples/tool_chat_template_grani...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
