# vllm-project/vllm#16967: [Bug]: The output of MathResponse is empty when running THUDM/GLM-Z1-32B-0414 with vLLM-0.8.4

| 字段 | 值 |
| --- | --- |
| Issue | [#16967](https://github.com/vllm-project/vllm/issues/16967) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The output of MathResponse is empty when running THUDM/GLM-Z1-32B-0414 with vLLM-0.8.4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug '''class MathResponse(BaseModel): steps: list[Step] final_answer: str client = OpenAI(base_url="[http://localhost:8000/v1",api_key="-](http://localhost:8000/v1%22,api_key=%22-)") completion = client.beta.chat.completions.parse( model="glmz1", messages=[ {"role": "system", "content": "You are a helpful expert math tutor."}, {"role": "user", "content": "Solve 8x + 31 = 2."}, ], response_format=MathResponse, extra_body=dict(guided_decoding_backend="outlines"), )''' '''output： ParsedChatCompletionMessage[MathResponse](content='{"steps": [], "final_answer": ""}', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, parsed=MathResponse(steps=[], final_answer=''), reasoning_content=None)''' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: urrent environment ### 🐛 Describe the bug '''class MathResponse(BaseModel): steps: list[Step] final_answer: str client = OpenAI(base_url="[http://localhost:8000/v1",api_key="-](http://localhost:8000/v1%22,api_key=%22-)"...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: = 2."}, ], response_format=MathResponse, extra_body=dict(guided_decoding_backend="outlines"), )''' '''output： ParsedChatCompletionMessage[MathResponse](content='{"steps": [], "final_answer": ""}', refusal=None, role='as...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ''' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: del="glmz1", messages=[ {"role": "system", "content": "You are a helpful expert math tutor."}, {"role": "user", "content": "Solve 8x + 31 = 2."}, ], response_format=MathResponse, extra_body=dict(guided_decoding_backend=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Response is empty when running THUDM/GLM-Z1-32B-0414 with vLLM-0.8.4 bug;stale ### Your current environment ### 🐛 Describe the bug '''class MathResponse(BaseModel): steps: list[Step] final_answer: str client = OpenAI(ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
