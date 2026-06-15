# vllm-project/vllm#19022: [Bug]: Models misbehaves when --tensor-parallel-size 2 on 2x Nvidia L4

| 字段 | 值 |
| --- | --- |
| Issue | [#19022](https://github.com/vllm-project/vllm/issues/19022) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Models misbehaves when --tensor-parallel-size 2 on 2x Nvidia L4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug LLMs give gibberish outputs when ```--tensor-parallel-size 2``` Code to start the server: ```bash python -m vllm.entrypoints.openai.api_server --model "meta-llama/Llama-3.1-8B-Instruct" --tensor-parallel-size 2 --host 0.0.0.0 --port 8001 ``` Curl request: ```bash curl -X POST http://0.0.0.0:8001/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "meta-llama/Llama-3.1-8B-Instruct", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": "Hello! Can you tell me a fun fact about AI?" } ], "max_completion_tokens": 2048, "temperature": 0.7, "top_p": 0.9, "top_k": 40, "stop_token_ids": [128001, 128009], "skip_special_tokens": true, "apply_chat_template": true }' ``` Output: ```bash {"id":"chatcmpl-c3319ea161604081ad5edd70fe97846f","object":"chat.completion","created":1748869787,"model":"meta-llama/Llama-3.1-8B-Instruct","choices":[{"index":0,"message":{"role":"assistant","reasoning_content":null,"content":"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 9, "top_k": 40, "stop_token_ids": [128001, 128009], "skip_special_tokens": true, "apply_chat_template": true }' ``` Output: ```bash {"id":"chatcmpl-c3319ea161604081ad5edd70fe97846f","object":"chat.completion","created":...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Models misbehaves when --tensor-parallel-size 2 on 2x Nvidia L4 bug;stale ### Your current environment ### 🐛 Describe the bug LLMs give gibberish outputs when ```--tensor-parallel-size 2``` Code to start the serv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ug]: Models misbehaves when --tensor-parallel-size 2 on 2x Nvidia L4 bug;stale ### Your current environment ### 🐛 Describe the bug LLMs give gibberish outputs when ```--tensor-parallel-size 2``` Code to start the server...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ms? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
