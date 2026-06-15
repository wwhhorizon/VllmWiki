# vllm-project/vllm#31877: [Feature]: Contribute changes from vllm/flash-attention fork back upstream

| 字段 | 值 |
| --- | --- |
| Issue | [#31877](https://github.com/vllm-project/vllm/issues/31877) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Contribute changes from vllm/flash-attention fork back upstream

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The fact that vllm uses a custom fork of flash-attention makes many things more complicated and requires constant synchronization (e.g. pick up features from upstream back to the fork, update the fork here), aside of course from vastly increasing the build times due to rebuilding something that could otherwise be consumed pre-built (if depending on vanilla upstream flash-attention). My question therefore is whether there are any plans or efforts to upstream the changes in https://github.com/vllm-project/flash-attention (cannot open an issue there, otherwise I would have) back to https://github.com/Dao-AILab/flash-attention? From my limited understanding, the fork is primarily due to better support for KV caching; there are a couple issues upstream that look relevant, e.g. this one: https://github.com/Dao-AILab/flash-attention/issues/797 PS. I help contribute to conda-forge, where we want to provide CUDA-enabled builds of vllm for a wide variety of machines. Using `TORCH_CUDA_ARCH_LIST="5.0;6.0;7.0;7.5;8.0;8.6;8.9;9.0;10.0;12.0+PTX"`, the vendored flash-attention (as built by default) is absolutely [ginormous](https://github.com/conda-forge/v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: fork, update the fork here), aside of course from vastly increasing the build times due to rebuilding something that could otherwise be consumed pre-built (if depending on vanilla upstream flash-attention). My question...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sues/797 PS. I help contribute to conda-forge, where we want to provide CUDA-enabled builds of vllm for a wide variety of machines. Using `TORCH_CUDA_ARCH_LIST="5.0;6.0;7.0;7.5;8.0;8.6;8.9;9.0;10.0;12.0+PTX"`, the vendo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Contribute changes from vllm/flash-attention fork back upstream feature request;stale ### 🚀 The feature, motivation and pitch The fact that vllm uses a custom fork of flash-attention makes many things more complicated a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: │ │ 1.75 GiB - lib/python3.12/site-packages/vllm/vllm_flash_attn/_vllm_fa3_C.abi3.so │ │ 837.90 MiB - lib/python3.12/site-packages/vllm/_C.abi3.so │ │ 220.30 MiB - lib/python3.12/site-packages/vllm/vllm_flash_attn/_vllm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ck/issues/25): ``` │ │ Package statistics: 2916 files (2896 content, 20 metadata), total size: 2.99 GiB │ │ Largest files: │ │ 1.75 GiB - lib/python3.12/site-packages/vllm/vllm_flash_attn/_vllm_fa3_C.abi3.so │ │ 837.90...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
