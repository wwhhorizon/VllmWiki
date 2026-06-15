# vllm-project/vllm#21303: [Bug]: Mistral Tool Parser Crashes with Empty JSONDecodeError for Mistral Small 3.2 24B FP8 Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#21303](https://github.com/vllm-project/vllm/issues/21303) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral Tool Parser Crashes with Empty JSONDecodeError for Mistral Small 3.2 24B FP8 Instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The Mistral tool parser crashes with a `JSONDecodeError` when encountering empty or whitespace-only content after the bot token during streaming. This occurs when the model has only generated the `[TOOL_CALLS]` token but no actual tool call content yet. We use the new mistral model https://huggingface.co/RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-FP8 with this quantization on two NVIDIA L40-S. Our customers use tool calling with our API endpoint and mistral parser, but we suppose we received this error by a customer using n8n to create tool calling requests with their online tool. Of course, all parsers and tool calling templates are set to `mistral`. **Error Details:** ``` ERROR 07-21 01:38:31 [mistral_tool_parser.py:365] Error trying to handle streaming tool call. ERROR 07-21 01:38:31 [mistral_tool_parser.py:365] Traceback (most recent call last): ERROR 07-21 01:38:31 [mistral_tool_parser.py:365] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py", line 220, in extract_tool_calls_streaming ERROR 07-21 01:38:31 [mistral_tool_parser.py:365] tool_call_arr: list[dict] = parti...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: -only content after the bot token during streaming. This occurs when the model has only generated the `[TOOL_CALLS]` token but no actual tool call content yet. We use the new mistral model https://huggingface.co/RedHatA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Mistral Tool Parser Crashes with Empty JSONDecodeError for Mistral Small 3.2 24B FP8 Instruct bug;stale ### Your current environment ### 🐛 Describe the bug The Mistral tool parser crashes with a `JSONDecodeError`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;quan...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Tool Parser Crashes with Empty JSONDecodeError for Mistral Small 3.2 24B FP8 Instruct bug;stale ### Your current environment ### 🐛 Describe the bug The Mistral tool parser crashes with a `JSONDecodeError` when encounter...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Bug]: Mistral Tool Parser Crashes with Empty JSONDecodeError for Mistral Small 3.2 24B FP8 Instruct bug;stale ### Your current environment ### 🐛 Describe the bug The Mistral tool parser crashes with a `JSONDecodeError`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
