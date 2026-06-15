# vllm-project/vllm#12549: [Installation]: Docker novice installation help (urgent)

| 字段 | 值 |
| --- | --- |
| Issue | [#12549](https://github.com/vllm-project/vllm/issues/12549) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;moe |
| 子分类 | memory |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Docker novice installation help (urgent)

### Issue 正文摘录

### Your current environment I used this command "DOCKER_BUILDKIT=1 docker build . --target vllm-openai-base --tag vllm/vllm-openai" to build the vllm image, but at one step the build became unusually slow `root@iZwz9av7dpqr38k3rph9ziZ:~/vllm# DOCKER_BUILDKIT=1 docker build . --target vllm-openai-base --tag vllm/vllm-openai --build-arg torch_cuda_arch_list="" [+] Building 418.7s (28/37) docker:default => [internal] load build definition from Dockerfile 0.0s => => transferring dockerfile: 12.57kB 0.0s => WARN: FromAsCasing: 'as' and 'FROM' keywords' casing do not match (line 141) 0.0s => [internal] load metadata for docker.io/nvidia/cuda:12.4.1-devel-ubuntu22.04 0.3s => [internal] load metadata for docker.io/nvidia/cuda:12.4.1-devel-ubuntu20.04 0.3s => [internal] load .dockerignore 0.0s => => transferring context: 387B 0.0s => [vllm-base 1/11] FROM docker.io/nvidia/cuda:12.4.1-devel-ubuntu22.04@sha256:da6791294b0b04d7e65d87b7451d6f2390b4 0.0s => CACHED [vllm-base 6/11] RUN --mount=type=cache,target=/root/.cache/pip if [ "linux/amd64" = "linux/arm64" ]; 0.0s => CACHED [vllm-base 2/11] WORKDIR /vllm-workspace 0.0s => CACHED [vllm-base 3/11] RUN PYTHON_VERSION_STR=$(echo 3.12 | sed 's...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Docker novice installation help (urgent) installation ### Your current environment I used this command "DOCKER_BUILDKIT=1 docker build . --target vllm-openai-base --tag vllm/vllm-openai" to build the vllm
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ild . --target vllm-openai-base --tag vllm/vllm-openai --build-arg torch_cuda_arch_list="" [+] Building 418.7s (28/37) docker:default => [internal] load build definition from Dockerfile
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: line 141) 0.0s => [internal] load metadata for docker.io/nvidia/cuda:12.4.1-devel-ubuntu22.04 0.3s => [internal] load metadata for docker.io/nvidia/cuda:12.4.1-devel-ubuntu20.04
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: et-selections && echo 'tzda 0.0s => CACHED [vllm-base 5/11] RUN ldconfig /usr/local/cuda-$(echo 12.4.1 | cut -d. -f1,2)/compat/ 0.0s => [base 1/11] FROM docker.io/nvidia/cuda:12.4.1-devel-ubuntu20.04@sha256:8d577fd078ae...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: => => # [1/256] Building CXX object CMakeFiles/_moe_C.dir/csrc/moe/torch_bindings.cpp.o => => # [2/256] Building CXX object CMakeFiles/cumem_allocator.dir/csrc/cumem_allocator.cpp.o => => # [3/256] Lin

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
