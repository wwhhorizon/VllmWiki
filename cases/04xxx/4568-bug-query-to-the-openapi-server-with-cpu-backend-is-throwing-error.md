# vllm-project/vllm#4568: [Bug]: Query to the openapi server with cpu backend is throwing error

| 字段 | 值 |
| --- | --- |
| Issue | [#4568](https://github.com/vllm-project/vllm/issues/4568) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Query to the openapi server with cpu backend is throwing error

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.8.16 (default, Mar 2 2023, 03:21:46) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1054-azure-x86_64-with-glibc2.17 Is CUDA available: False CUDA runtime version: 11.3.109 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.0 HIP runtime version: N/A MIOpen runtime versi...

## 现有链接修复摘要

#4590 [Bugfix] fix func var in cpuworker.execute_model() [bug 4568]

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ironment information... PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ub...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Query to the openapi server with cpu backend is throwing error bug ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cpu I...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: environment information... PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubunt...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4590](https://github.com/vllm-project/vllm/pull/4590) | closes_keyword | 0.95 | [Bugfix] fix func var in cpuworker.execute_model() [bug 4568] | FIX #4568 [(https://github.com/vllm-project/vllm/issues/4568)] **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
