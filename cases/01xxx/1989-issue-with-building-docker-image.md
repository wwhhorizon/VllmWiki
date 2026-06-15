# vllm-project/vllm#1989: Issue with building Docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#1989](https://github.com/vllm-project/vllm/issues/1989) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Issue with building Docker image

### Issue 正文摘录

```DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai --build-arg max_jobs=8``` Outputs: ``` [+] Building 44.7s (27/29) docker:desktop-linux => [internal] load .dockerignore 0.0s => => transferring context: 2B 0.0s => [internal] load build definition from Dockerfile 0.0s => => transferring dockerfile: 2.21kB 0.0s => [internal] load metadata for docker.io/nvidia/cuda:12.1.0-base-ubuntu22.04 1.4s => [internal] load metadata for docker.io/nvidia/cuda:12.1.0-devel-ubuntu22.04 1.4s => [auth] nvidia/cuda:pull token for registry-1.docker.io 0.0s => [dev 1/7] FROM docker.io/nvidia/cuda:12.1.0-devel-ubuntu22.04@sha256:e3a8f7b933e77ecee74731198a2a5483e965b585cea2660675cf4bb152237e9b 0.0s => [internal] load build context 0.0s => => transferring context: 785.55kB 0.0s => [vllm-base 1/5] FROM docker.io/nvidia/cuda:12.1.0-base-ubuntu22.04@sha256:40042016a816cbbe0504dd0a396e7cfc036a8aa43f5694af60dd6f8f87d24e52 0.0s => CACHED [dev 2/7] RUN apt-get update -y && apt-get install -y python3-pip 0.0s => CACHED [dev 3/7] WORKDIR /workspace 0.0s => [dev 4/7] COPY requirements.txt requirements.txt 0.0s => CACHED [vllm-base 2/5] RUN apt-get update -y && apt-get install -y python3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Issue with building Docker image ```DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai --build-arg max_jobs=8``` Outputs: ``` [+] Building 44.7s (27/29)
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0.0s => [internal] load metadata for docker.io/nvidia/cuda:12.1.0-base-ubuntu22.04 1.4s => [internal] load metadata for docker.io/nvidia/cuda:12.1.0-devel-ubuntu22.04
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.0s => [internal] load metadata for docker.io/nvidia/cuda:12.1.0-base-ubuntu22.04 1.4s => [internal] load metadata for docker.io/nvidia/cuda:12.1.0-devel-ubuntu22.04
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: setup.py build_ext --inplace 36 | 37 | # image to run unit testing suite -------------------- ERROR: failed to solve: process "/bin/sh -c python3 setup.py build_ext --inplace" did not complete successfully: exit code: 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
