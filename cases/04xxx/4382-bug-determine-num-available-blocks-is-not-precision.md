# vllm-project/vllm#4382: [Bug]: determine_num_available_blocks is not precision

| 字段 | 值 |
| --- | --- |
| Issue | [#4382](https://github.com/vllm-project/vllm/issues/4382) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: determine_num_available_blocks is not precision

### Issue 正文摘录

### Your current environment ```text vllm v0.4.1 ``` ### 🐛 Describe the bug the code in worker.py `num_gpu_blocks = int( (total_gpu_memory * self.cache_config.gpu_memory_utilization - peak_memory) // cache_block_size)` i think it should be `num_gpu_blocks = int( (total_gpu_memory * self.cache_config.gpu_memory_utilization - (total_gpu_memory - self.init_gpu_memory) - peak_memory) // cache_block_size)` because the origin way didnt consider about part of initial memory. The calculation of free GPU blocks needs to consider initialized memory. This may lead to confusion regarding the actual available memory size?

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: determine_num_available_blocks is not precision bug;stale ### Your current environment ```text vllm v0.4.1 ``` ### 🐛 Describe the bug the code in worker.py `num_gpu_blocks = int( (total_gpu_memory * self.cache_co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: determine_num_available_blocks is not precision bug;stale ### Your current environment ```text vllm v0.4.1 ``` ### 🐛 Describe the bug the code in worker.py `num_gpu_blocks = int( (total_gpu_memory * self.cache_co...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: determine_num_available_blocks is not precision bug;stale ### Your current environment ```text vllm v0.4.1 ``` ### 🐛 Describe the bug the code in worker.py `num_gpu_blocks = int( (total_gpu_memory * self.cache_co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ker.py `num_gpu_blocks = int( (total_gpu_memory * self.cache_config.gpu_memory_utilization - peak_memory) // cache_block_size)` i think it should be `num_gpu_blocks = int( (total_gpu_memory * self.cache_config.gpu_memor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: determine_num_available_blocks is not precision bug;stale ### Your current environment ```text vllm v0.4.1 ``` ### 🐛 Describe the bug the code in worker.py `num_gpu_blocks = int( (total_gpu_memory * self.cache_co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
