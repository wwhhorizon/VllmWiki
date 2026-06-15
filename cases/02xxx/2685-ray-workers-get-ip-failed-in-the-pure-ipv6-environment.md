# vllm-project/vllm#2685: Ray Workers `get_ip` failed in the pure IPv6 environment

| 字段 | 值 |
| --- | --- |
| Issue | [#2685](https://github.com/vllm-project/vllm/issues/2685) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Ray Workers `get_ip` failed in the pure IPv6 environment

### Issue 正文摘录

This line will raise an `Network is unreachable` OSError in the pure IPv6 environment, which fails `_init_workers_ray` method. https://github.com/vllm-project/vllm/blob/1af090b57d0e23d268e79941f8084bf0a8ad8621/vllm/utils.py#L166

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
