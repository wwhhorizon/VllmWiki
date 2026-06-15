# vllm-project/vllm#3673: [Installation]:  LIBNVTOOLSEXT not set during installation from source

| 字段 | 值 |
| --- | --- |
| Issue | [#3673](https://github.com/vllm-project/vllm/issues/3673) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]:  LIBNVTOOLSEXT not set during installation from source

### Issue 正文摘录

### Your current environment A fresh new installation in a conda environment will cause `LIBNVTOOLSEXT not set during installation from source` error. The problem is our cmake procedure imports torch cmake, which tries to find many locations that only exist in a full installation of cuda toolkit: ```cmake find_library(LIBNVTOOLSEXT libnvToolsExt.so PATHS ${CUDA_TOOLKIT_ROOT_DIR}/lib64/) ``` We cannot assume users have a full installation of cuda toolkit. Maybe we should write cmake ourselves, and find out the libraries needed by vllm. The minimal procedure users needs to build from source: ```shell $ conda create -n myenv python=3.9 -y $ conda activate myenv $ conda install cuda=12.1 -c nvidia # then we will have `nvcc` under ${CONDA_PREFIX}/bin/nvcc # and cuda-related libraries under ${CONDA_PREFIX}/lib/ , such as libcudart.so $ git clone https://github.com/vllm-project/vllm.git $ cd vllm $ pip install -e . # this will install pytorch, which stores its dependent libraries under ${CONDA_PREFIX}/site-packages/nvidia/{lib_name}/lib/ , typically we don't want to link against these libraries # the library files of pytorch itself is in ${CONDA_PREFIX}/site-packages/torch/lib/ , with he...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: LIBNVTOOLSEXT not set during installation from source installation;stale ### Your current environment A fresh new installation in a conda environment will cause `LIBNVTOOLSEXT not set during installation
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: h tries to find many locations that only exist in a full installation of cuda toolkit: ```cmake find_library(LIBNVTOOLSEXT libnvToolsExt.so PATHS ${CUDA_TOOLKIT_ROOT_DIR}/lib64/) ``` We cannot assume users have a full i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Installation]: LIBNVTOOLSEXT not set during installation from source installation;stale ### Your current environment A fresh new installation in a conda environment will cause `LIBNVTOOLSEXT not set during installation...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: on]: LIBNVTOOLSEXT not set during installation from source installation;stale ### Your current environment A fresh new installation in a conda environment will cause `LIBNVTOOLSEXT not set during installation from sourc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
