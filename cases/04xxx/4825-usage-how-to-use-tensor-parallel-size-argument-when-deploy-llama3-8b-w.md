# vllm-project/vllm#4825: [Usage]: How to use tensor-parallel-size argument when deploy Llama3-8b with AsyncLLMEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#4825](https://github.com/vllm-project/vllm/issues/4825) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use tensor-parallel-size argument when deploy Llama3-8b with AsyncLLMEngine

### Issue 正文摘录

### Your current environment ```text My model is Llama3-8B which takes about 14GB GPU-memory. And the machine have 2 * 40GB GPUs. （NVIDIA L40S） ``` ### How would you like to use vllm Hey, Recently I tried to use AsyncLLMEngine to speed up my LLM inference server. My model is Llama3-8B which takes about 14GB GPU-memory. And the machine have 2 * 40GB GPUs（NVIDIA L40S）. I want to know that: 1. What is the meaning of the "tensor-parallel-size" when init the AsyncLLMEngine? if I set it as 2, how is the parallelism been executed when a inference request comes, It parallel the input tensors to the 2 different GPUs? or it paralle-distribute the model's weight? 2. When I test the time-comsuming of the server with "tensor-parallel-size" = 1or2, I didn't see an obvious difference on them, so I was wondering maybe I didn't use AsyncLLMEngine and "tensor-parallel-size" in a correct-way. Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to use tensor-parallel-size argument when deploy Llama3-8b with AsyncLLMEngine usage ### Your current environment ```text My model is Llama3-8B which takes about 14GB GPU-memory. And the machine have 2 * 40...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ize" when init the AsyncLLMEngine? if I set it as 2, how is the parallelism been executed when a inference request comes, It parallel the input tensors to the 2 different GPUs? or it paralle-distribute the model's weigh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: if I set it as 2, how is the parallelism been executed when a inference request comes, It parallel the input tensors to the 2 different GPUs? or it paralle-distribute the model's weight? 2. When I test the time-comsumin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: different GPUs? or it paralle-distribute the model's weight? 2. When I test the time-comsuming of the server with "tensor-parallel-size" = 1or2, I didn't see an obvious difference on them, so I was wondering maybe I did...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
