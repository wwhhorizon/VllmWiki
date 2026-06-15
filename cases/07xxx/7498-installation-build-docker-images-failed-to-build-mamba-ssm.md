# vllm-project/vllm#7498: [Installation]: build docker images: Failed to build mamba-ssm

| 字段 | 值 |
| --- | --- |
| Issue | [#7498](https://github.com/vllm-project/vllm/issues/7498) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: build docker images: Failed to build mamba-ssm

### Issue 正文摘录

### Your current environment ``` => ERROR [mamba-builder 3/3] RUN pip --verbose wheel -r requirements-mamba.txt --no-build-isolation --no-deps --no-cache-dir 909.8s ------ > [mamba-builder 3/3] RUN pip --verbose wheel -r requirements-mamba.txt --no-build-isolation --no-deps --no-cache-dir: 1.518 Collecting mamba-ssm>=1.2.2 (from -r requirements-mamba.txt (line 2)) 1.776 Downloading mamba_ssm-2.2.2.tar.gz (85 kB) 1.904 Preparing metadata (setup.py): started 1.904 Running command python setup.py egg_info 4.070 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' 4.146 4.146 4.147 torch.__version__ = 2.4.0+cu121 4.147 4.148 4.149 running egg_info 4.149 creating /tmp/pip-pip-egg-info-d2_c2trw/mamba_ssm.egg-info 4.154 writing /tmp/pip-pip-egg-info-d2_c2trw/mamba_ssm.egg-info/PKG-INFO 4.154 writing dependency_links to /tmp/pip-pip-egg-info-d2_c2trw/mamba_ssm.egg-info/dependency_links.txt 4.155 writing requirements to /tmp/pip-pip-egg-info-d2_c2trw/mamba_ssm.egg-info/requires.txt 4.156 writing top-level names to /tmp/pip-pip-egg-info-d2_c2trw/mamba_ssm.egg-info/top_level.txt 4.156 writing manifest file '/tmp/pip-pip-egg-info-d2_c2trw/mamba_ssm.egg-info/SOURCES.txt' 4.250 reading m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: build docker images: Failed to build mamba-ssm installation ### Your current environment ``` => ERROR [mamba-builder 3/3] RUN pip --verbose wheel -r requirements-mamba.txt --no-build-isolation --no-de
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Installation]: build docker images: Failed to build mamba-ssm installation ### Your current environment ``` => ERROR [mamba-builder 3/3] RUN pip --verbose wheel -r requirements-mamba.txt --no-build-isolation --no-deps...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 2)) 1.776 Downloading mamba_ssm-2.2.2.tar.gz (85 kB) 1.904 Preparing metadata (setup.py): started 1.904 Running command python setup.py egg_info 4.070 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' 4.146 4....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
