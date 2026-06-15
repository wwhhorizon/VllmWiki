# vllm-project/vllm#42628: macOS source checkout resolves to UnspecifiedPlatform (empty device_type)

| 字段 | 值 |
| --- | --- |
| Issue | [#42628](https://github.com/vllm-project/vllm/issues/42628) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> macOS source checkout resolves to UnspecifiedPlatform (empty device_type)

### Issue 正文摘录

**Description:** When running vLLM from a source checkout on macOS (no `pip install`), `cpu_platform_plugin()` returns `None` because the `sys.platform.startswith("darwin")` fallback is unreachable. This causes `resolve_current_platform_cls_qualname()` to select `UnspecifiedPlatform`, which has `device_type = ""`, crashing any `torch.device("")` call. **Minimal Reproducible Example:** ```python # On macOS, from a source checkout (no pip install): from vllm.platforms import current_platform print(current_platform.device_type) # "" → torch.device("") crashes ``` **Expected behavior:** `cpu_platform_plugin()` returns `"vllm.platforms.cpu.CpuPlatform"` on macOS regardless of package install state. **Actual behavior:** `RuntimeError: Device string must not be empty` **Hypothesis:** `vllm_version_matches_substr("cpu")` re-raises `PackageNotFoundError` in source checkouts. The macOS fallback (`sys.platform.startswith("darwin")`) is inside the same `try` block, so the exception skips it entirely. **Environment:** macOS (darwin), Python 3.13, source checkout without pip install.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: macOS source checkout resolves to UnspecifiedPlatform (empty device_type) **Description:** When running vLLM from a source checkout on macOS (no `pip install`), `cpu_platform_plugin()` returns `None` because the `sys.pl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: plugin()` returns `None` because the `sys.platform.startswith("darwin")` fallback is unreachable. This causes `resolve_current_platform_cls_qualname()` to select `UnspecifiedPlatform`, which has `device_type = ""`, cras...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: has `device_type = ""`, crashing any `torch.device("")` call. **Minimal Reproducible Example:** ```python # On macOS, from a source checkout (no pip install): from vllm.platforms import current_platform print(current_pl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: fallback (`sys.platform.startswith("darwin")`) is inside the same `try` block, so the exception skips it entirely. **Environment:** macOS (darwin), Python 3.13, source checkout without pip install.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
