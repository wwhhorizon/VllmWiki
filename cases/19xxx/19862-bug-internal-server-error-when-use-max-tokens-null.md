# vllm-project/vllm#19862: [Bug]: Internal Server Error when use max_tokens=null

| 字段 | 值 |
| --- | --- |
| Issue | [#19862](https://github.com/vllm-project/vllm/issues/19862) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Internal Server Error when use max_tokens=null

### Issue 正文摘录

### Your current environment "version": "0.8.5.post1" ### 🐛 Describe the bug vllm completions api does not support max_tokens=null, although openai does. https://platform.openai.com/docs/api-reference/completions/create Request: http://vllm.host/v1/completions ``` { "model":"Qwen/Qwen2.5-Coder-7B-Instruct-AWQ", "prompt":"test", "temperature": 0, "max_tokens": null } ``` Response: `Internal Server Error` logs ``` AssertionError 2025-06-19 16:10:24.613 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 2025-06-19 16:10:24.613 assert request.max_tokens is not None 2025-06-19 16:10:24.613 File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_completion.py", line 419, in request_output_to_completion_response 2025-06-19 16:10:24.613 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 2025-06-19 16:10:24.613 response = self.request_output_to_completion_response( 2025-06-19 16:10:24.613 File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_completion.py", line 219, in create_completion 2025-06-19 16:10:24.613 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 2025-06-19 16:10:24.613 generator = await handler.create_completion(request, raw_request) 2025-06-19 16:10:2...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ence/completions/create Request: http://vllm.host/v1/completions ``` { "model":"Qwen/Qwen2.5-Coder-7B-Instruct-AWQ", "prompt":"test", "temperature": 0, "max_tokens": null } ``` Response: `Internal Server Error` logs ```...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Internal Server Error when use max_tokens=null bug;stale ### Your current environment "version": "0.8.5.post1" ### 🐛 Describe the bug vllm completions api does not support max_tokens=null, although openai does. h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 19 16:10:24.613 File "/usr/local/lib/python3.12/dist-packages/fastapi/routing.py", line 212, in run_endpoint_function 2025-06-19 16:10:24.613 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 2025-06-19 16:10:24.613 raw_response = await run...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Error when use max_tokens=null bug;stale ### Your current environment "version": "0.8.5.post1" ### 🐛 Describe the bug vllm completions api does not support max_tokens=null, although openai does. https://platform.openai....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
