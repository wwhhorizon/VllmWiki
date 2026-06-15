# vllm-project/vllm#8493: [Installation]: I want to install with CPU follow the guide on windows (wsl2, ubuntu) but the wsl crash.

| 字段 | 值 |
| --- | --- |
| Issue | [#8493](https://github.com/vllm-project/vllm/issues/8493) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: I want to install with CPU follow the guide on windows (wsl2, ubuntu) but the wsl crash.

### Issue 正文摘录

### Your current environment Hello, I apologize for the interruption. I am a newcomer and currently following a tutorial for installation. I have encountered some issues, and I have looked into some other people's questions, but I haven't found any that resolve my problem. I hope I can receive some assistance. I was following the guide to install vllm with CPU(because my gpu only has 8G ram, not sufficient to run llama3.1 8b)，and after cmake，I run this command in wsl ubuntu: ```bash VLLM_TARGET_DEVICE=cpu python setup.py install ``` and finally the wsl crashed, exit to the powershell. ```text (myenv) wangkun@DESKTOP-5HLONVC:/mnt/c/Users/wangk/ubuntu/vllm$ VLLM_TARGET_DEVICE=cpu python setup.py install running install /mnt/c/Users/wangk/ubuntu/myenv/lib/python3.12/site-packages/setuptools/_distutils/cmd.py:66: SetuptoolsDeprecationWarning: setup.py install is deprecated. !! ******************************************************************************** Please avoid running ``setup.py`` directly. Instead, use pypa/build, pypa/installer or other standards-based tools. See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details. *********************************...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: I want to install with CPU follow the guide on windows (wsl2, ubuntu) but the wsl crash. installation ### Your current environment Hello, I apologize for the interruption. I am a newcomer and currently fo
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: lm/model_executor/layers/fused_moe/configs/E=8,N=8192,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8.json -> build/lib.linux-x86_64-cpython-312/vllm/model_executor/layers/fused_moe/configs running build_ext -- Build t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: tall vllm with CPU(because my gpu only has 8G ram, not sufficient to run llama3.1 8b)，and after cmake，I run this command in wsl ubuntu: ```bash VLLM_TARGET_DEVICE=cpu python setup.py install ``` and finally the wsl cras...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: > build/lib.linux-x86_64-cpython-312/vllm 312/vllm/model_executor/layers/quantization copying vllm/model_executor/layers/quantization/marlin.py -> build/lib.linux-x86_64-cpython-312/vllm/model_executor/layers/quantizati...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: bdist.linux-x86_64/egg running install_lib running build_py copying vllm/block.py -> build/lib.linux-x86_64-cpython-312/vllm copying vllm/commit_id.py -> build/lib.linux-x86_64-cpython-312/vllm copying vllm/config.py ->...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
