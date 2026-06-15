# vllm-project/vllm#32059: [Feature]: Use platform op if inside a custom op

| 字段 | 值 |
| --- | --- |
| Issue | [#32059](https://github.com/vllm-project/vllm/issues/32059) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Use platform op if inside a custom op

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We have the `CustomOp` for SIluandMul ``` @staticmethod def forward_native(x: torch.Tensor) -> torch.Tensor: """PyTorch-native implementation equivalent to forward().""" d = x.shape[-1] // 2 return F.silu(x[..., :d]) * x[..., d:] def forward_cuda(self, x: torch.Tensor) -> torch.Tensor: d = x.shape[-1] // 2 output_shape = x.shape[:-1] + (d,) out = torch.empty(output_shape, dtype=x.dtype, device=x.device) self.op(out, x) return out def forward_xpu(self, x: torch.Tensor) -> torch.Tensor: d = x.shape[-1] // 2 output_shape = x.shape[:-1] + (d,) out = torch.empty(output_shape, dtype=x.dtype, device=x.device) self.op(out, x) return out ``` If the `CustomOp` is inside a `custom_op` (hiding from torch compile), we end up running the `forward_native` WITHOUT torch compile And example of this is running shared expert stream where the shared expert runs inside the custom op. This means we currently run unfused Solutions: A) We are working to unwrap the custom op B) If a CustomOp is inside a cusom op, we should run the platform version, not the native version cc @ProExpertProg ### Alternatives _No response_ ### Additional context _No response_ ### Before...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rn out ``` If the `CustomOp` is inside a `custom_op` (hiding from torch compile), we end up running the `forward_native` WITHOUT torch compile And example of this is running shared expert stream where the shared expert...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -1] // 2 return F.silu(x[..., :d]) * x[..., d:] def forward_cuda(self, x: torch.Tensor) -> torch.Tensor: d = x.shape[-1] // 2 output_shape = x.shape[:-1] + (d,) out = torch.empty(output_shape, dtype=x.dtype, device=x.de...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: tput_shape = x.shape[:-1] + (d,) out = torch.empty(output_shape, dtype=x.dtype, device=x.device) self.op(out, x) return out def forward_xpu(self, x: torch.Tensor) -> torch.Tensor: d = x.shape[-1] // 2 output_shape = x.s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ard_native` WITHOUT torch compile And example of this is running shared expert stream where the shared expert runs inside the custom op. This means we currently run unfused Solutions: A) We are working to unwrap the cus...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Use platform op if inside a custom op feature request ### 🚀 The feature, motivation and pitch We have the `CustomOp` for SIluandMul ``` @staticmethod def forward_native(x: torch.Tensor) -> torch.Tensor: """Py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
