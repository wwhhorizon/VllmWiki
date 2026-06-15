# vllm-project/vllm#9636: [Bug]: Fused Moe pytest is failing with large number of experts

| 字段 | 值 |
| --- | --- |
| Issue | [#9636](https://github.com/vllm-project/vllm/issues/9636) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fused Moe pytest is failing with large number of experts

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```Python # sample code to reproduce the error """Tests for the MOE layers. Run `pytest tests/kernels/test_moe.py`. """ import pytest import torch from transformers import MixtralConfig from transformers.models.mixtral.modeling_mixtral import MixtralSparseMoeBlock from vllm.model_executor.layers.activation import SiluAndMul from fused_moe_tp_new import fused_moe from vllm.model_executor.models.mixtral import MixtralMoE def torch_moe(a, w1, w2, score, topk): B, D = a.shape a = a.view(B, -1, D).repeat(1, topk, 1).reshape(-1, D) out = torch.zeros(B * topk, w2.shape[1], dtype=a.dtype, device=a.device) score = torch.softmax(score, dim=-1, dtype=torch.float32) topk_weight, topk_ids = torch.topk(score, topk) topk_weight = topk_weight.view(-1) topk_ids = topk_ids.view(-1) for i in range(w1.shape[0]): mask = topk_ids == i if mask.sum(): out[mask] = SiluAndMul()( a[mask] @ w1[i].transpose(0, 1)) @ w2[i].transpose(0, 1) return (out.view(B, -1, w2.shape[1]) * topk_weight.view(B, -1, 1).to(out.dtype)).sum(dim=1) @pytest.mark.parametrize("bl", [32768]) @pytest.mark.parametrize("h", [6144, 7168]) @pytest.mark...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ""Tests for the MOE layers. Run `pytest tests/kernels/test_moe.py`. """ import pytest import torch from transformers import MixtralConfig from transformers.models.mixtral.modeling_mixtral import MixtralSparseMoeBlock fr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: (1, topk, 1).reshape(-1, D) out = torch.zeros(B * topk, w2.shape[1], dtype=a.dtype, device=a.device) score = torch.softmax(score, dim=-1, dtype=torch.float32) topk_weight, topk_ids = torch.topk(score, topk) topk_weight...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: Dumps _No response_ ### 🐛 Describe the bug ```Python # sample code to reproduce the error """Tests for the MOE layers. Run `pytest tests/kernels/test_moe.py`. """ import pytest import torch from transformers import Mixt...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Fused Moe pytest is failing with large number of experts bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```Python # sample code to reproduce the error """Tests f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pk: int, dtype: torch.dtype, ): a = torch.randn((bl, h), device='cuda', dtype=dtype) / 10 w1 = torch.randn((e, 2 * h2, h), device='cuda', dtype=dtype) / 10 w2 = torch.randn((e, h, h2), device='cuda', dtype=dtype) / 10 s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
