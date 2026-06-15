# vllm-project/vllm#1060: Building from source by running `pip install -e .` CUDA version mismatches

| 字段 | 值 |
| --- | --- |
| Issue | [#1060](https://github.com/vllm-project/vllm/issues/1060) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Building from source by running `pip install -e .` CUDA version mismatches

### Issue 正文摘录

Building from source failed for me. torch version: ``` Python 3.10.11 (main, May 16 2023, 00:28:57) [GCC 11.2.0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> import torch >>> print(torch.__version__) 2.0.1+cu118 >>> ``` nvidia-smai ``` nvidia-smi Fri Sep 15 15:24:14 2023 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.104.05 Driver Version: 535.104.05 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA RTX A6000 On | 00000000:52:00.0 On | Off | | 30% 43C P8 30W / 300W | 695MiB / 49140MiB | 0% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ +---------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |============...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: Building from source by running `pip install -e .` CUDA version mismatches Building from source failed for me. torch version: ``` Python 3.10.11 (main, May 16 2023, 00:28:57) [GCC 11.2.0] on linux Type "help", "copyrigh
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Building from source by running `pip install -e .` CUDA version mismatches Building from source failed for me. torch version: ``` Python 3.10.11 (main, May 16 2023, 00:28:57) [GCC 11.2.0] on linux Type "help", "copyrigh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Building from source by running `pip install -e .` CUDA version mismatches Building from source failed for me. torch version: ``` Python 3.10.11 (main, May 16 2023, 00:28:57) [GCC 11.2.0] on linux Type "help", "copyrigh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: and/editable_wheel.py", line 345, in _create_wheel_file files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp) File "/tmp/pip-build-env-4xnh4rb6/overlay/lib/python3.10/site-packages/setuptools/command/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> import torch >>> print(torch.__version__) 2.0.1+cu118 >>> ``` nvidia-smai ``` nvidia-smi Fri Sep 15 15:24:14 2023 +----------------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
