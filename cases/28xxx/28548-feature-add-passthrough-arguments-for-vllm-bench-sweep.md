# vllm-project/vllm#28548: [Feature]: Add passthrough arguments for vllm bench sweep

| 字段 | 值 |
| --- | --- |
| Issue | [#28548](https://github.com/vllm-project/vllm/issues/28548) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add passthrough arguments for vllm bench sweep

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm trying to re-create the InferenceMAX benchmark suite: https://inferencemax.semianalysis.com/ They practically use extracted vLLM bench code to test multiple frameworks (vLLM, sglang, trt-llm), and create pareto-front curves of e.g. throughput vs latency. I'm only interested in vLLM so I can just use vllm bench sweep directly, however I encounter one problem: I don't directly see an option for passthrough parameters (i.e. Parameters that are linked between the serve and bench serve commands) E.g.: `--max-num-seqs` and `--max-concurrency` are fundamentally the same variable (for me), but one lives in the serve parameter space and the other in the bench serve parameter space. Due to the cartesian product being taken between the two configs, I end up with a lot of runs that are nonsensical. The only option I have at the moment is do run an external loop over bench sweep and setting these variables to the same fixed value, and then merging the summary.json's myself at the end, which is not so nice. I'm not entirely sure how one could go about implementing such a feature, clearly the parameters should become parametric in some way; perhaps def...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: feature, motivation and pitch I'm trying to re-create the InferenceMAX benchmark suite: https://inferencemax.semianalysis.com/ They practically use extracted vLLM bench code to test multiple frameworks (vLLM, sglang, tr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ectly see an option for passthrough parameters (i.e. Parameters that are linked between the serve and bench serve commands) E.g.: `--max-num-seqs` and `--max-concurrency` are fundamentally the same variable (for me), bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: arameter space. Due to the cartesian product being taken between the two configs, I end up with a lot of runs that are nonsensical. The only option I have at the moment is do run an external loop over bench sweep and se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add passthrough arguments for vllm bench sweep feature request ### 🚀 The feature, motivation and pitch I'm trying to re-create the InferenceMAX benchmark suite: https://inferencemax.semianalysis.com/ They pra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
