# vllm-project/vllm#6916: [Bug]: Unable to build image from `vllm` repo Dockerfile

| 字段 | 值 |
| --- | --- |
| Issue | [#6916](https://github.com/vllm-project/vllm/issues/6916) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to build image from `vllm` repo Dockerfile

### Issue 正文摘录

### Your current environment Not applicable -- Dockerfile. ### 🐛 Describe the bug Steps to reproduce: - Clone the `vllm` repo - run `docker build . --target vllm-base` - Build fails ```shell ❯ docker build . --target vllm-base [+] Building 4.4s (23/51) docker:desktop-linux => [internal] load .dockerignore 0.0s => => transferring context: 50B 0.0s => [internal] load build definition from Dockerfile 0.0s => => transferring dockerfile: 8.97kB 0.0s => [internal] load metadata for docker.io/nvidia/cuda:12.4.1-base-ubuntu20.04 0.8s => [internal] load metadata for docker.io/nvidia/cuda:12.4.1-devel-ubuntu20.04 0.9s => [auth] nvidia/cuda:pull token for registry-1.docker.io 0.0s => [internal] load build context 0.0s => => transferring context: 31.49kB 0.0s => [base 1/13] FROM docker.io/nvidia/cuda:12.4.1-devel-ubuntu20.04@sha256:8d577fd078ae56c37493af4454a5b700c72a7f1aeb9ff3d0adc0459fc 0.0s => [vllm-base 1/10] FROM docker.io/nvidia/cuda:12.4.1-base-ubuntu20.04@sha256:6fdb33fd81a5e214cfff44685aa32e3ab085c4ac506c2bd987c74 0.0s => CACHED [vllm-base 2/10] WORKDIR /vllm-workspace 0.0s => CACHED [vllm-base 3/10] RUN echo 'tzdata tzdata/Areas select America' | debconf-set-selections && echo 'tzda...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Unable to build image from `vllm` repo Dockerfile bug;stale ### Your current environment Not applicable -- Dockerfile. ### 🐛 Describe the bug Steps to reproduce: - Clone the `vllm` repo - run `docker build . --ta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0.0s => [internal] load metadata for docker.io/nvidia/cuda:12.4.1-base-ubuntu20.04 0.8s => [internal] load metadata for docker.io/nvidia/cuda:12.4.1-devel-ubuntu20.04
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 0.0s => CACHED [vllm-base 7/10] RUN ldconfig /usr/local/cuda-$(echo 12.4.1 | cut -d. -f1,2)/compat/ 0.0s => CACHED [base 2/13] RUN echo 'tzdata tzdata/Areas select America' | debconf-set-selections && echo 'tzdata
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ronment Not applicable -- Dockerfile. ### 🐛 Describe the bug Steps to reproduce: - Clone the `vllm` repo - run `docker build . --target vllm-base` - Build fails ```shell ❯ docker build . --target vllm-base [+] Building...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.0s => [internal] load metadata for docker.io/nvidia/cuda:12.4.1-base-ubuntu20.04 0.8s => [internal] load metadata for docker.io/nvidia/cuda:12.4.1-devel-ubuntu20.04

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
