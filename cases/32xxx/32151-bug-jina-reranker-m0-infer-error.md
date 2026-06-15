# vllm-project/vllm#32151: [Bug]: jina-reranker-m0 infer error

| 字段 | 值 |
| --- | --- |
| Issue | [#32151](https://github.com/vllm-project/vllm/issues/32151) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: jina-reranker-m0 infer error

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : mtos 22.03 (LTS-SP1) (x86_64) GCC version : (GCC) 10.3.1 Clang version : Could not collect CMake version : version 3.31.8 Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Aug 8 2025, 15:49:45) [GCC 10.3.1] (64-bit runtime) Python platform : Linux-4.18.0-147.mt20200626.413.el8_1.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA L40 Nvidia driver version : 535.129.03 cuDNN version : Probably one of the following: /usr/local/cuda-12.8/targets/x86_64-linux/lib/libcudnn.so.8.9.4 /usr/local/cuda-12.8/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.4 /usr/local/cuda-12.8/targets/x86_64-linux/lib/libcudnn_adv_train.so...

## 现有链接修复摘要

#39695 Introduce De-dup/Similarity-Check in CI Workflow for PR/Issue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ======= OS : mtos 22.03 (LTS-SP1) (x86_64) GCC version : (GCC) 10.3.1 Clang version : Could not collect CMake version : version 3.31.8 Libc version : glibc-2.34 ============================== PyTo
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: DA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA L40 Nvidia driver version : 535.129.03 cuDNN version : Probably one of the following: /usr/local/cuda-12.8/targets/x...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: jina-reranker-m0 infer error bug;stale ### Your current environment ============================== System Info ============================== OS : mtos 22.03 (LTS-SP1) (x86_64) GCC version : (GCC) 10.3
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] mt-tritonclient==1.0.4 [pip3] mypy_extensions==1.1.0 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39695](https://github.com/vllm-project/vllm/pull/39695) | mentioned | 0.6 | Introduce De-dup/Similarity-Check in  CI Workflow for PR/Issue | na-reranker-m0 [image_index] IndexError: list index out of range \| [#32151](https://github.com/vllm-project/vllm/issues/32151) [Bug]: jina-reranker-m0 infer error \| --- <detail |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
