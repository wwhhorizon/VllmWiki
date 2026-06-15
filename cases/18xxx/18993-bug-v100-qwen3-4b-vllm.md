# vllm-project/vllm#18993: [Bug]: V100能启动Qwen3-4B，但无法对其进行调用，一旦调用，vllm服务会直接停掉

| 字段 | 值 |
| --- | --- |
| Issue | [#18993](https://github.com/vllm-project/vllm/issues/18993) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V100能启动Qwen3-4B，但无法对其进行调用，一旦调用，vllm服务会直接停掉

### Issue 正文摘录

### Your current environment INFO 06-01 00:13:12 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.0 | packaged by Anaconda, Inc. | (main, Oct 2 2023, 17:29:18) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.0-59-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.131 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: Tesla V100-SXM3-32GB Nvidia driver version : 550.144.03 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: t INFO 06-01 00:13:12 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Mitigation; Clear Register File Vulnerability Retbleed: Not affected Vulnerability Spec rstack ov...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: V100能启动Qwen3-4B，但无法对其进行调用，一旦调用，vllm服务会直接停掉 bug ### Your current environment INFO 06-01 00:13:12 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ======================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dio==2.7.0 [pip3] torchvision==0.22.0 [pip3] transformers==4.51.3 [pip3] triton==3.3.0 [conda] cudatoolkit 8.0 3 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free [conda] numpy 2.2.6 pypi_0 pypi [conda]

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
