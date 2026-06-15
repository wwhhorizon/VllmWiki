# vllm-project/vllm#6056: [Bug]: debugging guide for device >= 0 && device < num_gpus INTERNAL ASSERT FAILED at "../aten/src/ATen/cuda/CUDAContext.cpp"

| 字段 | 值 |
| --- | --- |
| Issue | [#6056](https://github.com/vllm-project/vllm/issues/6056) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;multimodal_vlm |
| 子分类 | debug |
| Operator 关键词 | cuda;operator |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: debugging guide for device >= 0 && device < num_gpus INTERNAL ASSERT FAILED at "../aten/src/ATen/cuda/CUDAContext.cpp"

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug This is a compond and annoying bug, coupled with pytorch bug https://github.com/pytorch/pytorch/pull/122815 . Basically, pytorch `torch.cuda.device_count` function will cache the device count when first called. Users might not call it directly, but if you use `import torch._dynamo` , it will be called. The call chain is: ```text File "/usr/local/lib/python3.10/dist-packages/torchvision/ops/roi_align.py", line 4, in import torch._dynamo File " ", line 1027, in _find_and_load File " ", line 1006, in _find_and_load_unlocked File " ", line 688, in _load_unlocked File " ", line 883, in exec_module File " ", line 241, in _call_with_frames_removed File "/usr/local/lib/python3.10/dist-packages/torch/_dynamo/__init__.py", line 2, in from . import convert_frame, eval_frame, resume_execution File " ", line 1078, in _handle_fromlist File " ", line 241, in _call_with_frames_removed File " ", line 1027, in _find_and_load File " ", line 1006, in _find_and_load_unlocked File " ", line 688, in _load_unlocked File " ", line 883, in exec_module File " ", line 241, in _call_with_frames_removed File "...

## 现有链接修复摘要

#15366 [Bugfix][V1] Avoid importing PreTrainedModel

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ackages/torch/_dynamo/convert_frame.py", line 40, in from . import config, exc, trace_rules File " ", line 1078, in _handle_fromlist File " ", line 241, in _call_with_frames_removed File " ", line 1027, in _find_and_loa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: unt when first called. Users might not call it directly, but if you use `import torch._dynamo` , it will be called. The call chain is: ```text File "/usr/local/lib/python3.10/dist-packages/torchvision/ops/roi_align.py",...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ine 21, in from .image_transforms import center_crop, normalize, rescale File " ", line 1027, in _find_and_load File " ", line 1006, in _find_and_load_unlocked File " ", line 688, in _load_unlocked File " ", line 883, i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce >= 0 && device < num_gpus INTERNAL ASSERT FAILED at "../aten/src/ATen/cuda/CUDAContext.cpp" bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug This is a compond...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: vnext.py", line 8, in from ..ops.misc import Conv2dNormActivation, Permute File " ", line 1027, in _find_and_load File " ", line 992, in _find_and_load_unlocked File " ", line 241, in _call_with_frames_removed File " ",...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#15366](https://github.com/vllm-project/vllm/pull/15366) | mentioned | 0.6 | [Bugfix][V1] Avoid importing PreTrainedModel | 741#issuecomment-2705517085 Currently we will have errors similar to #6056: device >= 0 && device < num_gpus INTERNAL ASSERT FAILED at "../aten/src/ATen/cuda/CUDAContext.cpp" in V… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
