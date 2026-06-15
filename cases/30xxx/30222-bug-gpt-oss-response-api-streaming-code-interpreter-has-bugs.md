# vllm-project/vllm#30222: [Bug]: gpt-oss response api: streaming + code interpreter has bugs

| 字段 | 值 |
| --- | --- |
| Issue | [#30222](https://github.com/vllm-project/vllm/issues/30222) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gpt-oss response api: streaming + code interpreter has bugs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Gpt-oss in streaming mode cannot see internal code interpreter output the problem is with https://github.com/vllm-project/vllm/blob/af0444bf40b7db2f3fb9fe1508d25ceba24cac87/vllm/entrypoints/context.py#L720-L732 I can see that tool call result is not appended to message. My basic testing code looks like this ```python stream = client.responses.create( model="vllm-model", input=[{"role": "user", "content": "what is 123^456 mod 1000000007? use python tool to solve this problem"}], tools=[{"type": "code_interpreter", "container": {"type": "auto"}}], max_output_tokens=32768, temperature=1.0, reasoning={"effort": "high"}, stream=True, instructions=system_prompt, extra_body={ "min_p": 0.02, "stop_token_ids": stop_token_ids, "chat_template_kwargs": {"enable_thinking": True}, } ) current_tool_code = "" for event in stream: generation_idx += 1 # Reasoning text if event.type == "response.reasoning_text.delta": delta = event.delta reasoning_response += delta text_response += delta print(delta, end="", flush=True) # Real-time output # Message text elif event.type == "response.output_text.delta": delta = event.delta text_response += delta prin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: gpt-oss response api: streaming + code interpreter has bugs bug;stale ### Your current environment ### 🐛 Describe the bug Gpt-oss in streaming mode cannot see internal code interpreter output the problem is with h
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pass ``` model response (ignore the pretty looking, it is just another version for visualization) ```bash ============================================================ 💭 REASONING: We need to compute 123^456 mod 10000000...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: gpt-oss response api: streaming + code interpreter has bugs bug;stale ### Your current environment ### 🐛 Describe the bug Gpt-oss in streaming mode cannot see internal code interpreter output the problem is with...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 2 I can see that tool call result is not appended to message. My basic testing code looks like this ```python stream = client.responses.create( model="vllm-model", input=[{"role": "user", "content": "what is 123^456 mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
