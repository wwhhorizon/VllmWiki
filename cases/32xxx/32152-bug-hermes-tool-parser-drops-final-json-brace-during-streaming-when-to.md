# vllm-project/vllm#32152: [Bug]: hermes_tool_parser drops final JSON brace during streaming when tokens are chunked (e.g., MTP enabled)

| 字段 | 值 |
| --- | --- |
| Issue | [#32152](https://github.com/vllm-project/vllm/issues/32152) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: hermes_tool_parser drops final JSON brace during streaming when tokens are chunked (e.g., MTP enabled)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The Hermes2ProToolParser (in vllm/tool_parsers/hermes_tool_parser.py) fails to stream the final characters of tool call arguments when the model generates the end of the JSON and the closing tag within the same streaming chunk. This results in truncated tool calls (e.g., missing the final `}` ) at the client side. This is particularly reproducible when using: Multi-Token Prediction (MTP): Which groups the final JSON tokens and the tool call closing tag into a single predicted block. **Context:** In my environment, I am using the `LGAI-EXAONE/K-EXAONE-236B-A23B` model. I've found that when Multi-Token Prediction (MTP) is enabled, it consistently triggers the issue where the final `}` of the tool call arguments is truncated during streaming. The bug is as follows: In the picture, there should be `}` between red double quotes and single quote, but it's missing. I suspect the bug stems from here: L274 of hermes_tool_parser.py ``` elif ( cur_tool_start_count == cur_tool_end_count and cur_tool_end_count >= prev_tool_end_count ): ... if '"}' not in delta_text: return None ``` If the model emits a chunk like } , vLLM first truncates the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: missing the final `}` ) at the client side. This is particularly reproducible when using: Multi-Token Prediction (MTP): Which groups the final JSON tokens and the tool call closing tag into a single predicted block. **C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: et. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: final JSON tokens and the tool call closing tag into a single predicted block. **Context:** In my environment, I am using the `LGAI-EXAONE/K-EXAONE-236B-A23B` model. I've found that when Multi-Token Prediction (MTP) is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: N brace during streaming when tokens are chunked (e.g., MTP enabled) bug;stale ### Your current environment ### 🐛 Describe the bug The Hermes2ProToolParser (in vllm/tool_parsers/hermes_tool_parser.py) fails to stream th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
