# vllm-project/vllm#18583: [Bug]: v0.9.0 version source code compilation failed！

| 字段 | 值 |
| --- | --- |
| Issue | [#18583](https://github.com/vllm-project/vllm/issues/18583) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.9.0 version source code compilation failed！

### Issue 正文摘录

### Your current environment Currently I need to use version 0.9.0, mainly because it supports torch2.7 for the use of lmcahce modules. But I found that I can only compile the source code, but the source code compilation is not successful! ``` pip install -e . -i https://pypi.tuna.tsinghua.edu.cn/simple Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple Obtaining file:///3rdparty/vllm-0.9.0 Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements to build editable did not run successfully. │ exit code: 1 ╰─> [37 lines of output] /tmp/pip-build-env-gjh6493e/overlay/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:276: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:81.) cpu = _conversion_method_template(device=torch.device("cpu")) /bin/bash: line 1: lsmod: command not found /bin/bash: line 1: lsmod: command not found /bin/bash: line 1: lsmod: command not found Traceback (most recent call last): File "/root/anaconda3/envs/vl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: v0.9.0 version source code compilation failed！ bug ### Your current environment Currently I need to use version 0.9.0, mainly because it supports torch2.7 for the use of lmcahce modules. But I found that I can on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on_method_template(device=torch.device("cpu")) /bin/bash: line 1: lsmod: command not found /bin/bash: line 1: lsmod: command not found /bin/bash: line 1: lsmod: command not found Traceback (most recent call last): File...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: /vllm-0.9.0 Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lls, a git checkout without the .git folder) don't contain the necessary metadata and will not work. For example, if you're using pip, instead of https://github.com/user/proj/archive/master.zip use git+https://github.co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py", line 157, in get_requires_for_build_editable return hook(config_settings) ^^^^^^^^^^^^^^^^^^^^^ File "/tmp/pip-build-env-gjh6493e/overlay/lib/python3.12/site-packages/setuptools/build_meta.py", line 473, in get_re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
