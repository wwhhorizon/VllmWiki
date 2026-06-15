# vllm-project/vllm#13130: [Installation]: When build the 0.7.2 docker image using the Dockerfile , got "LookupError: setuptools-scm was unable to detect version for /workspace."

| 字段 | 值 |
| --- | --- |
| Issue | [#13130](https://github.com/vllm-project/vllm/issues/13130) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: When build the 0.7.2 docker image using the Dockerfile , got "LookupError: setuptools-scm was unable to detect version for /workspace."

### Issue 正文摘录

### Your current environment ```text #28 [build 6/8] RUN --mount=type=cache,target=/root/.cache/ccache --mount=type=cache,target=/root/.cache/pip --mount=type=bind,source=.git,target=.git if [ "$USE_SCCACHE" != "1" ]; then python3 setup.py bdist_wheel --dist-dir=dist --py-limited-api=cp38; fi #28 sha256:e7f4157cc8455904b3ad15306d1389093b8d6d1074a5c6af28798d765b7829f8 #28 2.876 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' #28 2.883 /bin/sh: 1: lsmod: not found #28 2.889 /bin/sh: 1: lsmod: not found #28 2.898 /bin/sh: 1: lsmod: not found #28 2.930 Traceback (most recent call last): #28 2.930 File "/workspace/setup.py", line 633, in #28 2.930 version=get_vllm_version(), #28 2.930 ^^^^^^^^^^^^^^^^^^ #28 2.930 File "/workspace/setup.py", line 482, in get_vllm_version #28 2.930 version = get_version( #28 2.930 ^^^^^^^^^^^^ #28 2.930 File "/usr/local/lib/python3.12/dist-packages/setuptools_scm/_get_version_impl.py", line 163, in get_version #28 2.930 _version_missing(config) #28 2.930 File "/usr/local/lib/python3.12/dist-packages/setuptools_scm/_get_version_impl.py", line 117, in _version_missing #28 2.930 raise LookupError( #28 2.930 LookupError: setuptools-scm was unable...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: When build the 0.7.2 docker image using the Dockerfile , got "LookupError: setuptools-scm was unable to detect version for /workspace." installation;stale ### Your current environment ```text #28 [build 6
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 57cc8455904b3ad15306d1389093b8d6d1074a5c6af28798d765b7829f8 #28 2.876 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' #28 2.883 /bin/sh: 1: lsmod: not found #28 2.889 /bin/sh: 1: lsmod: not found #28 2.898 /...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lls, a git checkout without the .git folder) don't contain the necessary metadata and will not work. #28 2.930 #28 2.930 For example, if you're using pip, instead of https://github.com/user/proj/archive/master.zip use g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ersion_impl.py", line 163, in get_version #28 2.930 _version_missing(config) #28 2.930 File "/usr/local/lib/python3.12/dist-packages/setuptools_scm/_get_version_impl.py", line 117, in _version_missing #28 2.930 raise Lo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: etuptools-scm was unable to detect version for /workspace." installation;stale ### Your current environment ```text #28 [build 6/8] RUN --mount=type=cache,target=/root/.cache/ccache --mount=type=cache,target=/root/.cach...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
