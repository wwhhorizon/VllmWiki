# vllm-project/vllm#3986: [Installation]: python setup.py develop is broken due to vllm-nccl

| 字段 | 值 |
| --- | --- |
| Issue | [#3986](https://github.com/vllm-project/vllm/issues/3986) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: python setup.py develop is broken due to vllm-nccl

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh python setup.py develop ``` Running vllm_nccl_cu12-2.18.1.0.2.0/setup.py -vv bdist_egg --dist-dir /tmp/easy_install-swnt_7mn/vllm_nccl_cu12-2.18.1.0.2.0/egg-dist-tmp-5nhikqct error: SandboxViolation: mkdir('/home/paperspace/.config/vllm', 511) {} The package setup script has attempted to modify files on your system that are not within the EasyInstall build area, and has been aborted. This package cannot be safely installed by EasyInstall, and may not support alternate installation locations even if you run its setup script by hand. Please inform the package's author and the EasyInstall maintainers to find out if a fix or workaround is available. So the problem is, when we use `vllm-nccl` to manage nccl version, we try to install `/home/paperspace/.config/vllm/nccl/cu12/libnccl.so` , but `python setup.py develop` will use a sandbox installation. Essentially we forbid the way of `python setup.py develop`. Fortunately, `pip install -e .` still works. Do we need to delete the section of `python setup.py develop` in the doc? cc @simon-mo @WoosukKwon @zhuohan123

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: python setup.py develop is broken due to vllm-nccl installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh python setup.py devel
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /egg-dist-tmp-5nhikqct error: SandboxViolation: mkdir('/home/paperspace/.config/vllm', 511) {} The package setup script has attempted to modify files on your system that are not within the EasyInstall build area, and ha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
