# vllm-project/vllm#9760: [Usage]: vLLM For maximally batched use case

| 字段 | 值 |
| --- | --- |
| Issue | [#9760](https://github.com/vllm-project/vllm/issues/9760) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vLLM For maximally batched use case

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hey, I am trying to run LLAMA 3.1 70b on an 8xL40s (PCI-E) setup. My use case is a single massive batch, and I want to run the run_batch endpoint with maximally large throughput. Since it's an offline use case I do not care about the latency much. Any tips as to the best parameters? Specifically what to set max_num_batched_tokens to And is there any benefit to running it in tensor/pipeline parallel performance wise? Would also love any thoughts on reordering the prompts (There's no shared prefix) I've looked at #2492 and #8513 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ive batch, and I want to run the run_batch endpoint with maximally large throughput. Since it's an offline use case I do not care about the latency much. Any tips as to the best parameters? Specifically what to set max_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: u like to use vllm Hey, I am trying to run LLAMA 3.1 70b on an 8xL40s (PCI-E) setup. My use case is a single massive batch, and I want to run the run_batch endpoint with maximally large throughput. Since it's an offline...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 513 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: env.py` ``` ### How would you like to use vllm Hey, I am trying to run LLAMA 3.1 70b on an 8xL40s (PCI-E) setup. My use case is a single massive batch, and I want to run the run_batch endpoint with maximally large throu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vLLM For maximally batched use case usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hey, I am trying to run LLAMA 3.1 70b on an 8xL4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
