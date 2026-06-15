# vllm-project/vllm#43713: [Bug]: qwen3_xml tool parser emits invalid JSON for multiple <function=...> blocks inside one <tool_call>

| 字段 | 值 |
| --- | --- |
| Issue | [#43713](https://github.com/vllm-project/vllm/issues/43713) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | quantization;sampling |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3_xml tool parser emits invalid JSON for multiple <function=...> blocks inside one <tool_call>

### Issue 正文摘录

### Your current environment vLLM nightly `bf610c2f56764e1b30bc6065f4ceace3d6e59036`, 2x RTX 3090 TP=2, served model `Qwen/Qwen3.6-27B` (AutoRound INT4 quant), `--tool-call-parser qwen3_xml --reasoning-parser qwen3 --enable-auto-tool-choice`, streaming requests. ### 🐛 Describe the bug `StreamingXMLToolCallParser` (`vllm/tool_parsers/qwen3xml_tool_parser.py`) emits invalid JSON in streamed `delta.tool_calls.function.arguments` when the model output contains multiple ` ` blocks inside a single ` `. Two interacting issues: 1. **Function-scoped state is not cleared on ` `.** After `_end_element("function")` emits the closing `}`, `self.parameters` and `self.current_function_name` are left populated. When a subsequent ` ` opens, `_start_element` calls `_auto_close_open_parameter_if_needed("function")` which sees `current_function_name` still set and re-fires `_end_element("function")`, re-emitting `}` from stale `self.parameters` → streamed args become `}}` (or `{}{}` when the prior function had no parameters). 2. **Multiple ` ` in the same ` ` are concatenated into one tool_call slot.** `tool_call_index` is only incremented at ` ` open, so all functions in one tool_call land in the sa...

## 现有链接修复摘要

#43714 [Bugfix] qwen3_xml: emit one OpenAI tool_call per <function=...>, fix duplicate close

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 3d6e59036`, 2x RTX 3090 TP=2, served model `Qwen/Qwen3.6-27B` (AutoRound INT4 quant), `--tool-call-parser qwen3_xml --reasoning-parser qwen3 --enable-auto-tool-choice`, streaming requests. ### 🐛 Describe the bug `Stream...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: environment vLLM nightly `bf610c2f56764e1b30bc6065f4ceace3d6e59036`, 2x RTX 3090 TP=2, served model `Qwen/Qwen3.6-27B` (AutoRound INT4 quant), `--tool-call-parser qwen3_xml --reasoning-parser qwen3 --enable-auto-tool-ch...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: g]: qwen3_xml tool parser emits invalid JSON for multiple <function=...> blocks inside one <tool_call> ### Your current environment vLLM nightly `bf610c2f56764e1b30bc6065f4ceace3d6e59036`, 2x RTX 3090 TP=2, served model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen3_xml tool parser emits invalid JSON for multiple <function=...> blocks inside one <tool_call> ### Your current environment vLLM nightly `bf610c2f56764e1b30bc6065f4ceace3d6e59036`, 2x RTX 3090 TP=2, served mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: qwen3_xml --reasoning-parser qwen3 --enable-auto-tool-choice`, streaming requests. ### 🐛 Describe the bug `StreamingXMLToolCallParser` (`vllm/tool_parsers/qwen3xml_tool_parser.py`) emits invalid JSON in streamed `delta....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43714](https://github.com/vllm-project/vllm/pull/43714) | closes_keyword | 0.95 | [Bugfix] qwen3_xml: emit one OpenAI tool_call per <function=...>, fix duplicate close | Fixes #43713. The `qwen3_xml` streaming tool-call parser emits invalid JSON in `delta.tool_calls.function.arguments` when the model output contains multiple `<function=...>` block |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
