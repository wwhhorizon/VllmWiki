# vllm-project/vllm#14722: [Bug]: try reinforce++ training with vllm-eager-mode, the inference result is quite different for eager-mode and cuda-graph for greedy-decoding evaluation

| 字段 | 值 |
| --- | --- |
| Issue | [#14722](https://github.com/vllm-project/vllm/issues/14722) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: try reinforce++ training with vllm-eager-mode, the inference result is quite different for eager-mode and cuda-graph for greedy-decoding evaluation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use reinforce++ with baseline to train a rl model. When training, i use eager-mode for vllm generation. When I use the ckpt for evaluation, the results are quiet confusing. The amc23-dataset shows big difference when using different mode(eager/cuda-graph). The decoding strategy is greedy-decoding. eager-mode for inference: amc23: 52.5 cuda-graph-mode for inference: amc23: 47.5 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;model_support cuda env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m-eager-mode, the inference result is quite different for eager-mode and cuda-graph for greedy-decoding evaluation bug;stale ### Your current environment ### 🐛 Describe the bug I use reinforce++ with baseline to train a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ult is quite different for eager-mode and cuda-graph for greedy-decoding evaluation bug;stale ### Your current environment ### 🐛 Describe the bug I use reinforce++ with baseline to train a rl model. When training, i use...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ### 🐛 Describe the bug I use reinforce++ with baseline to train a rl model. When training, i use eager-mode for vllm generation. When I use the ckpt for evaluation, the results are quiet confusing. The amc23-dataset sho...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: fferent for eager-mode and cuda-graph for greedy-decoding evaluation bug;stale ### Your current environment ### 🐛 Describe the bug I use reinforce++ with baseline to train a rl model. When training, i use eager-mode for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
