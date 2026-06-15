# vllm-project/vllm#14749: [Usage]:  How to apply expert parallelization in MoE models with VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#14749](https://github.com/vllm-project/vllm/issues/14749) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  How to apply expert parallelization in MoE models with VLLM

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a MoE model like DeepSeek V2, I want to customize the placement of model expert layers, such as placing different experts on different GPUs. How should I set this up? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Usage]: How to apply expert parallelization in MoE models with VLLM usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: V2, I want to customize the placement of model expert layers, such as placing different experts on different GPUs. How should I set this up? ### Before submitting a new issue... - [x] Make sure you already searched for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: p? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How to apply expert parallelization in MoE models with VLLM usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: age]: How to apply expert parallelization in MoE models with VLLM usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
