# vllm-project/vllm#3779: [Bug]: vllm-0.4.0 is much slower than vllm-0.3.3

| 字段 | 值 |
| --- | --- |
| Issue | [#3779](https://github.com/vllm-project/vllm/issues/3779) |
| 状态 | closed |
| 标签 |  |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm-0.4.0 is much slower than vllm-0.3.3

### Issue 正文摘录

### Your current environment Traceback (most recent call last): File "/zhanghongbo/collect_env.py", line 719, in main() File "/zhanghongbo/collect_env.py", line 698, in main output = get_pretty_env_info() File "/zhanghongbo/collect_env.py", line 693, in get_pretty_env_info return pretty_str(get_env_info()) File "/zhanghongbo/collect_env.py", line 530, in get_env_info vllm_version = get_vllm_version() File "/zhanghongbo/collect_env.py", line 262, in get_vllm_version return vllm.__version__ AttributeError: module 'vllm' has no attribute '__version__' I encountered the above issue, so I commented out a line of code. PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.3 LTS (x86_64) GCC version: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 Clang version: Could not collect CMake version: version 3.26.1 Libc version: glibc-2.31 Python version: 3.9.17 (main, Jul 5 2023, 20:41:20) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-8...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: File "/zhanghongbo/collect_env.py", line 530, in get_env_info vllm_version = get_vllm_version() File "/zhanghongbo/collect_env.py", line 262, in get_vllm_version return vllm.__version__ AttributeError: module 'vllm' has...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: out a line of code. PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.3 LTS (x86_64) GCC version: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB Nvidia driver version: 525.105.17...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 1 [pip3] torchaudio==2.1.2+cu118 [pip3] torchvision==0.16.2+cu118 [pip3] triton==2.1.0 [conda] numpy 1.23.5 pypi_0 pypi [conda] torch 2.1.2+cu118 pypi_0 pypi [conda] torch-tb-profiler 0.4.1
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nted out a line of code. PyTorch version: 2.1.2+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.3 LTS (x86_64) GCC version: (Ubuntu 9.3.0-17ubuntu1~20.04) 9....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
