# vllm-project/vllm#34000: Move the Python kernel abstraction package (selectors + interfaces) under `vllm/model_executor` so unquantized linear kernels don’t need to be referenced from a quantization-specific directory.

| 字段 | 值 |
| --- | --- |
| Issue | [#34000](https://github.com/vllm-project/vllm/issues/34000) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Move the Python kernel abstraction package (selectors + interfaces) under `vllm/model_executor` so unquantized linear kernels don’t need to be referenced from a quantization-specific directory.

### Issue 正文摘录

Move the `kernels` from `quantization` into `model_executor` Final directory layout ``` vllm/ └── vllm/ └── model_executor/ └── kernels/ ├── __init__.py ├── mixed_precision │ ├── MPLinearKernel.py │ ├── __init__.py │ ├── allspark.py │ ├── bitblas.py │ ├── conch.py │ ├── cpu.py │ ├── cutlass.py │ ├── dynamic_4bit.py │ ├── exllama.py │ ├── machete.py │ ├── marlin.py │ └── xpu.py └── scaled_mm ├── ScaledMMLinearKernel.py ├── __init__.py ├── aiter.py ├── cpu.py ├── cutlass.py ├── flashinfer.py ├── pytorch.py ├── rocm.py └── triton.py ```

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: │ ├── conch.py │ ├── cpu.py │ ├── cutlass.py │ ├── dynamic_4bit.py │ ├── exllama.py │ ├── machete.py │ ├── marlin.py │ └── xpu.py └── scaled_mm ├── Sca
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: action package (selectors + interfaces) under `vllm/model_executor` so unquantized linear kernels don’t need to be referenced from a quantization-specific directory. Move the `kernels` from `quantization` into `model_ex...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e Python kernel abstraction package (selectors + interfaces) under `vllm/model_executor` so unquantized linear kernels don’t need to be referenced from a quantization-specific directory. Move the `kernels` from `quantiz...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: / └── kernels/ ├── __init__.py ├── mixed_precision │ ├── MPLinearKernel.py │ ├── __init__.py │ ├── allspark.py │ ├── bitblas.py │ ├── conch.py │ ├── cpu.py │
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ntized linear kernels don’t need to be referenced from a quantization-specific directory. Move the `kernels` from `quantization` into `model_executor` Final directory layout ``` vllm/ └── vllm/ └── model_executor/ └── k...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
