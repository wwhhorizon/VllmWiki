# vllm-project/vllm#39048: [Bug]:  NVML_SUCCESS == r INTERNAL ASSERT FAILED and OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#39048](https://github.com/vllm-project/vllm/issues/39048) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;triton |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  NVML_SUCCESS == r INTERNAL ASSERT FAILED and OOM

### Issue 正文摘录

### Your current environment GPU: H200 Nvidia Drivers: 580.126.09 Nvidia CUDA : 13.0 OS: Redhat Container Runtime: Podman ### 🐛 Describe the bug I don't understand why I have all theses new errors and other OOM when I tried on my H200 GPU to launch multiples models. Theorically i Got this: ```` ```yaml version: "3.9" services: vllm-gpt: image: vllm/vllm-openai:v0.18.1 container_name: vllm-gpt devices: - nvidia.com/gpu=all ports: - "127.0.0.1:8001:8000" volumes: - /data/huggingface:/root/.cache/huggingface ipc: host environnement: - HF_TOKEN="TOKEN" command: > --model openai/gpt-oss-120b --no-enable-prefix-caching --max-cudagraph-capture-size 2048 --max-num-batched-tokens 8192 --stream-interval 20 --max-model-len 16384 --max-num-seqs 10 --tensor-parallel-size 1 --enable-auto-tool-choice --tool-call-parser openai --gpu-memory-utilization 0.4 --port 8000 --api-key YYYYYYYYYYYYYYYYYYYYYYYYYY vllm-qwen: image: vllm/vllm-openai:v0.18.1 container_name: vllm-qwen devices: - nvidia.com/gpu=all ports: - "127.0.0.1:8002:8000" volumes: - /data/huggingface:/root/.cache/huggingface ipc: host command: > --model Qwen/Qwen3.5-27B-FP8 --gpu-memory-utilization 0.4 --reasoning-parser qwen3 --enable-a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: new errors and other OOM when I tried on my H200 GPU to launch multiples models. Theorically i Got this: ```` ```yaml version: "3.9" services: vllm-gpt: image: vllm/vllm-openai:v0.18.1 container_name: vllm-gpt devices:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: mp_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['none'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_output', 'vllm::unified_m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 0 GPU to launch multiples models. Theorically i Got this: ```` ```yaml version: "3.9" services: vllm-gpt: image: vllm/vllm-openai:v0.18.1 container_name: vllm-gpt devices: - nvidia.com/gpu=all ports: - "127.0.0.1:8001:8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: /huggingface ipc: host command: > --model Qwen/Qwen3.5-27B-FP8 --gpu-memory-utilization 0.4 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder --max-model-len 16384 --kv-cache-dtype fp8 --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: # Your current environment GPU: H200 Nvidia Drivers: 580.126.09 Nvidia CUDA : 13.0 OS: Redhat Container Runtime: Podman ### 🐛 Describe the bug I don't understand why I have all theses new errors and other OOM when I tri...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
