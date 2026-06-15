# vllm-project/vllm#5339: [Performance]: [Automatic Prefix Caching] When hitting the KV cached blocks, the first execute is slow, and then is fast.

| 字段 | 值 |
| --- | --- |
| Issue | [#5339](https://github.com/vllm-project/vllm/issues/5339) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: [Automatic Prefix Caching] When hitting the KV cached blocks, the first execute is slow, and then is fast.

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I load llama3-70b into 4 gpus. I record the common_computed_block_nums and show its context_lens_tensor. Also, I record the model execute time. Interestingly, I find that (1)when request first hit the common prefix cached, the model execute is slow. And except the first hitting, other request hitting the prefix cached is fast. (2) no hitting prefix cached seems more fast. I know that using KV cached means context attention forward within prefill stage, and no KV cache means full attention forward. **no hitting the prefix cached.** > INFO 06-04 19:27:53 block_manager_v1.py:253] Automatic prefix caching is enabled. > Processed prompts: 0%| | 0/6 [00:00 ########## common_computed_block_nums: > ########## common_computed_block_nums: > ########## common_computed_block_nums: > ########## common_computed_block_nums: > ########## common_computed_block_nums: > ########## common_computed_block_nums: > ############ context_lens_tensor: tensor([0, 0, 0, 0, 0, 0], device='cuda:0', dtype=torch.int32) > #### model_executable time: **_0.039289_** **First hitting the prefix cached.** > ########## common_computed...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cached blocks, the first execute is slow, and then is fast. performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I load llama3-70b into 4 gpus. I record the common_com...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Performance]: [Automatic Prefix Caching] When hitting the KV cached blocks, the first execute is slow, and then is fast. performance;stale ### Proposal to improve performance _No response_ ### Report of performance reg...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: performance _No response_ ### Report of performance regression I load llama3-70b into 4 gpus. I record the common_computed_block_nums and show its context_lens_tensor. Also, I record the model execute time. Interestingl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cache;frontend_api;model_support attention;cache;cuda slowdown dtype;env_dependency Proposal to improve performance
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ###### context_lens_tensor: tensor([0, 0, 0, 0, 0, 0], device='cuda:0', dtype=torch.int32) > #### model_executable time: **_0.039289_** **First hitting the prefix cached.** > ########## common_computed_block_nums: [0, 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
