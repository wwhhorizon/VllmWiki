# vllm-project/vllm#24523: [Bug]: Unclear error message when `--num-redundant-experts` provided without `--enable-eplb`

| 字段 | 值 |
| --- | --- |
| Issue | [#24523](https://github.com/vllm-project/vllm/issues/24523) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unclear error message when `--num-redundant-experts` provided without `--enable-eplb`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Starting vLLM with `--num-redundant-experts=16` but accidentally omitting `--enable-eplb`, I got an error message that did not clearly identify the fault was a missing flag, and had to ask someone experienced. ``` (APIServer pid=1) pydantic_core._pydantic_core.ValidationError: 1 validation error for ParallelConfig (APIServer pid=1) Value error, num_redundant_experts should be used with EPLB.16. [type=value_error, input_value=ArgsKwargs((), {'pipeline...text_parallel_size': 1}), input_type=ArgsKwargs] ``` We should improve the error mesasge. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Describe the bug Starting vLLM with `--num-redundant-experts=16` but accidentally omitting `--enable-eplb`, I got an error message that did not clearly identify the fault was a missing flag, and had to ask someone exper...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ntic_core._pydantic_core.ValidationError: 1 validation error for ParallelConfig (APIServer pid=1) Value error, num_redundant_experts should be used with EPLB.16. [type=value_error, input_value=ArgsKwargs((), {'pipeline....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Unclear error message when `--num-redundant-experts` provided without `--enable-eplb` bug ### Your current environment ### 🐛 Describe the bug Starting vLLM with `--num-redundant-experts=16` but accidentally omitt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
