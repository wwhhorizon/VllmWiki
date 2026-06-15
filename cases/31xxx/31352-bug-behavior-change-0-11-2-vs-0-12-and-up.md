# vllm-project/vllm#31352: [Bug]: Behavior change 0.11.2 vs 0.12 (and up)

| 字段 | 值 |
| --- | --- |
| Issue | [#31352](https://github.com/vllm-project/vllm/issues/31352) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Behavior change 0.11.2 vs 0.12 (and up)

### Issue 正文摘录

### Your current environment When config is not explicitly set. using get_cached_compilation_config() with 0.11.2 ``` INFO 12-25 12:08:19 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. {'level': None, 'mode': , 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', **'custom_ops': ['all']**, 'splitting_ops': None, 'compile_mm_encoder': False, 'use_inductor': None, 'compile_sizes': [], 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': , 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [], 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {}, 'max_cudagraph_capture_size': 0, 'local_cache_dir': None} ``` with 0.12.0 ``` INFO 12-25 12:07:35 [scheduler.py:228] Chunked prefill is enabled with max_num_batched_tokens=2048. {'level': None, 'mode': , 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', **'custom_ops': ['none']**, 'splitting_ops': ['vllm::unified_attent...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Behavior change 0.11.2 vs 0.12 (and up) bug;stale ### Your current environment When config is not explicitly set. using get_cached_compilation_config() with 0.11.2 ``` INFO 12-25 12:08:19 [scheduler.py:216] Chunk...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: mp_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', **'custom_ops': ['all']**, 'splitting_ops': None, 'compile_mm_encoder': False, 'use_inductor': None, 'compile_sizes': [], 'i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: (and up) bug;stale ### Your current environment When config is not explicitly set. using get_cached_compilation_config() with 0.11.2 ``` INFO 12-25 12:08:19 [scheduler.py:216] Chunked prefill is enabled with max_num_bat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': , 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [], 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nge 0.11.2 vs 0.12 (and up) bug;stale ### Your current environment When config is not explicitly set. using get_cached_compilation_config() with 0.11.2 ``` INFO 12-25 12:08:19 [scheduler.py:216] Chunked prefill is enabl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
