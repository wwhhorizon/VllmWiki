# vllm-project/vllm#34642: [Bug]: Incorrect warning when both mistral & HF format are present in repo

| 字段 | 值 |
| --- | --- |
| Issue | [#34642](https://github.com/vllm-project/vllm/issues/34642) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect warning when both mistral & HF format are present in repo

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```sh uv pip install soxr librosa soundfile ``` Followed by: ``` VLLM_DISABLE_COMPILE_CACHE=1 vllm serve mistralai/Voxtral-Mini-4B-Realtime-2602 --compilation_config '{"cudagraph_mode": "PIECEWISE"}' ``` still leads to some very annoying warnings that are harmless but user experience takes a significant hit: ``` ', 'backend': 'inductor', 'custom_ops': [], 'splitting_ops': None, 'compile_mm_encoder': False, 'compile_sizes': None, 'compile_ranges_split_points': None, 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mo de': , 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': None, 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': None, 'pass_config': {}, 'max_cudagraph_capture_size': None, 'dynamic_shapes_config': {'type': , 'evaluate_guards': False, 'assume_32_bit_indexing': False}, 'local_cache_dir': None, 'fast_moe_cold_start': None, 'static_all_moe_layers': []}} (APIServer pid=2573353) WARNING 02-16 19:14:33 [config.py:1152] The params.json file is missing 'max_posi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ug ### Your current environment ### 🐛 Describe the bug ```sh uv pip install soxr librosa soundfile ``` Followed by: ``` VLLM_DISABLE_COMPILE_CACHE=1 vllm serve mistralai/Voxtral-Mini-4B-Realtime-2602 --compilation_confi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Incorrect warning when both mistral & HF format are present in repo bug ### Your current environment ### 🐛 Describe the bug ```sh uv pip install soxr librosa soundfile ``` Followed by: ``` VLLM_DISABLE_COMPILE_CA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: lm serve mistralai/Voxtral-Mini-4B-Realtime-2602 --compilation_config '{"cudagraph_mode": "PIECEWISE"}' ``` still leads to some very annoying warnings that are harmless but user experience takes a significant hit: ``` '...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: onfig': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mo de': , 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': None, 'cudag...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: that are harmless but user experience takes a significant hit: ``` ', 'backend': 'inductor', 'custom_ops': [], 'splitting_ops': None, 'compile_mm_encoder': False, 'compile_sizes': None, 'compile_ranges_split_points': No...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
