# vllm-project/vllm#39133: [Bug]: Gemma 4 31B INT4 on 2×24GB GPUs (TP=2): GPU KV cache size is 25,200 tokens at max_model_len=131072, gpu_memory_utilization=0.96, BF16 KV

| 字段 | 值 |
| --- | --- |
| Issue | [#39133](https://github.com/vllm-project/vllm/issues/39133) |
| 状态 | open |
| 标签 |  |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;quantization;triton |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 31B INT4 on 2×24GB GPUs (TP=2): GPU KV cache size is 25,200 tokens at max_model_len=131072, gpu_memory_utilization=0.96, BF16 KV

### Issue 正文摘录

### Your current environment - vLLM: `0.1.dev1+gd56e95223` (custom container built from this commit of `main`) - Hardware: 2× NVIDIA RTX 3090 (SM 8.6, 24 GB each), tensor parallel across both - Model: [`cyankiwi/gemma-4-31B-it-AWQ-4bit`](https://huggingface.co/cyankiwi/gemma-4-31B-it-AWQ-4bit) - Quantization (from the model's `config.json` → `quantization_config`): `quant_method: compressed-tensors`, `format: pack-quantized`, `num_bits: 4`, `group_size: 32`, `observer: mse`, `strategy: group`, `symmetric: true`, `type: int`. - Architecture (from the model's `config.json` → `text_config`): - `num_hidden_layers: 60` - `num_attention_heads: 32` - `num_key_value_heads: 16` - `head_dim: 256` - `global_head_dim: 512` - `sliding_window: 1024` - `layer_types`: 60 entries, of which **50 are `sliding_attention`** and **10 are `full_attention`** (verified by counting the array) ### `vllm serve` arguments ``` /models/cyankiwi/gemma-4-31B-it-AWQ-4bit --tensor-parallel-size 2 --max-num-seqs 1 --gpu-memory-utilization 0.96 --max-model-len 131072 --reasoning-parser gemma4 --enable-auto-tool-choice --tool-call-parser gemma4 --enable-prefix-caching --limit-mm-per-prompt '{"image": 0, "audio": 0}' -...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Gemma 4 31B INT4 on 2×24GB GPUs (TP=2): GPU KV cache size is 25,200 tokens at max_model_len=131072, gpu_memory_utilization=0.96, BF16 KV ### Your current environment - vLLM: `0.1.dev1+gd56e95223` (custom containe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Gemma 4 31B INT4 on 2×24GB GPUs (TP=2): GPU KV cache size is 25,200 tokens at max_model_len=131072, gpu_memory_utilization=0.96, BF16 KV ### Your current environment - vLLM: `0.1.dev1+gd56e95223` (custom containe...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: obal_head_dim=512). Forcing TRITON_ATTN backend to prevent mixed-backend numerical divergence. INFO [cuda.py:302] Using AttentionBackendEnum.TRITON_ATTN backend. INFO [gpu_model_runner.py:4820] Model loading took 10.46...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: custom container built from this commit of `main`) - Hardware: 2× NVIDIA RTX 3090 (SM 8.6, 24 GB each), tensor parallel across both - Model: [`cyankiwi/gemma-4-31B-it-AWQ-4bit`](https://huggingface.co/cyankiwi/gemma-4-3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: as heterogeneous head dimensions (head_dim=256, global_head_dim=512). Forcing TRITON_ATTN backend to prevent mixed-backend numerical divergence. INFO [cuda.py:302] Using AttentionBackendEnum.TRITON_ATTN backend. INFO [g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
