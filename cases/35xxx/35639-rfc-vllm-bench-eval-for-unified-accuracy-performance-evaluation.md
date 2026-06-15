# vllm-project/vllm#35639: [RFC]: `vllm bench eval` for Unified Accuracy + Performance Evaluation

| 字段 | 值 |
| --- | --- |
| Issue | [#35639](https://github.com/vllm-project/vllm/issues/35639) |
| 状态 | open |
| 标签 | rocm;RFC |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: `vllm bench eval` for Unified Accuracy + Performance Evaluation

### Issue 正文摘录

### Motivation. ## Summary Add `vllm bench eval`, a new `vllm bench` subcommand that runs an [lm_eval](https://github.com/EleutherAI/lm-evaluation-harness) accuracy evaluation and a Prometheus `/metrics` performance collection pass **in the same server session**, producing a single JSONL record per run that contains accuracy results, latency/throughput metrics, and structured environment info (`vllm collect-env`). ## Motivation We already run lm_eval suites in CI and on hardware validation rigs. Those runs spin up a `vllm serve` process, send thousands of requests through it, then tear it down, consuming significant GPU-hours. Today we get accuracy numbers from those runs but **nothing about inference performance**: no TTFT, no TPOT, no throughput, no cache utilisation. As a result: - **Performance regressions go undetected** until a user reports slowdowns after a release. - **Hardware-specific pathologies** (e.g. a ROCm kernel regression on MI300X, a NCCL change on a 8-GPU node) are invisible in CI accuracy dashboards. - **Accuracy and performance are tracked in separate systems** with no shared provenance it's impossible to correlate "this commit improved accuracy by 0.3 points...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: [RFC]: `vllm bench eval` for Unified Accuracy + Performance Evaluation rocm;RFC ### Motivation. ## Summary Add `vllm bench eval`, a new `vllm bench` subcommand that runs an [lm_eval](https://github.com/EleutherAI/lm-eva...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [RFC]: `vllm bench eval` for Unified Accuracy + Performance Evaluation rocm;RFC ### Motivation. ## Summary Add `vllm bench eval`, a new `vllm bench` subcommand that runs an [lm_eval](https://github.com/EleutherAI/lm-eva...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: etrics` performance collection pass **in the same server session**, producing a single JSONL record per run that contains accuracy results, latency/throughput metrics, and structured environment info (`vllm collect-env`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g for. ### Proposed Change. ### High-level flow ``` vllm bench eval --model --tasks [--tp N] [--output results.jsonl] 1. collect-env (before GPU is loaded, ~2s) 2. vllm serve (managed subprocess) 3. /metrics polling (ba...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ation rigs. Those runs spin up a `vllm serve` process, send thousands of requests through it, then tear it down, consuming significant GPU-hours. Today we get accuracy numbers from those runs but **nothing about inferen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
