# vllm-project/vllm#582: does not work in distributed mode

| 字段 | 值 |
| --- | --- |
| Issue | [#582](https://github.com/vllm-project/vllm/issues/582) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> does not work in distributed mode

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/93528700/949b8541-8b8d-4045-ab94-5f964de6d12d) ![image](https://github.com/vllm-project/vllm/assets/93528700/1ff4c44d-b50a-4941-a394-89bbbfc3e42e) When I set tensor_parallel_size to 2, the model doesn't work. When I set it to 1, it works fine.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d-b50a-4941-a394-89bbbfc3e42e) When I set tensor_parallel_size to 2, the model doesn't work. When I set it to 1, it works fine.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
