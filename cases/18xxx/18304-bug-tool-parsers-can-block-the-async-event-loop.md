# vllm-project/vllm#18304: [Bug]: tool parsers can block the async event loop

| 字段 | 值 |
| --- | --- |
| Issue | [#18304](https://github.com/vllm-project/vllm/issues/18304) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tool parsers can block the async event loop

### Issue 正文摘录

### Your current environment I hit this in some testing of the berkeley function calling leaderboard with pythonic_tool_parser.py (ie `pythonic`) as my tool call parser with a Llama 4 Scout model on vLLM 0.8.5.post1. ### 🐛 Describe the bug Tool call parsers run within an async event loop. If a tool call parser takes a long time servicing a single request for whatever reason, it can block that event loop until the parser is finished executing. This ends up blocking the processing of other requests until the tool call parser finishes. This is fine if the tool call parsers are all written in such a way that they have a lower upper-bound of possible execution time. However, in my case, the pythonic tool parser had a very long (30+ minutes) execution time for a single request, due to a complex regular expression match that appears to trigger some catastrophic backtracking behavior on certain inputs. Here's a very contrived example that takes the regex from pythonic_tool_parser.py to demonstrate this: ``` import re test_string = """[foo(testingsomethingagain=True, a=, b=, c=, d=, e= [reschedule_event(event_identifier="your_event_id", new_datetime="next_friday_date_in_iso_format")] [resc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: within an async event loop. If a tool call parser takes a long time servicing a single request for whatever reason, it can block that event loop until the parser is finished executing. This ends up blocking the processi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: th pythonic_tool_parser.py (ie `pythonic`) as my tool call parser with a Llama 4 Scout model on vLLM 0.8.5.post1. ### 🐛 Describe the bug Tool call parsers run within an async event loop. If a tool call parser takes a lo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: tool parsers can block the async event loop bug;good first issue ### Your current environment I hit this in some testing of the berkeley function calling leaderboard with pythonic_tool_parser.py (ie `pythonic`) a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: c event loop. If a tool call parser takes a long time servicing a single request for whatever reason, it can block that event loop until the parser is finished executing. This ends up blocking the processing of other re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
