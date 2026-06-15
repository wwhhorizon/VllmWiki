# vllm-project/vllm#23429: [Bug]: DeepSeek-V3.1 reasoning content incorrectly placed in `reasoning_content` field when `thinking: false`

| 字段 | 值 |
| --- | --- |
| Issue | [#23429](https://github.com/vllm-project/vllm/issues/23429) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V3.1 reasoning content incorrectly placed in `reasoning_content` field when `thinking: false`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Problem Description When using DeepSeek-V3.1 with the `deepseek_r1` reasoning parser in a vLLM Docker container, there's an issue with how content is distributed between the `content` and `reasoning_content` fields in the API response based on the `thinking` parameter. **Expected behavior:** - When `thinking: false` → Main response should be in `content` field, `reasoning_content` should be empty or contain actual reasoning tokens - When `thinking: true` → Main response should be in `content` field, reasoning process should be in `reasoning_content` field **Actual behavior:** - When `thinking: false` → Main response incorrectly appears in `reasoning_content` field, `content` field is `null` - When `thinking: true` → Works correctly with main response in `content` and reasoning in `reasoning_content` ### Reproduction Steps 1. Start vLLM using Docker Compose with the following configuration: ```yaml version: "3.9" services: vllm-ht: image: vllm/vllm-openai:v0.10.1 container_name: vllm-deepseek-v31-ht deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu] shm_size: "16g" ports: ["8001:8000"] vo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: en using DeepSeek-V3.1 with the `deepseek_r1` reasoning parser in a vLLM Docker container, there's an issue with how content is distributed between the `content` and `reasoning_content` fields in the API response based...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: - --gpu-memory-utilization - "0.90" - --enable-chunked-prefill - --max-num-batched-tokens - "8192" - --max-num-seqs - "256" - --reasoning-parser - deepseek_r1 ``` 2. Make a request with `thinking: false`: ```bash curl h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ld? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eproduction Steps 1. Start vLLM using Docker Compose with the following configuration: ```yaml version: "3.9" services: vllm-ht: image: vllm/vllm-openai:v0.10.1 container_name: vllm-deepseek-v31-ht deploy: resources: re...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: - /models/DeepSeek-V3.1 - --dtype - auto - --enable-expert-parallel - --tensor-parallel-size - "8" - --served-model-name - DeepSeek-V3.1 - --max-model-len - "131072" - --gpu-memory-utilization - "0.90" - --enable-chunk

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
