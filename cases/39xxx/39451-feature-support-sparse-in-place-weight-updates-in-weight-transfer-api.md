# vllm-project/vllm#39451: [Feature]: Support sparse in-place weight updates in weight transfer API

| 字段 | 值 |
| --- | --- |
| Issue | [#39451](https://github.com/vllm-project/vllm/issues/39451) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support sparse in-place weight updates in weight transfer API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In online RL, the trainer periodically syncs updated weights to a vLLM inference server. After a single optimizer step, typically >99% of bf16 elements are unchanged. We'd like to transfer and apply only the delta. ### Problem `receive_weights` operates on full dense tensors. For each parameter, it allocates the full shape and broadcasts the entire tensor: ```python # nccl_engine.py — receive_weights for name, dtype_name, shape in zip(update_info.names, update_info.dtype_names, update_info.shapes): weight = torch.empty(shape, dtype=dtype, device="cuda") self.model_update_group.broadcast(weight, src=0) load_weights([(name, weight)]) ``` There's no way to say "here are the 0.3% of elements that changed — apply them in-place." This forces us to keep a full CPU bf16 snapshot on the vLLM side to reconstruct dense tensors from sparse patches before calling `load_weights`. ### Possible API A sparse variant that broadcasts only indices + values, then scatters directly into the existing GPU parameter: ```python # Sparse path — broadcast only the delta indices = torch.empty(nnz, dtype=torch.int32, device="cuda") values = torch.empty(nnz, dtype=dtype,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: vLLM inference server. After a single optimizer step, typically >99% of bf16 elements are unchanged. We'd like to transfer and apply only the delta. ### Problem `receive_weights` operates on full dense tensors. For each...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pdate_info.shapes): weight = torch.empty(shape, dtype=dtype, device="cuda") self.model_update_group.broadcast(weight, src=0) load_weights([(name, weight)]) ``` There's no way to say "here are the 0.3% of elements that c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s): weight = torch.empty(shape, dtype=dtype, device="cuda") self.model_update_group.broadcast(weight, src=0) load_weights([(name, weight)]) ``` There's no way to say "here are the 0.3% of elements that changed — apply t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Support sparse in-place weight updates in weight transfer API feature request ### 🚀 The feature, motivation and pitch In online RL, the trainer periodically syncs updated weights to a vLLM inference server. After a s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
