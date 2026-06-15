# vllm-project/vllm#13048: [Installation]: There is an error installing vllm from Git source.

| 字段 | 值 |
| --- | --- |
| Issue | [#13048](https://github.com/vllm-project/vllm/issues/13048) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: There is an error installing vllm from Git source.

### Issue 正文摘录

### Your current environment ```text Ubuntu 24.04 LTS (6.8.0-41-generic) ROCM 6.3.0 Dual GPUs AMD Radeon 7900XTX ``` There is an error installing vllm from Git source. I have tested many Vllm releases, usually never had any problems. But today a strange error occurred. Vllm does not install. ### How you are installing vllm ```sh git clone https://github.com/vllm-project/vllm.git cd vllm DOCKER_BUILDKIT=1 docker build --build-arg BASE_IMAGE="rocm/vllm-dev:navi_nightly" -f Dockerfile.rocm -t vllm-rocm . [+] Building 135.3s (22/24) docker:default => [internal] load build definition from Dockerfile.rocm 0.0s => => transferring dockerfile: 3.95kB 0.0s => [internal] load metadata for docker.io/rocm/vllm-dev:navi_base 0.5s => [internal] load .dockerignore 0.0s => => transferring context: 387B 0.0s => [base 1/5] FROM docker.io/rocm/vllm-dev:navi_base@sha256:65ec84298875a6024988f5698101952ac822d73ad0cbcb0f7e1ac9b8b8d0a168 0.0s => [internal] load build context 0.1s => => transferring context: 129.90kB 0.1s => CACHED [base 2/5] RUN apt-get update -q -y && apt-get install -q -y sqlite3 libsqlite3-dev libfmt-dev libmsgpack-dev libsuitesparse-dev 0.0s => CACHED [base 3/5] RUN python3 -m pip ins...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: There is an error installing vllm from Git source. installation ### Your current environment ```text Ubuntu 24.04 LTS (6.8.0-41-generic) ROCM 6.3.0 Dual GPUs AMD Radeon 7900XTX ``` There is an error insta
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ## Your current environment ```text Ubuntu 24.04 LTS (6.8.0-41-generic) ROCM 6.3.0 Dual GPUs AMD Radeon 7900XTX ``` There is an error installing vllm from Git source. I have tested many Vllm releases, usually never had...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: on 7900XTX ``` There is an error installing vllm from Git source. I have tested many Vllm releases, usually never had any problems. But today a strange error occurred. Vllm does not install. ### How you are installing v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.0s => [internal] load metadata for docker.io/rocm/vllm-dev:navi_base 0.5s => [internal] load .dockerignore
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .20.3. 0.0s => CACHED [final 3/7] RUN python3 -m pip install --upgrade huggingface-hub[cli] 0.0s => CACHED [final 4/7] RUN if [ 1 -eq "1" ]; then git clone -b nvtx_enabled https://github.com/R

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
