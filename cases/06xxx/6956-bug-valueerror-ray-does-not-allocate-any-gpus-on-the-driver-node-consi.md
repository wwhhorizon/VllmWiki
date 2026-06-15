# vllm-project/vllm#6956: [Bug]: ValueError: Ray does not allocate any GPUs on the driver node. Consider adjusting the Ray placement group or running the driver on a GPU node.

| 字段 | 值 |
| --- | --- |
| Issue | [#6956](https://github.com/vllm-project/vllm/issues/6956) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: Ray does not allocate any GPUs on the driver node. Consider adjusting the Ray placement group or running the driver on a GPU node.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug We should improve the way we create the default placement group in https://github.com/vllm-project/vllm/blob/cbbc904470668b9420e71595edeef76d673a2d59/vllm/executor/ray_utils.py#L119-L131 1. If we are in a placement group, but it does not contain the current node, error out. (this is a rare case, users usually don't set placement groups) 2. If not, we are creating a placement group. Make sure it contains the current node.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
