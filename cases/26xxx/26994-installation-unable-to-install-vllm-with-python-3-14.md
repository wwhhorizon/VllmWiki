# vllm-project/vllm#26994: [Installation]: Unable to Install vllm with python 3.14

| 字段 | 值 |
| --- | --- |
| Issue | [#26994](https://github.com/vllm-project/vllm/issues/26994) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Unable to Install vllm with python 3.14

### Issue 正文摘录

### Your current environment Hi, vllm installation is getting stucked due to "numba" package. ```sh Collecting numba==0.61 (from vllm) Using cached numba-0.61.0.tar.gz (2.8 MB) Preparing metadata (setup.py) ... error error: subprocess-exited-with-error ▒ python setup.py egg_info did not run successfully. ▒ exit code: 1 ▒▒> [18 lines of output] Traceback (most recent call last): File " ", line 2, in exec(compile(''' ~~~~^^^^^^^^^^^^ # This is -- a caller that pip uses to run setup.py ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ... ... exec(compile(setup_py_code, filename, "exec")) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ''' % ('/tmp/pip-install-67eioooo/numba_1f494ef99f254895b4ed3a8e0621bb4d/setup.py',), " ", "ex ec")) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^ File " ", line 35, in File "/tmp/pip-install-67eioooo/numba_1f494ef99f254895b4ed3a8e0621bb4d/setup.py", line 51, in _guard_py_ver() ~~~~~~~~~~~~~^^ File "/tmp/pip-install-67eioooo/numba_1f494ef99f254895b4ed3a8e0621bb4d/setup.py", line 48, in _guard_py_ver raise RuntimeError(msg.format(cur_py, min_py, max_py)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Unable to Install vllm with python 3.14 installation;stale ### Your current environment Hi, vllm installation is getting stucked due to "numba" package. ```sh Collecting numba==0.61 (from vllm) Using
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.61 (from vllm) Using cached numba-0.61.0.tar.gz (2.8 MB) Preparing metadata (setup.py) ... error error: subprocess-exited-with-error ▒ python setup.py egg_info did not run successfully. ▒ exit code: 1 ▒▒> [18 lines of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 4d/setup.py", line 48, in _guard_py_ver raise RuntimeError(msg.format(cur_py, min_py, max_py)) RuntimeError: Cannot install on Python version 3.14.0; only versions >=3.10, See above for output. note: This is an issue wi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Unable to Install vllm with python 3.14 installation;stale ### Your current environment Hi, vllm installation is getting stucked due to "numba" package. ```sh Collecting numba==0.61 (from vllm) Using cac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
