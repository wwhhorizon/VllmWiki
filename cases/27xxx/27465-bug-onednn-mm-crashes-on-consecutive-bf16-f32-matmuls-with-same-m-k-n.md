# vllm-project/vllm#27465: [Bug]: onednn_mm crashes on consecutive bf16, f32 matmuls with same M,K,N

| 字段 | 值 |
| --- | --- |
| Issue | [#27465](https://github.com/vllm-project/vllm/issues/27465) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: onednn_mm crashes on consecutive bf16, f32 matmuls with same M,K,N

### Issue 正文摘录

### 🐛 Describe the bug onednn_mm crashes when consecutive matmuls of different dtypes but same M,K,N I think, the oneDNN handler of the first matmul cached and reused for the second matmul which is of different dtype. It only happens if all M,K,N are the same for the 2 matmuls. Reproducer: ``` # SPDX-FileCopyrightText: Copyright 2025 Arm Limited and/or its affiliate # SPDX-License-Identifier: BSD-3-Clause import torch from vllm import _custom_ops as ops def onednn_gemm_test(m: int, n: int, k: int, device: str = "cpu"): ## fp32 a_f32 = torch.rand((m, k), dtype=torch.float32, device=device) b_f32 = torch.rand((n, k), dtype=torch.float32, device=device) out_f32_ref = torch.nn.functional.linear(a_f32, b_f32) handler_f32 = ops.create_onednn_mm( b_f32.t(), ) out_f32 = ops.onednn_mm(handler_f32, a_f32, bias=None) torch.testing.assert_close(out_f32, out_f32_ref) print("Done FP32", flush=True) ## bf16 a_bf16 = torch.rand((m, k), dtype=torch.bfloat16, device=device) b_bf16 = torch.rand((n, k), dtype=torch.bfloat16, device=device) out_bf16_ref = torch.nn.functional.linear(a_bf16, b_bf16) handler_bf16 = ops.create_onednn_mm( b_bf16.t(), ) out_bf16 = ops.onednn_mm(handler_bf16, a_bf16, bias=No...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: onednn_mm crashes on consecutive bf16, f32 matmuls with same M,K,N bug ### 🐛 Describe the bug onednn_mm crashes when consecutive matmuls of different dtypes but same M,K,N I think, the oneDNN handler of the first...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ent dtype. It only happens if all M,K,N are the same for the 2 matmuls. Reproducer: ``` # SPDX-FileCopyrightText: Copyright 2025 Arm Limited and/or its affiliate # SPDX-License-Identifier: BSD-3-Clause import torch from...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: m Limited and/or its affiliate # SPDX-License-Identifier: BSD-3-Clause import torch from vllm import _custom_ops as ops def onednn_gemm_test(m: int, n: int, k: int, device: str = "cpu"): ## fp32 a_f32 = torch.rand((m, k...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: SD-3-Clause import torch from vllm import _custom_ops as ops def onednn_gemm_test(m: int, n: int, k: int, device: str = "cpu"): ## fp32 a_f32 = torch.rand((m, k), dtype=torch.float32, device=device) b_f32 = torch.rand((n

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
