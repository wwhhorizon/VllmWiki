# vllm-project/vllm#31035: [Bug]: ROCm docker image failed to build

| 字段 | 值 |
| --- | --- |
| Issue | [#31035](https://github.com/vllm-project/vllm/issues/31035) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ROCm docker image failed to build

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to build the vllm docker image to support a Radeon RX 7800 XT. ``` katharta@calibarn:/opt/llm/git $ git clone https://github.com/vllm-project/vllm.git Cloning into 'vllm'... remote: Enumerating objects: 153377, done. remote: Counting objects: 100% (38/38), done. remote: Compressing objects: 100% (35/35), done. remote: Total 153377 (delta 15), reused 6 (delta 3), pack-reused 153339 (from 3) Receiving objects: 100% (153377/153377), 128.99 MiB | 48.15 MiB/s, done. Resolving deltas: 100% (120921/120921), done. katharta@calibarn:/opt/llm/git $ cd vllm katharta@calibarn:/opt/llm/git/vllm $ echo "DOCKER_BUILDKIT=1 docker build -f ./docker/Dockerfile.rocm -t vllm-rocm:v0 --build-arg ARG_PYTORCH_ROCM_ARCH=gfx1101 /opt/llm/images/vllm-rocm" > build katharta@calibarn:/opt/llm/git/vllm $ bash build [+] Building 1.2s (15/27) docker:default => [internal] load build definition from Dockerfile.rocm 0.0s => => transferring dockerfile: 5.46kB 0.0s => [internal] load metadata for docker.io/rocm/vllm-dev:base 0.0s => [internal] load .dockerignore 0.0s => => transferring context: 2B 0.0s => [internal] load build context 0.0s => => transfe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: ROCm docker image failed to build bug;rocm ### Your current environment ### 🐛 Describe the bug I am trying to build the vllm docker image to support a Radeon RX 7800 XT. ``` katharta@calibarn:/opt/llm/git $ git c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: ROCm docker image failed to build bug;rocm ### Your current environment ### 🐛 Describe the bug I am trying to build the vllm docker image to support a Radeon RX 7800 XT. ``` katharta@calibarn:/opt/llm/git $ git c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: =type=cache,target=/root/.cache/uv uv pip install --system --upgrade huggingface-hub[cli] 0.8s => CACHED [fetch_vllm 1/1] ONBUILD COPY ./ vllm/
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: >=24.2 setuptools>=77.0.3, =8 runai-model-streamer[s3,gcs]==0.15.3 conch-triton-kernels==1.2.1 timm>=1.0.17 fastsafetensors @ git+https://github.com/foundation-model-stack/fastsafetensors.git@d6f998a03432b2452f8de2bb5ce...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 0.0s => [internal] load metadata for docker.io/rocm/vllm-dev:base 0.0s => [internal] load .dockeri

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
