# vllm-project/vllm#30959: [Installation]: AssertionError: CUDA_HOME is not set

| 字段 | 值 |
| --- | --- |
| Issue | [#30959](https://github.com/vllm-project/vllm/issues/30959) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: AssertionError: CUDA_HOME is not set

### Issue 正文摘录

### Your current environment Hi, I am trying to build a docker image for `vllm==0.12.0` and I am unable to build because the setup fails with `AssertionError: CUDA_HOME is not set` and there is a numpy error as well in the logs. I tried the chatbot, downgraded dumpy but it does not work. The same dockerfile if I try and install `v0.11.2` it works. Could I get some help with this issue? ``` STEP 14/19: RUN pip install "numpy 873ebe309fa0 STEP 15/19: RUN pip install --no-cache-dir -U vllm==0.12.0 torch Collecting vllm==0.12.0 Downloading https://www.artifactrepository.net/artifactory/vllm-0.12.0.tar.gz (17.6 MB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.6/17.6 MB 46.0 MB/s 0:00:00 Installing build dependencies: started Installing build dependencies: still running... Installing build dependencies: still running... Installing build dependencies: still running... Installing build dependencies: still running... Installing build dependencies: still running... Installing build dependencies: finished with status 'done' Getting requirements to build wheel: started Getting requirements to build wheel: finished with status 'error' error: subprocess-exited-with-error × Getting requirements t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: AssertionError: CUDA_HOME is not set installation ### Your current environment Hi, I am trying to build a docker image for `vllm==0.12.0` and I am unable to build because the setup fails with `AssertionE
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: AssertionError: CUDA_HOME is not set installation ### Your current environment Hi, I am trying to build a docker image for `vllm==0.12.0` and I am unable to build because the setup fails with `AssertionE...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cc python3.12-devel sudo make bison --nobest RUN yum install -y gcc-toolset-12-runtime gcc-toolset-12-binutils --nobest --skip-broken RUN yum install -y gcc-toolset-12-gcc --nobest --skip-broken # downgraded per the sug...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s/_in_process.py", line 143, in get_requires_for_build_wheel return hook(config_settings) ^^^^^^^^^^^^^^^^^^^^^ File "/tmp/pip-build-env-sqh5u9zl/overlay/lib/python3.12/site-packages/setuptools/build_meta.py", line 331,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: installing vllm ``` FROM docker-enterprise/redhat-python-rhel8/e3.12:latest ARG PYTHON_VERSION=3.12 WORKDIR /srv/ COPY --chmod=777 . /srv/ ENV PIP_CONFIG_FILE=pip.conf RUN sed -i "s/USERNAME/$ARTIFACTORY_USERNAME/g;s/PA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
