# vllm-project/vllm#39428: [torch.compile] E2E correctness testing for fusions

| 字段 | 值 |
| --- | --- |
| Issue | [#39428](https://github.com/vllm-project/vllm/issues/39428) |
| 状态 | open |
| 标签 | help wanted;torch.compile |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [torch.compile] E2E correctness testing for fusions

### Issue 正文摘录

E2E tests for fusions (`tests/compile/fusions_e2e`) have done a great job preventing fusion regressions where model/forward code changes break a custom torch.compile fusion pass. However, we currently have no way of testing correctness for these fusion configurations. It would be good to investigate an approach where we only run a few layers of a model and compare the outputs. This would be helpful for correctness testing in general, and we could compare the outputs to both a baseline vLLM configuration and the huggingface baseline. This would likely require some work to fix weight loading for models like DeepSeek when `--hf-overrides.num_hidden_layers` is overriden.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: /fusions_e2e`) have done a great job preventing fusion regressions where model/forward code changes break a custom torch.compile fusion pass. However, we currently have no way of testing correctness for these fusion con...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [torch.compile] E2E correctness testing for fusions help wanted;torch.compile E2E tests for fusions (`tests/compile/fusions_e2e`) have done a great job preventing fusion regressions where model/forward code changes brea...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [torch.compile] E2E correctness testing for fusions help wanted;torch.compile E2E tests for fusions (`tests/compile/fusions_e2e`) have done a great job preventing fusion regressions where model/forward code changes brea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
