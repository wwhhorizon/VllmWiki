# vllm-project/vllm#36857: [Bug]: The arguments invoked by the tool in the GLM-5 streaming output cannot be parsed into the JSON format.

| 字段 | 值 |
| --- | --- |
| Issue | [#36857](https://github.com/vllm-project/vllm/issues/36857) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The arguments invoked by the tool in the GLM-5 streaming output cannot be parsed into the JSON format.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed and tested GLM-5-w4a8-mtp in the Function Call streaming output scenario on vLLM 0.16.0. The relevant configuration and test result are provided at the end. Streaming output result of the GLM-5 model: ``` data: {"id":"chatcmpl-","object":"chat.completion.chunk","created":xx,"model":"glm-5","choices":[{"index":0,"delta":{"tool_calls":[{"index":0,"function":{"arguments":"iz"}}]},"logprobs":null,"finish_reason":null,"token_ids":null}]} data: {"id":"chatcmpl-","object":"chat.completion.chunk","created":xx,"model":"glm-5","choices":[{"index":0,"delta":{"tool_calls":[{"index":0,"function":{"arguments":"hu.js"}}]},"logprobs":null,"finish_reason":null,"token_ids":null}]} data: {"id":"chatcmpl-","object":"chat.completion.chunk","created":xx,"model":"glm-5","choices":[{"index":0,"delta":{"tool_calls":[{"index":0,"function":{"arguments":"\""}}]},"logprobs":null,"finish_reason":null,"token_ids":null}]} data: {"id":"chatcmpl-","object":"chat.completion.chunk","created":xx,"model":"glm-5","choices":[{"index":0,"delta":{"tool_calls":[{"id":null,"type":null,"index":0,"function":{"name":null,"arguments":"{\"content\": \"//Dou Dizhu\\nl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: by the tool in the GLM-5 streaming output cannot be parsed into the JSON format. bug ### Your current environment ### 🐛 Describe the bug I deployed and tested GLM-5-w4a8-mtp in the Function Call streaming output scenari...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: expected_call = json.dumps(args, ensure_ascii=False) # get what we've streamed so far for arguments # for the current tool actual_call = tool_parser.streamed_args_for_tool[index
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nk. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: expected_call = args else: expected_call = json.dumps(args, ensure_ascii=False) # get what we've streamed so far for arguments # for the current tool
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ### Your current environment ### 🐛 Describe the bug I deployed and tested GLM-5-w4a8-mtp in the Function Call streaming output scenario on vLLM 0.16.0. The relevant configuration and test result are provided at the end....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
