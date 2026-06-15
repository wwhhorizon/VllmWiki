# vllm-project/vllm#26399: [Bug]: basic reasoning parser has bug

| 字段 | 值 |
| --- | --- |
| Issue | [#26399](https://github.com/vllm-project/vllm/issues/26399) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: basic reasoning parser has bug

### Issue 正文摘录

### Your current environment Ubuntu 22.04 docker container with latest vllm ### 🐛 Describe the bug [This line](https://github.com/vllm-project/vllm/blob/335b28f7d1020911af7974f50e27b708113c5e3f/vllm/reasoning/basic_parsers.py#L155) is a bug. Currently it's `return model_output, None` But this should be `return None, model_output` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ning parser has bug bug;stale ### Your current environment Ubuntu 22.04 docker container with latest vllm ### 🐛 Describe the bug [This line](https://github.com/vllm-project/vllm/blob/335b28f7d1020911af7974f50e27b708113c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /vllm/reasoning/basic_parsers.py#L155) is a bug. Currently it's `return model_output, None` But this should be `return None, model_output` ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: basic reasoning parser has bug bug;stale ### Your current environment Ubuntu 22.04 docker container with latest vllm ### 🐛 Describe the bug [This line](https://github.com/vllm-project/vllm/blob/335b28f7d1020911af...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: stale ### Your current environment Ubuntu 22.04 docker container with latest vllm ### 🐛 Describe the bug [This line](https://github.com/vllm-project/vllm/blob/335b28f7d1020911af7974f50e27b708113c5e3f/vllm/reasoning/basi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
