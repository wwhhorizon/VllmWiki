# vllm-project/vllm#4360: [Installation]: GitHub access required during install for vllm >=0.4.1 (for cu12-libnccl.so.2.18.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#4360](https://github.com/vllm-project/vllm/issues/4360) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: GitHub access required during install for vllm >=0.4.1 (for cu12-libnccl.so.2.18.1)

### Issue 正文摘录

### Your current environment Current environment has no internet access. Using a local pypi mirror to install packages. Using the CUDA version of vllm on an Nvidia A10. ### How you are installing vllm Using a local pypi mirror to install packages in an environment without internet access. The following works: ```sh pip install -vvv vllm==0.4.0.post1 ``` The following does not work: ```sh pip install -vvv vllm==0.4.1 ``` ```sh Running setup.py (path:/tmp/pip-install-wot5g_wr/vllm-nccl-cu12_7614e24f467d4cef9205802e1b0b89cb/setup.py) egg_info for package vllm-nccl-cu12 Created temporary directory: /tmp/pip-pip-egg-info-lwr60hk0 Running command python setup.py egg_info Traceback (most recent call last): File " ", line 2, in File " ", line 34, in File "/tmp/pip-install-wot5g_wr/vllm-nccl-cu12_7614e24f467d4cef9205802e1b0b89cb/setup.py", line 83, in if get_md5_hash(destination) != file_hash: ^^^^^^^^^^^^^^^^^^^^^^^^^ File "/tmp/pip-install-wot5g_wr/vllm-nccl-cu12_7614e24f467d4cef9205802e1b0b89cb/setup.py", line 43, in get_md5_hash with open(file_path, "rb") as f: # Open file in binary read mode ^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: ' /.config/vllm/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: GitHub access required during install for vllm >=0.4.1 (for cu12-libnccl.so.2.18.1) installation ### Your current environment Current environment has no internet access. Using a local pypi mirror to insta
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nternet access. Using a local pypi mirror to install packages. Using the CUDA version of vllm on an Nvidia A10. ### How you are installing vllm Using a local pypi mirror to install packages in an environment without int...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: ' /.config/vllm/nccl/cu12/libnccl.so.2.18.1' Downloading nccl package from https://github.com/vllm-project/vllm-nccl/releases/download/v0.1.0/cu12-libnc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
