# vllm-project/vllm#196: No `device_map` option. 

| 字段 | 值 |
| --- | --- |
| Issue | [#196](https://github.com/vllm-project/vllm/issues/196) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> No `device_map` option. 

### Issue 正文摘录

Currently there is no way to use large models hence there is no support for 8-bit quantization and more importantly there is no support for device mapping. As you can see first GPU is filled but second GPU is left unallocated. ![image](https://github.com/vllm-project/vllm/assets/47108366/a3e7cc39-921f-44ac-b0fb-bb6f73e29cda) Here is the error message: `OutOfMemoryError: CUDA out of memory. Tried to allocate 270.00 MiB (GPU 0; 23.70 GiB total capacity; 22.40 GiB already allocated; 247.50 MiB free; 22.40 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF`

## 现有链接修复摘要

#17997 [CI] Fix Nightly Failures | #18002 [Bugfix] Fix FBGEMM integration | #18537 Use prebuilt FlashInfer x86_64 PyTorch 2.7 CUDA 12.8 wheel for CI

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e large models hence there is no support for 8-bit quantization and more importantly there is no support for device mapping. As you can see first GPU is filled but second GPU is left unallocated. ![image](https://github...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Failures | #18002 [Bugfix] Fix FBGEMM integration | #18537 Use prebuilt FlashInfer x86_64 PyTorch 2.7 CUDA 12.8 wheel for CI Currently there is no way to use large models hence there is no support for 8-bit quantization...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: there is no way to use large models hence there is no support for 8-bit quantization and more importantly there is no support for device mapping. As you can see first GPU is filled but second GPU is left unallocated. ![...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: f-44ac-b0fb-bb6f73e29cda) Here is the error message: `OutOfMemoryError: CUDA out of memory. Tried to allocate 270.00 MiB (GPU 0; 23.70 GiB total capacity; 22.40 GiB already allocated; 247.50 MiB free; 22.40 GiB reserved...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: _ALLOC_CONF` performance quantization;scheduler_memory cuda;quantization oom #17997 [CI] Fix Nightly Failures | #18002 [Bugfix] Fix FBGEMM integration | #18537 Use prebuilt FlashInfer x86_64 PyTorch 2.7 CUDA 12.8 wheel...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17997](https://github.com/vllm-project/vllm/pull/17997) | closes_keyword | 0.95 | [CI] Fix Nightly Failures | fix / disable nightly failures (https://buildkite.com/vllm/ci/builds/19754#0196bd80-d167-461d-81b3-bb9d0a7b49d1) * @mgoin looking at fixing the FI issues * @jinzhen-lin - looking a |
| [#18002](https://github.com/vllm-project/vllm/pull/18002) | mentioned | 0.6 | [Bugfix] Fix FBGEMM integration | ` ==== Original failure found in CI: https://buildkite.com/vllm/ci/builds/19754#0196bd80-d18b-4c8a-bf76-50e9a53c5a6c/43-353 ``` ERROR 05-10 22:15:39 [multiproc_executor.py:487] Fi… |
| [#18537](https://github.com/vllm-project/vllm/pull/18537) | mentioned | 0.6 | Use prebuilt FlashInfer x86_64 PyTorch 2.7 CUDA 12.8 wheel for CI | ting Prebuilt wheel is used now https://buildkite.com/vllm/fastcheck/builds/24717#0196f710-8140-4bf5-9532-ff57b8322398/6-8549 cc @simon-mo @kevin314 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
