# vllm-project/vllm#15253: [Performance]: V0 and V1 give the same throughput number

| 字段 | 值 |
| --- | --- |
| Issue | [#15253](https://github.com/vllm-project/vllm/issues/15253) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: V0 and V1 give the same throughput number

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I constructed an experiment to assess the impact of preemption on inference throughput in V0 and V1. In this experiment, I intentionally designed the workload to exceed GPU memory capacity by setting the number of prompts to 100 and the output length to 4096. This scenario is intended to induce memory overflow and trigger preemption. I executed the benchmark_throughput.py script on a single GPU node with both V0 and V1, but the resulting throughput numbers were surprisingly similar. ```bash MODEL_NAME="NousResearch/Hermes-3-Llama-3.1-8B" NUM_PROMPTS=100 DATASET_NAME="sonnet" DATASET_PATH="benchmarks/sonnet.txt" numactl --cpunodebind=1 --membind=1 python3 benchmarks/benchmark_throughput.py \ --model "${MODEL_NAME}" \ --dataset-name "${DATASET_NAME}" \ --dataset-path "${DATASET_PATH}" \ --output-len 4096 \ --num-prompts "${NUM_PROMPTS}" \ --gpu_memory_utilization 0.8 \ ``` V0 results are: ``` Throughput: 0.16 requests/s, 735.49 total tokens/s, 654.65 output tokens/s ``` V1 results are: ``` Throughput: 0.16 requests/s, 726.89 total tokens/s, 647.00 o...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: periment, I intentionally designed the workload to exceed GPU memory capacity by setting the number of prompts to 100 and the output length to 4096. This scenario is intended to induce memory overflow and trigger preemp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: put numbers were surprisingly similar. ```bash MODEL_NAME="NousResearch/Hermes-3-Llama-3.1-8B" NUM_PROMPTS=100 DATASET_NAME="sonnet" DATASET_PATH="benchmarks/sonnet.txt" numactl --cpunodebind=1 --membind=1 python3 bench...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: he resulting throughput numbers were surprisingly similar. ```bash MODEL_NAME="NousResearch/Hermes-3-Llama-3.1-8B" NUM_PROMPTS=100 DATASET_NAME="sonnet" DATASET_PATH="benchmarks/sonnet.txt" numactl --cpunodebind=1 --mem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: V0 and V1 give the same throughput number performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I constr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: V0 and V1 give the same throughput number performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I constr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
