# vllm-project/vllm#763: pip install error - CUDA version mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#763](https://github.com/vllm-project/vllm/issues/763) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> pip install error - CUDA version mismatch

### Issue 正文摘录

I have the torch version 2.0.1+cu117 ``` import torch print(torch.__version__) print(torch.version.cuda) 2.0.1+cu117 11.7 ``` However pip install vllm fails with ``` File "/tmp/pip-build-env-jw9yras7/overlay/lib/python3.8/site-packages/torch/utils/cpp_extension.py", line 387, in _check_cuda_version raise RuntimeError(CUDA_MISMATCH_MESSAGE.format(cuda_str_version, torch.version.cuda)) RuntimeError: The detected CUDA version (12.2) mismatches the version that was used to compile PyTorch (11.7). Please make sure to use the same CUDA versions. [end of output] ``` nvidia-smi ``` Tue Aug 15 11:43:53 2023 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 525.125.06 Driver Version: 525.125.06 CUDA Version: 12.0 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |===============================+======================+======================| | 0 NVIDIA A40 On | 00000000:35:00.0 Off | 0 | | 0% 39C P8 61W / 300W | 0MiB / 46068MiB | 0% Default | | | | N/A | +-----------------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: pip install error - CUDA version mismatch installation I have the torch version 2.0.1+cu117 ``` import torch print(torch.__version__) print(torch.version.cuda) 2.0.1+cu117 11.7 ``` However pip install vllm fails with ``...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pip install error - CUDA version mismatch installation I have the torch version 2.0.1+cu117 ``` import torch print(torch.__version__) print(torch.version.cuda) 2.0.1+cu117 11.7 ``` However pip install vllm fails with ``...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pip install error - CUDA version mismatch installation I have the torch version 2.0.1+cu117 ``` import torch print(torch.__version__) print(torch.version.cuda) 2.0.1+cu117 11.7 ``` However pip install vllm fails with ``...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=============================================================================| | No running processes found
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n _check_cuda_version raise RuntimeError(CUDA_MISMATCH_MESSAGE.format(cuda_str_version, torch.version.cuda)) RuntimeError: The detected CUDA version (12.2) mismatches the version that was used to compile PyTorch (11.7)....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
