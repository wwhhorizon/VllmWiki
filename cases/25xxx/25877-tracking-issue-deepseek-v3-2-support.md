# vllm-project/vllm#25877: Tracking Issue: DeepSeek V3.2 support

| 字段 | 值 |
| --- | --- |
| Issue | [#25877](https://github.com/vllm-project/vllm/issues/25877) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tracking Issue: DeepSeek V3.2 support

### Issue 正文摘录

The main PR https://github.com/vllm-project/vllm/pull/25896 has been merged, and the nightly wheel can be used. Following the recipes, you should be able to run it. Recipe: https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2-Exp.html .

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: github.com/vllm-project/vllm/pull/25896 has been merged, and the nightly wheel can be used. Following the recipes, you should be able to run it. Recipe: https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Tracking Issue: DeepSeek V3.2 support feature request;stale The main PR https://github.com/vllm-project/vllm/pull/25896 has been merged, and the nightly wheel can be used. Following the recipes, you should be able to ru...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ld be able to run it. Recipe: https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2-Exp.html .

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
