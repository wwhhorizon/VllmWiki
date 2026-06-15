# vllm-project/vllm#3687: [Bug]: Automatic Prefix Caching doesn't support Nvidia Turing Arch.

| 字段 | 值 |
| --- | --- |
| Issue | [#3687](https://github.com/vllm-project/vllm/issues/3687) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Automatic Prefix Caching doesn't support Nvidia Turing Arch.

### Issue 正文摘录

### 🐛 Describe the bug `triton==2.1.0` doesn't support Turing arch, and has been fixed in https://github.com/openai/triton/pull/2364 Upgrade to `triton==2.2.0` will resolve this issue. Perhaps this could be planned after #3442.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Caching doesn't support Nvidia Turing Arch. bug ### 🐛 Describe the bug `triton==2.1.0` doesn't support Turing arch, and has been fixed in https://github.com/openai/triton/pull/2364 Upgrade to `triton==2.2.0` will resolv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Automatic Prefix Caching doesn't support Nvidia Turing Arch. bug ### 🐛 Describe the bug `triton==2.1.0` doesn't support Turing arch, and has been fixed in https://github.com/openai/triton/pull/2364 Upgrade to `tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
