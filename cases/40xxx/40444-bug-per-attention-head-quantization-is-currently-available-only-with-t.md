# vllm-project/vllm#40444: [Bug]: Per-attention-head quantization is currently available only with the Flash Attention backend and requires the calibration pathway provided by llm-compressor.

| 字段 | 值 |
| --- | --- |
| Issue | [#40444](https://github.com/vllm-project/vllm/issues/40444) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Per-attention-head quantization is currently available only with the Flash Attention backend and requires the calibration pathway provided by llm-compressor.

### Issue 正文摘录

### Your current environment Per-attention-head quantization is currently available only with the Flash Attention backend and requires the calibration pathway provided by llm-compressor. 在flashinfer后端的话，支持per attention head量化的算子吗？ 有对应的算子实现吗？ 如果量化模型是per attention head FP8+ flasinfer后端，那attention计算是有对应的算子实现还是 回推到flash attention3的fp8计算 ### 🐛 Describe the bug "quantization_config": { "config_groups": { "group_0": { "format": "dense", "input_activations": { "actorder": null, "block_structure": null, "dynamic": false, "group_size": null, "num_bits": 8, "observer": "memoryless_minmax", "observer_kwargs": {}, "scale_dtype": null, "strategy": "attn_head", "symmetric": true, "type": "float", "zp_dtype": null }, "output_activations": null, "targets": [ "Qwen3VLTextAttention" ], "weights": null }, "group_1": { "format": "float-quantized", "input_activations": { "actorder": null, "block_structure": null, "dynamic": true, "group_size": 128, "num_bits": 8, "observer": null, "observer_kwargs": {}, "scale_dtype": null, "strategy": "group", "symmetric": true, "type": "float", "zp_dtype": null }, "output_activations": null, "targets": [ "Linear" ], "weights": { "actorder": null, "block_structure": [...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Per-attention-head quantization is currently available only with the Flash Attention backend and requires the calibration pathway provided by llm-compressor. bug ### Your current environment Per-attention-head qu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 子实现还是 回推到flash attention3的fp8计算 ### 🐛 Describe the bug "quantization_config": { "config_groups": { "group_0": { "format": "dense", "input_activations": { "actorder": null, "block_structure": null, "dynamic": false, "gro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: g]: Per-attention-head quantization is currently available only with the Flash Attention backend and requires the calibration pathway provided by llm-compressor. bug ### Your current environment Per-attention-head quant...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ", "input_activations": { "actorder": null, "block_structure": null, "dynamic": false, "group_size": null, "num_bits": 8, "observer": "memoryless_minmax", "observer_kwargs": {}, "scale_dtype": null,
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: compressed", "sparsity_config": {}, "transform_config": {}, "version": "0.15.0.1" }, ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bot...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
