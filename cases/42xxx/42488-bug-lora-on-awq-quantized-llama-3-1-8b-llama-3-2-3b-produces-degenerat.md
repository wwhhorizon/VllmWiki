# vllm-project/vllm#42488: [Bug]: LoRA on AWQ-quantized Llama-3.1-8B / Llama-3.2-3B produces degenerate output (same LoRA infra works on AWQ Mistral and on FP8 / BF16 Llama)

| 字段 | 值 |
| --- | --- |
| Issue | [#42488](https://github.com/vllm-project/vllm/issues/42488) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;quantization |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRA on AWQ-quantized Llama-3.1-8B / Llama-3.2-3B produces degenerate output (same LoRA infra works on AWQ Mistral and on FP8 / BF16 Llama)

### Issue 正文摘录

### Your current environment ## Environment ``` vLLM: 0.20.0 torch: 2.11.0+cu130 transformers: 4.57.6 Python: 3.12.9 GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (sm_120), 97 GB CUDA: 13.0 OS: Debian Linux 6.1 ``` ### 🐛 Describe the bug ## Summary When serving an **AWQ-quantized Llama-3 base model with a LoRA adapter**, output is degenerate: - ~45% of requests have **neither expected label token in `top_logprobs=20`** — the output distribution is shifted off the target subset entirely. - The remaining ~55% produce a near-constant prediction (`recall ≈ 1.0, precision ≈ 0.08` on a binary toxicity classification, or the inverse: `recall ≈ 0, precision ≈ 0` depending on which Llama variant). - AUROC ≈ 0.58, vs ≈ 0.98 on FP8 / BF16 Llama with the same LoRA. The same Punica + LoRA wrapper code paths handle **Mistral-7B-Instruct-v0.3 AWQ + LoRA** correctly (AUROC 0.97), and the **Llama AWQ base without LoRA** produces perfectly sensible zero-shot output. So the failure is specifically at the intersection **Llama-family architecture × AWQ-quantized base × LoRA**. ## Reproducer ```bash # Broken: Llama-3.1-8B AWQ + toxicity LoRA python -m vllm.entrypoints.openai.api_server \ --model hu...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: LoRA on AWQ-quantized Llama-3.1-8B / Llama-3.2-3B produces degenerate output (same LoRA infra works on AWQ Mistral and on FP8 / BF16 Llama) bug ### Your current environment ## Environment ``` vLLM: 0.20.0 torch:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: LoRA on AWQ-quantized Llama-3.1-8B / Llama-3.2-3B produces degenerate output (same LoRA infra works on AWQ Mistral and on FP8 / BF16 Llama) bug ### Your current environment ## Environment ``` vLLM: 0.20.0 torch:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: The remaining ~55% produce a near-constant prediction (`recall ≈ 1.0, precision ≈ 0.08` on a binary toxicity classification, or the inverse: `recall ≈ 0, precision ≈ 0` depending on which Llama variant). - AUROC ≈ 0.58,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 20.0 torch: 2.11.0+cu130 transformers: 4.57.6 Python: 3.12.9 GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (sm_120), 97 GB CUDA: 13.0 OS: Debian Linux 6.1 ``` ### 🐛 Describe the bug ## Summary When serving an **AWQ-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: exp(logprob) over tokens normalizing to "true"` over `Σ over {"true","false"}`. Note: both LoRA repos and the evaluation dataset (`rungalileo/automated-ft-luna-toxicity`) are gated on the rungalileo HF org. A maintainer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
