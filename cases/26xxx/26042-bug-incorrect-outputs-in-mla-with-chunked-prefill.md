# vllm-project/vllm#26042: [Bug]: Incorrect outputs in MLA with chunked prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#26042](https://github.com/vllm-project/vllm/issues/26042) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect outputs in MLA with chunked prefill

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running MLA models with the flashinfer prefill are giving incorrect outputs when the input exceeds max_num_batched_tokens (when chunked prefill runs). It looks like something is getting overwritten and it only ever ends up using the first chunk (or the last?). Here's an example deployment to reproduce on 8xB200: ```bash VLLM_ATTENTION_BACKEND=FLASHINFER_MLA VLLM_FLASHINFER_MOE_BACKEND=latency VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve deepseek-ai/DeepSeek-R1-0528 -tp 8 --max-model-len 8192 --no-enable-prefix-caching --port 8049 --max-num-batched-tokens 512 ``` GSM8k results (expected 93+ %): ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.6467|± |0.0132| | | |strict-match | 5|exact_match|↑ |0.6414|± |0.0132| ``` It gets worse if the chunked prefill size goes smaller. Unsure if it's specific to blackwell right now, but I initially encountered this with 4xB200 running DSR1-FP4 with CUTLASS_MLA, so it might not be flashinfer's fault ### Before submitting a new issue... - [x] Make sure you already sear...

## 现有链接修复摘要

#25984 [Spec Decode] Enable efficient speculative decoding with FlashInfer-MLA

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rst chunk (or the last?). Here's an example deployment to reproduce on 8xB200: ```bash VLLM_ATTENTION_BACKEND=FLASHINFER_MLA VLLM_FLASHINFER_MOE_BACKEND=latency VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve deepseek-ai/DeepS...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: rent environment ### 🐛 Describe the bug Running MLA models with the flashinfer prefill are giving incorrect outputs when the input exceeds max_num_batched_tokens (when chunked prefill runs). It looks like something is g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: x-num-batched-tokens 512 ``` GSM8k results (expected 93+ %): ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-ex...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Incorrect outputs in MLA with chunked prefill bug ### Your current environment ### 🐛 Describe the bug Running MLA models with the flashinfer prefill are giving incorrect outputs when the input exceeds max_num_bat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ASHINFER_MLA VLLM_FLASHINFER_MOE_BACKEND=latency VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve deepseek-ai/DeepSeek-R1-0528 -tp 8 --max-model-len 8192 --no-enable-prefix-caching --port 8049 --max-num-batched-tokens 512 ``` G...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25984](https://github.com/vllm-project/vllm/pull/25984) | mentioned | 0.6 | [Spec Decode] Enable efficient speculative decoding with FlashInfer-MLA | deprecate `Cutlass-MLA` when speculative decoding is enabled.~~ See #26042 for tracking on this correctness issue, which seems to indicate the root cause is MLA chunked prefill. T… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
