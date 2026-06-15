# vllm-project/vllm#7983: [Usage]: Deploying multimodal retrieval models

| 字段 | 值 |
| --- | --- |
| Issue | [#7983](https://github.com/vllm-project/vllm/issues/7983) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Deploying multimodal retrieval models

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of [ColPali](https://huggingface.co/vidore/colpali). I don't know how to integrate it with vllm. It used `PaliGemma` which is there in `vLLM` , but it also loads some adapters. Please let me know if it can be used right-away, or if any changes need to be made, let me know, I am happy to contribute. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Deploying multimodal retrieval models usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of [ColPali](https://h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: Deploying multimodal retrieval models usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of [ColPali](https://h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: te. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: idore/colpali). I don't know how to integrate it with vllm. It used `PaliGemma` which is there in `vLLM` , but it also loads some adapters. Please let me know if it can be used right-away, or if any changes need to be m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Deploying multimodal retrieval models usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of [ColPali](https://h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
