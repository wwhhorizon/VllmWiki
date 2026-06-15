# vllm-project/vllm#30052: [Bug]: An error will occur when using a quantization configuration with modules_to_not_convert for the DeepSeek-V3.2 model on non-NVIDIA GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#30052](https://github.com/vllm-project/vllm/issues/30052) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | gemm;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: An error will occur when using a quantization configuration with modules_to_not_convert for the DeepSeek-V3.2 model on non-NVIDIA GPUs

### Issue 正文摘录

### Your current environment vllm_version: - release/v0.11.1 DeepSeek-V3.2-Exp-AWQ: https://huggingface.co/QuantTrio/DeepSeek-V3.2-Exp-AWQ/blob/main/config.json "quantization_config": { -- "quant_method": "awq", "bits": 4, "group_size": 128, "version": "gemm", "zero_point": true, "modules_to_not_convert": ["mlp.gate.", "indexer", "model.layers.0.", "model.layers.1.", "model.layers.2.", "model.layers.60.", "model.layers.61."] }, server launch code - python -m vllm.entrypoints.openai.api_server --port 8000 --model=/home/models/DeepSeek-V3.2-Exp-AWQ --tensor-parallel-size=8 --disable-log-requests --gpu-memory-utilization=0.8 --block-size=64 --dtype=auto --max-model-len=10 --max-num-batched-tokens 10 --max-num-seqs 1 --trust-remote-code --enforce-eager --quantization=awq error: (Worker_TP0 pid=10292) ERROR 12-04 10:31:42 [multiproc_executor.py:743] File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 1124, in __init__ (Worker_TP0 pid=10292) ERROR 12-04 10:31:42 [multiproc_executor.py:743] self.mlp = DeepseekV2MoE( (Worker_TP0 pid=10292) ERROR 12-04 10:31:42 [multiproc_executor.py:743] File "/usr/local/lib/python3.10/dist-packages/vllm/model_ex...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: An error will occur when using a quantization configuration with modules_to_not_convert for the DeepSeek-V3.2 model on non-NVIDIA GPUs bug ### Your current environment vllm_version: - release/v0.11.1 DeepSeek-V3....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ": { -- "quant_method": "awq", "bits": 4, "group_size": 128, "version": "gemm", "zero_point": true, "modules_to_not_convert": ["mlp.gate.", "indexer", "model.layers.0.", "model.layers.1.", "model.layers.2.", "model.laye...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: eek-V3.2 model on non-NVIDIA GPUs bug ### Your current environment vllm_version: - release/v0.11.1 DeepSeek-V3.2-Exp-AWQ: https://huggingface.co/QuantTrio/DeepSeek-V3.2-Exp-AWQ/blob/main/config.json "quantization_config...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: An error will occur when using a quantization configuration with modules_to_not_convert for the DeepSeek-V3.2 model on non-NVIDIA GPUs bug ### Your current environment vllm_version: - release/v0.11.1 DeepSeek-V3....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: allel-size=8 --disable-log-requests --gpu-memory-utilization=0.8 --block-size=64 --dtype=auto --max-model-len=10 --max-num-batched-tokens 10 --max-num-seqs 1 --trust-remote-code --enforce-eager --quantization=awq error:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
