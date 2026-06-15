# vllm-project/vllm#16310: [Usage]: TPU Offline benchmark Error TypeError: PlaceholderAttentionMetadata.__init__() got an unexpected keyword argument 'context_lens'

| 字段 | 值 |
| --- | --- |
| Issue | [#16310](https://github.com/vllm-project/vllm/issues/16310) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: TPU Offline benchmark Error TypeError: PlaceholderAttentionMetadata.__init__() got an unexpected keyword argument 'context_lens'

### Issue 正文摘录

### Your current environment When I run ``` gcloud compute tpus tpu-vm describe v5litepod-1 --zone=us-east1-c ``` This is my TPU specs. ``` acceleratorConfig: topology: 1x1 type: V5LITE_POD acceleratorType: v5litepod-1 apiVersion: V2 ``` This is my environment. ``` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] (64-bit runtime) Python platform: Linux-5.19.0-1022-gcp-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU(s): 24 On-line CPU(s) list: 0-23 Vendor ID: AuthenticAMD Model name: AMD EPYC 7B13 CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 24 On-line CP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: nfig: topology: 1x1 type: V5LITE_POD acceleratorType: v5litepod-1 apiVersion: V2 ``` This is my environment. ``` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyT...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: s my environment. ``` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: v5litepod-1 --zone=us-east1-c ``` This is my TPU specs. ``` acceleratorConfig: topology: 1x1 type: V5LITE_POD acceleratorType: v5litepod-1 apiVersion: V2 ``` This is my environment. ``` PyTorch version: 2.6.0+cu124 Is d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: TPU Offline benchmark Error TypeError: PlaceholderAttentionMetadata.__init__() got an unexpected keyword argument 'context_lens' usage;stale ### Your current environment When I run ``` gcloud compute tpus tpu-v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Usage]: TPU Offline benchmark Error TypeError: PlaceholderAttentionMetadata.__init__() got an unexpected keyword argument 'context_lens' usage;stale ### Your current environment When I run ``` gcloud compute tpus tpu-v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
