# vllm-project/vllm#21504: [RFC] [ROCm] [AITER]: Propose a `_aiter_ops` class like `_custom_ops` and `_ipex_ops`

| 字段 | 值 |
| --- | --- |
| Issue | [#21504](https://github.com/vllm-project/vllm/issues/21504) |
| 状态 | closed |
| 标签 | rocm;RFC;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | gemm_linear;hardware_porting;quantization |
| 子分类 | install |
| Operator 关键词 | fp8;kernel;operator;quantization |
| 症状 | import_error |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] [ROCm] [AITER]: Propose a `_aiter_ops` class like `_custom_ops` and `_ipex_ops`

### Issue 正文摘录

### Motivation. This RFC proposes the creation of a new module, `vllm/_aiter_ops.py`, to centralize the management, conditional loading, and registration of AITER kernels for ROCm. This new module will be analogous to the existing `_custom_ops.py` and `_ipex_ops.py`, providing a single, authoritative source for all AITER-related operations. This change will improve code organization, prevent circular dependencies, simplify the developer experience, and streamline testing. As the integration of AITER kernels into vLLM deepens, the current ad-hoc approach of importing and checking for these kernels across different parts of the codebase is becoming unsustainable. This leads to several challenges: - **Code Scatttering & Discoverability**: AITER kernels and their enabling logic are spread across various files, such as `vllm/model_executor/layers/linear.py` (for unquantized layers) and `vllm/model_executor/layers/quantization/utils/fp8_utils.py ` (for quantized layers). This makes it difficult for developers to find where a specific kernel is implemented or to understand the full scope of AITER integration. - **Risk of Circular Imports**: As more modules begin to depend on AITER kernel...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -related operations. This change will improve code organization, prevent circular dependencies, simplify the developer experience, and streamline testing. As the integration of AITER kernels into vLLM deepens, the curre...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: oss various files, such as `vllm/model_executor/layers/linear.py` (for unquantized layers) and `vllm/model_executor/layers/quantization/utils/fp8_utils.py ` (for quantized layers). This makes it difficult for developers...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [RFC] [ROCm] [AITER]: Propose a `_aiter_ops` class like `_custom_ops` and `_ipex_ops` rocm;RFC;unstale ### Motivation. This RFC proposes the creation of a new module, `vllm/_aiter_ops.py`, to centralize the management,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC] [ROCm] [AITER]: Propose a `_aiter_ops` class like `_custom_ops` and `_ipex_ops` rocm;RFC;unstale ### Motivation. This RFC proposes the creation of a new module, `vllm/_aiter_ops.py`, to centralize the management,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ng the actual AITER kernels (potentially within try...except ImportError blocks for lazy loading) and exposing them through a consistent interface. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any O...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
