# vllm-project/vllm#7138: [Bug]: zmq.error.ZMQError: No such device

| 字段 | 值 |
| --- | --- |
| Issue | [#7138](https://github.com/vllm-project/vllm/issues/7138) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: zmq.error.ZMQError: No such device

### Issue 正文摘录

### Your current environment ```text Collecting environment information... /app/apps/anaconda3/envs/vllm_053p1_main/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.16) or chardet (5.2.0)/charset_normalizer (2.0.4) doesn't match a supported version! warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported " PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.9.12 (main, Apr 5 2022, 06:56:58) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.4.0-148-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 550.90.07 cuDNN version: Probably one of the following: /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn.so.8.2.4 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.2.4 /usr/loca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 053p1_main/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.16) or chardet (5.2.0)/charset_normalizer (2.0.4) doesn't match a supported version! warnings.warn("urllib3 ({})...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: t match a supported " PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: evice bug ### Your current environment ```text Collecting environment information... /app/apps/anaconda3/envs/vllm_053p1_main/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ... /app/apps/anaconda3/envs/vllm_053p1_main/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.16) or chardet (5.2.0)/charset_normalizer (2.0.4) doesn't match a supported ver...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: transformers==4.43.2 [pip3] transformers-stream-generator==0.0.4 [pip3] triton==3.0.0 [conda] blas 1.0 mkl [conda] mkl 2021.4.0 h06a4308_640 [conda] mkl-service 2.4.0 py39h7f8727e_0 [c

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
