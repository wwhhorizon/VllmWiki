# vllm-project/vllm#36459: [RFC]: vLLM IR Out-of-Tree (OOT) Kernel Registration

| 字段 | 值 |
| --- | --- |
| Issue | [#36459](https://github.com/vllm-project/vllm/issues/36459) |
| 状态 | closed |
| 标签 | RFC;vllm-ir |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: vLLM IR Out-of-Tree (OOT) Kernel Registration

### Issue 正文摘录

### Motivation. https://github.com/vllm-project/vllm/issues/32358 proposes vLLM IR, and PR [#33825](https://github.com/vllm-project/vllm/pull/33825) established the vLLM IR infrastructure: `IrOp` / `IrOpImpl` for op registration and priority-based dispatch, and `VllmIRLoweringPass` for lowering IR ops to concrete implementations during Inductor compilation. Backend kernel modules (`vllm_c.py`, `aiter_ops.py`, `oink_ops.py`) register their implementations via `@rms_norm.register_impl(...)`. The original `vllm/kernels/__init__.py` imported all kernel modules unconditionally: ```python from . import aiter_ops, oink_ops, vllm_c ``` This is unfriendly to OOT platforms — an OOT hardware backend may not have CUDA/ROCm C extensions available, and it needs to register its own IR implementations without loading vLLM's built-in kernels. The solution is a mechanism that lets **each platform control which kernel modules are loaded**. ### Proposed Change. ### Core Idea: `Platform.import_kernels()` as the Kernel Registration Entry Point Ownership of kernel module loading is delegated to the platform class. `vllm/kernels/__init__.py` no longer imports any kernel directly; instead it calls a platf...

## 现有链接修复摘要

#33825 [vLLM IR] 1/N Implement IR skeleton and rms_norm op

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: is is unfriendly to OOT platforms — an OOT hardware backend may not have CUDA/ROCm C extensions available, and it needs to register its own IR implementations without loading vLLM's built-in kernels. The solution is a m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: `@rms_norm.register_impl(...)`. The original `vllm/kernels/__init__.py` imported all kernel modules unconditionally: ```python from . import aiter_ops, oink_ops, vllm_c ``` This is unfriendly to OOT platforms — an OOT h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: frastructure: `IrOp` / `IrOpImpl` for op registration and priority-based dispatch, and `VllmIRLoweringPass` for lowering IR ops to concrete implementations during Inductor compilation. Backend kernel modules (`vllm_c.py...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: with contextlib.suppress(ImportError): import vllm._moe_C # noqa: F401 with contextlib.suppress(ImportError): import vllm.kernels.vllm_c # noqa: F401 # oink: SM100 (Blackwell) with contextlib.suppress(ImportError): impo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ion and priority activation are performed atomically inside `IrOpPriorityConfig.set_priority()`, so **there is no window where an implementation is registered but not yet dispatched**: ```python # vllm/config/kernel.py...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33825](https://github.com/vllm-project/vllm/pull/33825) | mentioned | 0.45 | [vLLM IR] 1/N Implement IR skeleton and rms_norm op | //github.com/vllm-project/vllm/issues/32358 proposes vllm ir, and pr [#33825](https://github.com/vllm-project/vllm/pull/33825) established the vllm ir infrastructure: `irop` / `ir… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
