# vllm-project/vllm#5586: [Feature]: Decouple the benchmark script from the components of vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#5586](https://github.com/vllm-project/vllm/issues/5586) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Decouple the benchmark script from the components of vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, [the benchmark script](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_serving.py) of vLLM supports multiple backends, and the overall functionality is also relatively rich. And it relies on `backend_request_func` and `get_tokenizer`. The `backend_request_func` is independent and is a separate file but if we want to use `get_tokenizer`, we need to clone the repository or install Python package. https://github.com/vllm-project/vllm/blob/845a3f26f9706acafe8fa45ae452846d8cc3b97f/benchmarks/benchmark_serving.py#L37-L42 https://github.com/vllm-project/vllm/blob/845a3f26f9706acafe8fa45ae452846d8cc3b97f/vllm/transformers_utils/tokenizer.py#L57 When we typically use the vLLM script to benchmark other backends, we do not want to rely on vLLM components. We don't want to clone the repository or install a Python package. May I submit a PR to extract the function `get_tokenizer` into `backend_request_func`? Do you think this is okay or do you have any other suggestions? Thanks. @ywang96 @simon-mo ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: llm/blob/main/benchmarks/benchmark_serving.py) of vLLM supports multiple backends, and the overall functionality is also relatively rich. And it relies on `backend_request_func` and `get_tokenizer`. The `backend_request...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ut if we want to use `get_tokenizer`, we need to clone the repository or install Python package. https://github.com/vllm-project/vllm/blob/845a3f26f9706acafe8fa45ae452846d8cc3b97f/benchmarks/benchmark_serving.py#L37-L42...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ture]: Decouple the benchmark script from the components of vLLM feature request ### 🚀 The feature, motivation and pitch Currently, [the benchmark script](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: Decouple the benchmark script from the components of vLLM feature request ### 🚀 The feature, motivation and pitch Currently, [the benchmark script](https://github.com/vllm-project/vllm/blob/main/benchmarks/be...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
