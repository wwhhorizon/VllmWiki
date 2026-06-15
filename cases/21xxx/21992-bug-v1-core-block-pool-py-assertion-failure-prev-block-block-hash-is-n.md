# vllm-project/vllm#21992: [Bug]: [v1/core/block_pool.py] Assertion Failure: prev_block.block_hash is not None

| 字段 | 值 |
| --- | --- |
| Issue | [#21992](https://github.com/vllm-project/vllm/issues/21992) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [v1/core/block_pool.py] Assertion Failure: prev_block.block_hash is not None

### Issue 正文摘录

## Environment vLLM V1 T16 single host LLAMA4 Maverick TP8 Will crash per hours because of this engine failure. ## Code Pointer In cache_full_blocks() https://github.com/vllm-project/vllm/blob/055bd3978ededea015fb8f0cb6aa3cc48d84cde8/vllm/v1/core/block_pool.py#L127-L139 ## Stack Trace Line numbers may be inaccurate ERROR EngineCore encountered a fatal error. ERROR Traceback (most recent call last): ERROR File "engine/core.py", line 640, in run_engine_core ERROR engine_core.run_busy_loop() ERROR File "engine/core.py", line 667, in run_busy_loop ERROR self._process_engine_step() ERROR File "engine/core.py", line 692, in _process_engine_step ERROR outputs, model_executed = self.step_fn() ERROR File "engine/core.py", line 280, in step ERROR scheduler_output = self.scheduler.schedule() ERROR File "core/sched/scheduler.py", line 440, in schedule ERROR new_blocks = self.kv_cache_manager.allocate_slots( ERROR File "core/kv_cache_manager.py", line 302, in allocate_slots ERROR self.coordinator.cache_blocks( ERROR File "core/kv_cache_coordinator.py", line 113, in cache_blocks ERROR manager.cache_blocks(request, block_hashes, num_computed_tokens) ERROR File "core/single_type_kv_cache_manager....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _block.block_hash is not None bug ## Environment vLLM V1 T16 single host LLAMA4 Maverick TP8 Will crash per hours because of this engine failure. ## Code Pointer In cache_full_blocks() https://github.com/vllm-project/vl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: [v1/core/block_pool.py] Assertion Failure: prev_block.block_hash is not None bug ## Environment vLLM V1 T16 single host LLAMA4 Maverick TP8 Will crash per hours because of this engine failure. ## Code Pointer In...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: elf.step_fn() ERROR File "engine/core.py", line 280, in step ERROR scheduler_output = self.scheduler.schedule() ERROR File "core/sched/scheduler.py", line 440, in schedule ERROR new_blocks = self.kv_cache_manager.alloca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
