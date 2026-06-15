# vllm-project/vllm#12289: [Usage]:How to implement concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#12289](https://github.com/vllm-project/vllm/issues/12289) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:How to implement concurrency

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I used vllm to serve a multi-card deployment model and called the openai api concurrently through fastapi, and I found that I was not answering the question at the same time. What can I do to achieve concurrency. `async def generate_text(prompt: str): client = OpenAI( base_url="http://192.168.80.35:8000/v1", api_key="token-abc123", ) completion = client.chat.completions.create( model="/home/linweibin/liujian/model/Qwen2.5-14B-Instruct", messages=[ {"role": "user", "content": prompt} ], temperature=0, ) return completion.choices[0].message.content @app.post("/generate") async def generate_text_endpoint(input: TextInput): result = await generate_text(input.prompt) return {"result": result}` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: would you like to use vllm I used vllm to serve a multi-card deployment model and called the openai api concurrently through fastapi, and I found that I was not answering the question at the same time. What can I do to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t}` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]:How to implement concurrency usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I used vllm to serve a multi-card deployment model and c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
