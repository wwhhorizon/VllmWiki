# vllm-project/vllm#23315: [Bug]: Structured Output Not Supported in Qwen3-30B-A3B-Instruct-2507

| 字段 | 值 |
| --- | --- |
| Issue | [#23315](https://github.com/vllm-project/vllm/issues/23315) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Structured Output Not Supported in Qwen3-30B-A3B-Instruct-2507

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’ve deployed Qwen3-30B-A3B-Instruct-2507 in vLLM, but it doesn’t seem to respect the defined response format or decode messages into the structured format I specify. When I tested with Qwen3-30B-A3B, structured output worked as expected, so I assumed this model should behave the same way. However, it isn’t working. Below is my docker config of using vLLM Dockerfile ```Dockerfile FROM vllm/vllm-openai:v0.9.2 COPY . . RUN pip install -r requirements.txt ``` docker compose file ```yaml services: vllm-openai: # image: vllm/vllm-openai:v0.9.2 build: . ports: - "8000:8000" deploy: resources: reservations: devices: - capabilities: [gpu] command: > --model Qwen/Qwen3-30B-A3B-Instruct-2507 --host 0.0.0.0 --port 8000 --swap-space 2 --tensor-parallel-size 8 --pipeline-parallel-size 2 --max-model-len 80000 --enable_prefix_caching --gpu-memory-utilization 0.9 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser hermes --middleware middlewares.tracing.phoenix_middleware environment: - HUGGING_FACE_HUB_TOKEN= ${HF_TOKEN} - OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf - OTEL_TRACES_SAMPLER=always_on - OTEL_EXPORTER_OTLP_TRA...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: fined response format or decode messages into the structured format I specify. When I tested with Qwen3-30B-A3B, structured output worked as expected, so I assumed this model should behave the same way. However, it isn’...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Structured Output Not Supported in Qwen3-30B-A3B-Instruct-2507 bug ### Your current environment ### 🐛 Describe the bug I’ve deployed Qwen3-30B-A3B-Instruct-2507 in vLLM, but it doesn’t seem to respect the defined...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 7 in vLLM, but it doesn’t seem to respect the defined response format or decode messages into the structured format I specify. When I tested with Qwen3-30B-A3B, structured output worked as expected, so I assumed this mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
