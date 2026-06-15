# vllm-project/vllm#19376: [RFC]: A Strategic Framework for Extensibility and Innovation in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#19376](https://github.com/vllm-project/vllm/issues/19376) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: A Strategic Framework for Extensibility and Innovation in vLLM

### Issue 正文摘录

### Motivation. # TL;DR: This proposal outlines a strategic shift in how vLLM manages components and extensions. vLLM's support for hardware- and model-specific plugins has been a cornerstone of its growth, empowering the community to greatly expand the project's hardware coverage and functionality. To build upon this foundation and extend that same flexibility across the entire application, we propose evolving from this specific plugin model to a comprehensive **Dependency Injection (DI)** framework. This transition will solve the underlying challenges of brittle, out-of-tree extensions and, more importantly, provide a robust architectural foundation. Adopting DI will **accelerate iterative development**, simplify testing, and pave the way for advanced capabilities like A/B testing. We recommend a pragmatic, phased adoption, starting with a lightweight simulation of DI to demonstrate value before integrating a full-fledged framework like `dependency-injector`. # The Common Goal: Stable and Decoupled Components At their core, both the existing plugin ideology and a formal DI framework share the same fundamental goals: * **Stable Component APIs**: To create clearly defined, version...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ges components and extensions. vLLM's support for hardware- and model-specific plugins has been a cornerstone of its growth, empowering the community to greatly expand the project's hardware coverage and functionality....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ndation. Adopting DI will **accelerate iterative development**, simplify testing, and pave the way for advanced capabilities like A/B testing. We recommend a pragmatic, phased adoption, starting with a lightweight simul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: RFC]: A Strategic Framework for Extensibility and Innovation in vLLM RFC;stale ### Motivation. # TL;DR: This proposal outlines a strategic shift in how vLLM manages components and extensions. vLLM's support for hardware...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vLLM manages components and extensions. vLLM's support for hardware- and model-specific plugins has been a cornerstone of its growth, empowering the community to greatly expand the project's hardware coverage and functi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: brittle, out-of-tree extensions and, more importantly, provide a robust architectural foundation. Adopting DI will **accelerate iterative development**, simplify testing, and pave the way for advanced capabilities like...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
