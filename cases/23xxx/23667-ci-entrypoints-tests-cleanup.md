# vllm-project/vllm#23667: [CI]: Entrypoints tests cleanup

| 字段 | 值 |
| --- | --- |
| Issue | [#23667](https://github.com/vllm-project/vllm/issues/23667) |
| 状态 | closed |
| 标签 | ci/build;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Entrypoints tests cleanup

### Issue 正文摘录

- Identify places where LoRA is unnecessary + centralize all LoRA-related tests into a central file. - Replace all 7B parameter models with https://huggingface.co/hmellor/tiny-random-LlamaForCausalLM (see https://github.com/vllm-project/vllm/issues/23456) - Review Server Fixtures + move to package level if we can (see https://github.com/vllm-project/vllm/issues/23590) - Maximize the sharing - Do this piecemeal. So identify the top test groups and start there

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: all LoRA-related tests into a central file. - Replace all 7B parameter models with https://huggingface.co/hmellor/tiny-random-LlamaForCausalLM (see https://github.com/vllm-project/vllm/issues/23456) - Review Server Fixt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Entrypoints tests cleanup ci/build;stale - Identify places where LoRA is unnecessary + centralize all LoRA-related tests into a central file. - Replace all 7B parameter models with https://huggingface.co/hmellor/ti
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI]: Entrypoints tests cleanup ci/build;stale - Identify places where LoRA is unnecessary + centralize all LoRA-related tests into a central file. - Replace all 7B parameter models with https://huggingface.co/hmellor/t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Entrypoints tests cleanup ci/build;stale - Identify places where LoRA is unnecessary + centralize all LoRA-related tests into a central file. - Replace all 7B parameter models with https://huggingface.co/hmellor/t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
