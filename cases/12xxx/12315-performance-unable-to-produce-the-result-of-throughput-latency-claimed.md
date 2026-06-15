# vllm-project/vllm#12315: [Performance]: Unable to produce the result of throughput & latency claimed on vLLM dashboard v0

| 字段 | 值 |
| --- | --- |
| Issue | [#12315](https://github.com/vllm-project/vllm/issues/12315) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Unable to produce the result of throughput & latency claimed on vLLM dashboard v0

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression We have used this command for producing the shared result of 5.13 req/s on 4 x A100 - tp 4 with llama 3.3 70b model: python3 benchmark_throughput.py --dataset ShareGPT_V3_unfiltered_cleaned_split.json --device cuda --output-json throughput_results_tp_4_a100.json --tensor-parallel-size 4 --model meta-llama/Llama-3.3-70B-Instruct --num-prompts 200 --seed 0 --num-scheduler-steps 10 --max-num-seqs 256 ### Misc discussion on performance vLLM version: 0.6.6 Device: 4 x A100 Target Model: meta-llama/Llama-3.3-70B-Instruct Dataset: anon8231489123/ShareGPT_Vicuna_unfiltered Our results on 4 x A100 with same config shared on vllm dashboard v0: - > Throughput: 3.28 requests/s, 1414.42 total tokens/s, 714.48 output tokens/s @ --num-scheduler-steps 1 - > Throughput: 3.47 requests/s, 1496.33 total tokens/s, 755.85 output tokens/s @ --num-scheduler-steps 10 - > Latency: 4.946 sec We are not able to produce the result of dashboard v0 for A100 while we can replicate or beat the result of same dashboard with H200 device. If we are missing any flag while running the command please let me know to optimise. Also is...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Performance]: Unable to produce the result of throughput & latency claimed on vLLM dashboard v0 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression We have used this...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: result of throughput & latency claimed on vLLM dashboard v0 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression We have used this command for producing the shared res...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ### Report of performance regression We have used this command for producing the shared result of 5.13 req/s on 4 x A100 - tp 4 with llama 3.3 70b model: python3 benchmark_throughput.py --dataset ShareGPT_V3_unfiltered_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e used this command for producing the shared result of 5.13 req/s on 4 x A100 - tp 4 with llama 3.3 70b model: python3 benchmark_throughput.py --dataset ShareGPT_V3_unfiltered_cleaned_split.json --device cuda --output-j...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nd for producing the shared result of 5.13 req/s on 4 x A100 - tp 4 with llama 3.3 70b model: python3 benchmark_throughput.py --dataset ShareGPT_V3_unfiltered_cleaned_split.json --device cuda --output-json throughput_re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
