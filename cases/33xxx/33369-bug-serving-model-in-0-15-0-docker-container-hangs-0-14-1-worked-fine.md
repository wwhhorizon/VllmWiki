# vllm-project/vllm#33369: [Bug]: Serving model in 0.15.0 Docker container hangs - 0.14.1 worked fine

| 字段 | 值 |
| --- | --- |
| Issue | [#33369](https://github.com/vllm-project/vllm/issues/33369) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;quantization |
| 症状 | import_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Serving model in 0.15.0 Docker container hangs - 0.14.1 worked fine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug As the title says, this container worked fine in 0.14.1. However, it hangs in 0.15.0. Docker-compose config for this container is as follows: ``` vllm-gpt-oss: container_name: vllm-gpt-oss image: vllm/vllm-openai:latest-cu130 restart: always ipc: host environment: OMP_NUM_THREADS: '16' HF_HUB_OFFLINE: '0' TIKTOKEN_RS_CACHE_DIR: /tmp/encodings TIKTOKEN_ENCODINGS_BASE: /tmp/encodings NCCL_DMABUF_ENABLE: '1' NCCL_P2P_LEVEL: PCI NCCL_IGNORE_CPU_AFFINITY: '1' VLLM_LOGGING_LEVEL: DEBUG volumes: - /models/vllm_cache:/root/.cache/huggingface - /models/encodings:/tmp/encodings:ro - /tmp/nvidia-mps:/tmp/nvidia-mps cpuset: 192-207 healthcheck: test: - CMD - curl - -f - http://localhost:8000/health interval: 10s retries: 10 start_period: 110s ports: - 8000:8000 command: '--model openai/gpt-oss-120b --served-model-name vllm-gpt-oss --quantization mxfp4 --tensor-parallel-size 2 --gpu-memory-utilization 0.55 --speculative-config ''{"model": "nvidia/gpt-oss-120b-Eagle3-throughput", "method": "eagle3", "num_speculative_tokens": 1}'' --port 8000' deploy: resources: reservations: devices: - driver: nvidia device_ids: - '4' - '5' capabilities: - gpu...

## 现有链接修复摘要

#33992 [Bugfix] Fix CUDA compatibility path setting for both datacenter and consumer NVIDIA GPUs

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Serving model in 0.15.0 Docker container hangs - 0.14.1 worked fine bug ### Your current environment ### 🐛 Describe the bug As the title says, this container worked fine in 0.14.1. However, it hangs in 0.15.0. Do...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Serving model in 0.15.0 Docker container hangs - 0.14.1 worked fine bug ### Your current environment ### 🐛 Describe the bug As the title says, this container worked fine in 0.14.1. However, it hangs in 0.15.0. Do...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: command: '--model openai/gpt-oss-120b --served-model-name vllm-gpt-oss --quantization mxfp4 --tensor-parallel-size 2 --gpu-memory-utilization 0.55 --speculative-config ''{"model": "nvidia/gpt-oss-120b-Eagle3-throughput"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ion mxfp4 --tensor-parallel-size 2 --gpu-memory-utilization 0.55 --speculative-config ''{"model": "nvidia/gpt-oss-120b-Eagle3-throughput", "method": "eagle3", "num_speculative_tokens": 1}'' --port 8000' deploy: resource...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: orm cuda. DEBUG 01-29 13:15:36 [utils/import_utils.py:74] Loading module triton_kernels from /usr/local/lib/python3.12/dist-packages/vllm/third_party/triton_kernels/__init__.py. DEBUG 01-29 13:15:37 [entrypoints/utils.p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33992](https://github.com/vllm-project/vllm/pull/33992) | closes_keyword | 0.95 | [Bugfix] Fix CUDA compatibility path setting for both datacenter and consumer NVIDIA GPUs | Fix #33369 Closes #34226 Fixes the core problem in https://github.com/vllm-project/vllm/issues/32373 and https://github.com/vllm-project/vllm/issues/33369, introduced from https:/ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
