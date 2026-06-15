# vllm-project/vllm#18231: [Bug]: SamplingParams() use_beam_search error

| 字段 | 值 |
| --- | --- |
| Issue | [#18231](https://github.com/vllm-project/vllm/issues/18231) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SamplingParams() use_beam_search error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to recreate a docker network that I had created about a year ago. I used the following docker-compose setup: ``` services: # Create network of docker containers fastchat-controller: image: fastchat:latest ports: - '31001:31001' entrypoint: ['python3', '-m', 'fastchat.serve.controller', '--host', '0.0.0.0', '--port', '31001'] fastchat-model-worker-mistral7b: # Create container for Mistral7B LLM image: fastchat:latest environment: HF_TOKEN: 'HF-TOKEN' ports: - '31002:31002' deploy: resources: reservations: devices: - driver: nvidia device_ids: ['0'] capabilities: [gpu] entrypoint: ['python3', '-m', 'fastchat.serve.vllm_worker', '--model-path', 'mistralai/Mistral-7B-v0.1', '--trust-remote-code', '--model-impl', 'transformers','--gpu-memory-utilization', '0.4', '--max-model-len', '16300', '--worker-address', 'http://fastchat-model-worker-mistral7b:31002', '--controller-address', 'http://fastchat-controller:31001', '--host', '0.0.0.0', '--port', '31002'] fastchat-api-server: # Create API server container image: fastchat:latest ports: - '8080:8080' entrypoint: ['python3', '-m', 'fastchat.serve.openai_api_server', '--control...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: urrent environment ### 🐛 Describe the bug I am trying to recreate a docker network that I had created about a year ago. I used the following docker-compose setup: ``` services: # Create network of docker containers fast...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t.serve.controller', '--host', '0.0.0.0', '--port', '31001'] fastchat-model-worker-mistral7b: # Create container for Mistral7B LLM image: fastchat:latest environment: HF_TOKEN: 'HF-TOKEN' ports: - '31002:31002' deploy:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: SamplingParams() use_beam_search error bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to recreate a docker network that I had created about a year ago. I used the following docker-compo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: RROR | stderr | File "/app/venv/lib/python3.11/site-packages/starlette/routing.py", line 714, in __call__ fastchat-model-worker-mistral7b-1 | 2025-05-15 23:11:06 | ERROR | stderr | await self.middleware_stack(scope, rec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: SamplingParams() use_beam_search error bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to recreate a docker network that I had created about a year ago. I used the following docker-compo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
