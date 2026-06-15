# vllm-project/vllm#43750: [Bug]: [XPU] compressed-tensors WNA16 MoE selector ignores XPU platform, crashes on Marlin path

| 字段 | 值 |
| --- | --- |
| Issue | [#43750](https://github.com/vllm-project/vllm/issues/43750) |
| 状态 | open |
| 标签 | bug;intel-gpu |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: [XPU] compressed-tensors WNA16 MoE selector ignores XPU platform, crashes on Marlin path

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On XPU, loading a `compressed-tensors` W4A16 **MoE** model crashes during `process_weights_after_loading` with: ``` AttributeError: '_OpNamespace' '_C' object has no attribute 'gptq_marlin_repack' ``` The cause is the backend selector in `compressed_tensors_moe.py`, which only excludes ROCm from the Marlin path: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py ```python # Prefer to use the MarlinMoE kernel when it is supported. if ( not check_moe_marlin_supports_layer(layer, group_size) or current_platform.is_rocm() ): # ... CompressedTensorsWNA16MoEMethod (Triton, works on XPU) else: # ... CompressedTensorsWNA16MarlinMoEMethod (CUDA-only, crashes on XPU) return CompressedTensorsWNA16MarlinMoEMethod(...) ``` XPU has the same problem ROCm has — Marlin custom ops are not registered (the entire `torch.ops._C` namespace is effectively empty on the XPU build, since `vllm._C` isn't built for XPU) — but XPU isn't in the bypass condition, so it falls through to Marlin and crashes. Same-format **dense** W4A16 models work fine on XPU b...

## 现有链接修复摘要

#41426 [XPU][MoE] Add WNA16 oracle backend for GPTQ sym-int4 (xpu_fused_moe)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: red (the entire `torch.ops._C` namespace is effectively empty on the XPU build, since `vllm._C` isn't built for XPU) — but XPU isn't in the bypass condition, so it falls through to Marlin and crashes. Same-format **dens...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ttps://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py ```python # Prefer to use the MarlinMoE kernel when it is support...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: the backend selector in `compressed_tensors_moe.py`, which only excludes ROCm from the Marlin path: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/compressed_tensors/compressed_te...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 🐛 Describe the bug On XPU, loading a `compressed-tensors` W4A16 **MoE** model crashes during `process_weights_after_loading` with: ``` AttributeError: '_OpNamespace' '_C' object has no attribute 'gptq_marlin_repack' ```...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: [XPU] compressed-tensors WNA16 MoE selector ignores XPU platform, crashes on Marlin path bug;intel-gpu ### Your current environment ### 🐛 Describe the bug On XPU, loading a `compressed-tensors` W4A16 **MoE** mode...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41426](https://github.com/vllm-project/vllm/pull/41426) | mentioned | 0.45 | [XPU][MoE] Add WNA16 oracle backend for GPTQ sym-int4 (xpu_fused_moe) | essed-tensors w4a16 moe specifically. ### relationship to #41426 pr #41426 adds a native xpu int4 moe path for inc/gptq-quantized models via vllm-xpu-kernels. that work targets a… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
