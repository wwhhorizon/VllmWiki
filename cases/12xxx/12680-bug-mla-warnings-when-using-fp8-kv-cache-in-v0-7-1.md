# vllm-project/vllm#12680: [Bug]: MLA Warnings when using FP8 KV cache in v0.7.1

| 字段 | 值 |
| --- | --- |
| Issue | [#12680](https://github.com/vllm-project/vllm/issues/12680) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MLA Warnings when using FP8 KV cache in v0.7.1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Since v0.7.1, there are a lot of warnings when using fp8 KV cache on models quantized with llm-compressor : WARNING 02-02 22:55:17 config.py:991] compressed-tensors MLA support requires fp8 activations and weights in group 'group_0', but got activations type 'float' and weights type 'float'. WARNING 02-02 22:55:17 config.py:991] Full config: {'config_groups': {'group_0': {'input_activations': {'actorder': None, 'block_structure': None, 'dynamic': False, 'group_size': None, 'num_bits': 8, 'observer': 'minmax', 'observer_kwargs': {}, 'strategy': 'tensor', 'symmetric': True, 'type': 'float'}, 'output_activations': None, 'targets': ['Linear'], 'weights': {'actorder': None, 'block_structure': None, 'dynamic': False, 'group_size': None, 'num_bits': 8, 'observer': 'minmax', 'observer_kwargs': {}, 'strategy': 'tensor', 'symmetric': True, 'type': 'float'}}}, 'format': 'float-quantized', 'global_compression_ratio': 1.462046196596282, 'ignore': ['lm_head'], 'kv_cache_scheme': {'actorder': None, 'block_structure': None, 'dynamic': False, 'group_size': None, 'num_bits': 8, 'observer': 'minmax', 'observer_kw...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ng FP8 KV cache in v0.7.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Since v0.7.1, there are a lot of warnings when using fp8 KV cache on models quantized with llm-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: MLA Warnings when using FP8 KV cache in v0.7.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Since v0.7.1, there are a lot of warnings when using fp8 KV cache o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: {'config_groups': {'group_0': {'input_activations': {'actorder': None, 'block_structure': None, 'dynamic': False, 'group_size': None, 'num_bits': 8, 'observer': 'minmax', 'observer_kwargs': {}, 'strategy': 'tensor', 'sy...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 601 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: MLA Warnings when using FP8 KV cache in v0.7.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Since v0.7.1, there are a lot of warnings when using fp8 KV cache o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
