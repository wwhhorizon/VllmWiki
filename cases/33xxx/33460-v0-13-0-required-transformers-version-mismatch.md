# vllm-project/vllm#33460: [v0.13.0] Required Transformers version mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#33460](https://github.com/vllm-project/vllm/issues/33460) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [v0.13.0] Required Transformers version mismatch

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/v0.13.0/vllm/model_executor/models/transformers/base.py#L347-L349 This implies that vllm 0.13.0 is compatible with Transformers 5.0. However, I tried installing Transformers 5.0 manually and it's clearly not compatible as this was renamed in Transformers 5.0: ```bash Traceback (most recent call last): ... File "/usr/local/lib/python3.12/dist-packages/vllm/__init__.py", line 74, in __getattr__ module = import_module(module_name, __package__) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/importlib/__init__.py", line 90, in import_module return _bootstrap._gcd_import(name[level:], package, level) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/llm.py", line 20, in from vllm.config import ( File "/usr/local/lib/python3.12/dist-packages/vllm/config/__init__.py", line 18, in from vllm.config.model import ( File "/usr/local/lib/python3.12/dist-packages/vllm/config/model.py", line 14, in from transformers.configuration_utils import ALLOWED_LAYER_TYPES ImportError: cannot import name 'ALLOWED_LAYER_TYPES' from 'transformers.configuration_utils' (/usr/local/lib/p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [v0.13.0] Required Transformers version mismatch https://github.com/vllm-project/vllm/blob/v0.13.0/vllm/model_executor/models/transformers/base.py#L347-L349 This implies that vllm 0.13.0 is compatible with Transformers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: version mismatch https://github.com/vllm-project/vllm/blob/v0.13.0/vllm/model_executor/models/transformers/base.py#L347-L349 This implies that vllm 0.13.0 is compatible with Transformers 5.0. However, I tried installing...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: there currently any way to get encoder-only support for the Transformers backend?
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [v0.13.0] Required Transformers version mismatch https://github.com/vllm-project/vllm/blob/v0.13.0/vllm/model_executor/models/transformers/base.py#L347-L349 This implies that vllm 0.13.0 is compatible with Transformers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [v0.13.0] Required Transformers version mismatch https://github.com/vllm-project/vllm/blob/v0.13.0/vllm/model_executor/models/transformers/base.py#L347-L349 This implies that vllm 0.13.0 is compatible with Transformers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
