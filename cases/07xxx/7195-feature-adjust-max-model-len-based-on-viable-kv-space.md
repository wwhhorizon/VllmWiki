# vllm-project/vllm#7195: [Feature]: Adjust max_model_len based on viable KV space

| 字段 | 值 |
| --- | --- |
| Issue | [#7195](https://github.com/vllm-project/vllm/issues/7195) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Adjust max_model_len based on viable KV space

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, when loading a model onto a GPU that doesn't have sufficient memory for full max_len sized KV cache, this error pops up: ``` ValueError: The model's max seq len (32768) is larger than the maximum number of tokens that can be stored in KV cache (22032). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. ``` Which originates from this code: https://github.com/vllm-project/vllm/blob/9118217f58c39040aa935b7c85250c7364ffa72d/vllm/worker/worker.py#L214-L216 Although there are some workarounds can be found [here](https://github.com/vllm-project/vllm/issues/2418), wouldn't it be better to adjust the `self.model_config.max_model_len`size to the maximum affordable size? We could pop a warning to notify that the full context length cannot be used. If this idea is OK, I'd love to attempt a fix. Thanks for reading 🙇‍♂️ ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Adjust max_model_len based on viable KV space feature request ### 🚀 The feature, motivation and pitch Currently, when loading a model onto a GPU that doesn't have sufficient memory for full max_len sized KV c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pitch Currently, when loading a model onto a GPU that doesn't have sufficient memory for full max_len sized KV cache, this error pops up: ``` ValueError: The model's max seq len (32768) is larger than the maximum number...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: el onto a GPU that doesn't have sufficient memory for full max_len sized KV cache, this error pops up: ``` ValueError: The model's max seq len (32768) is larger than the maximum number of tokens that can be stored in KV...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Adjust max_model_len based on viable KV space feature request ### 🚀 The feature, motivation and pitch Currently, when loading a model onto a GPU that doesn't have sufficient memory for full max_len sized KV c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
