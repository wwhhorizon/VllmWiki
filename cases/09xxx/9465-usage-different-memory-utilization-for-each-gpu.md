# vllm-project/vllm#9465: [Usage]: Different memory utilization for each gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#9465](https://github.com/vllm-project/vllm/issues/9465) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Different memory utilization for each gpu

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to use multi gpu since the model does not fit into single gpu but I wonder if there is a way to specify different memory utilization for each gpu for example at first one it will be 0.9 for the other one it ll be 0.7 . Thnx in advance! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: model does not fit into single gpu but I wonder if there is a way to specify different memory utilization for each gpu for example at first one it will be 0.9 for the other one it ll be 0.7 . Thnx in advance! ### Before...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ` ### How would you like to use vllm I want to use multi gpu since the model does not fit into single gpu but I wonder if there is a way to specify different memory utilization for each gpu for example at first one it w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
