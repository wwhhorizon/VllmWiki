# vllm-project/vllm#611: undefined symbol: _ZN3c106detail19maybe_wrap_dim_slowEllb

| 字段 | 值 |
| --- | --- |
| Issue | [#611](https://github.com/vllm-project/vllm/issues/611) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> undefined symbol: _ZN3c106detail19maybe_wrap_dim_slowEllb

### Issue 正文摘录

I get this error when I try to import. `/local_disk0/.ephemeral_nfs/envs/pythonEnv-83e459d1-1266-4d71-a155-ef12c7c6cd22/lib/python3.10/site-packages/vllm/activation_ops.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c106detail19maybe_wrap_dim_slowEllb`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: undefined symbol: _ZN3c106detail19maybe_wrap_dim_slowEllb I get this error when I try to import. `/local_disk0/.ephemeral_nfs/envs/pythonEnv-83e459d1-1266-4d71-a155-ef12c7c6cd22/lib/python3.10/site-packages/vllm/activat

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
