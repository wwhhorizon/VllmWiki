# vllm-project/vllm#2165: when use gptq  using v100   CUDA 12.2, RuntimeError: CUDA error: no kernel image is available for execution on the device 

| 字段 | 值 |
| --- | --- |
| Issue | [#2165](https://github.com/vllm-project/vllm/issues/2165) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;quantization |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> when use gptq  using v100   CUDA 12.2, RuntimeError: CUDA error: no kernel image is available for execution on the device 

### Issue 正文摘录

File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/quantization/gptq.py", line 209, in apply_weights output = ops.gptq_gemm(reshaped_x, weights["qweight"], RuntimeError: CUDA error: no kernel image is available for execution on the device CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. @chu-tianxiang

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: when use gptq using v100 CUDA 12.2, RuntimeError: CUDA error: no kernel image is available for execution on the device File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/quantization/gptq.py", line...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: correctness frontend_api;quantization cuda;kernel;operator;quantization mismatch File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/quantization/gptq.py", line 209, in apply_weights
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/quantization/gptq.py", line 209, in apply_weights output = ops.gptq_gemm(reshaped_x, weights["qweight"], RuntimeError: CUDA error: no kernel image...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: cution on the device File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/quantization/gptq.py", line 209, in apply_weights output = ops.gptq_gemm(reshaped_x, weights["qweight"], RuntimeError: CUDA e...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: /quantization/gptq.py", line 209, in apply_weights output = ops.gptq_gemm(reshaped_x, weights["qweight"], RuntimeError: CUDA error: no kernel image is available for execution on the device CUDA kernel errors might be as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
