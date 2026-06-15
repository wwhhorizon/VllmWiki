# vllm-project/vllm#1771: Fatal python error:Bus error

| 字段 | 值 |
| --- | --- |
| Issue | [#1771](https://github.com/vllm-project/vllm/issues/1771) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Fatal python error:Bus error

### Issue 正文摘录

![WechatIMG1287](https://github.com/vllm-project/vllm/assets/42851990/06ad0512-d1da-466d-8689-b0cad348e76a) I deployed vllm on RTX4090 * 2 and encountered an error. Can anyone help me?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sets/42851990/06ad0512-d1da-466d-8689-b0cad348e76a) I deployed vllm on RTX4090 * 2 and encountered an error. Can anyone help me?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
