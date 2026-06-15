# vllm-project/vllm#26884: [Bug]: Qwen3-VL-8B No available memory for the cache blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#26884](https://github.com/vllm-project/vllm/issues/26884) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-8B No available memory for the cache blocks

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deployment Command: docker run --gpus '"device=1"' -p 38943:38943 \ --name Qwen3-VL-8B \ -v /storage/models/Qwen/Qwen3-VL-8B-Instruct:/storage/model \ swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/vllm/vllm-openai:v0.11.0 \ --served-model-name Qwen3-VL-8B \ --model /storage/model \ --port 38943 \ --api-key EMPTY \ --tensor-parallel-size 1 \ --gpu_memory_utilization 0.3 \ --mm-processor-kwargs '{"min_pixels": 200704, "max_pixels": 1003520, "fps": 2.0}' \ --max_model_len 8192 Issue Description: Before deployment, GPU device=1 was already using 32,196 MiB out of 81,920 MiB (approximately 39% utilization). When I attempted to deploy the container, an error was thrown. EngineCore_DP0 pid=269) INFO 10-14 22:48:36 [backends.py:559] Dynamo bytecode transform time: 5.80 s (EngineCore_DP0 pid=269) INFO 10-14 22:48:40 [backends.py:197] Cache the graph for dynamic shape for later use (EngineCore_DP0 pid=269) INFO 10-14 22:49:05 [backends.py:218] Compiling a graph for dynamic shape takes 28.96 s (EngineCore_DP0 pid=269) INFO 10-14 22:49:17 [monitor.py:34] torch.compile takes 34.76 s in total (EngineCore_DP0 pid=269) INFO 10-14 22:49:18 [...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug Deployment Command: docker run --gpus '"device=1"' -p 38943:38943 \ --name Qwen3-VL-8B \ -v /storage/models/Qwen/Qwen3-VL-8B-Instruct:/storage/model \ swr.cn-north-4.myhua...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-VL-8B No available memory for the cache blocks bug ### Your current environment ### 🐛 Describe the bug Deployment Command: docker run --gpus '"device=1"' -p 38943:38943 \ --name Qwen3-VL-8B \ -v /storage/m
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: iner, an error was thrown. EngineCore_DP0 pid=269) INFO 10-14 22:48:36 [backends.py:559] Dynamo bytecode transform time: 5.80 s (EngineCore_DP0 pid=269) INFO 10-14 22:48:40 [backends.py:197] Cache the graph for dynamic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Qwen3-VL-8B No available memory for the cache blocks bug ### Your current environment ### 🐛 Describe the bug Deployment Command: docker run --gpus '"device=1"' -p 38943:38943 \ --name Qwen3-VL-8B \ -v /storage/mo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
