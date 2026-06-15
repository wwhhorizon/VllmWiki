# vllm-project/vllm#34076: [Bug]: KV Cache Memory Bottleneck Calculation in Pipeline Parallel (_check_enough_kv_cache_memory in get_kv_cache_configs)

| 字段 | 值 |
| --- | --- |
| Issue | [#34076](https://github.com/vllm-project/vllm/issues/34076) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;fp8 |
| 症状 |  |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV Cache Memory Bottleneck Calculation in Pipeline Parallel (_check_enough_kv_cache_memory in get_kv_cache_configs)

### Issue 正文摘录

### Your current environment 0: NVIDIA GeForce RTX 5070 Ti 16303MiB 1: NVIDIA GeForce RTX 5090 D 32607MiB vllm-0.15.2rc1.dev93+g11a4c9d30.cu128-cp312-cp312-linux_x86_64.whl ### 🐛 Describe the bug I am trying to deploy a vLLM service locally for my OpenClaw backend, so I need a sufficiently long context length. I set VLLM_PP_LAYER_PARTITION=16,32 to assign the model layers across the two GPUs (an RTX 5070 Ti with 16GB and an RTX 5090D with 32GB): `bash VLLM_PP_LAYER_PARTITION=16,32 CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0,1 vllm serve ./Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 --gpu-memory-utilization 0.9 --served-model-name Qwen3-Coder-30B-A3B-Instruct-FP8 --pipeline-parallel-size 2 --enable-chunked-prefill --enable-auto-tool-choice --tool-call-parser qwen3_coder` I encountered the following error: `(EngineCore_DP0 pid=1094) ValueError: To serve at least one request with the models's max seq len (262144), (24.0 GiB KV cache is needed, which is larger than the available KV cache memory (3.18 GiB). Based on the available memory, the estimated maximum model length is 34736. Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. See...

## 现有链接修复摘要

#34078 [bugfix] fix: correctly identify bottleneck worker in pipeline parallel KV cache allocation (#34076)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: CUDA_VISIBLE_DEVICES=0,1 vllm serve ./Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 --gpu-memory-utilization 0.9 --served-model-name Qwen3-Coder-30B-A3B-Instruct-FP8 --pipeline-parallel-size 2 --enable-chunked-prefill --enable-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: et_kv_cache_configs) bug ### Your current environment 0: NVIDIA GeForce RTX 5070 Ti 16303MiB 1: NVIDIA GeForce RTX 5090 D 32607MiB vllm-0.15.2rc1.dev93+g11a4c9d30.cu128-cp312-cp312-linux_x86_64.whl ### 🐛 Describe the bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tion in Pipeline Parallel (_check_enough_kv_cache_memory in get_kv_cache_configs) bug ### Your current environment 0: NVIDIA GeForce RTX 5070 Ti 16303MiB 1: NVIDIA GeForce RTX 5090 D 32607MiB vllm-0.15.2rc1.dev93+g11a4c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 3-Coder-30B-A3B-Instruct-FP8 --pipeline-parallel-size 2 --enable-chunked-prefill --enable-auto-tool-choice --tool-call-parser qwen3_coder` I encountered the following error: `(EngineCore_DP0 pid=1094) ValueError: To ser...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: be the bug I am trying to deploy a vLLM service locally for my OpenClaw backend, so I need a sufficiently long context length. I set VLLM_PP_LAYER_PARTITION=16,32 to assign the model layers across the two GPUs (an RTX 5...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34078](https://github.com/vllm-project/vllm/pull/34078) | closes_keyword | 0.95 | [bugfix] fix: correctly identify bottleneck worker in pipeline parallel KV cache allocation (#34076) | fix: correctly identify bottleneck worker in pipeline parallel KV cache allocation (#34076) ## Purpose In pipeline parallel, the bottleneck worker for KV cache allocation is dete |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
