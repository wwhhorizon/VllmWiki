# vllm-project/vllm#13883: [Bug]: Incorrect first_token_time and first_scheduled_time metrics results

| 字段 | 值 |
| --- | --- |
| Issue | [#13883](https://github.com/vllm-project/vllm/issues/13883) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect first_token_time and first_scheduled_time metrics results

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am profiling TTFT on long context (32K, 128K) and detecting wrong concept of TTFT reporting for first_scheduled_time and first_token_time metrics. Could you please help to get correct metric's values? - model: llama3.1-8B - GPU type: A100 80GBs, TP=1 - dataset: sonnet dynamic dataset - context: 32K+ Issue description: Incorrect metrics calculation occurs because of: "prompt N" first_token_time is reported after "prompt N+1" first_scheduled_time. "prompt N" first_token_time should be reported at the end of "prompt N" execution, not during execution of "prompt N+1". 32K analysis. In current benchmark issue occurs after first prompt for every 8 prompts because of batch_size(max-num-seqs)=8 As list of first_token_time contains incorrect values, reported TTFT is ~10% higher than real TTFT. ``` maybe_set_first_scheduled_time 1740408012.291758 maybe_set_first_token_time 1740408015.5311732 maybe_set_first_scheduled_time 1740408031.1913495 maybe_set_first_scheduled_time 1740408034.012218 maybe_set_first_token_time 1740408034.506182 maybe_set_first_scheduled_time 1740408037.75051 maybe_set_first_token_time 1740408037.9672878 maybe_set_fi...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: e help to get correct metric's values? - model: llama3.1-8B - GPU type: A100 80GBs, TP=1 - dataset: sonnet dynamic dataset - context: 32K+ Issue description: Incorrect metrics calculation occurs because of: "prompt N" f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Incorrect first_token_time and first_scheduled_time metrics results bug;stale ### Your current environment ### 🐛 Describe the bug I am profiling TTFT on long context (32K, 128K) and detecting wrong concept of TTFT repor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ruct/ --tensor-parallel-size 1 --max-num-seqs 8 --disable-log-requests --dtype bfloat16 --gpu-memory-util 0.9 --disable-log-stats --max-model-len 33792&` benchmark: `python3 benchmark_serving.py --model /llama3.1/Meta-L...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: bug;stale ### Your current environment ### 🐛 Describe the bug I am profiling TTFT on long context (32K, 128K) and detecting wrong concept of TTFT reporting for first_scheduled_time and first_token_time metrics. Could yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
