# vllm-project/vllm#14951: [Bug]: vLLM response on tool_calls does not align with OpenAI standard

| 字段 | 值 |
| --- | --- |
| Issue | [#14951](https://github.com/vllm-project/vllm/issues/14951) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM response on tool_calls does not align with OpenAI standard

### Issue 正文摘录

### Your current environment: vLLM 0.7.3 latest We are trying to use tool_calls with vLLM running llama 3.1 or 3.2. We found that the tool_calls data returned from vLLM is not the same as what OpenAI demonstrated so the OpenAI Adaptors are not working as expected (the function name is concated as a very long string so it cannot be found). As per OpenAI API document: [OpenAI Document for streaming function calling](https://platform.openai.com/docs/guides/function-calling?api-mode=chat&lang=javascript#streaming) However, what we get from vLLM is: Then the processor is trying to do the same as receiving data from OpenAI and cause the confusion on function name. So I found this is due to the code in [vllm/entrypoints/openai/serving_chat.py](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/serving_chat.py) in first_iteration, it is sending a simple choice: and in each chunk sending the function name repeatedly: So I would like to suggest a following change: and also: I have attached the complete code as attached: [serving_chat.py](https://github.com/user-attachments/files/19285168/serving_chat.py.txt) Thanks for looking into this. ### 🐛 Describe the bug We are usi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt: vLLM 0.7.3 latest We are trying to use tool_calls with vLLM running llama 3.1 or 3.2. We found that the tool_calls data returned from vLLM is not the same as what OpenAI demonstrated so the OpenAI Adaptors are not w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ug]: vLLM response on tool_calls does not align with OpenAI standard bug;stale;tool-calling ### Your current environment: vLLM 0.7.3 latest We are trying to use tool_calls with vLLM running llama 3.1 or 3.2. We found th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: andard bug;stale;tool-calling ### Your current environment: vLLM 0.7.3 latest We are trying to use tool_calls with vLLM running llama 3.1 or 3.2. We found that the tool_calls data returned from vLLM is not the same as w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
