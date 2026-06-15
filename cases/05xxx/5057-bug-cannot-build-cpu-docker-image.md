# vllm-project/vllm#5057: [Bug]: Cannot build cpu docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#5057](https://github.com/vllm-project/vllm/issues/5057) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Cannot build cpu docker image

### Issue 正文摘录

### Your current environment Docker -- not relevant ### 🐛 Describe the bug Following the quick start instructions at ["Installation with CPU"](https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html) ``` vllm$ sudo docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . [+] Building 2.0s (10/12) docker:default => [internal] load build definition from Dockerfile.cpu 0.0s => => transferring dockerfile: 724B 0.0s => [internal] load metadata for docker.io/library/ubuntu:22.04 1.1s => [internal] load .dockerignore 0.0s => => transferring context: 2B 0.0s => [1/8] FROM docker.io/library/ubuntu:22.04@sha256:a6d2b38300ce017add71440577d5b0a90460d0e57fd7aec21dd0d1b0761bbfb2 0.0s => [internal] load build context 0.0s => => transferring context: 36B 0.0s => CACHED [2/8] RUN apt-get update -y && apt-get install -y git wget vim numactl gcc-12 g++-12 python3 python3-pip && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave / 0.0s => CACHED [3/8] RUN pip install --upgrade pip && pip install wheel packaging ninja setuptools>=49.4.0 numpy 0.0s => CACHED [4/8] COPY ./ /workspace/vllm 0.0s => CACHED [5/8] WORKDIR /workspace/vllm 0.0s => ERROR [6/8] RUN pip i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Cannot build cpu docker image bug ### Your current environment Docker -- not relevant ### 🐛 Describe the bug Following the quick start instructions at ["Installation with CPU"](https://docs.vllm.ai/en/latest/gett...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.0s => [internal] load metadata for docker.io/library/ubuntu:22.04 1.1s => [internal] load .dockerig
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tart instructions at ["Installation with CPU"](https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html) ``` vllm$ sudo docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . [+] Building 2.0s (10/12)

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
