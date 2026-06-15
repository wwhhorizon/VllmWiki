# vllm-project/vllm#5830: [Usage]: Multi-LoRA questions

| 字段 | 值 |
| --- | --- |
| Issue | [#5830](https://github.com/vllm-project/vllm/issues/5830) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Multi-LoRA questions

### Issue 正文摘录

### Your current environment N/A ### How would you like to use vllm I am trying to understand how vLLM has implemented multi-lora. - Adapter swapping: The S-LoRA paper describes a lookahead, and swapping based on the upcoming queue. LoRAX implements something similar, I was curious the exact details of how swapping is handled. Is it based on queue size of each adapter, is time in queue weighted vs queue size? Is this controllable? (If i have an online workload I care more about my tail latency, but offline I want raw throughput) - Can I specify the max number of adapters stored in GPU memory? How can I tell how many adapters are in memory? Is that in User control? - How can I determine the current state of my model server wrt adapters? Example: I have 2 model servers, Model server 1 has adapters A & B loaded in GPU mem. Model server 2 has adapter C loaded. Either of the model servers _can_ serve a request for C. but model server 2 serving the request for C would be more efficient. I would like to route based on these characteristics. Is there a way to expose this information?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Is that in User control? - How can I determine the current state of my model server wrt adapters? Example: I have 2 model servers, Model server 1 has adapters A & B loaded in GPU mem. Model server 2 has adapter C loaded...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e S-LoRA paper describes a lookahead, and swapping based on the upcoming queue. LoRAX implements something similar, I was curious the exact details of how swapping is handled. Is it based on queue size of each adapter,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: is controllable? (If i have an online workload I care more about my tail latency, but offline I want raw throughput) - Can I specify the max number of adapters stored in GPU memory? How can I tell how many adapters are...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: re about my tail latency, but offline I want raw throughput) - Can I specify the max number of adapters stored in GPU memory? How can I tell how many adapters are in memory? Is that in User control? - How can I determin...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: nt raw throughput) - Can I specify the max number of adapters stored in GPU memory? How can I tell how many adapters are in memory? Is that in User control? - How can I determine the current state of my model server wrt...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
