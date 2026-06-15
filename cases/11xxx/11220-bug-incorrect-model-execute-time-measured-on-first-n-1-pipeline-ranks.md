# vllm-project/vllm#11220: [Bug]: Incorrect `model_execute_time` measured on first N-1 pipeline ranks

| 字段 | 值 |
| --- | --- |
| Issue | [#11220](https://github.com/vllm-project/vllm/issues/11220) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect `model_execute_time` measured on first N-1 pipeline ranks

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Summary `vllm serve --collect-detailed-traces worker --pp ` currently reports the incorrect `model_execute_time` production metric (which feeds into the Prometheus dashboard). The issue arises because the worker latency is summed across PP ranks 0 to N-1, but the latency measured for ranks 0 to N-2 is inaccurate due to the absence of `torch.cuda.synchronize()` before measurement. Note that PP rank N-1’s measurement appears correct. This is because its underlying `ModelRunner` computes the logits, which results in a CUDA synchronization. ### Steps to reproduce 1. Add logging in `worker_base.py` to print the `model_execute_time` in each PP rank (see this commit https://github.com/JonnyKong/vllm/commit/121f0349ad0869b776212fa5a8357e2415293b8d). 2. Then run any benchmark script, e.g.: ```bash $ vllm serve meta-llama/Llama-3.1-8B-Instruct -tp 1 -pp 4 --collect-detailed-traces worker 2>&1 | grep "PP rank:" $ python benchmark_serving.py --model meta-llama/Llama-3.1-8B-Instruct --dataset-name sharegpt --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json ``` 3. We can observe that ranks 0 to N-2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: y measured for ranks 0 to N-2 is inaccurate due to the absence of `torch.cuda.synchronize()` before measurement. Note that PP rank N-1’s measurement appears correct. This is because its underlying `ModelRunner` computes...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: eds into the Prometheus dashboard). The issue arises because the worker latency is summed across PP ranks 0 to N-1, but the latency measured for ranks 0 to N-2 is inaccurate due to the absence of `torch.cuda.synchronize...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: putes the logits, which results in a CUDA synchronization. ### Steps to reproduce 1. Add logging in `worker_base.py` to print the `model_execute_time` in each PP rank (see this commit https://github.com/JonnyKong/vllm/c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Incorrect `model_execute_time` measured on first N-1 pipeline ranks bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Summary `vllm serve --collect-detailed-tra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
