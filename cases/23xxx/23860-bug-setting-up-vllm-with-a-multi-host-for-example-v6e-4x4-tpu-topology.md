# vllm-project/vllm#23860: [Bug]: Setting up vLLM with a multi-host for example v6e-4x4 TPU topology fails

| 字段 | 值 |
| --- | --- |
| Issue | [#23860](https://github.com/vllm-project/vllm/issues/23860) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Setting up vLLM with a multi-host for example v6e-4x4 TPU topology fails

### Issue 正文摘录

### Your current environment ### How would you like to use vllm I'm trying to use a multi-host TPU setup ( specifically v6e-4x4 ) to host any model ( in this case I'm specifically trying to load `meta-llama/Llama-3.1-70B` though ultimately my goal is to load `meta-llama/Llama-3.1-400B` or deepseek model with 600b parameters that do not fit in the single host tpu ( ct6e-standard-8t ) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rying to use a multi-host TPU setup ( specifically v6e-4x4 ) to host any model ( in this case I'm specifically trying to load `meta-llama/Llama-3.1-70B` though ultimately my goal is to load `meta-llama/Llama-3.1-400B` o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ould you like to use vllm I'm trying to use a multi-host TPU setup ( specifically v6e-4x4 ) to host any model ( in this case I'm specifically trying to load `meta-llama/Llama-3.1-70B` though ultimately my goal is to loa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t ) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g up vLLM with a multi-host for example v6e-4x4 TPU topology fails usage;stale ### Your current environment ### How would you like to use vllm I'm trying to use a multi-host TPU setup ( specifically v6e-4x4 ) to host an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
