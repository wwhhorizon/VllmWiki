# vllm-project/vllm#44156: Bug: missing colon in logits processor FQCN crashes engine init with unhelpful ValueError

| 字段 | 值 |
| --- | --- |
| Issue | [#44156](https://github.com/vllm-project/vllm/issues/44156) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bug: missing colon in logits processor FQCN crashes engine init with unhelpful ValueError

### Issue 正文摘录

## Bug In `_load_logitsprocs_by_fqcns()` (`vllm/v1/sample/logits_processor/__init__.py`, line 128), the code does: ```python module_path, qualname = logitproc.split(":") ``` If the user passes a plain dotted path like `"mypackage.mymodule.MyLogitsProcessor"` (missing the required `:`), Python raises: ``` ValueError: not enough values to unpack (expected 2, got 1) ``` This error is unhandled and crashes engine initialization. The same crash occurs with two colons (e.g. `"my:package:MyClass"`). Neither case produces a message explaining the expected format. ## Expected format The docstring says FQCNs must be ` : `, e.g. `x.y.z:CustomLogitProc`, but the code does not validate this before unpacking. ## Fix Replace the bare unpack with a `len(parts) != 2` guard that raises a descriptive `ValueError` naming the expected format.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: kage:MyClass"`). Neither case produces a message explaining the expected format. ## Expected format The docstring says FQCNs must be ` : `, e.g. `x.y.z:CustomLogitProc`, but the code does not validate this before unpack...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
