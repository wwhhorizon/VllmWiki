# vllm-project/vllm#5288: [Bug] [Speculative Decoding/flash_attn]: Flash attn backend crashes in speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#5288](https://github.com/vllm-project/vllm/issues/5288) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [Speculative Decoding/flash_attn]: Flash attn backend crashes in speculative decoding

### Issue 正文摘录

### Your current environment CI environment ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/pull/5286 and https://github.com/vllm-project/vllm/issues/5152 My guess is the way we encode multiple query tokens per sequence in an attention kernel invocation breaks the flash_attn contract somehow.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug] [Speculative Decoding/flash_attn]: Flash attn backend crashes in speculative decoding bug ### Your current environment CI environment ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/pull/5286 and h...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ackend crashes in speculative decoding bug ### Your current environment CI environment ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/pull/5286 and https://github.com/vllm-project/vllm/issues/5152 My gu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug] [Speculative Decoding/flash_attn]: Flash attn backend crashes in speculative decoding bug ### Your current environment CI environment ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/pull/5286 and h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
