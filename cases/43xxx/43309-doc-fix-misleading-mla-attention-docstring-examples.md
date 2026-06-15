# vllm-project/vllm#43309: [Doc]: Fix misleading MLA attention docstring examples

| 字段 | 值 |
| --- | --- |
| Issue | [#43309](https://github.com/vllm-project/vllm/issues/43309) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Fix misleading MLA attention docstring examples

### Issue 正文摘录

### Description The module-level docstring in `vllm/model_executor/layers/attention/mla_attention.py` appears to contain two misleading examples in the data-movement-friendly / `forward_mqa` section. Current text around lines 97-118 includes: ```python q_nope = (q_c @ W_UQ).view(-1, N, P) ql_nope = einsum("snh,lnh->snl", q, W_UK) ... return o.view(-1, N * V) @ self.num_heads @ W_O ``` The variable `q` is not defined in the surrounding example; it looks like this should use `q_nope`. Also, `@ self.num_heads @ W_O` appears to be a typo in the documented return expression; based on the MHA example and the stated shape of `W_O`, it likely should be `@ W_O`. ### Suggested fix Update only the docstring example, likely to: ```python ql_nope = einsum("snh,lnh->snl", q_nope, W_UK) ... return o.view(-1, N * V) @ W_O ``` ### Duplicate check I searched open issues and PRs for `mla_attention ql_nope q_nope W_O self.num_heads comment` and `MLA attention docstring typo`, and did not find an existing open issue or PR for this exact docstring problem. ### Note This is a documentation/comment issue only; it does not affect runtime behavior. Because this may be too small for a standalone PR under th...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , W_UK) ... return o.view(-1, N * V) @ W_O ``` ### Duplicate check I searched open issues and PRs for `mla_attention ql_nope q_nope W_O self.num_heads comment` and `MLA attention docstring typo`, and did not find an exi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: docstring examples ### Description The module-level docstring in `vllm/model_executor/layers/attention/mla_attention.py` appears to contain two misleading examples in the data-movement-friendly / `forward_mqa` section....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
