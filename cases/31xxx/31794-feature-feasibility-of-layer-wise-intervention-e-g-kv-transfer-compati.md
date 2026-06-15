# vllm-project/vllm#31794: [Feature]: Feasibility of Layer-wise Intervention (e.g., KV Transfer) compatible with V1 CUDA Graph architecture?

| 字段 | 值 |
| --- | --- |
| Issue | [#31794](https://github.com/vllm-project/vllm/issues/31794) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;kernel;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Feasibility of Layer-wise Intervention (e.g., KV Transfer) compatible with V1 CUDA Graph architecture?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Motivation I am working on a research project involving Layer-wise KV Cache Transmission (streaming KV cache to another instance layer-by-layer during inference) to minimize TTFT in migration scenarios. My goal is to insert custom logic (e.g., a network transmission or buffer copy operation) between Transformer layers. My Observations I have analyzed the vLLM V1 codebase and noticed the following: Source Level: The model definitions (e.g., vllm/model_executor/models/llama.py) still use a Python for loop to iterate over layers. Runtime Level: The V1 engine seems to rely heavily on CUDA Graph Capture (vllm/v1/cudagraph_dispatcher.py) and torch.compile (vllm/compilation/) for performance. The Problem If I insert Python-side logic (e.g., CPU synchronization or network I/O) inside the layer loop, it presumably breaks the CUDA Graph capture, forcing the engine to fallback to eager mode (via enforce_eager=True), which significantly degrades performance. Questions I would like to ask for advice on the feasibility of implementing layer-level interventions in the V1 architecture: Custom Ops in Graph: Is there a recommended way to register a custom "Gr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: eavily on CUDA Graph Capture (vllm/v1/cudagraph_dispatcher.py) and torch.compile (vllm/compilation/) for performance. The Problem If I insert Python-side logic (e.g., CPU synchronization or network I/O) inside the layer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: bility of Layer-wise Intervention (e.g., KV Transfer) compatible with V1 CUDA Graph architecture? feature request ### 🚀 The feature, motivation and pitch Motivation I am working on a research project involving Layer-wis...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: V1 engine seems to rely heavily on CUDA Graph Capture (vllm/v1/cudagraph_dispatcher.py) and torch.compile (vllm/compilation/) for performance. The Problem If I insert Python-side logic (e.g., CPU synchronization or netw...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: itch Motivation I am working on a research project involving Layer-wise KV Cache Transmission (streaming KV cache to another instance layer-by-layer during inference) to minimize TTFT in migration scenarios. My goal is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lyzed the vLLM V1 codebase and noticed the following: Source Level: The model definitions (e.g., vllm/model_executor/models/llama.py) still use a Python for loop to iterate over layers. Runtime Level: The V1 engine seem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
