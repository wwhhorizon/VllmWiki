# vllm-project/vllm#3821: [Bug]: tp>1 every worker takes memory in every GPU after upgrade to 0.4.0

| 字段 | 值 |
| --- | --- |
| Issue | [#3821](https://github.com/vllm-project/vllm/issues/3821) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tp>1 every worker takes memory in every GPU after upgrade to 0.4.0

### Issue 正文摘录

### Your current environment ```text $ python collect_env.py Collecting environment information... PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 5.4.0 Clang version: Could not collect CMake version: version 3.27.7 Libc version: glibc-2.17 Python version: 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-957.21.3.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.7.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB GPU 2: Tesla V100-SXM2-32GB GPU 3: Tesla V100-SXM2-32GB GPU 4: Tesla V100-SXM2-32GB GPU 5: Tesla V100-SXM2-32GB GPU 6: Tesla V100-SXM2-32GB GPU 7: Tesla V100-SXM2-32GB Nvidia driver version: 515.65.01 cuDNN version: /usr/local/cuda-9.2/targets/x86_64-linux/lib/libcudnn.so.7 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 72 On-line CPU(s) list: 0-71 Thread(s) per core: 1 Core(s) per...

## 现有链接修复摘要

#4021 [Core] avoid too many cuda context by caching p2p test

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: xt $ python collect_env.py Collecting environment information... PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 5.4.0 Clang version: Could...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nt environment ```text $ python collect_env.py Collecting environment information... PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ==2.1.2+cu118 [pip3] torchvision==0.15.2a0 [pip3] torchviz==0.0.2 [pip3] triton==2.1.0 [conda] blas 1.0 mkl https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main [conda] cudatoolkit 11.8.0 h4ba93d1_12 conda-forge
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=============================================================================| | 0 N/A N/A 995011 C python

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4021](https://github.com/vllm-project/vllm/pull/4021) | mentioned | 0.6 | [Core] avoid too many cuda context by caching p2p test | re] avoid too many cuda context by caching p2p test It is observed in #3821 that every worker takes memory in every GPU in `_can_p2p` , because the test will make all process allo… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
