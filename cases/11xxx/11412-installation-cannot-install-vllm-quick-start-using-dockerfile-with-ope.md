# vllm-project/vllm#11412: [Installation]: cannot install vllm quick start using dockerfile with openvino backend

| 字段 | 值 |
| --- | --- |
| Issue | [#11412](https://github.com/vllm-project/vllm/issues/11412) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: cannot install vllm quick start using dockerfile with openvino backend

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Failed to build msgspec ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (msgspec) ``` ### How you are installing vllm ```sh docker build -f Dockerfile.openvino -t vllm-openvino-env . [+] Building 295.0s (11/14) docker:default => [internal] load build definition from Dockerfile.openvino 0.1s => => transferring dockerfile: 1.05kB 0.0s => [internal] load metadata for docker.io/library/ubuntu:22.04 0.7s => [internal] load .dockerignore 0.0s => => transferring context: 446B 0.0s => [dev 1/10] FROM docker.io/library/ubuntu:22.04@sha256:0e5e4a57c2499249aafc3b40fcd541e9a456aab7296681a3994d631587203f97 0.0s => [internal] load build context 0.2s => => transferring context: 213.52kB 0.1s => CACHED [dev 2/10] RUN apt-get update -y && apt-get install -y git python3-pip ffmpeg libsm6 libxext6 libgl1 0.0s => CACHED [dev 3/10] WORKDIR /workspace 0.0s => CACHED [dev 4/10] COPY . . 0.0s => CACHED [dev 5/10] RUN --mount=type=bind,source=.git,target=.git if [ "0" != 0 ]; then bash tools/check_repo.sh ; fi 0.0s => CACHED [dev 6/10] RUN PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: cannot install vllm quick start using dockerfile with openvino backend installation ### Your current environment ```text The output of `python collect_env.py` Failed to build msgspec ERROR: ERROR: Failed
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e -y && apt-get install -y git python3-pip ffmpeg libsm6 libxext6 libgl1 0.0s => CACHED [dev 3/10] WORKDIR /workspace
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: atus 'done' 46.66 Collecting optimum-intel[nncf]@ git+https://github.com/huggingface/optimum-intel.git@main 46.66 Cloning https://github.com/huggingface/optimum-intel.git (to revision main) to /tmp/pip-install-blx0cev2/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: llation]: cannot install vllm quick start using dockerfile with openvino backend installation ### Your current environment ```text The output of `python collect_env.py` Failed to build msgspec ERROR: ERROR: Failed to bu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.0s => [internal] load metadata for docker.io/library/ubuntu:22.04 0.7s =

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
