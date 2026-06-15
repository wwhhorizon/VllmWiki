# vllm-project/vllm#39078: [Bug]: Sleep-Mode throws an error on DGX-Spark

| 字段 | 值 |
| --- | --- |
| Issue | [#39078](https://github.com/vllm-project/vllm/issues/39078) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;fp8;operator |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Sleep-Mode throws an error on DGX-Spark

### Issue 正文摘录

### Your current environment I'm running vllm on nvidia dgx spark in the latest container from nvidia. https://catalog.ngc.nvidia.com/orgs/nvidia/containers/vllm?version=26.03-py3 Driver Version: 590.48.01 CUDA Version: 13.1 ### 🐛 Describe the bug This is my Containerfile: FROM nvcr.io/nvidia/vllm:26.03-py3 RUN pip install --no-cache-dir --upgrade pip && \ pip install --no-cache-dir fastsafetensors && \ pip install --no-cache-dir git+https://github.com/huggingface/transformers.git This is my compose.yml services: nvllm: #image: nvcr.io/nvidia/vllm:26.03-py3 build: context: . dockerfile: Containerfile container_name: nvllm privileged: true shm_size: '32gb' networks: - proxy_net environment: - NVIDIA_VISIBLE_DEVICES=all - VLLM_API_KEY=xTq3QGBJjMFnyaUn2VcyHg1yGV3sLg9L5Z2ZxH - HUGGING_FACE_HUB_TOKEN=${HUG_TOKEN} - VLLM_SERVER_DEV_MODE=1 - FLASHINFER_DISABLE_AUTOTUNER=1 - FLASHINFER_DETERMINISTIC=1 volumes: - ~/.cache/huggingface:/root/.cache/huggingface - ~/.cache/vllm:/root/.cache/vllm expose: - "11434" ipc: host cap_add: - SYS_ADMIN deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu, utility] # vLLM Configuration for Qwen3-Coder on GB10 # Contex...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: from nvidia. https://catalog.ngc.nvidia.com/orgs/nvidia/containers/vllm?version=26.03-py3 Driver Version: 590.48.01 CUDA Version: 13.1 ### 🐛 Describe the bug This is my Containerfile: FROM nvcr.io/nvidia/vllm:26.03-py3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: onfiguration for Qwen3-Coder on GB10 # Context: 256k tokens | Cache: FP8 with Scales | System Headroom: ~51GB (at 0.60) command: > vllm serve "RedHatAI/Qwen3-Coder-Next-NVFP4" --host 0.0.0.0 --port 11434 --enable-sleep-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: stsafetensors && \ pip install --no-cache-dir git+https://github.com/huggingface/transformers.git This is my compose.yml services: nvllm: #image: nvcr.io/nvidia/vllm:26.03-py3 build: context: . dockerfile: Containerfile...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nvidia/containers/vllm?version=26.03-py3 Driver Version: 590.48.01 CUDA Version: 13.1 ### 🐛 Describe the bug This is my Containerfile: FROM nvcr.io/nvidia/vllm:26.03-py3 RUN pip install --no-cache-dir --upgrade pip && \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: GGING_FACE_HUB_TOKEN=${HUG_TOKEN} - VLLM_SERVER_DEV_MODE=1 - FLASHINFER_DISABLE_AUTOTUNER=1 - FLASHINFER_DETERMINISTIC=1 volumes: - ~/.cache/huggingface:/root/.cache/huggingface - ~/.cache/vllm:/root/.cache/vllm expose:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
