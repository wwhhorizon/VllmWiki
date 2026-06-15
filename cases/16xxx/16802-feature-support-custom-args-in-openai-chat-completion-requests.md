# vllm-project/vllm#16802: [Feature]: Support custom args in OpenAI (chat) completion requests

| 字段 | 值 |
| --- | --- |
| Issue | [#16802](https://github.com/vllm-project/vllm/issues/16802) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support custom args in OpenAI (chat) completion requests

### Issue 正文摘录

https://github.com/vllm-project/vllm/pull/13300 added an `extra_args` field to `SamplingParameters` to allow for passing arbitrary parameters through to custom sampler / logits processor implementations. A follow on is to expose this in the OpenAI API endpoints, see discussion at the end of that PR. This will be needed to support custom sampling parameters via V1 logits processor plugins once that's ready (https://github.com/vllm-project/vllm/pull/13360).

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support custom args in OpenAI (chat) completion requests feature request https://github.com/vllm-project/vllm/pull/13300 added an `extra_args` field to `SamplingParameters` to allow for passing arbitrary para...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
