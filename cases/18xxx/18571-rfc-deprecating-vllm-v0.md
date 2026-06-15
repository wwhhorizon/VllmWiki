# vllm-project/vllm#18571: [RFC]: Deprecating vLLM V0

| 字段 | 值 |
| --- | --- |
| Issue | [#18571](https://github.com/vllm-project/vllm/issues/18571) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 69; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Deprecating vLLM V0

### Issue 正文摘录

vLLM V1 has been the default engine since version v0.8.0, released approximately three months ago. With substantial user adoption and overwhelmingly positive feedback on V1, we propose formally deprecating vLLM V0 and **removing its implementation from the vLLM codebase**. ## TL;DR * Effective immediately, the **vLLM V0 codebase is frozen, with only minor bug fixes permitted.** * **Deprecation of V0 will occur at the end of June**, followed by the removal of its code. * By that time, migration of the remaining features from V0 to V1 will be completed. Certain features may be temporarily or permanently discontinued (details provided below). ## Motivation ### 1. Reduce Code Complexity and Technical Debt Currently, V0 and V1 share significant portions of code—such as models, configs, and utilities—which has introduced considerable complexity and technical debt. Contributors unfamiliar with V0 face difficulties assessing the impact of changes, especially when shared components inadvertently break V0 functionality. Eliminating V0 will simplify the codebase, enhance maintainability, and accelerate the development and improvement of V1. ### 2. Avoid User and Contributor Confusion The coe...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Deprecating vLLM V0 RFC;stale vLLM V1 has been the default engine since version v0.8.0, released approximately three months ago. With substantial user adoption and overwhelmingly positive feedback on V1, we propo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Deprecating vLLM V0 RFC;stale vLLM V1 has been the default engine since version v0.8.0, released approximately three months ago. With substantial user adoption and overwhelmingly positive feedback on V1, we propose form...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: al Debt Currently, V0 and V1 share significant portions of code—such as models, configs, and utilities—which has introduced considerable complexity and technical debt. Contributors unfamiliar with V0 face difficulties a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: * Logits processors (via new APIs) * OpenTelemetry APIs * **Hardware backends:** * Intel CPU and XPU ### Features Temporarily Discontinued * Encoder-decoder models (e.g., Whisper) * Draft model-based speculative decodin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ost Currently, a substantial portion of our CI resources are devoted to testing V0 code paths. Removing V0 is projected to reduce CI times and associated costs by at least half, reallocating these resources toward accel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
