# vllm-project/vllm#18814: [Bug] TP=2 fails on dual RTX 5090: TorchInductor compile error or CUDA illegal memory access (TP=1 works)

| 字段 | 值 |
| --- | --- |
| Issue | [#18814](https://github.com/vllm-project/vllm/issues/18814) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | activation;cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] TP=2 fails on dual RTX 5090: TorchInductor compile error or CUDA illegal memory access (TP=1 works)

### Issue 正文摘录

### Your current environment ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug] TP=2 fails on dual RTX 5090: TorchInductor compile error or CUDA illegal memory access (TP=1 works) bug;stale ### Your current environment ### Before submitting a new issue... - [x] Make sure you already searched...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug] TP=2 fails on dual RTX 5090: TorchInductor compile error or CUDA illegal memory access (TP=1 works) bug;stale ### Your current environment ### Before submitting a new issue... - [x] Make sure you already searched...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tend_api;model_support activation;cuda;kernel;operator build_error;crash;mismatch env_dependency;shape Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: . correctness activation_norm;ci_build;distributed_parallel;frontend_api;model_support activation;cuda;kernel;operator build_error;crash;mismatch env_dependency;shape Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rchInductor compile error or CUDA illegal memory access (TP=1 works) bug;stale ### Your current environment ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
