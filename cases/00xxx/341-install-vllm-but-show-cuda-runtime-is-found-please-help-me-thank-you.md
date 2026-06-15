# vllm-project/vllm#341: install vllm,but show CUDA runtime is found,please help me,thank you!

| 字段 | 值 |
| --- | --- |
| Issue | [#341](https://github.com/vllm-project/vllm/issues/341) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> install vllm,but show CUDA runtime is found,please help me,thank you!

### Issue 正文摘录

### Discussed in https://github.com/vllm-project/vllm/discussions/329 Originally posted by **dongkuang** July 2, 2023 running build_py running build_ext No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda-11.8' Traceback (most recent call last): File "/tmp/pip-build-env-1bv509_l/overlay/lib/python3.8/site-packages/setuptools/command/editable_wheel.py", line 155, in run self._create_wheel_file(bdist_wheel) File "/tmp/pip-build-env-1bv509_l/overlay/lib/python3.8/site-packages/setuptools/command/editable_wheel.py", line 344, in _create_wheel_file files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp) File "/tmp/pip-build-env-1bv509_l/overlay/lib/python3.8/site-packages/setuptools/command/editable_wheel.py", line 267, in _run_build_commands self._run_build_subcommands() File "/tmp/pip-build-env-1bv509_l/overlay/lib/python3.8/site-packages/setuptools/command/editable_wheel.py", line 294, in _run_build_subcommands self.run_command(name) File "/tmp/pip-build-env-1bv509_l/overlay/lib/python3.8/site-packages/setuptools/_distutils/cmd.py", line 318, in run_command self.distribution.run_command(command) File "/tmp/pip-build-env-1bv509_l/overlay/lib/python3.8/site-pac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: install vllm,but show CUDA runtime is found,please help me,thank you! installation ### Discussed in https://github.com/vllm-project/vllm/discussions/329 Originally posted by **dongkuang** July 2, 2023 running buil
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: install vllm,but show CUDA runtime is found,please help me,thank you! installation ### Discussed in https://github.com/vllm-project/vllm/discussions/329 Originally posted by **dongkuang** July 2, 2023 running build_py r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tools/command/editable_wheel.py", line 344, in _create_wheel_file files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp) File "/tmp/pip-build-env-1bv509_l/overlay/lib/python3.8/site-packages/setuptools...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
