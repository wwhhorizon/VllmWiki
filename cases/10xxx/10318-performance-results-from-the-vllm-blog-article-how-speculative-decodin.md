# vllm-project/vllm#10318: [Performance]: Results from the vLLM Blog article "How Speculative Decoding Boosts vLLM Performance by up to 2.8x" are unreproducible

| 字段 | 值 |
| --- | --- |
| Issue | [#10318](https://github.com/vllm-project/vllm/issues/10318) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;triton |
| 症状 | slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Results from the vLLM Blog article "How Speculative Decoding Boosts vLLM Performance by up to 2.8x" are unreproducible

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression We attempted to reproduce the results from the [vLLM Blog article _"How Speculative Decoding Boosts vLLM Performance by up to 2.8x"_](https://blog.vllm.ai/2024/10/17/spec-decode.html). However, we were unable to achieve the performance levels reported in the article. The experimental setup we used is detailed below: > vLLM version: 0.6.3 > Device: 4 x H100 PCIe > Target Model: meta-llama/Meta-Llama-3-70B-Instruct with TP=4 > Draft Model: turboderp/Qwama-0.5B-Instruct with TP=1 > Dataset: anon8231489123/ShareGPT_Vicuna_unfiltered > QPS: 1 > Num Speculative Tokens: 4 Since the article did not specify the maximum batch size, we experimented with various batch sizes to align with the conditions implied in the blog. The results are summarized in the table below: NUM_REQUESTS | BATCH_SIZE | latency | output_token_throughput | total_token_throughput | sequence_throughput | p99_ttft_ms | mean_tpot_ms | mean_e2e_ms -- | -- | -- | -- | -- | -- | -- | -- | -- 32 | 1 | 379.36 | 16.39 | 42.82 | 0.08 | 342058.66 | 59.24 | 192514.28 32 | 1 | 269.17 | 23.1 | 60.35 | 0.12 | 231910.81 | 48.47 | 132276.49 128 | 4...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Speculative Decoding Boosts vLLM Performance by up to 2.8x" are unreproducible performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression We attempted to reproduce the resul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Performance]: Results from the vLLM Blog article "How Speculative Decoding Boosts vLLM Performance by up to 2.8x" are unreproducible performance;stale ### Proposal to improve performance _No response_ ### Report of per...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: roposal to improve performance _No response_ ### Report of performance regression We attempted to reproduce the results from the [vLLM Blog article _"How Speculative Decoding Boosts vLLM Performance by up to 2.8x"_](htt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: detailed below: > vLLM version: 0.6.3 > Device: 4 x H100 PCIe > Target Model: meta-llama/Meta-Llama-3-70B-Instruct with TP=4 > Draft Model: turboderp/Qwama-0.5B-Instruct with TP=1 > Dataset: anon8231489123/ShareGPT_Vicu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: al setup we used is detailed below: > vLLM version: 0.6.3 > Device: 4 x H100 PCIe > Target Model: meta-llama/Meta-Llama-3-70B-Instruct with TP=4 > Draft Model: turboderp/Qwama-0.5B-Instruct with TP=1 > Dataset: anon8231...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
