# vllm-project/vllm#3435: Docker deployment with mistralai/Mistral-7B-v0.1 model

| 字段 | 值 |
| --- | --- |
| Issue | [#3435](https://github.com/vllm-project/vllm/issues/3435) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;model_support |
| 子分类 | install |
| Operator 关键词 | cache |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Docker deployment with mistralai/Mistral-7B-v0.1 model

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm trying to use docker to deploy vllm in EC2 instance here is my docker-compose.yaml looks like ``` services: vllm: image: vllm/vllm-openai:latest command: --model mistralai/Mistral-7B-v0.1 environment: - HUGGING_FACE_HUB_TOKEN="key" volumes: - ~/.cache/huggingface:/root/.cache/huggingface ports: - "8000:8000" deploy: resources: reservations: devices: - driver: nvidia count: 1 capabilities: [gpu] ``` When I was trying to run it, it always returned an error that said ` vllm-1 | ValueError: The model's max seq len (32768) is larger than the maximum number of tokens that can be stored in KV cache (16832). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine.` what should I change to make it run with my compose file? It seems like there is no env variables like gpu_memory_utilization and max_model_len that I can pass value in

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Docker deployment with mistralai/Mistral-7B-v0.1 model ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm trying to use docker to deploy vllm in EC2 i
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Docker deployment with mistralai/Mistral-7B-v0.1 model ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm trying to use docker to deploy vllm in EC2 ins...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 32768) is larger than the maximum number of tokens that can be stored in KV cache (16832). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine.` what should I change to mak...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: pose.yaml looks like ``` services: vllm: image: vllm/vllm-openai:latest command: --model mistralai/Mistral-7B-v0.1 environment: - HUGGING_FACE_HUB_TOKEN="key" volumes: - ~/.cache/huggingface:/root/.cache/huggingface por...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
