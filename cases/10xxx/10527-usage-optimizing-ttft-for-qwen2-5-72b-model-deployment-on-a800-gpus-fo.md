# vllm-project/vllm#10527: [Usage]: Optimizing TTFT for Qwen2.5-72B Model Deployment on A800 GPUs for RAG Application

| 字段 | 值 |
| --- | --- |
| Issue | [#10527](https://github.com/vllm-project/vllm/issues/10527) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Optimizing TTFT for Qwen2.5-72B Model Deployment on A800 GPUs for RAG Application

### Issue 正文摘录

### Your current environment Below is my current Docker Compose configuration: ```yaml services: vllm: image: vllm/vllm-openai:v0.6.4 deploy: resources: reservations: devices: - driver: nvidia device_ids: ['2', '3'] capabilities: [gpu] ipc: host command: - "--model" - "qwen/Qwen2___5-72B-Instruct-GPTQ-Int4" - "--gpu-memory-utilization" - "0.9" - "--served-model-name" - "qwen2.5-72b" - "--enable-auto-tool-choice" - "--tool-call-parser" - "hermes" - "--tensor-parallel-size" - "2" - "--enable-prefix-caching" - "--multi-step-stream-outputs" - "False" ``` ### How would you like to use vllm I'm currently deploying the Qwen2.5-72B model using VLLM on two NVIDIA A800 GPUs for a Retrieval-Augmented Generation (RAG) application. **The load on the model involves processing token sequences greater than 6000 tokens**. My goal is to reduce the Time to First Token (TTFT) for the service to improve overall performance and responsiveness. The current configuration results in a **considerably high TTFT**, which is impacting the overall performance of my RAG application. I would like to optimize the configuration to reduce the TTFT to improve the service's responsiveness. Thank you for your assistan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pplication usage;stale ### Your current environment Below is my current Docker Compose configuration: ```yaml services: vllm: image: vllm/vllm-openai:v0.6.4 deploy: resources: reservations: devices: - driver: nvidia dev...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: command: - "--model" - "qwen/Qwen2___5-72B-Instruct-GPTQ-Int4" - "--gpu-memory-utilization" - "0.9" - "--served-model-name" - "qwen2.5-72b" - "--enable-auto-tool-choice" - "--tool-call-parser" - "hermes" - "--tensor-par...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Optimizing TTFT for Qwen2.5-72B Model Deployment on A800 GPUs for RAG Application usage;stale ### Your current environment Below is my current Docker Compose configuration: ```yaml services: vllm: image: vllm/v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ying the Qwen2.5-72B model using VLLM on two NVIDIA A800 GPUs for a Retrieval-Augmented Generation (RAG) application. **The load on the model involves processing token sequences greater than 6000 tokens**. My goal is to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
