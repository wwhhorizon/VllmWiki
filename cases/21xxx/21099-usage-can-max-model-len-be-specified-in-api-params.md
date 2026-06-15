# vllm-project/vllm#21099: [Usage]: Can max_model_len be specified in API params?

| 字段 | 值 |
| --- | --- |
| Issue | [#21099](https://github.com/vllm-project/vllm/issues/21099) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can max_model_len be specified in API params?

### Issue 正文摘录

### Your current environment win11 I want to request to Api backend, and the params are like this, adjust max_model_len flexiable ```json { "model": "Qwen2___5-VL-32B-Instruct-awq", "max_model_len": "5000", "messages": [ { "role": "user", "content": [ *[ {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img}"}} for img in images ], { "type": "text", "text": tip } ] } ], "stream": True, "keep_alive": -1, "options": { "num_ctx": 8192 }, "enable_thinking": False } ``` Why ? Because after I set a large enough `max_model_len` in command line . The backend tokens/s are very low event I only pass one image to Api server ! So I want to adjust `max_model_len` according to my param size .... ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Usage]: Can max_model_len be specified in API params? usage;stale ### Your current environment win11 I want to request to Api backend, and the params are like this, adjust max_model_len flexiable ```json { "model": "Qw...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Can max_model_len be specified in API params? usage;stale ### Your current environment win11 I want to request to Api backend, and the params are like this, adjust max_model_len flexiable ```json { "model": "Qw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Can max_model_len be specified in API params? usage;stale ### Your current environment win11 I want to request to Api backend, and the params are like this, adjust max_model_len flexiable ```json { "model": "Qw...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sage;stale ### Your current environment win11 I want to request to Api backend, and the params are like this, adjust max_model_len flexiable ```json { "model": "Qwen2___5-VL-32B-Instruct-awq", "max_model_len": "5000", "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
