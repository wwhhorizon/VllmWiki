# vllm-project/vllm#40813: [Feature]: Add a standardized config extension point for out-of-tree platforms

| 字段 | 值 |
| --- | --- |
| Issue | [#40813](https://github.com/vllm-project/vllm/issues/40813) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add a standardized config extension point for out-of-tree platforms

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM's config dataclasses currently use strict Pydantic validation (`extra="forbid"`) and rely on native dataclass fields for downstream logic such as config hashing (`get_hash_factors`) and multiprocessing serialization. This makes it difficult for out-of-tree (OOT) hardware/platform integrations to attach platform-specific configuration values in a safe and maintainable way. Today, the available options are all problematic: 1. Relaxing validation with `extra="allow"` is unsafe and does not integrate cleanly with dataclass-based hashing. 2. Runtime schema mutation / metaprogramming is fragile and risky for serialization and long-term maintenance. 3. Manually adding a platform extension field to each config class is safe, but repetitive and easy to miss as new configs are added. I would like to propose a standardized `platform_extra: dict[str, Any]` extension point that is injected centrally by the existing `@config` decorator in `vllm/config/utils.py`. This keeps the change small and consistent while preserving: - strict validation for normal config fields - compatibility with `dataclasses.fields()` - compatibility with `get_hash_factors` -...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ing `@config` decorator in `vllm/config/utils.py`. This keeps the change small and consistent while preserving: - strict validation for normal config fields - compatibility with `dataclasses.fields()` - compatibility wi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r out-of-tree (OOT) hardware/platform integrations to attach platform-specific configuration values in a safe and maintainable way. Today, the available options are all problematic: 1. Relaxing validation with `extra="a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Add a standardized config extension point for out-of-tree platforms feature request ### 🚀 The feature, motivation and pitch vLLM's config dataclasses currently use strict Pydantic validation (`extra="forbid"`...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: a standardized config extension point for out-of-tree platforms feature request ### 🚀 The feature, motivation and pitch vLLM's config dataclasses currently use strict Pydantic validation (`extra="forbid"`) and rely on n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: bout. ### Additional context I already have a small implementation and tests for: - default instantiation - nested config propagation - hash factor coverage - pickle serialization - inherited dataclass safety If this di...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
