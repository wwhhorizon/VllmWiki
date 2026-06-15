# vllm-project/vllm#807: No CUDA GPUs are available

| 字段 | 值 |
| --- | --- |
| Issue | [#807](https://github.com/vllm-project/vllm/issues/807) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> No CUDA GPUs are available

### Issue 正文摘录

We are planning to deploy the vLLM using the docker image. Please find below the code for docker image ``` ARG base=nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04 ARG commit=main FROM ${base} ENV DEBIAN_FRONTEND=noninteractive LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 ARG CONDA_VERSION=py310_23.3.1-0 RUN apt update && \ apt install -y --no-install-recommends \ wget \ git \ build-essential \ ca-certificates && \ rm -rf /var/lib/apt/lists/* RUN set -x && \ UNAME_M="$(uname -m)" && \ if [ "${UNAME_M}" = "x86_64" ]; then \ MINICONDA_URL="[https://repo.anaconda.com/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh](https://repo.anaconda.com/miniconda/Miniconda3-$%7BCONDA_VERSION%7D-Linux-x86_64.sh)"; \ SHA256SUM="aef279d6baea7f67940f16aad17ebe5f6aac97487c7c03466ff01f4819e5a651"; \ elif [ "${UNAME_M}" = "s390x" ]; then \ MINICONDA_URL="[https://repo.anaconda.com/miniconda/Miniconda3-${CONDA_VERSION}-Linux-s390x.sh](https://repo.anaconda.com/miniconda/Miniconda3-$%7BCONDA_VERSION%7D-Linux-s390x.sh)"; \ SHA256SUM="ed4f51afc967e921ff5721151f567a4c43c4288ac93ec2393c6238b8c4891de8"; \ elif [ "${UNAME_M}" = "aarch64" ]; then \ MINICONDA_URL="[https://repo.anaconda.com/miniconda/Miniconda3-${CONDA_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: No CUDA GPUs are available We are planning to deploy the vLLM using the docker image. Please find below the code for docker image ``` ARG base=nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04 ARG commit=main FROM ${base} ENV...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: No CUDA GPUs are available We are planning to deploy the vLLM using the docker image. Please find below the code for docker image ``` ARG base=nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04 ARG commit=main FROM ${base} EN
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: SHA256SUM} miniconda.sh" > shasum && \ if [ "${CONDA_VERSION}" != "latest" ]; then sha256sum --check --status shasum; fi && \ mkdir -p /opt && \ bash miniconda.sh -b -p /opt/conda && \ rm miniconda.sh shasum && \ ln -s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
