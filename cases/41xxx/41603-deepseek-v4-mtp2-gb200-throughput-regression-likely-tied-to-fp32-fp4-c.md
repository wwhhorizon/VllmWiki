# vllm-project/vllm#41603: DeepSeek-V4 MTP2 GB200 throughput regression likely tied to FP32->FP4 cvt path (#41015)

| 字段 | 值 |
| --- | --- |
| Issue | [#41603](https://github.com/vllm-project/vllm/issues/41603) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> DeepSeek-V4 MTP2 GB200 throughput regression likely tied to FP32->FP4 cvt path (#41015)

### Issue 正文摘录

### Summary I'm seeing a large DeepSeek-V4-Pro MTP2 throughput regression on GB200 between a pre-merge PR container and newer vLLM images. A one-off test that reverts the FP32->FP4 cvt path from #41015 on top of the nightly recovers most of the lost throughput, so #41015 looks like the current lead suspect for this workload. ### Config - Model: `deepseek-ai/DeepSeek-V4-Pro` - Backend: Dynamo + vLLM, disaggregated serving - Hardware: GB200, 24 GPUs total - Layout: 2P/1D high-throughput MegaMOE - Prefill: TP8 / EP8 / `dp_attention=true` / 2 workers = 16 GPUs - Decode: TP8 / EP8 / `dp_attention=true` / 1 worker = 8 GPUs - Workload: ISL 8192 / OSL 1024, concurrency 1024, 10,240 completed requests - Features: MTP2 speculative decoding, FP4 indexer cache - Same srt-slurm recipe/knobs for the main comparison; only the container or patch changed. Metrics below use InferenceX conventions: - `total tok/s/GPU = (input tokens + output tokens) / benchmark duration / 24 GPUs` - `tok/s/user = 1000 / median TPOT_ms` - `AL (derived) = 1 + accepted_tokens / (drafted_token_positions / 2)` for MTP2. The vLLM log field is named `Drafted`; in these runs it appears to count drafted token positions, so I...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: rdware: GB200, 24 GPUs total - Layout: 2P/1D high-throughput MegaMOE - Prefill: TP8 / EP8 / `dp_attention=true` / 2 workers = 16 GPUs - Decode: TP8 / EP8 / `dp_attention=true` / 1 worker = 8 GPUs - Workload: ISL 8192 /...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: DeepSeek-V4 MTP2 GB200 throughput regression likely tied to FP32->FP4 cvt path (#41015) ### Summary I'm seeing a large DeepSeek-V4-Pro MTP2 throughput regression on GB200 between a pre-merge PR container and newer vLLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: eatures: MTP2 speculative decoding, FP4 indexer cache - Same srt-slurm recipe/knobs for the main comparison; only the container or patch changed. Metrics below use InferenceX conventions: - `total tok/s/GPU = (input tok...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t, so #41015 looks like the current lead suspect for this workload. ### Config - Model: `deepseek-ai/DeepSeek-V4-Pro` - Backend: Dynamo + vLLM, disaggregated serving - Hardware: GB200, 24 GPUs total - Layout: 2P/1D high...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: for this workload. ### Config - Model: `deepseek-ai/DeepSeek-V4-Pro` - Backend: Dynamo + vLLM, disaggregated serving - Hardware: GB200, 24 GPUs total - Layout: 2P/1D high-throughput MegaMOE - Prefill: TP8 / EP8 / `dp_at...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
