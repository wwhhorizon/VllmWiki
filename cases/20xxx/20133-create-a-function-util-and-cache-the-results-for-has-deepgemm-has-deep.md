# vllm-project/vllm#20133: Create a function util and cache the results for `has_deepgemm`, `has_deepep`, `has_pplx`

| 字段 | 值 |
| --- | --- |
| Issue | [#20133](https://github.com/vllm-project/vllm/issues/20133) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Create a function util and cache the results for `has_deepgemm`, `has_deepep`, `has_pplx`

### Issue 正文摘录

nit: create a function and cache the results. _Originally posted by @houseroad in https://github.com/vllm-project/vllm/pull/20090#discussion_r2169027989_ Thanks to @houseroad, there are a lot of code like `has_pplx = importlib.util.find_spec("pplx_kernels") is not None` anywhere. Same for `has_deepgemm`, `has_deepep` etc. We can create util function and cache the result for better readability and maintainablility. I will have a pr for this soon.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 027989_ Thanks to @houseroad, there are a lot of code like `has_pplx = importlib.util.find_spec("pplx_kernels") is not None` anywhere. Same for `has_deepgemm`, `has_deepep` etc. We can create util function and cache the...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Create a function util and cache the results for `has_deepgemm`, `has_deepep`, `has_pplx` nit: create a function and cache the results. _Originally posted by @houseroad in https://github.com/vllm-project/vllm/pull/20090...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
