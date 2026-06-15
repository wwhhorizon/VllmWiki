# vllm-project/vllm#13989: [Bug]: Model loading halts while loading Deepseek R1 on 8xH200 Node

| 字段 | 值 |
| --- | --- |
| Issue | [#13989](https://github.com/vllm-project/vllm/issues/13989) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model loading halts while loading Deepseek R1 on 8xH200 Node

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to run DeepSeek R1 using vLLM v0.7.3, model loading abruptly halts. Here's a `docker-compose.yaml` file which reproduces the issue: ``` x-common-variables: &common-variables HF_TOKEN: hf_omitted HUGGING_FACE_HUB_TOKEN: hf_omitted services: deepseek-r1-0: image: vllm/vllm-openai:v0.7.3 command: --model deepseek-ai/DeepSeek-R1 --max-model-len 16384 --max-num-seqs 1 --host 0.0.0.0 --port 14446 --enable-prefix-caching --enforce-eager --enable-reasoning --reasoning-parser deepseek_r1 --trust-remote-code --tensor-parallel-size 8 restart: always environment: <<: *common-variables VLLM_LOGGING_LEVEL: DEBUG CUDA_LAUNCH_BLOCKING: 1 NCCL_DEBUG: TRACE VLLM_TRACE_FUNCTION: 1 HF_DATASETS_CACHE: /root/models HF_HUB_CACHE: /root/models HUGGINGFACE_HUB_CACHE: /root/models HUGGINGFACE_ASSETS_CACHE: /root/models deploy: resources: reservations: devices: - driver: nvidia device_ids: ["0"] capabilities: [gpu] volumes: - /root/models:/root/models shm_size: "32gb" ipc: host network_mode: host privileged: true ``` The model loading starts, and the memory usage for each GPU begins to rise, and then they get completely stuck at this stage:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: DeepSeek R1 using vLLM v0.7.3, model loading abruptly halts. Here's a `docker-compose.yaml` file which reproduces the issue: ``` x-common-variables: &common-variables HF_TOKEN: hf_omitted HUGGING_FACE_HUB_TOKEN: hf_omit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nment: <<: *common-variables VLLM_LOGGING_LEVEL: DEBUG CUDA_LAUNCH_BLOCKING: 1 NCCL_DEBUG: TRACE VLLM_TRACE_FUNCTION: 1 HF_DATASETS_CACHE: /root/models HF_HUB_CACHE: /root/models HUGGINGFACE_HUB_CACHE: /root/models HUGG...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Model loading halts while loading Deepseek R1 on 8xH200 Node bug ### Your current environment ### 🐛 Describe the bug When attempting to run DeepSeek R1 using vLLM v0.7.3, model loading abruptly halts. Here's a `d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
