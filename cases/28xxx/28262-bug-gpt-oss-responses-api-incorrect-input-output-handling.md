# vllm-project/vllm#28262: [Bug]: [gpt-oss] Responses API incorrect input/output handling

| 字段 | 值 |
| --- | --- |
| Issue | [#28262](https://github.com/vllm-project/vllm/issues/28262) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [gpt-oss] Responses API incorrect input/output handling

### Issue 正文摘录

### Your current environment Any env ### 🐛 Describe the bug There is currently an implementation issue with gpt-oss on the Responses API in vLLM. This can be seen clearly in the [test which continues a conversation between API requests here](https://github.com/vllm-project/vllm/blob/4bf56c79cc252d285d0cb4f5edf323f02af735ca/tests/entrypoints/openai/test_response_api_with_harmony.py#L715). From the first request, the model outputs the following tokens (whitespace added for clarity): ``` analysis User asks for weather in Paris today. We have no direct API call yet, but we can use get_weather function. Coordinates for Paris: latitude 48.8566, longitude 2.3522. We'll call get_weather. assistant commentary to=functions.get_weather json {"latitude":48.8566,"longitude":2.3522} ``` When the output items from the first request are passed in as input to the second request, the tokens look like this (whitespace added for clarity): ``` user What's the weather like in Paris today? assistant User asks for weather in Paris today. We have no direct API call yet, but we can use get_weather function. Coordinates for Paris: latitude 48.8566, longitude 2.3522. We'll call get_weather. assistant to=func...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [gpt-oss] Responses API incorrect input/output handling bug;stale ### Your current environment Any env ### 🐛 Describe the bug There is currently an implementation issue with gpt-oss on the Responses API in vLLM....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: [gpt-oss] Responses API incorrect input/output handling bug;stale ### Your current environment Any env ### 🐛 Describe the bug There is currently an implementation issue with gpt-oss on the Responses API in vLLM....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: a lot of edge cases and challenges to properly represent Harmony Message metadata when the Responses API input/output types do not include that metadata, but we can improve on the current implementation. The changes we...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: h gpt-oss on the Responses API in vLLM. This can be seen clearly in the [test which continues a conversation between API requests here](https://github.com/vllm-project/vllm/blob/4bf56c79cc252d285d0cb4f5edf323f02af735ca/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
