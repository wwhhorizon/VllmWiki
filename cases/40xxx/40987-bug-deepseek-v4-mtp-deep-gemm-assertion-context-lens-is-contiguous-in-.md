# vllm-project/vllm#40987: [Bug][DeepSeek-V4][MTP] deep_gemm assertion: context_lens.is_contiguous() in paged MQA metadata

| 字段 | 值 |
| --- | --- |
| Issue | [#40987](https://github.com/vllm-project/vllm/issues/40987) |
| 状态 | open |
| 标签 | DSv4 |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;fp8;moe;quantization |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][DeepSeek-V4][MTP] deep_gemm assertion: context_lens.is_contiguous() in paged MQA metadata

### Issue 正文摘录

## Problem `vllm serve` with DeepSeek-V4-Pro + `speculative_config={"method":"mtp","num_speculative_tokens":1}` crashes under load with: ``` RuntimeError: Assertion error (.../deepgemm-src/csrc/apis/attention.hpp:200): context_lens.is_contiguous() ``` it's very easy to be triggered by a "1:2K" (50 batch) by "vllm bench" After first worker failure, DP collectives fail with `gloo ... Connection closed by peer` (secondary symptom). ## Environment - vLLM: image: vllm/vllm-openai:deepseekv4-cu129 - Model: `deepseek-ai/DeepSeek-V4-Pro` - Quantization: `deepseek_v4_fp8` - H200 * 2 * 8 - KV cache dtype: `fp8` - Data parallel: `--data-parallel-size 16 --data-parallel-size-local 8 --data-parallel-hybrid-lb` - Spec decode: `--speculative_config {"method":"mtp","num_speculative_tokens":1}` ## Reproduction ### Serve command ```bash vllm serve /model-cache/ \ --served-model-name deepseek-ai/DeepSeek-V4-Pro \ --port 8000 \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-hybrid-lb \ --data-parallel-size 16 \ --data-parallel-size-local 8 \ --data-parallel-address ***** \ --data-parallel-start-rank 8 \ --max-model-len 700000 \ --gpu-memory-...

## 现有链接修复摘要

#40989 [Bugfix] Ensure DeepGEMM metadata gets contiguous context_lens

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug][DeepSeek-V4][MTP] deep_gemm assertion: context_lens.is_contiguous() in paged MQA metadata DSv4 ## Problem `vllm serve` with DeepSeek-V4-Pro + `speculative_config={"method":"mtp","num_speculative_tokens":1}` crashe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: paged MQA metadata DSv4 ## Problem `vllm serve` with DeepSeek-V4-Pro + `speculative_config={"method":"mtp","num_speculative_tokens":1}` crashes under load with: ``` RuntimeError: Assertion error (.../deepgemm-src/csrc/a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: lm/vllm-openai:deepseekv4-cu129 - Model: `deepseek-ai/DeepSeek-V4-Pro` - Quantization: `deepseek_v4_fp8` - H200 * 2 * 8 - KV cache dtype: `fp8` - Data parallel: `--data-parallel-size 16 --data-parallel-size-local 8 --da...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: -ai/DeepSeek-V4-Pro` - Quantization: `deepseek_v4_fp8` - H200 * 2 * 8 - KV cache dtype: `fp8` - Data parallel: `--data-parallel-size 16 --data-parallel-size-local 8 --data-parallel-hybrid-lb` - Spec decode: `--speculati...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug][DeepSeek-V4][MTP] deep_gemm assertion: context_lens.is_contiguous() in paged MQA metadata DSv4 ## Problem `vllm serve` with DeepSeek-V4-Pro + `speculative_config={"method":"mtp","num_speculative_tokens":1}` crashe...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40989](https://github.com/vllm-project/vllm/pull/40989) | closes_keyword | 0.95 | [Bugfix] Ensure DeepGEMM metadata gets contiguous context_lens | closes #40987. ### NOTE Warning: **AI Assistance: This PR was created with AI assistance** I've no clear idea of the fix. So this PR is just a "stone" to inspire wh |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
