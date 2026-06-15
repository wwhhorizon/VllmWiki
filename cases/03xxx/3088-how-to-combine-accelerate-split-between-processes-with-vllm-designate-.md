# vllm-project/vllm#3088: How to combine `accelerate.split_between_processes` with `vllm` (designate a specific gpu in each process)?

| 字段 | 值 |
| --- | --- |
| Issue | [#3088](https://github.com/vllm-project/vllm/issues/3088) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to combine `accelerate.split_between_processes` with `vllm` (designate a specific gpu in each process)?

### Issue 正文摘录

I would like to do distributed inference. Specifically, I hope to split the inference prompts between the multiple gpus (as done by `accelerate.split_between_processes`), and then launch `vllm` in each process. However, when I set `os.environ['CUDA_VISIBLE_DEVICES'] = 'x'` and create the model, the following error can be raised: ``` RuntimeError: torch.distributed is already initialized but the torch world size does not match parallel_config.world_size (4 vs. 1). ``` I understand this is because `accelerate` has initialized a distributed mode with world size 4. But for a small model (e.g., 7B), I do not need pp or tp. Do you have suggestions on how to resolve it?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: and then launch `vllm` in each process. However, when I set `os.environ['CUDA_VISIBLE_DEVICES'] = 'x'` and create the model, the following error can be raised: ``` RuntimeError: torch.distributed is already initialized...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: er, when I set `os.environ['CUDA_VISIBLE_DEVICES'] = 'x'` and create the model, the following error can be raised: ``` RuntimeError: torch.distributed is already initialized but the torch world size does not match paral...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: combine `accelerate.split_between_processes` with `vllm` (designate a specific gpu in each process)? stale I would like to do distributed inference. Specifically, I hope to split the inference prompts between the multip...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tween_processes` with `vllm` (designate a specific gpu in each process)? stale I would like to do distributed inference. Specifically, I hope to split the inference prompts between the multiple gpus (as done by `acceler...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
