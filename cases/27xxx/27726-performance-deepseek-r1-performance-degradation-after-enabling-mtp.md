# vllm-project/vllm#27726: [Performance]: DeepSeek-R1 performance degradation after enabling MTP

| 字段 | 值 |
| --- | --- |
| Issue | [#27726](https://github.com/vllm-project/vllm/issues/27726) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: DeepSeek-R1 performance degradation after enabling MTP

### Issue 正文摘录

### Proposal to improve performance **NVIDIA H20** **Test results** MTP1 ==========================MTP================================== **MTP** export VLLM_USE_DEEP_GEMM=0 vllm serve /workspace/models1/DeepSeek-R1 -tp 8 --cuda-graph-sizes=32 --no-enable-prefix-caching --max-model-len 5120 --max-num-batched-tokens 2048 --speculative-config '{"num_speculative_tokens": 1,"method": "deepseek_mtp"}' -O.cudagraph_mode=PIECEWISE vllm bench serve --model /workspace/models1/DeepSeek-R1 --label bs8 --save-result --dataset-name random --num-prompts 32 --max-concurrency 32 --random-input-len 2048 --random-output-len 1024 --ignore-eos ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: VLLM_USE_DEEP_GEMM=0 vllm serve /workspace/models1/DeepSeek-R1 -tp 8 --cuda-graph-sizes=32 --no-enable-prefix-caching --max-model-len 5120 --max-num-batched-tokens 2048 --speculative-config '{"num_speculative_tokens": 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ============== **MTP** export VLLM_USE_DEEP_GEMM=0 vllm serve /workspace/models1/DeepSeek-R1 -tp 8 --cuda-graph-sizes=32 --no-enable-prefix-caching --max-model-len 5120 --max-num-batched-tokens 2048 --speculative-config...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nce]: DeepSeek-R1 performance degradation after enabling MTP performance;stale ### Proposal to improve performance **NVIDIA H20** **Test results** MTP1 ==========================MTP================================== **M...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rformance;stale ### Proposal to improve performance **NVIDIA H20** **Test results** MTP1 ==========================MTP================================== **MTP** export VLLM_USE_DEEP_GEMM=0 vllm serve /workspace/models1/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ormance distributed_parallel;model_support;speculative_decoding cuda env_dependency Proposal to improve performance

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
