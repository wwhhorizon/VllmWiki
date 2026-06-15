# vllm-project/vllm#2175: There are no x86_64-linux-gnu-g++ version bounds defined for CUDA version 12.1

| 字段 | 值 |
| --- | --- |
| Issue | [#2175](https://github.com/vllm-project/vllm/issues/2175) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> There are no x86_64-linux-gnu-g++ version bounds defined for CUDA version 12.1

### Issue 正文摘录

I am trying to build vllm with the provided Dockerfile on a node with an A10 and CUDA 12.1 ``` +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 530.30.02 Driver Version: 530.30.02 CUDA Version: 12.1 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA A10G Off| 00000000:00:1E.0 Off | 0 | | 0% 26C P0 53W / 300W| 0MiB / 23028MiB | 8% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ +---------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running processes found | +---------------------------------------------------------------------------------------+ ``` I clone the repository with...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: There are no x86_64-linux-gnu-g++ version bounds defined for CUDA version 12.1 I am trying to build vllm with the provided Dockerfile on a node with an A10 and CUDA 12.1 ``` +--------------------------------------------...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ttention #26 4.006 creating /workspace/build/temp.linux-x86_64-3.10/csrc/quantization #26 4.007 creating /workspace/build/temp.linux-x86_64-3.10/csrc/quantization/awq #26 4.008 creating /workspace/build/temp.linux-x86_6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: There are no x86_64-linux-gnu-g++ version bounds defined for CUDA version 12.1 I am trying to build vllm with the provided Dockerfile on a node with an A10 and CUDA 12.1 ``` +--------------------------------------------...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: PU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running processes fou
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: v0.2.6 DOCKER_BUILDKIT=1 docker build -t vllm . ``` I also tried with latest master branch. The error I get is: ``` > [build 8/8] RUN python3 setup.py build_ext --inplace: #26 3.922 No CUDA runtime is found, using CUDA_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
