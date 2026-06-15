# vllm-project/vllm#19071: [Bug]: vllm.third_party.pynvml.NVMLError_InvalidArgument: Invalid Argument

| 字段 | 值 |
| --- | --- |
| Issue | [#19071](https://github.com/vllm-project/vllm/issues/19071) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm.third_party.pynvml.NVMLError_InvalidArgument: Invalid Argument

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run the vllm with DP2+TP8 (2 nodes, 8xH20 GPUs per node), I missed the nvml error here: ``` INFO 06-03 09:22:34 [cuda.py:324] NvmlCudaPlatform.get_device_capability physical_device_id=8 Traceback (most recent call last): File " ", line 1, in File "/usr/lib/python3.10/multiprocessing/spawn.py", line 116, in spawn_main exitcode = _main(fd, parent_sentinel) File "/usr/lib/python3.10/multiprocessing/spawn.py", line 126, in _main self = reduction.pickle.load(from_parent) File "vllm/vllm/model_executor/layers/quantization/fp8.py", line 15, in from vllm.model_executor.layers.fused_moe import (FusedMoE, FusedMoEMethodBase, File "vllm/vllm/model_executor/layers/fused_moe/__init__.py", line 6, in from vllm.model_executor.layers.fused_moe.layer import ( File "vllm/vllm/model_executor/layers/fused_moe/layer.py", line 32, in from .fused_moe import fused_experts File "vllm/vllm/model_executor/layers/fused_moe/fused_moe.py", line 15, in from vllm.model_executor.layers.fused_moe.deep_gemm_moe import ( File "vllm/vllm/model_executor/layers/fused_moe/deep_gemm_moe.py", line 12, in from vllm.model_executor.layers.fused_moe.utils import (_fp8...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ion/fp8.py", line 15, in from vllm.model_executor.layers.fused_moe import (FusedMoE, FusedMoEMethodBase, File "vllm/vllm/model_executor/layers/fused_moe/__init__.py", line 6, in from vllm.model_executor.layers.fused_moe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: duction.pickle.load(from_parent) File "vllm/vllm/model_executor/layers/quantization/fp8.py", line 15, in from vllm.model_executor.layers.fused_moe import (FusedMoE, FusedMoEMethodBase, File "vllm/vllm/model_executor/lay...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: GPUs per node), I missed the nvml error here: ``` INFO 06-03 09:22:34 [cuda.py:324] NvmlCudaPlatform.get_device_capability physical_device_id=8 Traceback (most recent call last): File " ", line 1, in File "/usr/lib/pyth...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: in _main self = reduction.pickle.load(from_parent) File "vllm/vllm/model_executor/layers/quantization/fp8.py", line 15, in from vllm.model_executor.layers.fused_moe import (FusedMoE, FusedMoEMethodBase, File "vllm/vllm/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ization/fp8.py", line 15, in from vllm.model_executor.layers.fused_moe import (FusedMoE, FusedMoEMethodBase, File "vllm/vllm/model_executor/layers/fused_moe/__init__.py", line 6, in from vllm.model_executor.layers.fused...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
