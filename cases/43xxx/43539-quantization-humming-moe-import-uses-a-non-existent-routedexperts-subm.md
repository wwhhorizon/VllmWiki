# vllm-project/vllm#43539: [Quantization] Humming MoE import uses a non-existent RoutedExperts submodule

| 字段 | 值 |
| --- | --- |
| Issue | [#43539](https://github.com/vllm-project/vllm/issues/43539) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Quantization] Humming MoE import uses a non-existent RoutedExperts submodule

### Issue 正文摘录

### What happened `vllm/model_executor/layers/quantization/utils/humming_utils.py` currently imports: ```python from vllm.model_executor.layers.fused_moe.routed_experts import RoutedExperts ``` That submodule does not exist on `main`. `RoutedExperts` is exported from `vllm.model_executor.layers.fused_moe` itself, so the Humming helper is importing from a stale path and raises `ModuleNotFoundError` as soon as the Humming MoE helper gets imported. ### Why it matters This is on the Humming / MXFP4 MoE path, so the backend crashes when code reaches `get_humming_moe_quant_config` or `prepare_humming_moe_layer`. ### Repro With Humming installed: ```python import vllm.model_executor.layers.quantization.utils.humming_utils ``` The import fails because `vllm.model_executor.layers.fused_moe.routed_experts` is not present in the tree. ### History This looks like a regression from `#40735` (`4d591db47`), which switched `humming_utils.py` over to `RoutedExperts` but pointed it at `fused_moe.routed_experts` instead of the alias exported from `fused_moe.__init__`. ### Expected fix Import from: ```python from vllm.model_executor.layers.fused_moe import RoutedExperts ``` instead of the missing `fu...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Quantization] Humming MoE import uses a non-existent RoutedExperts submodule ### What happened `vllm/model_executor/layers/quantization/utils/humming_utils.py` currently imports: ```python from vllm.model_executor.laye
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Quantization] Humming MoE import uses a non-existent RoutedExperts submodule ### What happened `vllm/model_executor/layers/quantization/utils/humming_utils.py` currently imports: ```python from vllm.model_executor.laye...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ort uses a non-existent RoutedExperts submodule ### What happened `vllm/model_executor/layers/quantization/utils/humming_utils.py` currently imports: ```python from vllm.model_executor.layers.fused_moe.routed_experts im...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Quantization] Humming MoE import uses a non-existent RoutedExperts submodule ### What happened `vllm/model_executor/layers/quantization/utils/humming_utils.py` currently imports: ```python from vllm.model_executor.laye...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ed. ### Why it matters This is on the Humming / MXFP4 MoE path, so the backend crashes when code reaches `get_humming_moe_quant_config` or `prepare_humming_moe_layer`. ### Repro With Humming installed: ```python import...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
