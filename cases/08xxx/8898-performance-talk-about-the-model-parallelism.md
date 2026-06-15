# vllm-project/vllm#8898: [Performance]: Talk about the model parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#8898](https://github.com/vllm-project/vllm/issues/8898) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Talk about the model parallelism

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi, Thank you for your contribution to the LLM community. I have a question about the model parallelism. One part of the model is loading with Tensor Parallel (TP) and the other part is not. For example, there is a model. TP is performed on the linear layer in the FFN in the model, but TP is not performed on other layers, such as the attention block. So, when loading the model into the GPU, how are weights without TP distributed to multiple GPUs? Is it copied repeatedly to each GPU? Or is it only loaded on a single GPU, such as GPU:0? I'm not sure how this process happens in vllm. I would appreciate it if you could help me answer this question. Best regards, BAI Fan ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: Talk about the model parallelism performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi, Thank you for...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi, Thank you for your contribution to the LLM community. I have a question about the mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: h as GPU:0? I'm not sure how this process happens in vllm. I would appreciate it if you could help me answer this question. Best regards, BAI Fan ### Your current environment (if you think it is necessary) ```text The o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: he model, but TP is not performed on other layers, such as the attention block. So, when loading the model into the GPU, how are weights without TP distributed to multiple GPUs? Is it copied repeatedly to each GPU? Or i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: Talk about the model parallelism performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi, Thank you for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
