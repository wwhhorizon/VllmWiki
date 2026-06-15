# vllm-project/vllm#17790: [Usage]: hermes_tool_parser fails with JSONDecodeError on Qwen3-32B inference via OpenAI-compatible endpoint (vLLM 0.8.5)

| 字段 | 值 |
| --- | --- |
| Issue | [#17790](https://github.com/vllm-project/vllm/issues/17790) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: hermes_tool_parser fails with JSONDecodeError on Qwen3-32B inference via OpenAI-compatible endpoint (vLLM 0.8.5)

### Issue 正文摘录

### Your current environment ```text Hello vLLM team, We are currently running the Qwen/Qwen3-32B model using vLLM v0.8.5 with full context length and tool-calling enabled via the Hermes parser, as documented. However, during inference via the OpenAI-compatible endpoint, we consistently encounter the following error from the Hermes tool parser: `ERROR [hermes_tool_parser.py:110] Error in extracting tool call from response. Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/tool_parsers/hermes_tool_parser.py", line 88, in extract_tool_calls json.loads(match[0] if match[0] else match[1]) File "/usr/lib/python3.12/json/__init__.py", line 346, in loads return _default_decoder.decode(s) File "/usr/lib/python3.12/json/decoder.py", line 341, in decode raise JSONDecodeError("Extra data", s, end) json.decoder.JSONDecodeError: Extra data: line 3 column 1 (char 527)` This seems to indicate that the Hermes parser is failing to extract and decode the tool call due to extra data in the string passed to json.loads. **Our deployment configuration includes the following relevant arguments:** `args: - --host - 0.0.0.0 - --port - "8000" - --model...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: hermes_tool_parser fails with JSONDecodeError on Qwen3-32B inference via OpenAI-compatible endpoint (vLLM 0.8.5) usage;stale ### Your current environment ```text Hello vLLM team, We are currently running the Qw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: hermes_tool_parser fails with JSONDecodeError on Qwen3-32B inference via OpenAI-compatible endpoint (vLLM 0.8.5) usage;stale ### Your current environment ```text Hello vLLM team, We are currently running the Qw...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: py", line 88, in extract_tool_calls json.loads(match[0] if match[0] else match[1]) File "/usr/lib/python3.12/json/__init__.py", line 346, in loads return _default_decoder.decode(s) File "/usr/lib/python3.12/json/decoder...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: SON blocks or additional text beyond the expected tool call. **Steps to reproduce:** Deploy Qwen/Qwen3-32B with the above config. Query the OpenAI-compatible endpoint with a tool-calling prompt. Observe the traceback fr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
