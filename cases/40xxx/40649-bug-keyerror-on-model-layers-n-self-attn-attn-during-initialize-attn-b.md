# vllm-project/vllm#40649: [Bug]: KeyError on model.layers.N.self_attn.attn during initialize_attn_backend with pipeline_parallel_size=4 (V1 engine + Ray)

| 字段 | 值 |
| --- | --- |
| Issue | [#40649](https://github.com/vllm-project/vllm/issues/40649) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError on model.layers.N.self_attn.attn during initialize_attn_backend with pipeline_parallel_size=4 (V1 engine + Ray)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Current Environment - vLLM version: 0.19.1 - Python: 3.12 - CUDA: 12.x - GPU: 4× NVIDIA RTX 4090 (24 GB each), one per node - OS: Ubuntu (WSL2 detected on workers — `pin_memory=False`) - Ray version: (see logs — connected to existing cluster) - Quantization: awq_marlin - Attention backend: FLASH_ATTN (FlashAttention v2) ### Bug Description When serving a model with `--pipeline-parallel-size 4` and `--tensor-parallel-size 1` across 4 nodes (1 GPU per node) using the Ray distributed executor backend, the V1 engine crashes during KV cache initialization with a `KeyError` on attention layer names. The error occurs in `get_attn_backends_for_group` inside `gpu_model_runner.py`. Each pipeline parallel worker only holds its local stage layers (20 layers each for an 80-layer model with pp=4), but the KV cache group spec references global layer indices (e.g. `model.layers.20`, `model.layers.40`, `model.layers.60`). These global keys don't exist in the worker-local `layers` dict, causing a `KeyError`. The bug affects PP ranks 1, 2, and 3 (all non-zero ranks). PP rank 0 (layers 0–19) succeeds. All prior initialization steps succeed: - Ra...

## 现有链接修复摘要

#40678 [Bugfix] Fix KeyError in get_attn_backends_for_group when using PP | #40776 [Bugfix] V1: skip non-local layers in get_attn_backends_for_group under PP

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: environment ### 🐛 Describe the bug ### Current Environment - vLLM version: 0.19.1 - Python: 3.12 - CUDA: 12.x - GPU: 4× NVIDIA RTX 4090 (24 GB each), one per node - OS: Ubuntu (WSL2 detected on workers — `pin_memory=Fal...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: KeyError on model.layers.N.self_attn.attn during initialize_attn_backend with pipeline_parallel_size=4 (V1 engine + Ray) bug ### Your current environment ### 🐛 Describe the bug ### Current Environment - vLLM vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: he bug ### Current Environment - vLLM version: 0.19.1 - Python: 3.12 - CUDA: 12.x - GPU: 4× NVIDIA RTX 4090 (24 GB each), one per node - OS: Ubuntu (WSL2 detected on workers — `pin_memory=False`) - Ray version: (see log...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ch), one per node - OS: Ubuntu (WSL2 detected on workers — `pin_memory=False`) - Ray version: (see logs — connected to existing cluster) - Quantization: awq_marlin - Attention backend: FLASH_ATTN (FlashAttention v2) ###...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: KeyError on model.layers.N.self_attn.attn during initialize_attn_backend with pipeline_parallel_size=4 (V1 engine + Ray) bug ### Your current environment ### 🐛 Describe the bug ### Current Environment - vLLM vers...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40678](https://github.com/vllm-project/vllm/pull/40678) | closes_keyword | 0.95 | [Bugfix] Fix KeyError in get_attn_backends_for_group when using PP | Closes #40649. When models use pipeline parallel, each rank only has its local stage's layers. But the code still tries to access `kv_cache_group_spec.layer_names`, which are g |
| [#40776](https://github.com/vllm-project/vllm/pull/40776) | closes_keyword | 0.95 | [Bugfix] V1: skip non-local layers in get_attn_backends_for_group under PP | Fixes #40649. ## The bug Under `pipeline_parallel_size > 1` with the V1 engine (Ray backend in the report), non-zero PP ranks crash during `initialize_attn_backend` with e.g.: \ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
