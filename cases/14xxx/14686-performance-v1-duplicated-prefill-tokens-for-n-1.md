# vllm-project/vllm#14686: [Performance]: [V1] duplicated prefill tokens for n>1

| 字段 | 值 |
| --- | --- |
| Issue | [#14686](https://github.com/vllm-project/vllm/issues/14686) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: [V1] duplicated prefill tokens for n>1

### Issue 正文摘录

### Proposal to improve performance The following statement comes from https://github.com/vllm-project/vllm/pull/10980 > The vLLM v1 engine can exploit APC when a prompt repeats within a batch, even if that prompt was not seen in a previous batch. Therefore, no warmup request is required. Could you please show me the PR for this feature? I've tested on `v0.7.3` and it seems a warmup request is still required for n>1 cases. Here is a simple command to reproduce this problem. ```bash VLLM_USE_V1=1 python3 benchmarks/benchmark_latency.py --model meta-llama/Llama-3.1-8B -tp 1 --input-len 10 --n 2 --output-len 1 --batch-size 1 --trust-remote-code --num-iters 1 --num-iters-warmup 0 --load-format dummy ``` You can see `input_ids` set to `LlamaModel.forward` repeats twice, which leads to computation wastes on prefill tokens. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [d...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: est is required. Could you please show me the PR for this feature? I've tested on `v0.7.3` and it seems a warmup request is still required for n>1 cases. Here is a simple command to reproduce this problem. ```bash VLLM_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: problem. ```bash VLLM_USE_V1=1 python3 benchmarks/benchmark_latency.py --model meta-llama/Llama-3.1-8B -tp 1 --input-len 10 --n 2 --output-len 1 --batch-size 1 --trust-remote-code --num-iters 1 --num-iters-warmup 0 --lo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: [V1] duplicated prefill tokens for n>1 performance ### Proposal to improve performance The following statement comes from https://github.com/vllm-project/vllm/pull/10980 > The vLLM v1 engine can exploit A...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: up request is still required for n>1 cases. Here is a simple command to reproduce this problem. ```bash VLLM_USE_V1=1 python3 benchmarks/benchmark_latency.py --model meta-llama/Llama-3.1-8B -tp 1 --input-len 10 --n 2 --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
