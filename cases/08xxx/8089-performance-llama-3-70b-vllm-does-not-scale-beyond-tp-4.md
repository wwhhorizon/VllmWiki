# vllm-project/vllm#8089: [Performance]: Llama 3 70B; vLLM does not scale beyond TP=4

| 字段 | 值 |
| --- | --- |
| Issue | [#8089](https://github.com/vllm-project/vllm/issues/8089) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Llama 3 70B; vLLM does not scale beyond TP=4

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I have a single machine 8xH100 SXM system. I wanted to see how vLLM (0.5.5) compares to other engines with TP=8. The model I used for testing was fp8 llama 3 70b created using AutoFP8 repo. I tried several setups: 1. 1x TP=4 (useful baseline) 3. 2x TP=4, running vLLM with `--tensor-parallel-size=4` twice on the same 1 machine, load balanced with nginx 4. 1x TP=8, running vLLM with `--tensor-parallel-size=8` once on the same 1 machine One would expect **1x TP=8** to be able to handle the same QPS as **2x TP=4** with equal or better latency metrics. But that is not the case. The latency should be better, as there should be more opportunity for good scheduling and thus bigger batch sizes. In all cases I used these engine params: ``` --gpu-memory-utilization=0.95 --tensor-parallel-size=${ENGINE_TP:?} --disable-log-requests --enable-chunked-prefill --max-num-batched-tokens=8192 ``` For TP=8, I also tried different values of `--max-num-batched-tokens` and `--max-num-seqs`. Using 16K and 4K for `--max-num-batched-tokens` resulted in similarly poor performance. Using 512 lead to much lower throughput an...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: roposal to improve performance _No response_ ### Report of performance regression I have a single machine 8xH100 SXM system. I wanted to see how vLLM (0.5.5) compares to other engines with TP=8. The model I used for tes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: sponse_ ### Report of performance regression I have a single machine 8xH100 SXM system. I wanted to see how vLLM (0.5.5) compares to other engines with TP=8. The model I used for testing was fp8 llama 3 70b created usin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: Llama 3 70B; vLLM does not scale beyond TP=4 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I have a single machine 8xH100 SXM system. I wanted to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rget QPS ~6.6) -- does not reach the target QPS and has much worse latencies ``` Requests per second: 5.296937487309421 Average input tokens: 2594.345 Average output tokens: 66.69666666666667 Average time to first token...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Performance]: Llama 3 70B; vLLM does not scale beyond TP=4 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I have a single machine 8xH100 SXM system. I wanted to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
