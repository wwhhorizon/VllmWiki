# vllm-project/vllm#4998: [Performance]: Splitting model across GPUs with varying vRAM

| 字段 | 值 |
| --- | --- |
| Issue | [#4998](https://github.com/vllm-project/vllm/issues/4998) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | activation;cuda |
| 症状 | oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Splitting model across GPUs with varying vRAM

### Issue 正文摘录

### Proposal to improve performance I have 8 GPUs across two nodes (4 and 4). I have 4 3090s on one and 3 3090s on the other, along with a 3080. 3090s have 24gb of vram while 3080s only have 12. Thus, when loading in a large model such as llama3 70b, which splits the model so it takes up ~16gb per GPU, I get an OOM error. We can also take another, slightly smaller model as an example too so long as it ends up splitting it >~12gb. I have found a few ways to navigate this, and thought it would be interesting to bring up and see if it could/would ever be implemented in the future. ### Using `accelerate` Accelerate has a util called [get_balanced_memory](https://huggingface.co/docs/accelerate/package_reference/utilities#accelerate.utils.get_balanced_memory) which computes a max_memory dictionary for [infer_auto_device_map](https://huggingface.co/docs/accelerate/v0.30.1/en/package_reference/big_modeling#accelerate.infer_auto_device_map) when loading a model into memory for inferrence. This automatically calculates how to split up the model if there are multiple GPUs with varying amounts of vram. It can also be [manually set](https://huggingface.co/docs/accelerate/v0.30.1/en/concept_gui...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Performance]: Splitting model across GPUs with varying vRAM performance;stale ### Proposal to improve performance I have 8 GPUs across two nodes (4 and 4). I have 4 3090s on one and 3 3090s on the other, along with a 3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ence#designing-a-device-map). ### Manually getting GPU memory ```python import torch for i in range(torch.cuda.device_count()): print(i, torch.cuda.get_device_properties(i).total_memory) ``` This can then be used to set...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: up ~16gb per GPU, I get an OOM error. We can also take another, slightly smaller model as an example too so long as it ends up splitting it >~12gb. I have found a few ways to navigate this, and thought it would be inter...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: lama3 70b, which splits the model so it takes up ~16gb per GPU, I get an OOM error. We can also take another, slightly smaller model as an example too so long as it ends up splitting it >~12gb. I have found a few ways t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Splitting model across GPUs with varying vRAM performance;stale ### Proposal to improve performance I have 8 GPUs across two nodes (4 and 4). I have 4 3090s on one and 3 3090s on the other, along with a 3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
