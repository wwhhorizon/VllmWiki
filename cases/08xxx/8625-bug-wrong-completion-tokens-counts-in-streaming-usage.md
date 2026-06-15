# vllm-project/vllm#8625: [Bug]: Wrong "completion_tokens" counts in streaming usage

| 字段 | 值 |
| --- | --- |
| Issue | [#8625](https://github.com/vllm-project/vllm/issues/8625) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Wrong "completion_tokens" counts in streaming usage

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have used `vllm==0.6.1.post2` to host **Qwen2-VL-72B-Instruct** with the command: `python -m vllm.entrypoints.openai.api_server --served-model-name Qwen2-VL-72B-Instruct --model /models/Qwen2-VL-72B-Instruct --tensor-parallel-size 4 --gpu-memory-utilization 0.9` However, when I curl the endpoint with `streaming` and `include_usage=True`, the `completion_tokens` is always 1 until the last token. My curl: ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen2-VL-72B-Instruct", "max_tokens": 1024, "temperature": 0.1, "stream": true, "stream_options": {"include_usage": true}, "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hi."} ] }' ``` Output: ``` data: {"id":"chat-a440da300fcc4022947ccfe424f9c8ae","object":"chat.completion.chunk","created":1726735957,"model":"Qwen2-VL-72B-Instruct","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}],"usage":{"prompt_tokens":21,"total_tokens":21,"completion_tokens":0}} data: {"id":"chat-a440da300f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits cuda;triton build_error env_dependency Your current envi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: counts in streaming usage bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have used `vllm==0.6.1.post2` to host **Qwen2-VL-72B-Instruct** with the command: `python -m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: arallel;frontend_api;hardware_porting;model_support;sampling_logits cuda;triton build_error env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Wrong "completion_tokens" counts in streaming usage bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have used `vllm==0.6.1.post2` to host **Qwen2-VL-72B-Instruc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
