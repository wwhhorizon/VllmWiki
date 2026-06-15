# vllm-project/vllm#12440: [Bug]: python -m vllm.entrypoints.openai.api_server --served-model-name TableGPT2-7B --port 12233 --trust-remote-code --gpu-memory-utilization 0.9 --model ./TableGPT2-7B/ --dtype=half

| 字段 | 值 |
| --- | --- |
| Issue | [#12440](https://github.com/vllm-project/vllm/issues/12440) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | activation;cuda;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: python -m vllm.entrypoints.openai.api_server --served-model-name TableGPT2-7B --port 12233 --trust-remote-code --gpu-memory-utilization 0.9 --model ./TableGPT2-7B/ --dtype=half

### Issue 正文摘录

### Your current environment env ``` Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (conda-forge gcc 14.2.0-1) 14.2.0 Clang version: Could not collect CMake version: version 3.31.4 Libc version: glibc-2.17 Python version: 3.10.16 | packaged by conda-forge | (main, Dec 5 2024, 14:16:10) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.119.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB GPU 1: Tesla V100-PCIE-32GB GPU 2: Tesla V100-PCIE-32GB GPU 3: Tesla V100-PCIE-32GB Nvidia driver version: Could not collect cuDNN version: Probably one of the following: /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_adv.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_cnn.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_engines_precompiled.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcud...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment env ``` Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (conda-forge gcc 14.2.0-1) 14.2.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: python -m vllm.entrypoints.openai.api_server --served-model-name TableGPT2-7B --port 12233 --trust-remote-code --gpu-memory-utilization 0.9 --model ./TableGPT2-7B/ --dtype=half bug ### Your current environment en...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dio==2.1.1 [pip3] torchvision==0.19.0 [pip3] transformers==4.48.0 [pip3] triton==3.0.0 [conda] blas 1.0 mkl https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge [conda] cuda-cudart 11.8.89 0 nvid
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (conda-forge gcc 14.2.0-1) 14...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
