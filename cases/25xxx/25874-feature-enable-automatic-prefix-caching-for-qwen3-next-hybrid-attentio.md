# vllm-project/vllm#25874: [Feature]: Enable Automatic Prefix Caching for Qwen3-Next (hybrid attention)

| 字段 | 值 |
| --- | --- |
| Issue | [#25874](https://github.com/vllm-project/vllm/issues/25874) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable Automatic Prefix Caching for Qwen3-Next (hybrid attention)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The [Qwen3-Next Usage Guide](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html#known-limitations) states that: > Qwen3-Next currently does not support automatic prefix caching. Prefix caching for these models would be a really nice feature. Creating this issue to request it, and track if/when it gets implemented. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Enable Automatic Prefix Caching for Qwen3-Next (hybrid attention) feature request ### 🚀 The feature, motivation and pitch The [Qwen3-Next Usage Guide](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and pitch The [Qwen3-Next Usage Guide](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html#known-limitations) states that: > Qwen3-Next currently does not support automatic prefix caching. Prefix cachin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nable Automatic Prefix Caching for Qwen3-Next (hybrid attention) feature request ### 🚀 The feature, motivation and pitch The [Qwen3-Next Usage Guide](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html#...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: The [Qwen3-Next Usage Guide](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html#known-limitations) states that: > Qwen3-Next currently does not support automatic prefix caching. Prefix caching for thes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
