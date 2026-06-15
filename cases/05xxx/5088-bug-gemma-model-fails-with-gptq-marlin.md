# vllm-project/vllm#5088: [Bug]: Gemma model fails with GPTQ marlin

| 字段 | 值 |
| --- | --- |
| Issue | [#5088](https://github.com/vllm-project/vllm/issues/5088) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma model fails with GPTQ marlin

### Issue 正文摘录

### 🐛 Describe the bug Using docker and gemma finetuned model --model /data/merged_model_GPTQ --max-model-len 8192 --max-num-seqs 1024 --served-model-name model --quantization gptq_marlin fails with RuntimeError: Some weights are not initialized from checkpoints: {'model.layers.3.mlp.gate_up_proj.g_idx_sort_indices', 'model.layers.8.self_attn.qkv_proj.g_idx_sort_indices', 'model.layers.9.mlp.gate_up_proj.g_idx_sort_indices ..... The same works with --quantization gptq

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma model fails with GPTQ marlin bug ### 🐛 Describe the bug Using docker and gemma finetuned model --model /data/merged_model_GPTQ --max-model-len 8192 --max-num-seqs 1024
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g]: Gemma model fails with GPTQ marlin bug ### 🐛 Describe the bug Using docker and gemma finetuned model --model /data/merged_model_GPTQ --max-model-len 8192 --max-num-seqs 1024 --served-model-name model --quantization...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: --max-num-seqs 1024 --served-model-name model --quantization gptq_marlin fails with RuntimeError: Some weights are not initialized from checkpoints: {'model.layers.3.mlp.gate_up_proj.g_idx_sort_indices', 'model.layers.8...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma model fails with GPTQ marlin bug ### 🐛 Describe the bug Using docker and gemma finetuned model --model /data/merged_model_GPTQ --max-model-len 8192 --max-num-seqs 1024

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
