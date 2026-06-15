# vllm-project/vllm#8205: [Misc]: benchmark_serving with image input

| 字段 | 值 |
| --- | --- |
| Issue | [#8205](https://github.com/vllm-project/vllm/issues/8205) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: benchmark_serving with image input

### Issue 正文摘录

### Anything you want to discuss about vllm. Can the current benchmark_serving.py be used with Multimodal LLM (llava) and image input? The existing code send the request in the following format in backend_request_func.py, Is it possible to make it support image input? ``` payload = { "model": request_func_input.model, "messages": [ { "role": "user", "content": request_func_input.prompt, }, ], "temperature": 0.0, "max_tokens": request_func_input.output_len, "stream": True, } headers = { "Content-Type": "application/json", "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}", } ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: o discuss about vllm. Can the current benchmark_serving.py be used with Multimodal LLM (llava) and image input? The existing code send the request in the following format in backend_request_func.py, Is it possible to ma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Misc]: benchmark_serving with image input ### Anything you want to discuss about vllm. Can the current benchmark_serving.py be used with Multimodal LLM (llava) and image input? The existing code send the request in the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: age input? The existing code send the request in the following format in backend_request_func.py, Is it possible to make it support image input? ``` payload = { "model": request_func_input.model, "messages": [ { "role":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: with Multimodal LLM (llava) and image input? The existing code send the request in the following format in backend_request_func.py, Is it possible to make it support image input? ``` payload = { "model": request_func_in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
