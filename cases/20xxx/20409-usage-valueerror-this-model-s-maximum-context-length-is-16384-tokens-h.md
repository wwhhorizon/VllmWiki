# vllm-project/vllm#20409: [Usage]: ValueError: This model's maximum context length is 16384 tokens. However, you requested 122946 tokens (112946 in the messages, 10000 in the completion). Please reduce the length of the messages or completion.

| 字段 | 值 |
| --- | --- |
| Issue | [#20409](https://github.com/vllm-project/vllm/issues/20409) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: ValueError: This model's maximum context length is 16384 tokens. However, you requested 122946 tokens (112946 in the messages, 10000 in the completion). Please reduce the length of the messages or completion.

### Issue 正文摘录

### Your current environment python collect_env.py ```text INFO 07-03 03:28:30 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.27.6 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform : Linux-5.10.112-005.ali5000.al8.x86_64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.2.140 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidia driver version...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.27.6 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: xt INFO 07-03 03:28:30 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: ValueError: This model's maximum context length is 16384 tokens. However, you requested 122946 tokens (112946 in the messages, 10000 in the completion). Please reduce the length of the messages or completion. u...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 00.0, "sliding_window": null, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.49.0", "use_cache": false, "use_sliding_window": false, "vocab_size": 152064 } ``` then i run this script...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Error: This model's maximum context length is 16384 tokens. However, you requested 122946 tokens (112946 in the messages, 10000 in the completion). Please reduce the length of the messages or completion. usage;stale ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
