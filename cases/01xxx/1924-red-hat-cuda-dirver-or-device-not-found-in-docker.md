# vllm-project/vllm#1924: Red Hat: CUDA Dirver or Device not Found In Docker

| 字段 | 值 |
| --- | --- |
| Issue | [#1924](https://github.com/vllm-project/vllm/issues/1924) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Red Hat: CUDA Dirver or Device not Found In Docker

### Issue 正文摘录

Issue or feature description systerm: Red Hat Enterprise Linux release 9.3 host cuda driver: Driver Version: 535.113.01 CUDA Version: 12.2 ![image](https://github.com/vllm-project/vllm/assets/87475073/967bc819-3266-4c97-9acb-94716ba06935) **docker version: nvcr.io/nvidia/pytorch 23.08-py3** vllm version: 0.2.2 installed in docker **Problem: I ran an example with vllm and encountered the following problem. cuda driver not detected and nvidia-smi command not found in docker** ![image](https://github.com/vllm-project/vllm/assets/87475073/391f4395-f366-4873-8074-1fe117d55882) ![image](https://github.com/vllm-project/vllm/assets/87475073/615a55e1-8947-48d4-af1c-76e719f23bdb) I have installed the nvidia cuda toolkit according to the official documentation, but it still doesn't work. ``` curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \ sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo sudo yum install -y nvidia-container-toolkit ``` Can anyone help?Thanks.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Red Hat: CUDA Dirver or Device not Found In Docker Issue or feature description systerm: Red Hat Enterprise Linux release 9.3 host cuda driver: Driver Version: 535.113.01 CUDA Version: 12.2 ![image](https://github.com/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Red Hat: CUDA Dirver or Device not Found In Docker Issue or feature description systerm: Red Hat Enterprise Linux release 9.3 host cuda driver: Driver Version: 535.113.01 CUDA Version: 12.2 ![image](https://github.com/v...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
