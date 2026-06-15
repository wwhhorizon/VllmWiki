# vllm-project/vllm#714: Did vLLM support flashatten to save the memeory?

| 字段 | 值 |
| --- | --- |
| Issue | [#714](https://github.com/vllm-project/vllm/issues/714) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Did vLLM support flashatten to save the memeory?

### Issue 正文摘录

when i use flash-atten to do the `fschat/long-eval` test . i see the flash-attn saves a lot of gpu-memory usage. so im wondering if vLLm support this too?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: atten to save the memeory? when i use flash-atten to do the `fschat/long-eval` test . i see the flash-attn saves a lot of gpu-memory usage. so im wondering if vLLm support this too?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
