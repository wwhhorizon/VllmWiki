# vllm-project/vllm#31186: [Bug]: Qwen3-Next MTP Crash

| 字段 | 值 |
| --- | --- |
| Issue | [#31186](https://github.com/vllm-project/vllm/issues/31186) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next MTP Crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Getting a crash from Illegal Memory Access when running Qwen3-Next + MTP on 4xB200 with FLASH_ATTN. Works fine if I use FlashInfer, but note that TRTLLM attention does not apply here so FLASH_ATTN is the only one with full-cuda-graph support. That might be the real root cause here, hard to tell. ``` VLLM_ATTENTION_BACKEND=FLASH_ATTN \ vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \ --tokenizer-mode auto --gpu-memory-utilization 0.8 \ --tensor-parallel-size 4 --no-enable-chunked-prefill --no-enable-prefix-caching \ --speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' ``` Send GSM8k to reproduce crash. Sometimes need to send a second time before it dies ``` lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args base_url=$BASE_URL/v1/completions,model=$MODEL,tokenized_requests=False,tokenizer_backend=None,num_concurrent=512,timeout=120,max_retries=5 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of freq...

## 现有链接修复摘要

#33326 [Bugfix][Kernel] Fix negative memory offset in GDN Triton kernel | #34306 [CI][Bugfix] add regression test for GDN fused_recurrent kernel

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ng a crash from Illegal Memory Access when running Qwen3-Next + MTP on 4xB200 with FLASH_ATTN. Works fine if I use FlashInfer, but note that TRTLLM attention does not apply here so FLASH_ATTN is the only one with full-c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: running Qwen3-Next + MTP on 4xB200 with FLASH_ATTN. Works fine if I use FlashInfer, but note that TRTLLM attention does not apply here so FLASH_ATTN is the only one with full-cuda-graph support. That might be the real r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: NTION_BACKEND=FLASH_ATTN \ vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \ --tokenizer-mode auto --gpu-memory-utilization 0.8 \ --tensor-parallel-size 4 --no-enable-chunked-prefill --no-enable-prefix-caching \ --specu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Next MTP Crash bug ### Your current environment ### 🐛 Describe the bug Getting a crash from Illegal Memory Access when running Qwen3-Next + MTP on 4xB200 with FLASH_ATTN. Works fine if I use FlashInfer, but...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33326](https://github.com/vllm-project/vllm/pull/33326) | closes_keyword | 0.95 | [Bugfix][Kernel] Fix negative memory offset in GDN Triton kernel | Fixes #31186 cc @vadiklyutiy ### Root Cause The Triton kernel `fused_recurrent_gated_delta_rule_fwd_kernel` in GDN attention did not check for `PAD_SLOT_ID = -1` values in `ssm_s |
| [#34306](https://github.com/vllm-project/vllm/pull/34306) | closes_keyword | 0.95 | [CI][Bugfix] add regression test for GDN fused_recurrent kernel | Fix illegal memory access in `fused_recurrent` kernel when handling `PAD_SLOT_ID (-1)` for padded sequences ([Issue #31186](https://github.com/vllm-project/vllm/issues/31186)). ** |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
