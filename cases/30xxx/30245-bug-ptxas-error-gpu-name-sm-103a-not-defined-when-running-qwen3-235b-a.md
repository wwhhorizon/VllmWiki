# vllm-project/vllm#30245: [Bug]: PTXAS error: gpu-name sm_103a not defined when running Qwen3-235B-A22B-Instruct-2507 with vllm-openai:v0.12.0

| 字段 | 值 |
| --- | --- |
| Issue | [#30245](https://github.com/vllm-project/vllm/issues/30245) |
| 状态 | open |
| 标签 | bug;stale;nvidia |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda;triton |
| 症状 | crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PTXAS error: gpu-name sm_103a not defined when running Qwen3-235B-A22B-Instruct-2507 with vllm-openai:v0.12.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I try to serve the model Qwen/Qwen3-235B-A22B-Instruct-2507 using the official vllm/vllm-openai:v0.12.0 Docker image, vLLM fails to start the engine core due to a PTXAS / Triton codegen error: ptxas fatal : Value 'sm_103a' is not defined for option 'gpu-name' It looks like Triton / ptxas does not recognize the GPU architecture sm_103a that vLLM is trying to target. Environment vLLM version: v0.12.0 (Docker image vllm/vllm-openai:v0.12.0) Model: Qwen/Qwen3-235B-A22B-Instruct-2507 CUDA / Driver: NVIDIA driver: 580.105.08 CUDA version 13.0 GPU(s): Type: NVIDIA B300 SXM6 AC Count: 4 (using devices 4,5,6,7) OS (host): 24.04 Container runtime: Docker docker run --gpus '"device=4,5,6,7"' --ipc=host \ --ulimit memlock=-1 \ --ulimit stack=67108864 \ -p 8000:8000 \ -v /raid/huggingface:/root/.cache/huggingface \ vllm/vllm-openai:v0.12.0 \ --model Qwen/Qwen3-235B-A22B-Instruct-2507 \ --tensor-parallel-size 4 \ --max-model-len 32768 \ --gpu-memory-utilization 0.90 The container starts, but the engine core fails to initialize. The worker process crashes with a Triton / PTXAS error about sm_103a: (EngineCore_DP0 pid=270) ERROR 12-07 23:47...

## 现有链接修复摘要

#37630 [Bugfix] Add early detection for CUDA < 13.0 on sm_103+ GPUs (GB300)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: try to serve the model Qwen/Qwen3-235B-A22B-Instruct-2507 using the official vllm/vllm-openai:v0.12.0 Docker image, vLLM fails to start the engine core due to a PTXAS / Triton codegen error: ptxas fatal : Value 'sm_103a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: PTXAS error: gpu-name sm_103a not defined when running Qwen3-235B-A22B-Instruct-2507 with vllm-openai:v0.12.0 bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug When I try to serve the model Qwe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: PTXAS error: gpu-name sm_103a not defined when running Qwen3-235B-A22B-Instruct-2507 with vllm-openai:v0.12.0 bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug When I try to serve the model Qwe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: .12.0 Docker image, vLLM fails to start the engine core due to a PTXAS / Triton codegen error: ptxas fatal : Value 'sm_103a' is not defined for option 'gpu-name' It looks like Triton / ptxas does not recognize the GPU a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: (EngineCore_DP0 pid=270) ERROR 12-07 23:47:30 [core.py:843] num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=270) ERROR 12-07 23:47:30 [core.py:843] File "/usr/local/lib/...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37630](https://github.com/vllm-project/vllm/pull/37630) | closes_keyword | 0.95 | [Bugfix] Add early detection for CUDA < 13.0 on sm_103+ GPUs (GB300) | Fixes #30245 ## Test Plan Tested on GB300 (sm_103) with `vllm/vllm-openai:nightly` (cu129): ```bash python3 -m vllm.entrypoints.openai.api_server --model facebook/opt-125 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
