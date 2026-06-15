# vllm-project/vllm#44318: [Bug]: GGUF model loading fails on XPU: `_C` namespace missing `ggml_dequantize` custom op

| 字段 | 值 |
| --- | --- |
| Issue | [#44318](https://github.com/vllm-project/vllm/issues/44318) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GGUF model loading fails on XPU: `_C` namespace missing `ggml_dequantize` custom op

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Command:** ```bash vllm serve /data/shared/models/gguf/Qwen/Qwen3-1.7B-GGUF/Qwen3-1.7B-Q8_0.gguf \ --load-format gguf \ --tokenizer Qwen/Qwen3-1.7B \ -tp 1 -pp 1 -dp 1 ``` ## Log ## Error ``` AttributeError: '_OpNamespace' '_C' object has no attribute 'ggml_dequantize' ``` ### Full call chain (bottom-up) ``` File "vllm/_custom_ops.py", line 2201, in ggml_dequantize return torch.ops._C.ggml_dequantize(W, quant_type, m, n, dtype) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ AttributeError: '_OpNamespace' '_C' object has no attribute 'ggml_dequantize' ``` The crash propagates through: 1. `vllm/v1/engine/core.py:250` — `_initialize_kv_caches()` calls `determine_available_memory()` 2. `vllm/v1/worker/gpu_worker.py:392` — `profile_run()` runs a dummy forward pass 3. `vllm/v1/worker/gpu_model_runner.py:5948` → `_dummy_run()` at line 5616 4. Model forward: `vllm/model_executor/models/qwen3.py:323` → `vllm/model_executor/models/qwen2.py:389` 5. Compiled inductor code calls `torch.ops.vllm._apply_gguf_embedding.default()` 6. `vllm/model_executor/layers/quantization/gguf.py:401` — `_apply_gguf_embedding()`: ```python dequant = ops.ggml_dequantize(quant,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: utor/models/qwen3.py:323` → `vllm/model_executor/models/qwen2.py:389` 5. Compiled inductor code calls `torch.ops.vllm._apply_gguf_embedding.default()` 6. `vllm/model_executor/layers/quantization/gguf.py:401` — `_apply_g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: GGUF model loading fails on XPU: `_C` namespace missing `ggml_dequantize` custom op bug ### Your current environment ### 🐛 Describe the bug **Command:** ```bash vllm serve /data/shared/models/gguf/Qwen/Qwen3-1.7B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GGUF model loading fails on XPU: `_C` namespace missing `ggml_dequantize` custom op bug ### Your current environment ### 🐛 Describe the bug **Command:** ```bash vllm serve /data/shared/models/gguf/Qwen/Qwen3-1.7B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pe) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: `determine_available_memory()` 2. `vllm/v1/worker/gpu_worker.py:392` — `profile_run()` runs a dummy forward pass 3. `vllm/v1/worker/gpu_model_runner.py:5948` → `_dummy_run()` at line 5616 4. Model forward: `vllm/model_e...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
