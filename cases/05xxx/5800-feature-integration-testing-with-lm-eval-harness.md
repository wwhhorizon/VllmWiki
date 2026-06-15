# vllm-project/vllm#5800: [Feature]: Integration Testing with lm-eval-harness

| 字段 | 值 |
| --- | --- |
| Issue | [#5800](https://github.com/vllm-project/vllm/issues/5800) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integration Testing with lm-eval-harness

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As vLLM added more capable nodes for CI, I think it's a good time to start adding model quality test for both non-quantized and quantized model to ensure the kernel and scheduler changes do not degrade the model accuracy performance. This also ensure vLLM doesn't break lm-eval-harness's integration. I would like to ask for suggestions for concrete benchmarks to be added. For example, MMLU for Llama3-8B with a score >= X. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Feature]: Integration Testing with lm-eval-harness feature request ### 🚀 The feature, motivation and pitch As vLLM added more capable nodes for CI, I think it's a good time to start adding model quality test for both n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: dded more capable nodes for CI, I think it's a good time to start adding model quality test for both non-quantized and quantized model to ensure the kernel and scheduler changes do not degrade the model accuracy perform...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Integration Testing with lm-eval-harness feature request ### 🚀 The feature, motivation and pitch As vLLM added more capable nodes for CI, I think it's a good time to start adding model quality test for both n...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: odel to ensure the kernel and scheduler changes do not degrade the model accuracy performance. This also ensure vLLM doesn't break lm-eval-harness's integration. I would like to ask for suggestions for concrete benchmar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: The feature, motivation and pitch As vLLM added more capable nodes for CI, I think it's a good time to start adding model quality test for both non-quantized and quantized model to ensure the kernel and scheduler change...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
