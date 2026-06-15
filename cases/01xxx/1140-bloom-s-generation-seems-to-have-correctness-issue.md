# vllm-project/vllm#1140: bloom's  generation  seems to have correctness issue.

| 字段 | 值 |
| --- | --- |
| Issue | [#1140](https://github.com/vllm-project/vllm/issues/1140) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> bloom's  generation  seems to have correctness issue.

### Issue 正文摘录

we are on the master branch, the bloom model generates meanlingless garbage outputs. ![image-20230922](https://github.com/vllm-project/vllm/assets/93073135/90233d9a-89e2-4131-9b9a-7080f8227c61)

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: bloom's generation seems to have correctness issue. we are on the master branch, the bloom model generates meanlingless garbage outputs. ![image-20230922](https://github.com/vllm-project/vllm/assets/93073135/90233d9a-89e
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: seems to have correctness issue. we are on the master branch, the bloom model generates meanlingless garbage outputs. ![image-20230922](https://github.com/vllm-project/vllm/assets/93073135/90233d9a-89e2-4131-9b9a-7080f8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
