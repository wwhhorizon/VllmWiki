# vllm-project/vllm#38782: [vLLM IR] Op test & benchmark infra

| 字段 | 值 |
| --- | --- |
| Issue | [#38782](https://github.com/vllm-project/vllm/issues/38782) |
| 状态 | closed |
| 标签 | vllm-ir |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [vLLM IR] Op test & benchmark infra

### Issue 正文摘录

We should create infra & utilities to make it very easy to add tests & benchmarks for new ops. I think we should have tests for every op that test all supported providers and check their semantics match native and that native semantics are roughly as expected (e.g. `norm(2x) ~ norm(x)`). Also we should `opcheck` each provider to check args are not mutated and outputs do not alias inputs (except in the `maybe_inplace` case). Then we should also create utilities such that each provider can write their own tests comparing to native if they want, especially validating that `supports_args` works as intended. Not sure how to reduce duplication here yet. For benchmarks, we should have a single driver file, and each op should register a `get_inputs(case: BenchmarkCase) -> list[torch.Tensor]` function (`BenchmarkCase(num_tokens: int, hidden_size: int)`). And then we should have a fixed set of benchmark cases corresponding to `hidden_size`s from common models. This should be enough to start, and then later ops can extend `BenchmarkCase` to add more parameters (e.g. `group_size` for group quant).

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [vLLM IR] Op test & benchmark infra vllm-ir We should create infra & utilities to make it very easy to add tests & benchmarks for new ops. I think we should have tests for every op that test all supported providers and...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: provider can write their own tests comparing to native if they want, especially validating that `supports_args` works as intended. Not sure how to reduce duplication here yet. For benchmarks, we should have a single dri...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: tend `BenchmarkCase` to add more parameters (e.g. `group_size` for group quant).
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: fixed set of benchmark cases corresponding to `hidden_size`s from common models. This should be enough to start, and then later ops can extend `BenchmarkCase` to add more parameters (e.g. `group_size` for group quant).

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
