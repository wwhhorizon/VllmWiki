# vllm-project/vllm#7112: [Bug]: Cannot use FlashAttention-2 backend because the vllm_flash_attn package is not found. But I have installed vllm-flash-attn.

| 字段 | 值 |
| --- | --- |
| Issue | [#7112](https://github.com/vllm-project/vllm/issues/7112) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot use FlashAttention-2 backend because the vllm_flash_attn package is not found. But I have installed vllm-flash-attn.

### Issue 正文摘录

### Your current environment ```text Collecting environment information... /app/apps/anaconda3/envs/vllm_040p1/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.16) or char det (5.2.0)/charset_normalizer (2.0.4) doesn't match a supported version! warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported " WARNING 08-03 23:03:20 _custom_ops.py:15] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') PyTorch version: 2.4.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.9.12 (main, Apr 5 2022, 06:56:58) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.4.0-148-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 470.161.03 cuDNN version: Probably one of...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: n-2 backend because the vllm_flash_attn package is not found. But I have installed vllm-flash-attn. bug ### Your current environment ```text Collecting environment information... /app/apps/anaconda3/envs/vllm_040p1/lib/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: 20 _custom_ops.py:15] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') PyTorch version: 2.4.0+cu118 Is debug build: False CUDA used to build Py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: attn. bug ### Your current environment ```text Collecting environment information... /app/apps/anaconda3/envs/vllm_040p1/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.16)...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Cannot use FlashAttention-2 backend because the vllm_flash_attn package is not found. But I have installed vllm-flash-attn. bug ### Your current environment ```text Collecting environment information... /app/apps...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ation... /app/apps/anaconda3/envs/vllm_040p1/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.16) or char det (5.2.0)/charset_normalizer (2.0.4) doesn't match a supported ve...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
