# vllm-project/vllm#6098: [Bug]: Some cuda error when launching qwen2-instruct-7b

| 字段 | 值 |
| --- | --- |
| Issue | [#6098](https://github.com/vllm-project/vllm/issues/6098) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cache;cuda;quantization |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Some cuda error when launching qwen2-instruct-7b

### Issue 正文摘录

### Your current environment cuda118,3090 24gb*2 xinference-latest docker ### 🐛 Describe the bug Why would these cuda error happen when launching qwen2-instruct 7b？(if not specified, using cuda:1) {'max_model_len': 32768, 'gpu_memory_utilization': 0.95, 'swap_space': 0, 'enforce_eager': True, 'tokenizer_mode': 'auto', 'trust_remote_code': True, 'tensor_parallel_size': 1, 'block_size': 16, 'max_num_seqs': 256, 'quantization': None}： success {'max_model_len': 16384, 'gpu_memory_utilization': 0.85, 'swap_space': 0, 'enforce_eager': True, 'tokenizer_mode': 'auto', 'trust_remote_code': True, 'tensor_parallel_size': 1, 'block_size': 16, 'max_num_seqs': 256, 'quantization': None} cuda error {'max_model_len': 4096, 'gpu_memory_utilization': 0.9, 'swap_space': 4, 'tokenizer_mode': 'auto', 'trust_remote_code': True, 'tensor_parallel_size': 1, 'block_size': 16, 'max_num_seqs': 256, 'quantization': None} cuda error {'swap_space': 0, 'enforce_eager': True, 'tokenizer_mode': 'auto', 'trust_remote_code': True, 'tensor_parallel_size': 1, 'block_size': 16, 'gpu_memory_utilization': 0.9, 'max_num_seqs': 256, 'quantization': None, 'max_model_len': 4096} cuda error {'tokenizer_mode': 'auto', 'trust_r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: bug ### Your current environment cuda118,3090 24gb*2 xinference-latest docker ### 🐛 Describe the bug Why would these cuda error happen when launching qwen2-instruct 7b？(if not specified, using cuda:1) {'max_model_len':...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Some cuda error when launching qwen2-instruct-7b bug ### Your current environment cuda118,3090 24gb*2 xinference-latest docker ### 🐛 Describe the bug Why would these cuda error happen when launching qwen2-instruc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: True, 'tensor_parallel_size': 1, 'block_size': 16, 'max_num_seqs': 256, 'quantization': None}： success {'max_model_len': 16384, 'gpu_memory_utilization': 0.85, 'swap_space': 0, 'enforce_eager': True, 'tokenizer_mode': '...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Some cuda error when launching qwen2-instruct-7b bug ### Your current environment cuda118,3090 24gb*2 xinference-latest docker ### 🐛 Describe the bug Why would these cuda error happen when launching qwen2-instruc...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 32768) is larger than the maximum number of tokens that can be stored in KV cache (24192). {'gpu_memory_utilization': 0.85, 'swap_space': 0, 'enforce_eager': True, 'tokenizer_mode': 'auto', 'trust_remote_code': True, 't...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
