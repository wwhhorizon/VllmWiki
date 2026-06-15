# vllm-project/vllm#2579: benchmark error

| 字段 | 值 |
| --- | --- |
| Issue | [#2579](https://github.com/vllm-project/vllm/issues/2579) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> benchmark error

### Issue 正文摘录

why POST /generate HTTP/1.1" 404 Not Found? Can anyone help me, thanks. ![image](https://github.com/vllm-project/vllm/assets/9295202/922e3856-b750-4ab7-a8c4-94e6bfcc1575) ![image](https://github.com/vllm-project/vllm/assets/9295202/5797a0e1-94d9-4cc1-a911-a3e03196dd67) ![image](https://github.com/vllm-project/vllm/assets/9295202/f9103ec4-b4b6-4ba8-8047-fbe7b6c733c9)

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: benchmark error why POST /generate HTTP/1.1" 404 Not Found? Can anyone help me, thanks. ![image](https://github.com/vllm-project/vllm/assets/9295202/922e3856-b750-4ab7-a8c4-94e6bfcc1575) ![image](https://github.com/vllm

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
