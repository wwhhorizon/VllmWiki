# vllm-project/vllm#23404: [Bug]: Qwen3 vLLM Structured Output Ignores Field Descriptions

| 字段 | 值 |
| --- | --- |
| Issue | [#23404](https://github.com/vllm-project/vllm/issues/23404) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Qwen3 vLLM Structured Output Ignores Field Descriptions

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed Qwen3-4B-Instruct-2507 using vLLM and tested structured output — it worked correctly at first. However, when I added field descriptions to guide the output, the model did not follow them. Below is my Dockerfile: ```Dockerfile FROM vllm/vllm-openai:latest COPY requirements.txt . # Install python packages RUN pip install -r requirements.txt ``` docker compose file ```yaml x-common-config: &common-config build: . runtime: nvidia ipc: host shm_size: 32g volumes: - ~/.cache/huggingface:/root/.cache/huggingface - ./middlewares:/vllm-workspace/middlewares - ./logging:/vllm-workspace/logging # - ./engine:/usr/local/lib/python3.12/dist-packages/vllm/engine deploy: resources: reservations: devices: - capabilities: [gpu] services: small_llm: --model Qwen/Qwen3-4B-Instruct-2507 --host 0.0.0.0 --port 8000 --max-model-len 400 --max-num-seqs 5 --max-num-batched-tokens 500 --enforce-eager --enable-auto-tool-choice --enable_prefix_caching --tool-call-parser xlam --guided-decoding-backend auto --gpu-memory-utilization 0.6 --middleware middlewares.tracing_yield.phoenix_middleware ``` My code of using api server ```python import json from...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: iptions to guide the output, the model did not follow them. Below is my Dockerfile: ```Dockerfile FROM vllm/vllm-openai:latest COPY requirements.txt . # Install python packages RUN pip install -r requirements.txt ``` do...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3 vLLM Structured Output Ignores Field Descriptions bug;stale ### Your current environment ### 🐛 Describe the bug I deployed Qwen3-4B-Instruct-2507 using vLLM and tested structured output — it worked correctl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: servations: devices: - capabilities: [gpu] services: small_llm: --model Qwen/Qwen3-4B-Instruct-2507 --host 0.0.0.0 --port 8000 --max-model-len 400 --max-num-seqs 5 --max-num-batched-tokens 500 --enforce-eager --enable-a
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ble_prefix_caching --tool-call-parser xlam --guided-decoding-backend auto --gpu-memory-utilization 0.6 --middleware middlewares.tracing_yield.phoenix_middleware ``` My code of using api server ```python import json from...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3 vLLM Structured Output Ignores Field Descriptions bug;stale ### Your current environment ### 🐛 Describe the bug I deployed Qwen3-4B-Instruct-2507 using vLLM and tested structured output — it worked correctl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
