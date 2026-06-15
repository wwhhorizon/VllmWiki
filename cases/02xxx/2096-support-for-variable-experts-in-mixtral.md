# vllm-project/vllm#2096: support for variable experts in Mixtral

| 字段 | 值 |
| --- | --- |
| Issue | [#2096](https://github.com/vllm-project/vllm/issues/2096) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> support for variable experts in Mixtral

### Issue 正文摘录

Some early benchmarks show up a 1 point drop in perplexity when using 3 experts instead of the default 2 in Mixtral. https://github.com/ggerganov/llama.cpp/pull/4406#issuecomment-1855151885 Please could we have support to specify the number of experts active?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pp/pull/4406#issuecomment-1855151885 Please could we have support to specify the number of experts active?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: perts instead of the default 2 in Mixtral. https://github.com/ggerganov/llama.cpp/pull/4406#issuecomment-1855151885 Please could we have support to specify the number of experts active?
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: support for variable experts in Mixtral Some early benchmarks show up a 1 point drop in perplexity when using 3 experts instead of the default 2 in Mixtral. https://github.com/ggerganov/llama.cpp/pull/4406#issuecomment-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: support for variable experts in Mixtral Some early benchmarks show up a 1 point drop in perplexity when using 3 experts instead of the default 2 in Mixtral. https://github.com/ggerganov/llama.cpp/pull/4406#issuecomment-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
