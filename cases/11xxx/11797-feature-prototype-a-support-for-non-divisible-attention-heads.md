# vllm-project/vllm#11797: [Feature]: prototype a support for non divisible attention heads

| 字段 | 值 |
| --- | --- |
| Issue | [#11797](https://github.com/vllm-project/vllm/issues/11797) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: prototype a support for non divisible attention heads

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Commonly we see this assertion error gets triggered ```python # in config.py if total_num_attention_heads % tensor_parallel_size != 0: raise ValueError( f"Total number of attention heads ({total_num_attention_heads})" " must be divisible by tensor parallel size " f"({tensor_parallel_size}).") ... # in model file assert self.total_num_heads % tp_size == 0 assert self.total_num_kv_heads % tp_size == 0 ``` This is done with good intention that we can shard the model perfectly. However, recent models have weird shapes, one example is Qwen2-7B, which has 28 attention heads and 4 KV heads. This means it cannot be ran on 8GPU node. https://huggingface.co/Qwen/Qwen2-7B/blob/453ed1575b739b5b03ce3758b23befdb0967f40e/config.json#L15-L17 We would like to see a prototype PR that get rid of this limitation, potentially in the following way, but more ideas welcome 1. Padding so we add extra dimensions to the attention process filled with zeros. 2. Enabled replicated model so we do not perform attention in TP mode, note that this does cause more KV cache duplication. ### Alternatives Continue to enforce this warning. ### Additional context _No response_ ###...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tch Commonly we see this assertion error gets triggered ```python # in config.py if total_num_attention_heads % tensor_parallel_size != 0: raise ValueError( f"Total number of attention heads ({total_num_attention_heads}...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: prototype a support for non divisible attention heads feature request;stale ### 🚀 The feature, motivation and pitch Commonly we see this assertion error gets triggered ```python # in config.py if total_num_at...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: o we do not perform attention in TP mode, note that this does cause more KV cache duplication. ### Alternatives Continue to enforce this warning. ### Additional context _No response_ ### Before submitting a new issue......
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
