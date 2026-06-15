# vllm-project/vllm#2113: Tangential question about Dockerfile - where is `nvcc` installed?

| 字段 | 值 |
| --- | --- |
| Issue | [#2113](https://github.com/vllm-project/vllm/issues/2113) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
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

> Tangential question about Dockerfile - where is `nvcc` installed?

### Issue 正文摘录

Hi! I'm trying to mimic the build steps in the `Dockerfile` manually, and found that `nvcc` is a requirement. What I can't figure out is how the `vllm/vllm-openai` image has been built without `nvcc` specified in the `Dockerfile` - I'm guessing I'm missing something really stupid! My first thought is that maybe the CUDA runtime and `nvcc` is borrowed from the host builder, but [the suggested `docker build` command here](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html) doesn't seem to mount anything of that nature. Since this is a slightly strange question, I'll add some more context on what I'm trying to do. I'm trying to build a lighter image to make [inference on Modal](https://modal.com/docs/examples/vllm_inference) faster to build and load, since `nvcr.io/nvidia/pytorch:22.12-py3` is a very heavy base image (9 GiB) compared to `nvidia/cuda:12.1.0-base-ubuntu22.04` (3 GiB). ### Modal image building code/error ```python image = ( Image.from_registry( "nvidia/cuda:12.1.0-base-ubuntu22.04", setup_dockerfile_commands=[ "RUN apt-get update -y", "RUN apt-get install -y git python3-pip python-is-python3", ] ) .env({ "TORCH_CUDA_ARCH_LIST": "7.0 7.5 8.0 8.6 8.9 9.0+PT...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Tangential question about Dockerfile - where is `nvcc` installed? Hi! I'm trying to mimic the build steps in the `Dockerfile` manually, and found that `nvcc` is a requirement. What I can't figure out is how the `vllm/vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: I'm missing something really stupid! My first thought is that maybe the CUDA runtime and `nvcc` is borrowed from the host builder, but [the suggested `docker build` command here](https://docs.vllm.ai/en/latest/serving/d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ut [the suggested `docker build` command here](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html) doesn't seem to mount anything of that nature. Since this is a slightly strange question, I'll add some m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
