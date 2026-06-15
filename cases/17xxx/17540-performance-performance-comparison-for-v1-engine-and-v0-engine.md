# vllm-project/vllm#17540: [Performance]:  Performance comparison for v1 engine and v0 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#17540](https://github.com/vllm-project/vllm/issues/17540) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]:  Performance comparison for v1 engine and v0 engine

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Hi, I did a benchmark to compare the performance of v1 engine and v0 engine, using `benchmark_serving.py `on SharGPT and an internal dataset. The results for llama3-3-70b-instruct are shown as follows. ShareGPT: Our internal dataset: The average length prompts in our internal dataset is around 9k tokens. It seems that the performance of the v1 engine is much worse, and it seems that TTFT is much larger for long prompts under a high QPS v1 engine. For setup details: I used 4 H100s and kserve for both deployments. I used vLLM-0.8.4, using quantization `fp8-dynamic`. The launch params for v0 engine: ``` '--gpu-memory-utilization=0.90' '--tensor-parallel-size=4' '--enable-chunked-prefill' '--max-num-batched-tokens=8192' --enable-auto-tool-choice --tool-call-parser=llama3_json ``` The launch params for v1 engine: ``` '--gpu-memory-utilization=0.90' '--tensor-parallel-size=4' --enable-auto-tool-choice --tool-call-parser=llama3_json ``` The only difference is that for v1 engine, it does not need `enable-chunked-prefill` and max-num-batched-tokens is already 8192. Let me know whether it’s a fair compari...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression Hi, I did a benchmark to compare the performance of v1 engine and v0 engine, using `benchmark_serving.py `on SharGPT and an internal data...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: I used 4 H100s and kserve for both deployments. I used vLLM-0.8.4, using quantization `fp8-dynamic`. The launch params for v0 engine: ``` '--gpu-memory-utilization=0.90' '--tensor-parallel-size=4' '--enable-chunked-pref...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: long prompts under a high QPS v1 engine. For setup details: I used 4 H100s and kserve for both deployments. I used vLLM-0.8.4, using quantization `fp8-dynamic`. The launch params for v0 engine: ``` '--gpu-memory-utiliza...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rmance]: Performance comparison for v1 engine and v0 engine performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Hi, I did a benchmark to compare the performance of v1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: chmark_serving.py `on SharGPT and an internal dataset. The results for llama3-3-70b-instruct are shown as follows. ShareGPT: Our internal dataset: The average length prompts in our internal dataset is around 9k tokens....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
