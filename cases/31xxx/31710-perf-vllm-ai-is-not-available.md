# vllm-project/vllm#31710: perf.vllm.ai is not available

| 字段 | 值 |
| --- | --- |
| Issue | [#31710](https://github.com/vllm-project/vllm/issues/31710) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> perf.vllm.ai is not available

### Issue 正文摘录

> from my understanding , https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm should host the latest perf numbers. I also can't connect to http://perf.vllm.ai. _Originally posted by @louie-tsai in https://github.com/vllm-project/vllm/pull/22119#discussion_r2268189273_ The link is in bottom of front page https://vllm.ai/. https://github.com/intel-ai-tce/vllm/blob/more_cpu_models/.buildkite/nightly-benchmarks/README.md#introduction uses `See [vLLM performance dashboard](https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm) for the latest performance benchmark results`.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: om/vllm-project/vllm/pull/22119#discussion_r2268189273_ The link is in bottom of front page https://vllm.ai/. https://github.com/intel-ai-tce/vllm/blob/more_cpu_models/.buildkite/nightly-benchmarks/README.md#introductio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: is not available stale > from my understanding , https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm should host the latest perf numbers. I also can't connect to http://perf.vllm.ai. _Originally posted b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ge https://vllm.ai/. https://github.com/intel-ai-tce/vllm/blob/more_cpu_models/.buildkite/nightly-benchmarks/README.md#introduction uses `See [vLLM performance dashboard](https://hud.pytorch.org/benchmark/llms?repoName=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: perf.vllm.ai is not available stale > from my understanding , https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm should host the latest perf numbers. I also can't connect to http://perf.vllm.ai. _Origin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
