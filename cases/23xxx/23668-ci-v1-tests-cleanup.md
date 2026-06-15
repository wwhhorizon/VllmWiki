# vllm-project/vllm#23668: [CI]: V1 Tests cleanup

| 字段 | 值 |
| --- | --- |
| Issue | [#23668](https://github.com/vllm-project/vllm/issues/23668) |
| 状态 | closed |
| 标签 | ci/build;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: V1 Tests cleanup

### Issue 正文摘录

- Split into categories with some kind of grouping (~3 groups) - Where model used is arbitrary, replace with https://huggingface.co/hmellor/tiny-random-LlamaForCausalLM (see https://github.com/vllm-project/vllm/issues/23456) - Review Server Fixtures + widen scope as much as possible (to package level if we can) (see https://github.com/vllm-project/vllm/issues/23590) - Maximize the sharing - Do this piecemeal. So identify the top test groups and start there

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e - Split into categories with some kind of grouping (~3 groups) - Where model used is arbitrary, replace with https://huggingface.co/hmellor/tiny-random-LlamaForCausalLM (see https://github.com/vllm-project/vllm/issues...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: V1 Tests cleanup ci/build;stale - Split into categories with some kind of grouping (~3 groups) - Where model used is arbitrary, replace with https://huggingface.co/hmellor/tiny-random-LlamaForCausalLM (see https:/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI]: V1 Tests cleanup ci/build;stale - Split into categories with some kind of grouping (~3 groups) - Where model used is arbitrary, replace with https://huggingface.co/hmellor/tiny-random-LlamaForCausalLM (see https:/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: V1 Tests cleanup ci/build;stale - Split into categories with some kind of grouping (~3 groups) - Where model used is arbitrary, replace with https://huggingface.co/hmellor/tiny-random-LlamaForCausalLM (see https:/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
