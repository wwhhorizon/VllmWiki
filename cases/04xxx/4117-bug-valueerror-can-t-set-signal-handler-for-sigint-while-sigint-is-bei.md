# vllm-project/vllm#4117: [Bug]: ValueError: Can't set signal handler for SIGINT while SIGINT is being deferred within a DeferSigint context when tp>1

| 字段 | 值 |
| --- | --- |
| Issue | [#4117](https://github.com/vllm-project/vllm/issues/4117) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Can't set signal handler for SIGINT while SIGINT is being deferred within a DeferSigint context when tp>1

### Issue 正文摘录

### Your current environment ```text [2024-04-16T16:36:16.632583Z] b1d60799 || Collecting environment information... [2024-04-16T16:36:18.091248Z] b1d60799 || PyTorch version: 2.3.0a0+40ec155e58.nv24.03 [2024-04-16T16:36:18.091300Z] b1d60799 || Is debug build: False [2024-04-16T16:36:18.091309Z] b1d60799 || CUDA used to build PyTorch: 12.4 [2024-04-16T16:36:18.091315Z] b1d60799 || ROCM used to build PyTorch: N/A [2024-04-16T16:36:18.091321Z] b1d60799 || [2024-04-16T16:36:18.091326Z] b1d60799 || OS: Ubuntu 22.04.4 LTS (x86_64) [2024-04-16T16:36:18.091332Z] b1d60799 || GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 [2024-04-16T16:36:18.091337Z] b1d60799 || Clang version: Could not collect [2024-04-16T16:36:18.091342Z] b1d60799 || CMake version: version 3.28.3 [2024-04-16T16:36:18.091347Z] b1d60799 || Libc version: glibc-2.35 [2024-04-16T16:36:18.091352Z] b1d60799 || [2024-04-16T16:36:18.091358Z] b1d60799 || Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) [2024-04-16T16:36:18.091363Z] b1d60799 || Python platform: Linux-5.15.0-1031-aws-x86_64-with-glibc2.35 [2024-04-16T16:36:18.091368Z] b1d60799 || Is CUDA available: True [2024-04-16T16:36:18.09...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ronment information... [2024-04-16T16:36:18.091248Z] b1d60799 || PyTorch version: 2.3.0a0+40ec155e58.nv24.03 [2024-04-16T16:36:18.091300Z] b1d60799 || Is debug build: False [2024-04-16T16:36:18.091309Z] b1d60799 || CUDA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: 60799 || Is debug build: False [2024-04-16T16:36:18.091309Z] b1d60799 || CUDA used to build PyTorch: 12.4 [2024-04-16T16:36:18.091315Z] b1d60799 || ROCM used to build PyTorch: N/A [2024-04-16T16:36:18.091321Z] b1d60799...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: `text [2024-04-16T16:36:16.632583Z] b1d60799 || Collecting environment information... [2024-04-16T16:36:18.091248Z] b1d60799 || PyTorch version: 2.3.0a0+40ec155e58.nv24.03 [2024-04-16T16:36:18.091300Z] b1d60799 || Is de...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: tization==2.1.2 [2024-04-16T16:36:18.091716Z] b1d60799 || [pip3] pytorch-triton==2.2.0+e28a256d7 [2024-04-16T16:36:18.091720Z] b1d60799 || [pip3] torch==2.3.0a0+40ec155e58.nv24.3 [2024-04-16T16:36:18.091727Z] b1d60799 |...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: optree==0.10.0 [2024-04-16T16:36:18.091711Z] b1d60799 || [pip3] pytorch-quantization==2.1.2 [2024-04-16T16:36:18.091716Z] b1d60799 || [pip3] pytorch-triton==2.2.0+e28a256d7 [2024-04-16T16:36:18.091720Z] b1d60799 || [pip...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
