# vllm-project/vllm#40153: [Bug]: GPT-OSS-20B on RTX PRO 6000 (SM120) falls back to TRITON_ATTN + Marlin; forcing FLASHINFER fails with sink setting not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#40153](https://github.com/vllm-project/vllm/issues/40153) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS-20B on RTX PRO 6000 (SM120) falls back to TRITON_ATTN + Marlin; forcing FLASHINFER fails with sink setting not supported

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using vLLM on an **RTX PRO 6000 Blackwell (SM120 / compute capability 12.0)** with **GPT-OSS-20B**, the model works with the default backend selection, but it does **not** take the expected optimized backend path. Instead, on the default path, vLLM initializes successfully and selects: - `TRITON_ATTN` for attention - `Marlin` for the MXFP4 / MoE path What I expect on this GPU is: - **FlashInfer** for attention - **MXFP4_MXFP8_CUTLASS** for the MoE path When I explicitly force the attention backend to `FLASHINFER`, engine initialization fails immediately with: ```text ValueError: Selected backend AttentionBackendEnum.FLASHINFER is not valid for this configuration. Reason: ['sink setting not supported'] ``` I also observed the same kind of rejection when trying `FLASH_ATTN`. This looks like GPT-OSS on **SM120** is currently falling back to `TRITON_ATTN + Marlin` instead of taking a **FlashInfer** attention path plus an **MXFP4/MXFP8 CUTLASS** MoE path. --- ### To Reproduce Minimal repro: ```python from vllm import LLM llm = LLM( model="./gpt-oss-20b", tensor_parallel_size=1, max_num_seqs=1, max_model_len=8192, enable_chunked_prefil...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: [Bug]: GPT-OSS-20B on RTX PRO 6000 (SM120) falls back to TRITON_ATTN + Marlin; forcing FLASHINFER fails with sink setting not supported bug ### Your current environment ### 🐛 Describe the bug Using vLLM on an **RTX PRO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: GPT-OSS-20B on RTX PRO 6000 (SM120) falls back to TRITON_ATTN + Marlin; forcing FLASHINFER fails with sink setting not supported bug ### Your current environment ### 🐛 Describe the bug Using vLLM on an **RTX PRO...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: T-OSS-20B on RTX PRO 6000 (SM120) falls back to TRITON_ATTN + Marlin; forcing FLASHINFER fails with sink setting not supported bug ### Your current environment ### 🐛 Describe the bug Using vLLM on an **RTX PRO 6000 Blac...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: cessfully and selects: - `TRITON_ATTN` for attention - `Marlin` for the MXFP4 / MoE path What I expect on this GPU is: - **FlashInfer** for attention - **MXFP4_MXFP8_CUTLASS** for the MoE path When I explicitly force th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPT-OSS-20B on RTX PRO 6000 (SM120) falls back to TRITON_ATTN + Marlin; forcing FLASHINFER fails with sink setting not supported bug ### Your current environment ### 🐛 Describe the bug Using vLLM on an **RTX PRO...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
