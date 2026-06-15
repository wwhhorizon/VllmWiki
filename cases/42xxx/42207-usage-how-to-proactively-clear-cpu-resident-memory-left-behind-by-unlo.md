# vllm-project/vllm#42207: [Usage]: How to proactively clear CPU-resident memory left behind by unloaded LoRA adapters after calling `/v1/unload_lora_adapter`?

| 字段 | 值 |
| --- | --- |
| Issue | [#42207](https://github.com/vllm-project/vllm/issues/42207) |
| 状态 | open |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to proactively clear CPU-resident memory left behind by unloaded LoRA adapters after calling `/v1/unload_lora_adapter`?

### Issue 正文摘录

## Environment ```text OS: Ubuntu 22.04.4 LTS vLLM version: v0.17.1 Docker image: vllm/vllm-openai:v0.17.1 Model: Qwen/Qwen3-4B-Instruct-2507 Relevant env: VLLM_ALLOW_RUNTIME_LORA_UPDATING=True ``` --- ## Deployment Config ```yaml sampler-Qwen3-4B-Instruct-2507-trio002-1: container_name: release-sampler-Qwen3-4B-Instruct-2507-trio002-1 image: vllm/vllm-openai:v0.17.1 environment: HOSTNAME: release-sampler-Qwen3-4B-Instruct-2507-trio002-1 VLLM_ALLOW_RUNTIME_LORA_UPDATING: "True" VLLM_LOGGING_LEVEL: INFO volumes: - /data/models/Qwen:/data/models/Qwen:ro - /data/release/nano-tinker/outputs:/data/release/nano-tinker/outputs shm_size: "16g" deploy: resources: reservations: devices: - driver: nvidia device_ids: ["5"] capabilities: [gpu] command: - --model - /data/models/Qwen/Qwen3-4B-Instruct-2507 - --served-model-name - Qwen/Qwen3-4B-Instruct-2507 - --gpu-memory-utilization - "0.85" - --host - 0.0.0.0 - --port - "80" - --trust-remote-code - --max-model-len - "32768" - --enable-lora - --max-loras - "4" - --max-lora-rank - "64" restart: unless-stopped ``` --- ## Description We are using runtime LoRA loading/unloading through the REST API. We understand that after calling: ```text POST /v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: a_adapter`? usage ## Environment ```text OS: Ubuntu 22.04.4 LTS vLLM version: v0.17.1 Docker image: vllm/vllm-openai:v0.17.1 Model: Qwen/Qwen3-4B-Instruct-2507 Relevant env: VLLM_ALLOW_RUNTIME_LORA_UPDATING=True ``` ---...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: LTS vLLM version: v0.17.1 Docker image: vllm/vllm-openai:v0.17.1 Model: Qwen/Qwen3-4B-Instruct-2507 Relevant env: VLLM_ALLOW_RUNTIME_LORA_UPDATING=True ``` --- ## Deployment Config ```yaml sampler-Qwen3-4B-Instruct-2507...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e only reliable approach, or is there a more fine-grained cleanup mechanism? --- ## Additional Context Our workload is a long-running dynamic multi-LoRA service where adapters are frequently loaded and unloaded. So we w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
