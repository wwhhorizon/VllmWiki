# vllm-project/vllm#7039: [Bug]: Available context (gpu blocks) gets halved by pipeline parallel size

| 字段 | 值 |
| --- | --- |
| Issue | [#7039](https://github.com/vllm-project/vllm/issues/7039) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Available context (gpu blocks) gets halved by pipeline parallel size

### Issue 正文摘录

### Your current environment ```text vLLM main branch commit c8a7e932 ``` ### 🐛 Describe the bug Using `--pipeline_parallel_size=2`, it will throw an error if the prompt uses more than half the available tokens. vLLM reports a capacity of 1650 blocks / 26.4k tokens when loading the model, `--max_model_len` was set to 24000: ``` INFO 08-01 15:24:16 distributed_gpu_executor.py:56] # GPU blocks: 1650, # CPU blocks: 0 ``` But when sending any prompt with >13k tokens, it throws an `input prompt is too long` error: ``` WARNING 08-01 15:24:58 scheduler.py:706] Input prompt (512 tokens) is too long and exceeds the capacity of block_manager ``` Adding these print statements: ``` diff diff --git a/vllm/core/block_manager_v1.py b/vllm/core/block_manager_v1.py index e29eba37..3bf57230 100644 --- a/vllm/core/block_manager_v1.py +++ b/vllm/core/block_manager_v1.py @@ -224,6 +224,7 @@ class BlockSpaceManagerV1(BlockSpaceManager): ) -> None: self.block_size = block_size self.num_total_gpu_blocks = num_gpu_blocks + logger.info(f"self.num_total_gpu_blocks = {num_gpu_blocks}") self.num_total_cpu_blocks = num_cpu_blocks if enable_caching and sliding_window is not None: @@ -286,6 +287,7 @@ class Block...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Available context (gpu blocks) gets halved by pipeline parallel size bug;stale ### Your current environment ```text vLLM main branch commit c8a7e932 ``` ### 🐛 Describe the bug Using `--pipeline_parallel_size=2`, it will...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the prompt uses more than half the available tokens. vLLM reports a capacity of 1650 blocks / 26.4k tokens when loading the model, `--max_model_len` was set to 24000: ``` INFO 08-01 15:24:16 distributed_gpu_executor.py:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Available context (gpu blocks) gets halved by pipeline parallel size bug;stale ### Your current environment ```text vLLM main branch commit c8a7e932 ``` ### 🐛 Describe the bug Using `--pipeline_parallel_size=2`,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vLLM reports a capacity of 1650 blocks / 26.4k tokens when loading the model, `--max_model_len` was set to 24000: ``` INFO 08-01 15:24:16 distributed_gpu_executor.py:56] # GPU blocks: 1650, # CPU blocks: 0 ``` But when...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
