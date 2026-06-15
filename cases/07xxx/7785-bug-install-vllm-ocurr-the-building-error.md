# vllm-project/vllm#7785: [Bug]: install vllm ocurr the building error

| 字段 | 值 |
| --- | --- |
| Issue | [#7785](https://github.com/vllm-project/vllm/issues/7785) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | build_fail |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: install vllm ocurr the building error

### Issue 正文摘录

### Your current environment Building wheels for collected packages: vllm Building wheel for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building wheel for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [71 lines of output] /tmp/pip-build-env-o_ebi3i5/overlay/lib/python3.10/site-packages/torch/_subclasses/functional_tensor.py:258: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.) cpu = _conversion_method_template(device=torch.device("cpu")) fatal: not a git repository (or any of the parent directories): .git :56: RuntimeWarning: Failed to get commit hash: Command '['git', 'rev-parse', 'HEAD']' returned non-zero exit status 128. running bdist_wheel running build running build_py running build_ext CMake Error at CMakeLists.txt:3 (project): Running '/tmp/pip-build-env-bxpa0h4m/overlay/bin/ninja' '--version' failed with: no such file or directory -- Configuring incomplete, errors occurred! Traceback (most recent call last): File "/home/dj/anaconda3/envs/vllm/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in mai...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: install vllm ocurr the building error bug ### Your current environment Building wheels for collected packages: vllm Building wheel for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Build
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: RECTORY=/home/dj/vllm/build/lib.linux-x86_64-cpython-310/vllm', '-DCMAKE_ARCHIVE_OUTPUT_DIRECTORY=build/temp.linux-x86_64-cpython-310', '-DVLLM_TARGET_DEVICE=cuda', '-DVLLM_PYTHON_EXECUTABLE=/home/dj/anaconda3/envs/vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rocess/_in_process.py", line 251, in build_wheel return _build_backend().build_wheel(wheel_directory, config_settings, File "/tmp/pip-build-env-o_ebi3i5/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", li...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d with: no such file or directory -- Configuring incomplete, errors occurred! Traceback (most recent call last): File "/home/dj/anaconda3/envs/vllm/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
