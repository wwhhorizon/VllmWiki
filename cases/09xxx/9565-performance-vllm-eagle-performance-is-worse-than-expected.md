# vllm-project/vllm#9565: [Performance]: vllm Eagle performance is worse than expected

| 字段 | 值 |
| --- | --- |
| Issue | [#9565](https://github.com/vllm-project/vllm/issues/9565) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: vllm Eagle performance is worse than expected

### Issue 正文摘录

### Proposal to improve performance The spec dec performance of Eagleis worse than expected as shown below: Model: [meta-llama/Meta-Llama-3.1-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) Draft model:[ yuhuili/EAGLE-LLaMA3-Instruct-70B](https://huggingface.co/yuhuili/EAGLE-LLaMA3-Instruct-70B) Hardware: 4xH100 Target model TP=4 Dataset: [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered) vllm version: v0.6.1.post2 Even at low QPS, the performance is far from 2x speedup reported in the original eagle paper (light blue line is the original, the solid lines are with SD). We need to understand the performance gap here. Possible reasons include but not limited to 1. Miss tree verification kernel: For each position, we are choosing token from the top1 candidate instead of topk candidates. The reason is that we have not integrated tree verification kernel. 2. System overhead: unnecessary GPU/CPU communication somewhere. 3. We are testing on ShareGPT dataset while the heads are not finetuned on the same dataset. Profiling is required to understand the issue. Open this issue to track the progress. ### Report of performance regress...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: The spec dec performance of Eagleis worse than expected as shown below: Model: [meta-llama/Meta-Llama-3.1-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) Draft model:[ yuhuili/EAGLE-LLaMA3-Instru...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: System overhead: unnecessary GPU/CPU communication somewhere. 3. We are testing on ShareGPT dataset while the heads are not finetuned on the same dataset. Profiling is required to understand the issue. Open this issue t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: B](https://huggingface.co/yuhuili/EAGLE-LLaMA3-Instruct-70B) Hardware: 4xH100 Target model TP=4 Dataset: [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered) vllm version: v0.6.1.post2 E...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: vllm Eagle performance is worse than expected performance;stale ### Proposal to improve performance The spec dec performance of Eagleis worse than expected as shown below: Model: [meta-llama/Meta-Llama-3....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered) vllm version: v0.6.1.post2 Even at low QPS, the performance is far from 2x speedup reported in the original eagle paper (light blue line is the origina...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
