# vllm-project/vllm#1922: 0.2.3 sdist has inconsistent metadata according to pip

| 字段 | 值 |
| --- | --- |
| Issue | [#1922](https://github.com/vllm-project/vllm/issues/1922) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> 0.2.3 sdist has inconsistent metadata according to pip

### Issue 正文摘录

Trying to collect 0.2.3, pip errors with : `0.2.3.tar.gz has inconsistent version: expected '0.2.3', but metadata has '0.2.3+cu122'` ``` Discarding https://files.pythonhosted.org/packages/3c/57/df0399f26c2b6cc4e54417e756b32536429c5da18054e3a82d7904cbeccf/vllm-0.2.3.tar.gz (from https://pypi.org/simple/vllm/) (requires-python:>=3.8): Requested vllm==0.2.3 from https://files.pythonhosted.org/packages/3c/57/df0399f26c2b6cc4e54417e756b32536429c5da18054e3a82d7904cbeccf/vllm-0.2.3.tar.gz has inconsistent version: expected '0.2.3', but metadata has '0.2.3+cu122' ``` Not sure where pip sees `0.2.3+cu122` but I'll use the sources from Github instead of the one on PyPI. Can be reproduced with ``` (30815) wheels_builder (main *) 2023 $ pip download -v --no-cache --no-binary vllm --no-build-isolation --no-deps vllm==0.2.3 Looking in links: /cvmfs/soft.computecanada.ca/custom/python/wheelhouse/gentoo2023/x86-64-v3, /cvmfs/soft.computecanada.ca/custom/python/wheelhouse/gentoo2023/generic, /cvmfs/soft.computecanada.ca/custom/python/wheelhouse/generic Collecting vllm==0.2.3 File was already downloaded /home/coulombc/wheels_builder/vllm-0.2.3.tar.gz Running command Preparing metadata (pyproject.to...

## 现有链接修复摘要

#1923 Added support for BUILD_VERSION env variable. Allow one to set build …

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rying to collect 0.2.3, pip errors with : `0.2.3.tar.gz has inconsistent version: expected '0.2.3', but metadata has '0.2.3+cu122'` ``` Discarding https://files.pythonhosted.org/packages/3c/57/df0399f26c2b6cc4e54417e756...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: but I'll use the sources from Github instead of the one on PyPI. Can be reproduced with ``` (30815) wheels_builder (main *) 2023 $ pip download -v --no-cache --no-binary vllm --no-build-isolation --no-deps vllm==0.2.3 L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: -0.2.3.tar.gz Running command Preparing metadata (pyproject.toml) No CUDA runtime is found, using CUDA_HOME='/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v3/Core/cudacore/12.2.2' /home/coulombc/.envs/3081...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.2.3 sdist has inconsistent metadata according to pip Trying to collect 0.2.3, pip errors with : `0.2.3.tar.gz has inconsistent version: expected '0.2.3', but metadata has '0.2.3+cu122'` ``` Discarding https://files.py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: itialize NVML") running dist_info creating /tmp/pip-modern-metadata-yhfgt7ut/vllm.egg-info writing /tmp/pip-modern-metadata-yhfgt7ut/vllm.egg-info/PKG-INFO writing dependency_links to /tmp/pip-modern-metadata-yhfgt7ut/v...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#1923](https://github.com/vllm-project/vllm/pull/1923) | closes_keyword | 0.95 | Added support for BUILD_VERSION env variable. Allow one to set build … | Fixes #1922 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
