# vllm-project/vllm#43561: [Usage]: How to run Qwen3.5 models on V100 given the conflicting requirements of transformers version and vLLM architecture support

| 字段 | 值 |
| --- | --- |
| Issue | [#43561](https://github.com/vllm-project/vllm/issues/43561) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to run Qwen3.5 models on V100 given the conflicting requirements of transformers version and vLLM architecture support

### Issue 正文摘录

### Your current environment *(The environment collection script cannot be executed because this machine is deployed in an air-gapped/intranet environment. However, the core hardware is NVIDIA V100 GPU, running CUDA 12.4 and Python 3.10.)* ### How would you like to use vllm ### Description I want to deploy and run inference for the Qwen3.5 series models (e.g., Qwen3.5-9B) on an NVIDIA V100 GPU using vLLM. ### The Problem / Dilemma I am currently facing a dependency and compatibility catch-22: 1. **Model Requirement:** The Qwen3.5 models require `transformers>=5.x` (or specific latest versions) to be correctly tokenized and loaded, which is only integrated into recent vLLM releases. 2. **Hardware Constraint:** Newer versions of vLLM have dropped full support or optimized kernels (like FlashAttention) for the Volta architecture (V100, CC 7.0), causing compilation errors or runtime failures when trying to launch the service. If I downgrade vLLM to an older version that natively supports V100, it cannot load Qwen3.5 due to the outdated `transformers` and structural differences. If I upgrade vLLM, it fails on V100. ### Questions 1. Is there a recommended/stable vLLM version or a specif...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: wen3.5 models on V100 given the conflicting requirements of transformers version and vLLM architecture support usage ### Your current environment *(The environment collection script cannot be executed because this machi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: V100 given the conflicting requirements of transformers version and vLLM architecture support usage ### Your current environment *(The environment collection script cannot be executed because this machine is deployed in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: er versions of vLLM have dropped full support or optimized kernels (like FlashAttention) for the Volta architecture (V100, CC 7.0), causing compilation errors or runtime failures when trying to launch the service. If I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to run Qwen3.5 models on V100 given the conflicting requirements of transformers version and vLLM architecture support usage ### Your current environment *(The environment collection script cannot be execut...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: irement:** The Qwen3.5 models require `transformers>=5.x` (or specific latest versions) to be correctly tokenized and loaded, which is only integrated into recent vLLM releases. 2. **Hardware Constraint:** Newer version...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
