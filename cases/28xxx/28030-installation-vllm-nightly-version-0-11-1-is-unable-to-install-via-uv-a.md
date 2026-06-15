# vllm-project/vllm#28030: [Installation]: vLLM nightly version(0.11.1) is unable to install via uv according to vLLM recipes for DeepSeek-OCR models

| 字段 | 值 |
| --- | --- |
| Issue | [#28030](https://github.com/vllm-project/vllm/issues/28030) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vLLM nightly version(0.11.1) is unable to install via uv according to vLLM recipes for DeepSeek-OCR models

### Issue 正文摘录

### Your current environment Note: I ran the following script without Python3 virtual environment. ```text ============================== System Info ============================== OS : Debian GNU/Linux 12 (bookworm) (x86_64) GCC version : (Debian 12.2.0-14+deb12u1) 12.2.0 Clang version : 14.0.6 CMake version : version 3.25.1 Libc version : glibc-2.36 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 31 2025, 23:02:31) [Clang 21.1.4 ] (64-bit runtime) Python platform : Linux-6.1.0-30-amd64-x86_64-with-glibc2.36 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 11.8.89 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 Nvidia driver version : 555.42.02 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ======================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: vLLM nightly version(0.11.1) is unable to install via uv according to vLLM recipes for DeepSeek-OCR models installation ### Your current environment Note: I ran the following script without Python3 virtua
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ) is unable to install via uv according to vLLM recipes for DeepSeek-OCR models installation ### Your current environment Note: I ran the following script without Python3 virtual environment. ```text ===================...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Reg file data sampling: Not affected Vulnerability Retbl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.8.0 [pip3] torchvision==0.23.0 [pip3] transformers==4.57.1 [pip3] triton==3.4.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
