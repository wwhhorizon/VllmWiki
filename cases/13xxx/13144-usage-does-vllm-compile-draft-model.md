# vllm-project/vllm#13144: [Usage]: Does vLLM compile draft model?

| 字段 | 值 |
| --- | --- |
| Issue | [#13144](https://github.com/vllm-project/vllm/issues/13144) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vLLM compile draft model?

### Issue 正文摘录

I'm not sure vLLM compiles draft model. Does vLLM compile both the model base and draft model following compilation configuration?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Does vLLM compile draft model? usage;stale I'm not sure vLLM compiles draft model. Does vLLM compile both the model base and draft model following compilation configuration?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Does vLLM compile draft model? usage;stale I'm not sure vLLM compiles draft model. Does vLLM compile both the model base and draft model following compilation configuration?
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: Does vLLM compile draft model? usage;stale I'm not sure vLLM compiles draft model. Does vLLM compile both the model base and draft model following compilation configuration?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
