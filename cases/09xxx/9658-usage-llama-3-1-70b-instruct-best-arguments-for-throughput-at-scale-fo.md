# vllm-project/vllm#9658: [Usage]: Llama-3.1-70B-Instruct best arguments for throughput at scale for multiple users

| 字段 | 值 |
| --- | --- |
| Issue | [#9658](https://github.com/vllm-project/vllm/issues/9658) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Llama-3.1-70B-Instruct best arguments for throughput at scale for multiple users

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a Llama-3.1-70B-Instruct in kuberenetes and I am finding it a little difficult to understand the best possible parameters to get the best throughput. This model will be hit by multiple users concurrently sending lots of large and small requests. The aim is to maximise throughput for all users as best as possible. If anyone could give advice on my current arguments as well as offer suggestions for improvement that would be great, thanks! **Hardware available:** 8 A100 80gb GPUs 128 CPUs **Vllm Version: 0.63** **Current arguments:** currently running 2 replica pods with 4 GPU and 64 CPU each with the following args ``` - "--model= " - "--served-model-name=llama-31-70b-instruct" - "--tensor-parallel-size=4" - "--port=5000" - "--distributed-executor-backend=ray" - "--max-logprobs=1" - "--tokenizer-pool-size=128" - "--tokenizer-pool-type=ray" - "--enable-prefix-caching" - "--dtype=float16" - "--max-num-seqs=512" - "--max-model-len=32768" - "--disable-logprobs-during-spec-decoding" - "--disable-log-requests" - "--multi-step-stream-outputs=False" -...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: Llama-3.1-70B-Instruct best arguments for throughput at scale for multiple users usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: del will be hit by multiple users concurrently sending lots of large and small requests. The aim is to maximise throughput for all users as best as possible. If anyone could give advice on my current arguments as well a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Instruct best arguments for throughput at scale for multiple users usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Llama-3.1-70B-Instruct best arguments for throughput at scale for multiple users usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: Llama-3.1-70B-Instruct best arguments for throughput at scale for multiple users usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
