# vllm-project/vllm#39273: [Bug]: Ngram speculative decoding produces corrupted output on hybrid GDN (Qwen3.5) models

| 字段 | 值 |
| --- | --- |
| Issue | [#39273](https://github.com/vllm-project/vllm/issues/39273) |
| 状态 | open |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;fp8;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;nondeterministic |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ngram speculative decoding produces corrupted output on hybrid GDN (Qwen3.5) models

### Issue 正文摘录

### Your current environment - vLLM version: `0.18.1rc1.dev43+gdebd6e768` (also reproducible on latest nightly `0.18.1rc1.dev236`) - GPU: NVIDIA GH200 480GB - Model: Qwen3.5-9b (Qwen3.5 architecture, `model_type: qwen3_5_text`, hybrid GDN + full attention) ### Model description Qwen3.5-based model with hybrid architecture: 24 GatedDeltaNet (linear attention) layers + 8 full attention layers. FP8 quantized via compressed-tensors. Config includes `layer_types: [linear_attention, linear_attention, linear_attention, full_attention, ...]` repeating pattern. ### How to reproduce the error **Without ngram (correct output):** ```bash # Start vLLM with no speculative decoding vllm serve model-fp8 \ --trust-remote-code \ --enforce-eager \ --enable-chunked-prefill \ --max-model-len 131072 \ --max-num-batched-tokens 131072 \ --additional-config '{"gdn_prefill_backend": "triton"}' # Test curl -s http://localhost:8080/v1/completions -H "Content-Type: application/json" -d '{ "model": "model-fp8", "prompt": " \nclass Calculator:\n def add(self, a, b):\n return a + b\n \n \nAdd subtract and multiply methods\n ", "max_tokens": 300, "temperature": 0 }' ``` Output (correct): ``` class Calculator: def...

## 现有链接修复摘要

#40738 [Bugfix] Fix GDN conv + SSM state corruption with ngram spec decode

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Ngram speculative decoding produces corrupted output on hybrid GDN (Qwen3.5) models ### Your current environment - vLLM version: `0.18.1rc1.dev43+gdebd6e768` (also reproducible on latest nightly `0.18.1rc1.dev236...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: unning_state` and `new_num_computed_tokens` to determine which SSM state block to copy: ```python num_tokens_running_state = ( num_computed_tokens + num_scheduled_tokens - num_draft_tokens ) new_num_computed_tokens = nu...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: current environment - vLLM version: `0.18.1rc1.dev43+gdebd6e768` (also reproducible on latest nightly `0.18.1rc1.dev236`) - GPU: NVIDIA GH200 480GB - Model: Qwen3.5-9b (Qwen3.5 architecture, `model_type: qwen3_5_text`,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tput on hybrid GDN (Qwen3.5) models ### Your current environment - vLLM version: `0.18.1rc1.dev43+gdebd6e768` (also reproducible on latest nightly `0.18.1rc1.dev236`) - GPU: NVIDIA GH200 480GB - Model: Qwen3.5-9b (Qwen3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e: 24 GatedDeltaNet (linear attention) layers + 8 full attention layers. FP8 quantized via compressed-tensors. Config includes `layer_types: [linear_attention, linear_attention, linear_attention, full_attention, ...]` r...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40738](https://github.com/vllm-project/vllm/pull/40738) | closes_keyword | 0.95 | [Bugfix] Fix GDN conv + SSM state corruption with ngram spec decode | Fixes #39273 AI-assisted: Yes (Claude). Not duplicating any existing PR. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
