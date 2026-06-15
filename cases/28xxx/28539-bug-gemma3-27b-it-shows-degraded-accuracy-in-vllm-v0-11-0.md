# vllm-project/vllm#28539: [Bug]: gemma3-27b-it shows degraded accuracy in vLLM v0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#28539](https://github.com/vllm-project/vllm/issues/28539) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gemma3-27b-it shows degraded accuracy in vLLM v0.11.0

### Issue 正文摘录

### Your current environment **Current environment** vLLM version: v0.11.0 docker image: vllm/vllm-openai:v0.11.0 ### 🐛 Describe the bug I'm testing open-source models using vLLM v0.11.0 on Nvidia H20 and AMD Instinct MI308X using `lm_eval==0.4.9.1` from [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness). However, I found [gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) shows degraded accuracy compared to Hugging face transformers implementation, similar issue reported in https://github.com/vllm-project/vllm/issues/17689, [PR21927](https://github.com/vllm-project/vllm/pull/21927) try to address sliding window configuration issue, but it seems does not resolve the original accuracy issue. **HF transformers 4.57.1 results** `lm_eval --model hf --model_args pretrained=google/gemma-3-27b-it,dtype=bfloat16,trust_remote_code=True --tasks hellaswag,lambada_openai` Tasks | Version | Filter | n-shot | Metric | | Value | | Stderr -- | -- | -- | -- | -- | -- | -- | -- | -- hellaswag | 1 | none | 0 | acc | ↑ | 0.6503 | ± | 0.0048 | | none | 0 | acc_norm | ↑ | 0.8406 | ± | 0.0037 lambada_openai | 1 | none | 0 | acc | ↑ | 0.6953 | ± | 0.0064 | | none | 0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: M v0.11.0 bug ### Your current environment **Current environment** vLLM version: v0.11.0 docker image: vllm/vllm-openai:v0.11.0 ### 🐛 Describe the bug I'm testing open-source models using vLLM v0.11.0 on Nvidia H20 and...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: gemma3-27b-it shows degraded accuracy in vLLM v0.11.0 bug ### Your current environment **Current environment** vLLM version: v0.11.0 docker image: vllm/vllm-openai:v0.11.0 ### 🐛 Describe the bug I'm testing open-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: none | 0 | perplexity | ↓ | 960.5903 | ± | 76.8435 **AMD Instinct 308X Triton Flash Attention + vLLM 0.11.0 results** `VLLM_ROCM_USE_AITER=1 VLLM_USE_TRITON_FLASH_ATTN=1 VLLM_ROCM_USE_AITER_MHA=0 VLLM_ROCM_USE_AITER_PAG...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ts** `lm_eval --model hf --model_args pretrained=google/gemma-3-27b-it,dtype=bfloat16,trust_remote_code=True --tasks hellaswag,lambada_openai` Tasks | Version | Filter | n-shot | Metric | | Value | | Stderr -- | -- | --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: **AMD Instinct 308X Triton Flash Attention + vLLM 0.11.0 results** `VLLM_ROCM_USE_AITER=1 VLLM_USE_TRITON_FLASH_ATTN=1 VLLM_ROCM_USE_AITER_MHA=0 VLLM_ROCM_USE_AITER_PAGED_ATTN=0 lm_eval --model vllm --model_args pretrai...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
