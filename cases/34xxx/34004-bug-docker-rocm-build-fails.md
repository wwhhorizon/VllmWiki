# vllm-project/vllm#34004: [Bug]: docker ROCm build fails

| 字段 | 值 |
| --- | --- |
| Issue | [#34004](https://github.com/vllm-project/vllm/issues/34004) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: docker ROCm build fails

### Issue 正文摘录

### Your current environment Irrelevant because it's inside docker, not on my host. I'm building the docker container. ### 🐛 Describe the bug I followed this description: https://docs.vllm.ai/en/v0.6.5/getting_started/amd-installation.html I went for option 1 and i'm meeting the criteria exactly. I do have a AMD 7900XT so i did went for this docker build line: `DOCKER_BUILDKIT=1 docker build --build-arg BUILD_FA="0" -f Dockerfile.rocm -t vllm-rocm .` As per the suggestions. _Sidenote_ the paths to that rocm docker file apparently changes from the official documentation. It points to `https://github.com/vllm-project/vllm/blob/main/Dockerfile.rocm` which doesn't exist anymore. I went for `https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm` This is the command output: ``` > DOCKER_BUILDKIT=1 docker build --build-arg BUILD_FA="0" -f Dockerfile.rocm -t vllm-rocm . [+] Building 242.2s (14/31) docker:default => [internal] load build definition from Dockerfile.rocm 0.1s => => transferring dockerfile: 15.87kB 0.0s => [internal] load metadata for docker.io/rocm/vllm-dev:base 1.7s => [internal] load .dockerignore 0.0s => => transferring context: 2B 0.0s => [internal] load...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: docker ROCm build fails bug;rocm ### Your current environment Irrelevant because it's inside docker, not on my host. I'm building the docker container. ### 🐛 Describe the bug I followed this description: https://...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: docker ROCm build fails bug;rocm ### Your current environment Irrelevant because it's inside docker, not on my host. I'm building the docker container. ### 🐛 Describe the bug I followed this description: https://...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0.4s => => sha256:e2faa4da11d52149f9cd5affa3aa1deed079e090e736edd5c3288f9bbe66e44d 93B / 93B 0.6s => => sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 32B / 32B
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.0s => [internal] load metadata for docker.io/rocm/vllm-dev:base 1.7s => [internal] load .dockerignore
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
