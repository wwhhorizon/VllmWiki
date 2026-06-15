# vllm-project/vllm#735: Model(llama-2-13b-chat-hf) does not load with tensor_parallel_size=4

| 字段 | 值 |
| --- | --- |
| Issue | [#735](https://github.com/vllm-project/vllm/issues/735) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Model(llama-2-13b-chat-hf) does not load with tensor_parallel_size=4

### Issue 正文摘录

I'm using a g4dn.12xlarge instance which has 4x T4 GPUs. vllm version 0.1.3 `from vllm import LLM, SamplingParams` `v_llm = LLM(model=model_path, max_num_seqs=2048, tensor_parallel_size=4)` It gets stuck on the 2nd line for 20+ minutes. [Here's](https://p.ip.fi/w73y) the error log when I interrupt the execution. It keeps waiting for the ray worker to return the objects, but seems like the worker isn't returning anything. GPU utilisation also gets stuck when it loads 6911MB per GPU. ![image](https://github.com/vllm-project/vllm/assets/65669681/42083110-fa2f-4e64-9963-f8682710df39) Any ideas as to why this is happening? Is it a version mismatch with ray?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Model(llama-2-13b-chat-hf) does not load with tensor_parallel_size=4 I'm using a g4dn.12xlarge instance which has 4x T4 GPUs. vllm version 0.1.3 `from vllm import LLM, SamplingParams` `v_llm = LLM(model=model_path, max_
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: lel_size=4 I'm using a g4dn.12xlarge instance which has 4x T4 GPUs. vllm version 0.1.3 `from vllm import LLM, SamplingParams` `v_llm = LLM(model=model_path, max_num_seqs=2048, tensor_parallel_size=4)` It gets stuck on t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 63-f8682710df39) Any ideas as to why this is happening? Is it a version mismatch with ray?
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: -f8682710df39) Any ideas as to why this is happening? Is it a version mismatch with ray?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ://p.ip.fi/w73y) the error log when I interrupt the execution. It keeps waiting for the ray worker to return the objects, but seems like the worker isn't returning anything. GPU utilisation also gets stuck when it loads...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
