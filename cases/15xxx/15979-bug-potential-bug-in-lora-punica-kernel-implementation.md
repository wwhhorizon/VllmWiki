# vllm-project/vllm#15979: [Bug]: Potential bug in LoRA Punica Kernel implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#15979](https://github.com/vllm-project/vllm/issues/15979) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential bug in LoRA Punica Kernel implementation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There is a potential bug in the Punica Kernel implemementation. At [this line of code](https://github.com/vllm-project/vllm/blob/01b6113659cf4ad115c39e2ebb18de7535e423a7/vllm/lora/ops/triton_ops/lora_kernel_metadata.py#L114) we should use `torch.unique(sorted=True)` instead of the current `torch.unique(sorted=False)` For example, if `token_lora_mapping` is `[1, 2, 3, 1, 2, 3]` , then following the code execution: - `token_indices_sorted_by_lora_ids` will be `[0, 3, 1, 4, 2, 5]` - `lora_ids` will be `[1, 2, 3]` - `num_tokens_per_lora` will be `[2, 2, 2]` However, the above is an ideal case, since we are using `torch.unique(sorted=False)`, it is possible that `lora_ids` becomes `[3, 2, 1]` or `[1, 3, 2]` or whatever unsorted cases, and then the data loading like [here](https://github.com/vllm-project/vllm/blob/01b6113659cf4ad115c39e2ebb18de7535e423a7/vllm/lora/ops/triton_ops/lora_shrink.py#L59) will load the wrong data. Right now this is not triggering any issue, because according to [pytorch doc torch.unique](https://pytorch.org/docs/stable/generated/torch.unique.html) CUDA and CPU implementation always sort the tensor at the begi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: on this always sort behavior in pytorch. We should change the code explicitly to `torch.unique(sorted=True)` The correct result depends on lora_ids being sorted. ### Before submitting a new issue... - [x] Make sure you...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 13659cf4ad115c39e2ebb18de7535e423a7/vllm/lora/ops/triton_ops/lora_kernel_metadata.py#L114) we should use `torch.unique(sorted=True)` instead of the current `torch.unique(sorted=False)` For example, if `token_lora_mappin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rch.unique](https://pytorch.org/docs/stable/generated/torch.unique.html) CUDA and CPU implementation always sort the tensor at the beginning and ignore the sorted=True/False argument. But I think it is dangerous to depe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: project/vllm/blob/01b6113659cf4ad115c39e2ebb18de7535e423a7/vllm/lora/ops/triton_ops/lora_kernel_metadata.py#L114) we should use `torch.unique(sorted=True)` instead of the current `torch.unique(sorted=False)` For example...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
