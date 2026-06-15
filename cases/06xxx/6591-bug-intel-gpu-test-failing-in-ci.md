# vllm-project/vllm#6591: [Bug]: Intel GPU Test failing in CI

| 字段 | 值 |
| --- | --- |
| Issue | [#6591](https://github.com/vllm-project/vllm/issues/6591) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Intel GPU Test failing in CI

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug All CI builds are failing due to the Intel GPU Test failing (see log below) Can we fix or "soft fail" it? ``` bash .buildkite/run-xpu-test.sh -- | + docker build -t xpu-test -f Dockerfile.xpu . | [+] Building 2.5s (6/11) docker:default | => [internal] load build definition from Dockerfile.xpu 0.0s | => => transferring dockerfile: 1.26kB 0.0s | => [internal] load metadata for docker.io/intel/oneapi-basekit:2024.1.0-devel-ubuntu20.04 0.3s | => [internal] load .dockerignore 0.0s | => => transferring context: 50B 0.0s | => CACHED [1/7] FROM docker.io/intel/oneapi-basekit:2024.1.0-devel-ubuntu20.04@sha256:6adb5e03caac52ed86bc58163647d4a02e8c9220764ea5f0555aa72f63d86d13 0.0s | => [internal] load build context 0.1s | => => transferring context: 959.30kB 0.1s | => ERROR [2/7] RUN wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB \| gpg --dearmor \| tee /usr/share/keyrings/intel 2.2s | ------ | > [2/7] RUN wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB \| gpg --dearmor \| tee /usr/share/keyrings/intel-oneapi-archive...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Intel GPU Test failing in CI bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug All CI builds are failing due to the Intel GPU Test failing (see log be...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Intel GPU Test failing in CI bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug All CI builds are failing due to the Intel GPU Test failing (see log be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: SW-PRODUCTS.PUB \| gpg --dearmor \| tee /usr/share/keyrings/intel-oneapi-archive-keyring.gpg > /dev/null && echo "deb [signed-by=/usr/share/keyrings/intel-oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.0s | => [internal] load metadata for docker.io/intel/oneapi-basekit:2024.1.0-devel-ubuntu20.04 0.3s | => [internal] load .dockerignore
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Intel GPU Test failing in CI bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug All CI builds are failing due to the Intel GPU Test failing (see log be...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
