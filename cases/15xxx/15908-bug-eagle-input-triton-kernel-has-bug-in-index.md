# vllm-project/vllm#15908: [Bug]: Eagle input triton kernel has bug in index

| 字段 | 值 |
| --- | --- |
| Issue | [#15908](https://github.com/vllm-project/vllm/issues/15908) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Eagle input triton kernel has bug in index

### Issue 正文摘录

### 🐛 Describe the bug The triton kernel for preparing eagle input in #15729 seems to have a bug where it writes the same value across blocks. Added a colab notebook to highlight the bug and the fix: https://colab.research.google.com/drive/19RjTr8K2TTa-Zw7OUW7Bw0UfnMunUEFf?usp=sharing The example assumes 4 draft tokens, block size 2, 0 rejections. The 1st output shows that values are repeated for every 2 places since block size is 2. @WoosukKwon lmk if I misunderstood the indexing.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Eagle input triton kernel has bug in index bug ### 🐛 Describe the bug The triton kernel for preparing eagle input in #15729 seems to have a bug where it writes the same value across blocks. Added a colab notebook...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ded a colab notebook to highlight the bug and the fix: https://colab.research.google.com/drive/19RjTr8K2TTa-Zw7OUW7Bw0UfnMunUEFf?usp=sharing The example assumes 4 draft tokens, block size 2, 0 rejections. The 1st output...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: put in #15729 seems to have a bug where it writes the same value across blocks. Added a colab notebook to highlight the bug and the fix: https://colab.research.google.com/drive/19RjTr8K2TTa-Zw7OUW7Bw0UfnMunUEFf?usp=shar...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ive/19RjTr8K2TTa-Zw7OUW7Bw0UfnMunUEFf?usp=sharing The example assumes 4 draft tokens, block size 2, 0 rejections. The 1st output shows that values are repeated for every 2 places since block size is 2. @WoosukKwon lmk i...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
