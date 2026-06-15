# vllm-project/vllm#31064: [RFC]: Optional Hidden States Transfer in `KVConnectorBase_V1` to Eliminate Decoder Prefix-Prefill in P/D Disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#31064](https://github.com/vllm-project/vllm/issues/31064) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Optional Hidden States Transfer in `KVConnectorBase_V1` to Eliminate Decoder Prefix-Prefill in P/D Disaggregation

### Issue 正文摘录

### Motivation. vLLM supports **Prefill/Decode (P/D) disaggregation**, where prefill and decode are executed in separate vLLM instances and communicate via connector abstractions such as `KVConnectorBase_V1`. A key motivation of this design is to prevent prefill work from interrupting decode execution and to improve tail inter-token latency (ITL) under high concurrency. In the current vLLM v1 design, P/D disaggregation typically transfers **KV cache only** from the prefill worker to the decode worker. As a result, the decode worker must still recompute the **last-token hidden states** in order to sample the first output token. This recomputation is implemented by scheduling a **decoder-side prefix prefill**, leveraging existing prefix caching infrastructure. While functionally correct, this design introduces performance issues in certain deployment configurations. ### Deployment context This RFC is motivated by deploying **DeepSeek-R1 (MLA attention)** on Intel accelerators (Gaudi and Intel XPU) with the following configuration: - **Prefill**: Tensor Parallel (TP) - **Decode**: Data Parallel (DP) - **Connector**: NIXL connector with GDR enabled ### Observed issues Take the followi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: correct, this design introduces performance issues in certain deployment configurations. ### Deployment context This RFC is motivated by deploying **DeepSeek-R1 (MLA attention)** on Intel accelerators (Gaudi and Intel X...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: C]: Optional Hidden States Transfer in `KVConnectorBase_V1` to Eliminate Decoder Prefix-Prefill in P/D Disaggregation RFC ### Motivation. vLLM supports **Prefill/Decode (P/D) disaggregation**, where prefill and decode a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: work from interrupting decode execution and to improve tail inter-token latency (ITL) under high concurrency. In the current vLLM v1 design, P/D disaggregation typically transfers **KV cache only** from the prefill work...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: sponding to the *last prefill token* for each token ready for decoding - Dtype: model activation dtype (e.g., bf16 / fp16), consistent with the input to `lm_head` > `num_tokens` is used instead of `batch_size` to reflec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Sampled token IDs are broadcast to other DP ranks using existing mechanisms. - The scheduler proceeds with normal decode steps. No changes are required to async scheduling semantics. ### Configuration and compatibility...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
