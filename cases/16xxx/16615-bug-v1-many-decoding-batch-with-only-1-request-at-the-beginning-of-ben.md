# vllm-project/vllm#16615: [Bug][V1]: Many decoding batch with only 1 request at the beginning of benchmarking when request-rate is inf

| 字段 | 值 |
| --- | --- |
| Issue | [#16615](https://github.com/vllm-project/vllm/issues/16615) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][V1]: Many decoding batch with only 1 request at the beginning of benchmarking when request-rate is inf

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When `request-rate` is set to inf, we expect we are gradually increasing the number of decoding in a batch until it hits the kv cache capacity limit. But when I added the print code at the end of `_prepare_inputs`, ``` num_prefill = sum(x > 1 for x in num_scheduled_tokens_per_req) num_decoding = sum(x == 1 for x in num_scheduled_tokens_per_req) print(f"============ {num_prefill=}, {num_decoding=}") ``` I got ``` ============ num_prefill=1, num_decoding=0 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1 ============ num_prefill=0, num_decoding=1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: reasing the number of decoding in a batch until it hits the kv cache capacity limit. But when I added the print code at the end of `_prepare_inputs`, ``` num_prefill = sum(x > 1 for x in num_scheduled_tokens_per_req) nu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug][V1]: Many decoding batch with only 1 request at the beginning of benchmarking when request-rate is inf bug ### Your current environment ### 🐛 Describe the bug When `request-rate` is set to inf, we expect we are gr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: gradually increasing the number of decoding in a batch until it hits the kv cache capacity limit. But when I added the print code at the end of `_prepare_inputs`, ``` num_prefill = sum(x > 1 for x in num_scheduled_token...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m_decoding=9 ``` ### How to reproduce ``` VLLM_USE_V1=1 vllm serve meta-llama/Llama-3.1-8B-Instruct --disable-log-requests --gpu-memory-utilization 0.98 --max-num-batched-tokens 2048 --max-num-seqs 128 --max-model-len 2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
