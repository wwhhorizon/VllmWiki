# vllm-project/vllm#30628: [Bug]: For building a CUDA 13 vLLM docker image, when building LMCache, wrong version of NIXL (`nixl-cu12`) is downloaded

| 字段 | 值 |
| --- | --- |
| Issue | [#30628](https://github.com/vllm-project/vllm/issues/30628) |
| 状态 | closed |
| 标签 | bug;kv-connector;nvidia |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: For building a CUDA 13 vLLM docker image, when building LMCache, wrong version of NIXL (`nixl-cu12`) is downloaded

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I tried to build a cu130 docker image with the following command: ```bash DOCKER_BUILDKIT=1 docker build \ --pull \ --push \ --build-arg max_jobs=256 \ --build-arg nvcc_threads=2 \ --build-arg RUN_WHEEL_CHECK=false \ --build-arg CUDA_VERSION=13.0.1 \ --build-arg BUILD_BASE_IMAGE=nvidia/cuda:13.0.1-devel-ubuntu22.04 \ --build-arg FLASHINFER_AOT_COMPILE=true \ --build-arg torch_cuda_arch_list='9.0 10.0+PTX' \ --build-arg INSTALL_KV_CONNECTORS=true \ --platform "linux/arm64" \ --tag gitlab-master.nvidia.com:5005/shangw/container-images/vllm-openai:arm64-cuda1301-$(git rev-parse HEAD) \ --target vllm-openai \ --progress plain \ -f docker/Dockerfile \ . ``` (This was done on an arm64 machine, but the same error happens on amd64 too.) While the docker build did finish, I got the following error during the build process: ```text #51 [vllm-openai-base 1/1] RUN --mount=type=cache,target=/root/.cache/uv --mount=type=bind,source=requirements/kv_connectors.txt,target=/tmp/kv_connectors.txt,ro if [ "true" = "true" ]; then uv pip install --system -r /tmp/kv_connectors.txt; fi; if [ "linux/arm64" = "linux/arm64" ]; then BITSANDBYTES_VERSIO...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: For building a CUDA 13 vLLM docker image, when building LMCache, wrong version of NIXL (`nixl-cu12`) is downloaded bug;kv-connector;nvidia ### Your current environment ### 🐛 Describe the bug When I tried to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: NDBYTES_VERSION="0.46.1"; fi; uv pip install --system accelerate hf_transfer modelscope "bitsandbytes>=${BITSANDBYTES_VERSION}" 'timm>=1.0.17' 'runai-model-streamer[s3,gcs]>=0.15.3' #51 1.310 Using Python 3.12.12 enviro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: BUILD_BASE_IMAGE=nvidia/cuda:13.0.1-devel-ubuntu22.04 \ --build-arg FLASHINFER_AOT_COMPILE=true \ --build-arg torch_cuda_arch_list='9.0 10.0+PTX' \ --build-arg INSTALL_KV_CONNECTORS=true \ --platform "linux/arm64" \ --t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: For building a CUDA 13 vLLM docker image, when building LMCache, wrong version of NIXL (`nixl-cu12`) is downloaded bug;kv-connector;nvidia ### Your current environment ### 🐛 Describe the bug When I tried to build...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 256 \ --build-arg nvcc_threads=2 \ --build-arg RUN_WHEEL_CHECK=false \ --build-arg CUDA_VERSION=13.0.1 \ --build-arg BUILD_BASE_IMAGE=nvidia/cuda:13.0.1-devel-ubuntu22.04 \ --build-arg FLASHINFER_AOT_COMPILE=true \ --bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
