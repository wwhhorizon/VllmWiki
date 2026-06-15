# vllm-project/vllm#20345: [Usage]: I cannot compile vllm on RTX5090

| 字段 | 值 |
| --- | --- |
| Issue | [#20345](https://github.com/vllm-project/vllm/issues/20345) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: I cannot compile vllm on RTX5090

### Issue 正文摘录

### Your current environment 我的服务器配置是ubuntu20，conda使用的环境是python 3.12，我的安装命令如下： ```text git clone https://github.com/vllm-project/vllm.git cd vllm git checkout v0.8.3 python use_existing_torch.py pip install -r requirements/build.txt pip install setuptools_scm ``` 但是他却报错了： ```text /home/pc/data/envs/vllmlast/lib/python3.12/site-packages/setuptools/_distutils/dist.py:1021: _DebuggingTips: Problem in editable installation. !! ******************************************************************************** An error happened while installing `vllm` in editable mode. The following steps are recommended to help debug this problem: - Try to install the project normally, without using the editable mode. Does the error still persist? (If it does, try fixing the problem before attempting the editable mode). - If you are using binary extensions, make sure you have all OS-level dependencies installed (e.g. compilers, toolchains, binary libraries, ...). - Try the latest version of setuptools (maybe the error was already fixed). - If you (or your project dependencies) are using any setuptools extension or customization, make sure they support the editable mode. After following the steps above, i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Usage]: I cannot compile vllm on RTX5090 usage;stale ### Your current environment 我的服务器配置是ubuntu20，conda使用的环境是python 3.12，我的安装命令如下： ```text git clone https://github.com/vllm-project/vllm.git cd vllm git checkout v0.8.3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: I cannot compile vllm on RTX5090 usage;stale ### Your current environment 我的服务器配置是ubuntu20，conda使用的环境是python 3.12，我的安装命令如下： ```text git clone https://github.com/vllm-project/vllm.git cd vllm git checkout v0.8.3...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 3, in build_editable return hook(wheel_directory, config_settings, metadata_directory) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/pc/data/envs/vllmlast/lib/python3.12/site-packages/setuptools...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cess.py", line 303, in build_editable return hook(wheel_directory, config_settings, metadata_directory) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/pc/data/envs/vllmlast/lib/python3.12/site-pa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: how setuptools handles editable installations, please submit a reproducible example (see https://stackoverflow.com/help/minimal-reproducible-example) to: https://github.com/pypa/setuptools/issues See https://setuptools....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
