# vllm-project/vllm#34356: [Bug]: FP8 MoE Backend Regression: Nemotron-3 Models Fail in vLLM 0.15.0/0.15.1

| 字段 | 值 |
| --- | --- |
| Issue | [#34356](https://github.com/vllm-project/vllm/issues/34356) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;kernel;moe;quantization;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 MoE Backend Regression: Nemotron-3 Models Fail in vLLM 0.15.0/0.15.1

### Issue 正文摘录

### Your current environment ## Description Nemotron-3 models with FP8 quantization fail to load in vLLM 0.15.0 and 0.15.1, but work correctly in vLLM 0.14.1. ## Environment - **OS**: Rocky Linux 8.10 (Green Obsidian) - **Kernel**: 4.18.0-553.51.1.el8_10.x86_64 - **GPU**: NVIDIA L40S - **Driver Version**: 570.195.03 - **CUDA Version**: 12.8 - **Python**: 3.12 (from Singularity container) - **vLLM Working Version**: 0.14.1 - **vLLM Failing Versions**: 0.15.0, 0.15.1 ## Model Details - **Model**: nemotron-3-nano-30b-a3b-fp8 - **Architecture**: NemotronHForCausalLM - **Quantization**: ModelOpt FP8 - **Format**: FP8 MoE (Mixture of Experts) ## Reproduction Steps 1. Attempt to load Nemotron-3 FP8 model with vLLM 0.15.0/0.15.1 2. Use command similar to: ```bash vllm serve /path/to/nemotron-3-nano-30b-a3b-fp8 \ --served-model-name nemotron-3-nano-30b-a3b-fp8 \ --dtype auto \ --kv-cache-dtype auto \ --max-model-len 262144 \ --max-num-seqs 4 \ --gpu-memory-utilization 0.90 \ --enforce-eager \ --tensor-parallel-size 1 \ --trust-remote-code ``` ## Error Details **Error in vLLM 0.15.0/0.15.1:** **Working Behavior in vLLM 0.14.1:** - Successfully selects Triton backend for FP8 MoE - Model load...

## 现有链接修复摘要

#34404 [Bug Fix] Enable non-gated MoE support in Triton backends (#34356)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 MoE Backend Regression: Nemotron-3 Models Fail in vLLM 0.15.0/0.15.1 bug;unstale ### Your current environment ## Description Nemotron-3 models with FP8 quantization fail to load in vLLM 0.15.0 and 0.15.1, but...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: FP8 MoE Backend Regression: Nemotron-3 Models Fail in vLLM 0.15.0/0.15.1 bug;unstale ### Your current environment ## Description Nemotron-3 models with FP8 quantization fail to load in vLLM 0.15.0 and 0.15.1, but...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: FP8 MoE Backend Regression: Nemotron-3 Models Fail in vLLM 0.15.0/0.15.1 bug;unstale ### Your current environment ## Description Nemotron-3 models with FP8 quantization fail to load in vLLM 0.15.0 and 0.15.1, but...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ernel**: 4.18.0-553.51.1.el8_10.x86_64 - **GPU**: NVIDIA L40S - **Driver Version**: 570.195.03 - **CUDA Version**: 12.8 - **Python**: 3.12 (from Singularity container) - **vLLM Working Version**: 0.14.1 - **vLLM Failing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l8_10.x86_64 - **GPU**: NVIDIA L40S - **Driver Version**: 570.195.03 - **CUDA Version**: 12.8 - **Python**: 3.12 (from Singularity container) - **vLLM Working Version**: 0.14.1 - **vLLM Failing Versions**: 0.15.0, 0.15....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34404](https://github.com/vllm-project/vllm/pull/34404) | closes_keyword | 0.95 | [Bug Fix] Enable non-gated MoE support in Triton backends (#34356) | Fixes #34356 FP8 MoE models like NemotronH (nemotron-3-nano-30b-a3b-fp8) fail to load because TritonExperts and BatchedTritonExperts incorrectly reject non-gated MoE configuratio |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
