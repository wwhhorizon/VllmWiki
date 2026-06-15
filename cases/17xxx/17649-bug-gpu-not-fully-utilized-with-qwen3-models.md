# vllm-project/vllm#17649: [Bug]: GPU not fully utilized with Qwen3 models

| 字段 | 值 |
| --- | --- |
| Issue | [#17649](https://github.com/vllm-project/vllm/issues/17649) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU not fully utilized with Qwen3 models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run JunHowie/Qwen3-14B-GPTQ-Int4 or JunHowie/Qwen3-32B-GPTQ-Int4 from Huggingface I get around 70-80% of GPU utilization, which leads to 31t/s and 20t/s respectively. Compared to Ollama I get 66t/s and 31t/s. GPU: RTX 3090 Is this misconfiguration or vLLM is not utilizing the GPU enough? Here is my docker-compose config: ```docker-compose vllm: image: vllm/vllm-openai:v0.8.5 container_name: vllm #restart: unless-stopped ports: - 11435:8000 environment: - HUGGING_FACE_HUB_TOKEN=xxxxxx - PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True - NCCL_DEBUG=INFO # Enables logging/debug output from NCCL - NCCL_IB_DISABLE=1 # Disables InfiniBand support in NCCL - NCCL_P2P_DISABLE=1 # Disable P2P comunication (if no NvLink) - NCCL_P2P_LEVEL=SYS # Use system memory for GPU-to-GPU communication (if no NvLink) deploy: resources: reservations: devices: - driver: nvidia # count: all capabilities: [gpu] device_ids: ["1"] volumes: - ~/.cache/huggingface/hub:/root/.cache/huggingface/hub ipc: host command: [ "--model", "JunHowie/Qwen3-14B-GPTQ-Int4", # Works fine @ ~31.7 tokens/s "--max-model-len", "40960", # context size in tokens # "--model",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: is misconfiguration or vLLM is not utilizing the GPU enough? Here is my docker-compose config: ```docker-compose vllm: image: vllm/vllm-openai:v0.8.5 container_name: vllm #restart: unless-stopped ports: - 11435:8000 env...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: GPU not fully utilized with Qwen3 models bug ### Your current environment ### 🐛 Describe the bug When I run JunHowie/Qwen3-14B-GPTQ-Int4 or JunHowie/Qwen3-32B-GPTQ-Int4 from Huggingface I get around 70-80% of GPU...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vironment ### 🐛 Describe the bug When I run JunHowie/Qwen3-14B-GPTQ-Int4 or JunHowie/Qwen3-32B-GPTQ-Int4 from Huggingface I get around 70-80% of GPU utilization, which leads to 31t/s and 20t/s respectively. Compared to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: and 20t/s respectively. Compared to Ollama I get 66t/s and 31t/s. GPU: RTX 3090 Is this misconfiguration or vLLM is not utilizing the GPU enough? Here is my docker-compose config: ```docker-compose vllm: image: vllm/vll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
