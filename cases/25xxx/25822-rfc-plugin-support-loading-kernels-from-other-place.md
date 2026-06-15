# vllm-project/vllm#25822: [RFC][Plugin]: support loading kernels from other place

| 字段 | 值 |
| --- | --- |
| Issue | [#25822](https://github.com/vllm-project/vllm/issues/25822) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][Plugin]: support loading kernels from other place

### Issue 正文摘录

### Motivation. Currently, all the compiled kernels are loaded in `_custom_ops.py` by: ``` python import vllm._C import vllm._moe_C ... ``` This has several limits: - It needs to guarantee that the dynamic libraries are under the vllm's directory (usually under site-package). - If plugin(or out_of_tree) wanna reuse this file and adapted or registered the same kernels, they have to copy their kernels from plugin to vllm's folder during the installation. ### Proposed Change. We want to offer a platform interface to support load the platform-specific kernel operations: ```python class Platform: @classmethod def import_general_kernels(cls) -> None: """ Import any platform-specific C kernels. """ import vllm._C # noqa: F401 # import vllm.some_other_kernels @classmethod def import_moe_kernels(cls) -> None: """ Import any platform-specific Mixture of Experts kernels. """ import vllm._moe_C # noqa: F401 ``` and then, to load them by: ``` # in _custom_ops.py try: current_platform.import_general_kernels() except ImportError as e: logger.warning("Failed to load kernels with %r", e) supports_moe_ops = False with contextlib.suppress(ImportError): current_platform.import_moe_kernels() supports_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g kernels from other place RFC;stale ### Motivation. Currently, all the compiled kernels are loaded in `_custom_ops.py` by: ``` python import vllm._C import vllm._moe_C ... ``` This has several limits: - It needs to gua...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: platform-specific kernel operations: ```python class Platform: @classmethod def import_general_kernels(cls) -> None: """ Import any platform-specific C kernels. """ import vllm._C # noqa: F401 # import vllm.some_other_k...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: e loaded in `_custom_ops.py` by: ``` python import vllm._C import vllm._moe_C ... ``` This has several limits: - It needs to guarantee that the dynamic libraries are under the vllm's directory (usually under site-packag...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC][Plugin]: support loading kernels from other place RFC;stale ### Motivation. Currently, all the compiled kernels are loaded in `_custom_ops.py` by: ``` python import vllm._C import vllm._moe_C ... ``` This has seve...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ogger.warning("Failed to load kernels with %r", e) supports_moe_ops = False with contextlib.suppress(ImportError): current_platform.import_moe_kernels() supports_moe_ops = True ``` I've made a draft pr in #25823, any co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
