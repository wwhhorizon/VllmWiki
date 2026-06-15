# vllm-project/vllm#25590: [RFC]: llama.cpp CPU Backend for Enhanced CPU Performance & CI Testing

| 字段 | 值 |
| --- | --- |
| Issue | [#25590](https://github.com/vllm-project/vllm/issues/25590) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: llama.cpp CPU Backend for Enhanced CPU Performance & CI Testing

### Issue 正文摘录

### Motivation. ## Problem Statement I've been working with the vLLM Production Stack and noticed several CPU-related issues that are limiting deployment flexibility and causing real problems for users. ### Current Issues I've Observed - **CPU Performance Bottlenecks**: There's an [active issue](https://github.com/vllm-project/vllm/issues/10971) where CPU mode only uses a single core despite multi-core hardware being available - **Runtime Stability Problems**: Users are hitting [kernel compilation errors](https://github.com/vllm-project/vllm/issues/10478) with "Unable to get JIT kernel for brgemm" that cause complete failures - **Limited Production Readiness**: The current CPU backend feels more like a fallback option than something you'd actually deploy in production - **Platform Support Gaps**: Inconsistent behavior across different CPU architectures and deployment scenarios ### Roadmap Alignment Looking at the [Q3 2025 roadmap](https://github.com/vllm-project/vllm/issues/20336), there's a clear priority for "Stable CPU Release with Wheels and Containers" under Intel CPU support. The [production stack Q2 roadmap](https://github.com/vllm-project/production-stack/issues/300) also...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [RFC]: llama.cpp CPU Backend for Enhanced CPU Performance & CI Testing RFC ### Motivation. ## Problem Statement I've been working with the vLLM Production Stack and noticed several CPU-related issues that are limiting d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: llama.cpp CPU Backend for Enhanced CPU Performance & CI Testing RFC ### Motivation. ## Problem Statement I've been working with the vLLM Production Stack and noticed several CPU-related issues that are limiting d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [RFC]: llama.cpp CPU Backend for Enhanced CPU Performance & CI Testing RFC ### Motivation. ## Problem Statement I've been working with the vLLM Production Stack and noticed several CPU-related issues that are limiting d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: - **Platform Support Gaps**: Inconsistent behavior across different CPU architectures and deployment scenarios ### Roadmap Alignment Looking at the [Q3 2025 roadmap](https://github.com/vllm-project/vllm/issues/20336), t...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: com/vllm-project/vllm/issues/10478) with "Unable to get JIT kernel for brgemm" that cause complete failures - **Limited Production Readiness**: The current CPU backend feels more like a fallback option than something yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
