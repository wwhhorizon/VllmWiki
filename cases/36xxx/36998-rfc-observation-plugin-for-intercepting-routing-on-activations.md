# vllm-project/vllm#36998: [RFC]: Observation Plugin for Intercepting & Routing on Activations

| 字段 | 值 |
| --- | --- |
| Issue | [#36998](https://github.com/vllm-project/vllm/issues/36998) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;kernel;operator;triton |
| 症状 | slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Observation Plugin for Intercepting & Routing on Activations

### Issue 正文摘录

### Motivation. **Summary** This RFC proposes the introduction of an **Observation Plugin** into vLLM. It allows developers to register custom plugins that can securely intercept, inspect, and react to model activations (hidden states) during the forward pass of generation, without requiring core vLLM code modifications. ## Motivation ### Problem Statement There is a growing need in the LLM ecosystem to observe model activations natively at runtime. Use cases include: - **Safety and Alignment:** Scanning hidden states for policy violations and halting toxic requests early. - **Auditing and Interpretability:** Probing activations to understand model behavior or extracting conceptual representations. - **Dynamic Routing:** Early exiting or routing requests based on confidence scores derived from intermediate layers. Currently, developers must heavily fork and modify vLLM's core execution loops and PyTorch models to extract this data. This leads to massive maintenance overhead, broken upgrades, and an inability to easily share or compose different observation tools. ### Goals of This RFC - Provide a clean, stable, and unified API for plugins to access internal model activations. - Av...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: for plugins to access internal model activations. - Avoid any noticeable latency overhead when no plugins (or no relevant layers) are active. - Support continuous batching natively: map batched, flattened tensor activat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: gnment:** Scanning hidden states for policy violations and halting toxic requests early. - **Auditing and Interpretability:** Probing activations to understand model behavior or extracting conceptual representations. -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: essly intercepts PyTorch layer outputs inside the _GPUModelRunner_. ### Architecture Overview ```mermaid graph TD Engine["vLLM Engine"] --> Manager["PluginManager"] Manager --> Plugins["Observation Plugins"] GPU["GPU Mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [RFC]: Observation Plugin for Intercepting & Routing on Activations RFC ### Motivation. **Summary** This RFC proposes the introduction of an **Observation Plugin** into vLLM. It allows developers to register custom plug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nal, individual Request IDs. - Enable plugins to asynchronously abort specific requests mid-generation (e.g., if a safety scanner flags a request) without affecting other requests in the same batch. ### Proposed Change....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
