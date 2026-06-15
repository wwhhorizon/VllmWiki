# vllm-project/vllm#34225: [Bug]: `maybe_serialize_tool_calls()` fails to verify the `tool_calls` type

| 字段 | 值 |
| --- | --- |
| Issue | [#34225](https://github.com/vllm-project/vllm/issues/34225) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `maybe_serialize_tool_calls()` fails to verify the `tool_calls` type

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description `vllm/tokenizers/mistral.py.maybe_serialize_tool_calls()#67` does not verify whether `request.tool_calls` is of expected format: ```python 67 tool_calls_validator = message.get("tool_calls", ().__iter__()) 68 validated_tool_calls = [] 69 while True: 70 try: 71 tool_call = next(tool_calls_validator) # type: ignore ``` Line 71 executes `next()` on something that is not necessarily an iterable, resulting in an exception that is returned in HTTP response. ## Reproduction Include malformed `tool_calls` in one of the messages: ``` POST /v1/chat/completions HTTP/1.1 ... { "messages":[ ... { "role":"user", "content":"...", "tool_calls":"should_be_serialized_object_but_its_str" } } HTTP/1.1 400 Bad Request date: Tue, 10 Feb 2026 10:58:00 GMT server: uvicorn content-length: 284 content-type: application/json { "error":{ "message":"1 validation error for ValidatorIterator\n0\n Input should be a valid dictionary [type=dict_type, input_value='s', input_type=str]\n For further information visit https://errors.pydantic.dev/2.12/v/dict_type","type":"BadRequestError","param":null,"code":400 } } ``` ### Before submitting a new issue...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _calls()#67` does not verify whether `request.tool_calls` is of expected format: ```python 67 tool_calls_validator = message.get("tool_calls", ().__iter__()) 68 validated_tool_calls = [] 69 while True: 70 try: 71 tool_c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ers/mistral.py.maybe_serialize_tool_calls()#67` does not verify whether `request.tool_calls` is of expected format: ```python 67 tool_calls_validator = message.get("tool_calls", ().__iter__()) 68 validated_tool_calls =...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
