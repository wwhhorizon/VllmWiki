# vllm-project/vllm#31709: [Bug]: After upgrade to 0.11.2, vllm crashs with Qwen3.

| 字段 | 值 |
| --- | --- |
| Issue | [#31709](https://github.com/vllm-project/vllm/issues/31709) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After upgrade to 0.11.2, vllm crashs with Qwen3.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After upgrade to 0.11.2, vllm may crash sometimes with Qwen3. Command to start vllm: ``` VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 uv run vllm serve \ Qwen/Qwen3-32B-FP8 \ --host 0.0.0.0 --port $port --seed 42 --trust-remote-code \ --enable-chunked-prefill --enable-prefix-caching \ --enable-prompt-tokens-details \ --reasoning-parser deepseek_r1 \ --gpu-memory-utilization 0.97 \ --max_num_seqs 100 \ --enable-auto-tool-choice --tool-call-parser hermes \ --hf-overrides '{"rope-scaling": {"factor": 4.0, "original_max_position_embeddings": 32768, "rope_type": "yarn"}}' \ -O3 \ --quantization fp8 \ --tensor-parallel-size 1 --max-model-len 87040 >> "$LOG_FILE" 2>&1 & ``` Error logs when it is crashed: ``` /tmp/torchinductor_root/q5/cq5iuvdeguweyk7x36xgxz2jrq5ktxlkxxg3u6legsnlo62zqcrn.py:97: unknown: block: [4,0,0], thread: [0,0,0] Assertion `index out of bounds: 0 , 'debug_dump_path': None, 'cache_dir': '/root/.cache/vllm/torch_compile_cache/86fcff198d', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['none', '+quant_fp8', '+quant_fp8'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_output...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: After upgrade to 0.11.2, vllm crashs with Qwen3. bug ### Your current environment ### 🐛 Describe the bug After upgrade to 0.11.2, vllm may crash sometimes with Qwen3. Command to start vllm: ``` VLLM_ALLOW_LONG_MA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: .0 --port $port --seed 42 --trust-remote-code \ --enable-chunked-prefill --enable-prefix-caching \ --enable-prompt-tokens-details \ --reasoning-parser deepseek_r1 \ --gpu-memory-utilization 0.97 \ --max_num_seqs 100 \ -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nds: 0 , 'debug_dump_path': None, 'cache_dir': '/root/.cache/vllm/torch_compile_cache/86fcff198d', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['none', '+quant_fp8', '+quant_fp8'], 'split...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: /q5/cq5iuvdeguweyk7x36xgxz2jrq5ktxlkxxg3u6legsnlo62zqcrn.py:97: unknown: block: [4,0,0], thread: [0,0,0] Assertion `index out of bounds: 0 , 'debug_dump_path': None, 'cache_dir': '/root/.cache/vllm/torch_compile_cache/8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: LM_ALLOW_LONG_MAX_MODEL_LEN=1 uv run vllm serve \ Qwen/Qwen3-32B-FP8 \ --host 0.0.0.0 --port $port --seed 42 --trust-remote-code \ --enable-chunked-prefill --enable-prefix-caching \ --enable-prompt-tokens-details \ --re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
