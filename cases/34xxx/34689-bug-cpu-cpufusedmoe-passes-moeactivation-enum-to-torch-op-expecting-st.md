# vllm-project/vllm#34689: [Bug]: [cpu] CPUFusedMOE passes MoEActivation enum to torch op expecting str

| 字段 | 值 |
| --- | --- |
| Issue | [#34689](https://github.com/vllm-project/vllm/issues/34689) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [cpu] CPUFusedMOE passes MoEActivation enum to torch op expecting str

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Describe `CPUFusedMOE` fails on CPU because `torch.ops.vllm.cpu_fused_moe_torch` expects `activation` to be a `str` (per op schema), but the Python code passes a `MoEActivation` enum. TorchBind cannot cast Python enums to `str`, causing a runtime error. # How to reproduce ````yaml chmod +x .buildkite/scripts/hardware_ci/run-cpu-test-arm.sh bash .buildkite/scripts/hardware_ci/run-cpu-test-arm.sh ```` # minimum reproduce ````python import torch import vllm.model_executor.layers.fused_moe.cpu_fused_moe # triggers op registration from vllm.model_executor.layers.fused_moe.activation import MoEActivation out = torch.empty((1, 128), dtype=torch.float32) inp = torch.randn((1, 128), dtype=torch.float32) w = torch.rand((1, 2), dtype=torch.float32) ids = torch.tensor([[0, 1]], dtype=torch.int32) torch.ops.vllm.cpu_fused_moe_torch( 0, out, inp, w, ids, MoEActivation.SILU, # enum passed here -1, False, ) ```` # Error log Traceback (most recent call last): File "/home/micyan01/test.py", line 21, in torch.ops.vllm.cpu_fused_moe_torch(0, out, inp, w, ids, MoEActivation.SILU, -1, False) File "/home/micyan01/miniforge3/envs/vllm-test/lib/python3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: `str`, causing a runtime error. # How to reproduce ````yaml chmod +x .buildkite/scripts/hardware_ci/run-cpu-test-arm.sh bash .buildkite/scripts/hardware_ci/run-cpu-test-arm.sh ```` # minimum reproduce ````python import...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: [cpu] CPUFusedMOE passes MoEActivation enum to torch op expecting str bug;stale ### Your current environment ### 🐛 Describe the bug # Describe `CPUFusedMOE` fails on CPU because `torch.ops.vllm.cpu_fused_moe_torc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: s.fused_moe.activation import MoEActivation out = torch.empty((1, 128), dtype=torch.float32) inp = torch.randn((1, 128), dtype=torch.float32) w = torch.rand((1, 2), dtype=torch.float32) ids = torch.tensor([[0, 1]], dtyp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: d cannot cast Python enums to `str`, causing a runtime error. # How to reproduce ````yaml chmod +x .buildkite/scripts/hardware_ci/run-cpu-test-arm.sh bash .buildkite/scripts/hardware_ci/run-cpu-test-arm.sh ```` # minimu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
