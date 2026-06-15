# vllm-project/vllm#606: Memory usage decreases as batch size increases

| 字段 | 值 |
| --- | --- |
| Issue | [#606](https://github.com/vllm-project/vllm/issues/606) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Memory usage decreases as batch size increases

### Issue 正文摘录

Hi all, I am running OPT-6.7B [https://huggingface.co/facebook/opt-6.7b] on an A100 GPU with 80GB. The 'gpu_memory_utilization' is 0.9 (as default) and I am using `torch.cuda.memory_allocated` to get the GPU memory that's allocated. For input length and output length of 40 and 156, respectively, this is the allocated memory (GB) I see across batch sizes: Batch | Allocated memory 2 | 72.8 GB 4 | 72.68 GB 8 | 72.68 GB 16 | 72.55 GB 32 | 72.18 GB 64 | 71.68 GB 128 | 70.55 GB 256 | 68.18 GB 512 | 63.68 GB For smaller batch sizes, the allocated memory is around 80 * 0.9 as expected, but it becomes smaller as the batch size increases. Is there a reason to allocate less memory for larger batch sizes? Is the unallocated memory used for some other purposes? Following the discussion in other issues, the allocated memory for engine includes both the model for inference and KV cache. With the allocate memory numbers above, does vLLM allocates a smaller KV cache when batch size is bigger (where it is supposed to have larger KV cache)?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: I am running OPT-6.7B [https://huggingface.co/facebook/opt-6.7b] on an A100 GPU with 80GB. The 'gpu_memory_utilization' is 0.9 (as default) and I am using `torch.cuda.memory_allocated` to get the GPU memory that's alloc...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 0.9 (as default) and I am using `torch.cuda.memory_allocated` to get the GPU memory that's allocated. For input length and output length of 40 and 156, respectively, this is the allocated memory (GB) I see across batch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ecreases as batch size increases Hi all, I am running OPT-6.7B [https://huggingface.co/facebook/opt-6.7b] on an A100 GPU with 80GB. The 'gpu_memory_utilization' is 0.9 (as default) and I am using `torch.cuda.memory_allo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r KV cache)? performance attention_kv_cache;model_support cache;cuda env_dependency;shape Hi all,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
