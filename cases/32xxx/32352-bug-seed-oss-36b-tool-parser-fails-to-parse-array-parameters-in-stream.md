# vllm-project/vllm#32352: [Bug]: Seed OSS 36B Tool Parser Fails to Parse Array Parameters in Streaming Mode

| 字段 | 值 |
| --- | --- |
| Issue | [#32352](https://github.com/vllm-project/vllm/issues/32352) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Seed OSS 36B Tool Parser Fails to Parse Array Parameters in Streaming Mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Overview seed_oss_tool_parser.py does not perform type conversions in streaming mode, and therefore fails to parse array/json/dict parameters. This was made apparent after Roo Code deprecated their XML tool calling feature and now requires native tool calling for all models, which does not work correctly with Seed. # Example Seed outputs the following when calling the read_file tool from Roo Code: ```xml [{ "path": "main.py" }] ``` VLLM initiates the tool call but fails to include the parsed `read_file` parameter: ``` [Tool] Error: The tool execution failed with the following error: Missing value for required parameter 'args (containing valid file paths)'. Please retry with complete response. ... ``` The same request work correctly in non-streaming mode. # Cause The parser relies on the `convert_param_value()` function to convert and parse json-type objects: https://github.com/vllm-project/vllm/blob/8471b27df97c3eb79f891802fc0e858f8f7ac6a0/vllm/tool_parsers/seed_oss_tool_parser.py#L209-L231 However, this is nested as a subfunction of `_parse_xml_function_call()`, so `convert_param_value()` cannot be called directly from streami...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: be the bug # Overview seed_oss_tool_parser.py does not perform type conversions in streaming mode, and therefore fails to parse array/json/dict parameters. This was made apparent after Roo Code deprecated their XML tool...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ir XML tool calling feature and now requires native tool calling for all models, which does not work correctly with Seed. # Example Seed outputs the following when calling the read_file tool from Roo Code: ```xml [{ "pa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: SS 36B Tool Parser Fails to Parse Array Parameters in Streaming Mode bug;stale ### Your current environment ### 🐛 Describe the bug # Overview seed_oss_tool_parser.py does not perform type conversions in streaming mode,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
