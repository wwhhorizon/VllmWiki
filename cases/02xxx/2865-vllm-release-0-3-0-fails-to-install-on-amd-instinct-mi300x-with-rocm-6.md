# vllm-project/vllm#2865: vLLM Release 0.3.0 fails to install on AMD Instinct MI300X with ROCm 6.0.2

| 字段 | 值 |
| --- | --- |
| Issue | [#2865](https://github.com/vllm-project/vllm/issues/2865) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM Release 0.3.0 fails to install on AMD Instinct MI300X with ROCm 6.0.2

### Issue 正文摘录

Reproducing steps: 1. Clone the vllm repo and switch to [tag v0.3.0](https://github.com/vllm-project/vllm/tree/v0.3.0) 2. Build the Dockerfile.rocm dockerfile with instructions from [Option 3: Build from source with docker -Installation with ROCm](https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-docker-rocm) * The build arguments are kept default for first test. The build fails with [installing vllm](https://github.com/vllm-project/vllm/blob/v0.3.0/Dockerfile.rocm#L78). build command: ```sh docker build -f Dockerfile.rocm -t vllm-rocm . ``` The error below ```sh ... conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv 18.57 WARNING[XFORMERS]: xFormers can't load C++/CUDA extensions. xFormers was built for: 18.57 PyTorch 2.1.1+cu121 with CUDA 1201 (you have 2.1.1+git011de5c) 18.57 Python 3.9.18 (you have 3.9.18) 18.57 Please reinstall xformers (see https://github.com/facebookresearch/xformers#installing-xformers) 18.57 Memory-efficient attention, SwiGLU, sparse and more won't be available. 18.57 Set XFORMERS_MORE_DETAILS=1 for more details 20.52 WARNING[...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: vLLM Release 0.3.0 fails to install on AMD Instinct MI300X with ROCm 6.0.2 Reproducing steps: 1. Clone the vllm repo and switch to [tag v0.3.0](https://github.com/vllm-project/vllm/tree/v0.3.0) 2. Build the Dockerfile.r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: vLLM Release 0.3.0 fails to install on AMD Instinct MI300X with ROCm 6.0.2 Reproducing steps: 1. Clone the vllm repo and switch to [tag v0.3.0](https://github.com/vllm-project/vllm/tree/v0.3.0) 2. Build the Dockerfile.r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: om source with docker -Installation with ROCm](https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-docker-rocm) * The build arguments are kept default for first test. The build fails w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
