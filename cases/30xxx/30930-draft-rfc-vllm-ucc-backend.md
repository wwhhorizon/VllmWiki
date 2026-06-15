# vllm-project/vllm#30930: [Draft] [RFC]: vLLM + UCC Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#30930](https://github.com/vllm-project/vllm/issues/30930) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;operator |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Draft] [RFC]: vLLM + UCC Backend

### Issue 正文摘录

### Motivation. Integrating UCC (Unified Collective Communication) https://github.com/openucx/ucc into vLLM as an optional communication backend. ### Strengthening vLLM’s Backend Abstraction - UCC supports a wide range of hardware backends, - It decouples vLLM’s distributed engine from any single communication API. - It allows developers to register new communication backends through UCC’s standardized API. - This modularity supports future frameworks, accelerators, or transport technologies with minimal changes to vLLM internals. - Through UCC vLLM can advantage of many UCC’s key design philosophies, such as: - Enabling framework to use optimized collective implementations provided by the underlying transport (eg. ROCm/UCX for AMD, Level-Zero for Intel, and CUDA for NVIDIA). - By providing a unified interface through UCC vLLM takes advantage of many of its benefits. - Enable performance-optimized collectives on diverse hardware platforms through existing vendor or community-supported UCC transports. - Abstract away vendor-specific libraries behind a common API, reducing direct dependencies in vLLM’s communication layer. - Provide cross-platform support across CPU, GPU, and multi-...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: zed collective implementations provided by the underlying transport (eg. ROCm/UCX for AMD, Level-Zero for Intel, and CUDA for NVIDIA). - By providing a unified interface through UCC vLLM takes advantage of many of its b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Draft] [RFC]: vLLM + UCC Backend RFC;stale ### Motivation. Integrating UCC (Unified Collective Communication) https://github.com/openucx/ucc into vLLM as an optional communication backend. ### Strengthening vLLM’s Back
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vendor or community-supported UCC transports. - Abstract away vendor-specific libraries behind a common API, reducing direct dependencies in vLLM’s communication layer. - Provide cross-platform support across CPU, GPU,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r – backend introduction or algorithm optimizations through UCC’s plugin model without modifying vLLM directly. - Shared maintenance effort – allows vLLM to benefit from upstream advancements with minimal internal chang...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: formance experimentation framework – With UCC integrated, developers can benchmark and explore new algorithmic strategies for collective operations within vLLM without modifying its core communication layer. ### Propose...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
