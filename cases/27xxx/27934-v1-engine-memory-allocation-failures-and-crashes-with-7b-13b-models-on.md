# vllm-project/vllm#27934: V1 Engine: Memory allocation failures and crashes with 7B-13B models on RTX 3060 12GB

| 字段 | 值 |
| --- | --- |
| Issue | [#27934](https://github.com/vllm-project/vllm/issues/27934) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> V1 Engine: Memory allocation failures and crashes with 7B-13B models on RTX 3060 12GB

### Issue 正文摘录

## Environment - **vLLM version**: 0.11.1rc6.dev35+g29de3cdee (nightly), 0.6.4.post1 (stable) - **GPU**: NVIDIA RTX 3060 12GB (Compute 8.6, Ampere) - **CUDA**: 13.0 (Driver 580.95.05) - **OS**: Ubuntu 24.04 - **Python**: 3.12 - **Container**: `vllm/vllm-openai:nightly` and `vllm/vllm-openai:v0.6.4.post1` ## Description The V1 engine consistently fails to initialize with 7B-13B models on RTX 3060 12GB, despite having sufficient GPU memory. Multiple memory-related errors occur across different configurations. ## Models Tested All models fail with similar errors: - `Qwen/Qwen2.5-Coder-7B-Instruct` - `Gryphe/MythoMax-L2-13b` - `NousResearch/Nous-Hermes-2-SOLAR-10.7B` - `cognitivecomputations/dolphin-2.6-mistral-7b` ## Error Patterns ### Error 1: Insufficient Memory for Cache Blocks (with CPU offload) ``` ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine. ``` **Configuration**: `--cpu-offload-gb 8 --gpu-memory-utilization 0.5` **GPU Memory Available**: 11.63 GiB total, ~6-7 GiB free after model load ### Error 2: Memory Utilization Check Failure (without CPU offload) ``` ValueError: Free memory on device (6.44/11.6...

## 现有链接修复摘要

#28241 Fix CPU offload KV cache accounting and align CUDA xformers pin | #28810 v1: account for CPU offload capacity in KV cache check | #28812 v1: clamp max_model_len when KV cache exceeds GPU budget

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rashes with 7B-13B models on RTX 3060 12GB stale ## Environment - **vLLM version**: 0.11.1rc6.dev35+g29de3cdee (nightly), 0.6.4.post1 (stable) - **GPU**: NVIDIA RTX 3060 12GB (Compute 8.6, Ampere) - **CUDA**: 13.0 (Driv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: V1 Engine: Memory allocation failures and crashes with 7B-13B models on RTX 3060 12GB stale ## Environment - **vLLM version**: 0.11.1rc6.dev35+g29de3cdee (nightly), 0.6.4.post1 (stable) - **GPU**: NVIDIA RTX 3060 12GB (...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: nitialize with 7B-13B models on RTX 3060 12GB, despite having sufficient GPU memory. Multiple memory-related errors occur across different configurations. ## Models Tested All models fail with similar errors: - `Qwen/Qw...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: V1 Engine: Memory allocation failures and crashes with 7B-13B models on RTX 3060 12GB stale ## Environment - **vLLM version**: 0.11.1rc6.dev35+g29de3cdee (nightly), 0.6.4.post1 (stable) - **GPU**: NVIDIA RTX 3060 12GB (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: mory allocation failures and crashes with 7B-13B models on RTX 3060 12GB stale ## Environment - **vLLM version**: 0.11.1rc6.dev35+g29de3cdee (nightly), 0.6.4.post1 (stable) - **GPU**: NVIDIA RTX 3060 12GB (Compute 8.6,...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28241](https://github.com/vllm-project/vllm/pull/28241) | closes_keyword | 0.95 | Fix CPU offload KV cache accounting and align CUDA xformers pin | Closes #27934. |
| [#28810](https://github.com/vllm-project/vllm/pull/28810) | closes_keyword | 0.95 | v1: account for CPU offload capacity in KV cache check | Fixes #27934. ## Testing - `pytest tests/v1/kv_offload/test_cpu_offloading.py` |
| [#28812](https://github.com/vllm-project/vllm/pull/28812) | mentioned | 0.6 | v1: clamp max_model_len when KV cache exceeds GPU budget | cases where the clamp still cannot fit Addresses the second item in #27934. ## Testing - `pytest tests/v1/kv_offload/test_cpu_offloading.py` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
