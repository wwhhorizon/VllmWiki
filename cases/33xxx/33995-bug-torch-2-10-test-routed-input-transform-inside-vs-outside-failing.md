# vllm-project/vllm#33995: [Bug] [torch 2.10] test_routed_input_transform_inside_vs_outside failing

| 字段 | 值 |
| --- | --- |
| Issue | [#33995](https://github.com/vllm-project/vllm/issues/33995) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;moe;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [torch 2.10] test_routed_input_transform_inside_vs_outside failing

### Issue 正文摘录

### Your current environment Buildkite CI: https://buildkite.com/vllm/ci/builds/50239 ### 🐛 Describe the bug Related PR for torch 2.10 update: https://github.com/vllm-project/vllm/pull/30525 Looks like https://github.com/vllm-project/vllm/pull/32790 introduced this test However its failing on torch 2.10 update Failure can be seen here: https://buildkite.com/vllm/ci/builds/50239#019c2f78-fd4a-415e-bc4f-a8724dcaa19e ``` [2026-02-06T04:41:36Z] ________ test_routed_input_transform_inside_vs_outside[dtype0-128-64-1] ________ -- [2026-02-06T04:41:36Z] [2026-02-06T04:41:36Z] num_tokens = 1, hidden_size = 128, latent_size = 64, dtype = torch.bfloat16 [2026-02-06T04:41:36Z] dist_init = None, workspace_init = None [2026-02-06T04:41:36Z] [2026-02-06T04:41:36Z] @pytest.mark.parametrize("num_tokens", [1, 32]) [2026-02-06T04:41:36Z] @pytest.mark.parametrize("hidden_size,latent_size", [(256, 128), (128, 64)]) [2026-02-06T04:41:36Z] @pytest.mark.parametrize("dtype", [torch.bfloat16]) [2026-02-06T04:41:36Z] def test_routed_input_transform_inside_vs_outside( [2026-02-06T04:41:36Z] num_tokens: int, [2026-02-06T04:41:36Z] hidden_size: int, [2026-02-06T04:41:36Z] latent_size: int, [2026-02-06T04:41:36...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -02-06T04:41:36Z] ________ test_routed_input_transform_inside_vs_outside[dtype0-128-64-1] ________ -- [2026-02-06T04:41:36Z] [2026-02-06T04:41:36Z] num_tokens = 1, hidden_size = 128, latent_size = 64, dtype = torch.bflo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nsform_inside_vs_outside failing bug;stale ### Your current environment Buildkite CI: https://buildkite.com/vllm/ci/builds/50239 ### 🐛 Describe the bug Related PR for torch 2.10 update: https://github.com/vllm-project/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: hidden_states = torch.randn(num_tokens, hidden_size, device="cuda", dtype=dtype) [2026-02-06T04:41:36Z] router_logits = torch.randn(num_tokens, num_experts, device="cuda", dtype=dtype) [2026-02-06T04:41:36Z] [2026-02-06...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 6T04:41:36Z] ): [2026-02-06T04:41:36Z] """Compare SharedFusedMoE with transform inside vs manually applying outside. [2026-02-06T04:41:36Z] Method A (inside): SharedFusedMoE with routed_input_transform [2026-02-06T04:41...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [2026-02-06T04:41:36Z] [2026-02-06T04:41:36Z] > torch.testing.assert_close( [2026-02-06T04:41:36Z] routed_out_A, [2026-02-06T04:41:36Z] routed_out_B, [2026-02-06T04:41:36Z] atol=1e-3, [2026-02-06T04:41:36Z] rtol=1e-3,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
