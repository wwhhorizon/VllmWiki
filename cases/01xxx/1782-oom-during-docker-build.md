# vllm-project/vllm#1782: OOM during Docker build

| 字段 | 值 |
| --- | --- |
| Issue | [#1782](https://github.com/vllm-project/vllm/issues/1782) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> OOM during Docker build

### Issue 正文摘录

I was able to build from source in 0.2.1 but now I can't. I'm facing OOM of my entire system during Docker image build. Here is my `build.sh` script: ```bash #!/bin/sh set -e imageNAME="xxxxxxxx" git clone https://github.com/vllm-project/vllm.git && \ cd vllm/ # Build Classic DOCKER_BUILDKIT=1 docker build . --progress=plain --target vllm --tag $imageNAME:latest --build-arg max_jobs=8 # Broadcast image name and tag echo "$imageNAME" ``` ## About CUDA ```bash nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023 Cuda compilation tools, release 12.1, V12.1.105 Build cuda_12.1.r12.1/compiler.32688072_0 ``` ## Docker build logs: ```bash #19 [build 6/6] RUN python3 setup.py build_ext --inplace #19 1.622 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' #19 1.637 running build_ext #19 1.660 /usr/local/lib/python3.10/dist-packages/torch/utils/cpp_extension.py:424: UserWarning: There are no x86_64-linux-gnu-g++ version bounds defined for CUDA version 12.1 #19 1.660 warnings.warn(f'There are no {compiler_name} version bounds defined for CUDA version {cuda_str_version}') #19 1.660 building 'vllm._C' ex...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: OOM during Docker build I was able to build from source in 0.2.1 but now I can't. I'm facing OOM of my entire system during Docker image build. Here is my `build.sh` script: ```bash #!/bin/sh set -e imageNAME="xxxxxxxx"...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ttention #19 1.660 creating /workspace/build/temp.linux-x86_64-3.10/csrc/quantization #19 1.660 creating /workspace/build/temp.linux-x86_64-3.10/csrc/quantization/awq #19 1.660 creating /workspace/build/temp.linux-x86_6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: max_jobs=8 # Broadcast image name and tag echo "$imageNAME" ``` ## About CUDA ```bash nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: OOM during Docker build I was able to build from source in 0.2.1 but now I can't. I'm facing OOM of my entire system during Docker image build. Here is my `build.sh` script: ```bash #!/bin/sh set -e imageNAME="xxxxxx
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: LDKIT=1 docker build . --progress=plain --target vllm --tag $imageNAME:latest --build-arg max_jobs=8 # Broadcast image name and tag echo "$imageNAME" ``` ## About CUDA ```bash nvcc --version nvcc: NVIDIA (R) Cuda compil...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
