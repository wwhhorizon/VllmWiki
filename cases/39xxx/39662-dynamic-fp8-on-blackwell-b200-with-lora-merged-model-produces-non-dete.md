# vllm-project/vllm#39662: Dynamic FP8 on Blackwell B200 with LoRA-merged model produces non-deterministic degenerate output

| 字段 | 值 |
| --- | --- |
| Issue | [#39662](https://github.com/vllm-project/vllm/issues/39662) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | nondeterministic |
| 根因提示 | dtype;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Dynamic FP8 on Blackwell B200 with LoRA-merged model produces non-deterministic degenerate output

### Issue 正文摘录

## Summary Dynamic FP8 quantization (`--quantization fp8` on BF16 weights) on NVIDIA Blackwell B200 with a LoRA-merged 123B model (Mistral Large architecture) produces **non-deterministic degenerate output** — coherent text for ~500-1000 tokens that then enters repetition loops and degrades into gibberish. ## Environment - **GPU**: NVIDIA B200 192GB (single GPU) - **vLLM**: 0.19.0 - **PyTorch**: 2.10.0+cu128 - **CUDA**: 12.8 - **Model**: 123B parameter Mistral Large derivative, LoRA rank-64 merged into base via PEFT `merge_and_unload()` - **Quantization**: `--quantization fp8` (dynamic, no pre-quantized weights) ## Reproduction 1. Train a LoRA adapter on a 123B Mistral Large model 2. Merge LoRA into base with `model.merge_and_unload()`, save as BF16 safetensors 3. Serve with vLLM on B200: `--quantization fp8 --dtype bfloat16` 4. Send chat completions with `max_tokens >= 1024` ## Observed behavior - **~50% of generations**: Model produces coherent thinking/output for 500-1000 tokens, then enters a repetition loop (same phrase repeated 5+ times), then degrades into garbled tokens - **~50% of generations**: Model produces correct output with proper ` ` closing and coherent response -...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: Dynamic FP8 on Blackwell B200 with LoRA-merged model produces non-deterministic degenerate output ## Summary Dynamic FP8 quantization (`--quantization fp8` on BF16 weights) on NVIDIA Blackwell B200 with a LoRA-merged 12...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Dynamic FP8 on Blackwell B200 with LoRA-merged model produces non-deterministic degenerate output ## Summary Dynamic FP8 quantization (`--quantization fp8` on BF16 weights) on NVIDIA Blackwell B200 with a LoRA-merged 12...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: Dynamic FP8 on Blackwell B200 with LoRA-merged model produces non-deterministic degenerate output ## Summary Dynamic FP8 quantization (`--quantization fp8` on BF16 weights) on NVIDIA Blackwell B200 with a LoRA-merged 12...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: `, the model almost always hits token limit without closing its thinking block - The same model served **without** `--quantization fp8` (pure BF16 on 2x H200 with TP=2) works correctly ## Analysis We believe this is rel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Dynamic FP8 on Blackwell B200 with LoRA-merged model produces non-deterministic degenerate output ## Summary Dynamic FP8 quantization (`--quantization fp8` on BF16 weights) on NVIDIA Blackwell B200 with a LoRA-merged 12...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
