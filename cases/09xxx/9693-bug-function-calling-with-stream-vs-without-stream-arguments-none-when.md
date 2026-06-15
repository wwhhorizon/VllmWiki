# vllm-project/vllm#9693: [Bug]: Function calling with stream vs without stream, arguments=None when stream option is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#9693](https://github.com/vllm-project/vllm/issues/9693) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Function calling with stream vs without stream, arguments=None when stream option is enabled

### Issue 正文摘录

### Your current environment Dockerfile: vllm/vllm-openai:v0.6.3 Parameters: `--enable-auto-tool-choice --tool-call-parser hermes` ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using the VLLM library with a Docker container as a REST API, specifically the `v1/chat/completion/` endpoint with the OpenAI client. When I run chat completions without streaming, it returns `tool_calls` with the tool name and its arguments as expected. However, when I enable the streaming option, it only returns the tool name, with arguments set to `None`. I'm not sure why this is happening. I've tried searching for related issues but haven’t found anything helpful. Have tried `stream_options={"include_usage": True}` and it gives same output. Model generate this output: ``` {"arguments": {"n1": 2, "n2": 2}, "name": "sum"} ``` ``` chat_completion = client.chat.completions.create( model="tgi", messages=messages, stream=True, max_tokens=2000, temperature=0.3, tools=tools, tool_choice="auto", ) chunks = [] for chunk in chat_completion: chunks.append(chunk) if chunk.choices[0].delta.tool_calls: print(chunk.choices[0].delta.tool_calls[0]) else: print(chunk.choices[0].delta) chat_completion = cl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nts=None when stream option is enabled bug ### Your current environment Dockerfile: vllm/vllm-openai:v0.6.3 Parameters: `--enable-auto-tool-choice --tool-call-parser hermes` ### Model Input Dumps _No response_ ### 🐛 Des...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: elpful. Have tried `stream_options={"include_usage": True}` and it gives same output. Model generate this output: ``` {"arguments": {"n1": 2, "n2": 2}, "name": "sum"} ``` ``` chat_completion = client.chat.completions.cr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: guments set to `None`. I'm not sure why this is happening. I've tried searching for related issues but haven’t found anything helpful. Have tried `stream_options={"include_usage": True}` and it gives same output. Model...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lta.tool_calls: print(chunk.choices[0].delta.tool_calls[0]) else: print(chunk.choices[0].delta) chat_completion = client.chat.completions.create( model="tgi", messages=messages, stream=False, max_tokens=2000, temperatur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Parameters: `--enable-auto-tool-choice --tool-call-parser hermes` ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using the VLLM library with a Docker container as a REST API, specifically the `v1/chat/co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
