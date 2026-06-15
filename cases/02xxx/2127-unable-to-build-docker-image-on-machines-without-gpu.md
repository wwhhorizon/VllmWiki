# vllm-project/vllm#2127: Unable to build docker image on machines without GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#2127](https://github.com/vllm-project/vllm/issues/2127) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Unable to build docker image on machines without GPU

### Issue 正文摘录

Hello all, I tried to build the ROCM docker image on a machine without GPU, but I met the problem: > Traceback (most recent call last): File "/var/lib/jenkins/vllm/setup.py", line 207, in amd_arch = get_amdgpu_offload_arch() File "/var/lib/jenkins/vllm/setup.py", line 59, in get_amdgpu_offload_arch raise RuntimeError(error_message) from e RuntimeError: Error: Command '['/opt/rocm/llvm/bin/amdgpu-offload-arch']' returned non-zero exit status 1. It looks like it's unable to pip install vllm on a machine without GPU now, but I remember that vllm 0.2.1 on branch https://github.com/EmbeddedLLM/vllm-rocm/tree/v0.2.1.post1-rocm can be installed without GPUs. BTW, this problem also exists on CUDA platform. Hope you give some advice!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Unable to build docker image on machines without GPU Hello all, I tried to build the ROCM docker image on a machine without GPU, but I met the problem: > Traceback (most recent call last): File "/var/lib/jenkins/vllm/se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ild docker image on machines without GPU Hello all, I tried to build the ROCM docker image on a machine without GPU, but I met the problem: > Traceback (most recent call last): File "/var/lib/jenkins/vllm/setup.py", lin...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: lib/jenkins/vllm/setup.py", line 207, in amd_arch = get_amdgpu_offload_arch() File "/var/lib/jenkins/vllm/setup.py", line 59, in get_amdgpu_offload_arch raise RuntimeError(error_message) from e RuntimeError: Error: Comm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
