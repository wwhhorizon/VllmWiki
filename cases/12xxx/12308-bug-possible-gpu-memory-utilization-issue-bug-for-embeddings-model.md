# vllm-project/vllm#12308: [Bug]: Possible GPU Memory Utilization issue/bug for embeddings model

| 字段 | 值 |
| --- | --- |
| Issue | [#12308](https://github.com/vllm-project/vllm/issues/12308) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Possible GPU Memory Utilization issue/bug for embeddings model

### Issue 正文摘录

### Your current environment I am using docker env for vLLM: `vllm/vllm-openai:v0.6.4` ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running vLLM using docker/docker compose. My current docker-compose.yaml is- ```docker-compose embeddings: image: vllm/vllm-openai:v0.6.4 command: - "--task" - "embedding" - "--model" - "intfloat/multilingual-e5-large" - "--dtype" - "auto" - "--tensor-parallel-size" - "1" - "--host" - "0.0.0.0" - "--port" - "9000" - "--gpu-memory-utilization" - "0.25" - "--trust-remote-code" environment: - HF_TOKEN=$HF_TOKEN - CUDA_VISIBLE_DEVICES=0 volumes: - /home/ubuntu/.cache/huggingface/:/root/.cache/huggingface/ ports: - "9010:9000" deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu] healthcheck: test: curl -f http://localhost:9000/health || exit 1 interval: 60s timeout: 10s retries: 3 start_period: 30s restart: always ``` Here i am running an embeddings models on Nvidia RTX 4060Ti. As you can see my `--gpu-memory-utilization` is `0.25` which should be around 4GB for an Nvidia RTX 4060Ti. The corresponding snapshot of my `nvidia-smi` is: - ![Image](https://github.com/user-attachments/assets/a0848837-99a6-4...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: Bug]: Possible GPU Memory Utilization issue/bug for embeddings model bug;stale ### Your current environment I am using docker env for vLLM: `vllm/vllm-openai:v0.6.4` ### Model Input Dumps _No response_ ### 🐛 Describe th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: for embeddings model bug;stale ### Your current environment I am using docker env for vLLM: `vllm/vllm-openai:v0.6.4` ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running vLLM using docker/docker comp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: g" - "--model" - "intfloat/multilingual-e5-large" - "--dtype" - "auto" - "--tensor-parallel-size" - "1" - "--host" - "0.0.0.0" - "--port" - "9000" - "--gpu-memory-utilization" - "0.25" - "--trust-remote-code" en
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Possible GPU Memory Utilization issue/bug for embeddings model bug;stale ### Your current environment I am using docker env for vLLM: `vllm/vllm-openai:v0.6.4` ### Model Input Dumps _No response_ ### 🐛 Describe t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: --trust-remote-code" environment: - HF_TOKEN=$HF_TOKEN - CUDA_VISIBLE_DEVICES=0 volumes: - /home/ubuntu/.cache/huggingface/:/root/.cache/huggingface/ ports: - "9010:9000" deploy: resources: reservations: devices: - driv

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
