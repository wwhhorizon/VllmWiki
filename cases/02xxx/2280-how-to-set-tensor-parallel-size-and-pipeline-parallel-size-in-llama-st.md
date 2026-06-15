# vllm-project/vllm#2280: how to set tensor-parallel-size and pipeline-parallel-size in llama structure?

| 字段 | 值 |
| --- | --- |
| Issue | [#2280](https://github.com/vllm-project/vllm/issues/2280) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> how to set tensor-parallel-size and pipeline-parallel-size in llama structure?

### Issue 正文摘录

I want to deploy hf 70b model on 4 * A6000. Which kind of hyper parameters is better tp=2,pp=2 or tp=1,pp=4 or tp=4, pp=1?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: how to set tensor-parallel-size and pipeline-parallel-size in llama structure? I want to deploy hf 70b model on 4 * A6000. Which kind of hyper parameters is better tp=2,pp=2 or tp=1,pp=4 or tp=4, pp=1?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
