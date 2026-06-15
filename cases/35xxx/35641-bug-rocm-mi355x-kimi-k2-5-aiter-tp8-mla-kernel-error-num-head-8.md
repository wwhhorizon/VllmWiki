# vllm-project/vllm#35641: [Bug]: ROCm MI355X Kimi K2.5 AITER TP8 MLA kernel Error (num_head=8)

| 字段 | 值 |
| --- | --- |
| Issue | [#35641](https://github.com/vllm-project/vllm/issues/35641) |
| 状态 | closed |
| 标签 | bug;performance;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | attention;kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ROCm MI355X Kimi K2.5 AITER TP8 MLA kernel Error (num_head=8)

### Issue 正文摘录

### Your current environment `vllm/vllm-openai-rocm:v0.16.0` with `pip install amd-quark` inside the container ### 🐛 Describe the bug hi @powderluv @chunfangamd @andyluo7 Today i was trying to test out amd's mxfp4 checkpoint `amd/Kimi-K2.5-MXFP4` using amd's `vllm/vllm-openai-rocm:v0.16.0`. After getting over the inital hump (https://github.com/vllm-project/vllm/issues/35633) with `pip install amd-quark` inside the container, i got it to successfully run. I then try to set `export VLLM_ROCM_USE_AITER=1 ` as typically AITER kernels are much faster but unfortunately i run into following error that AITER MLA kernels don't support Kimi K2.5 `TP8` yet (num_head=8) and that it only supports `"16 or 128 number of heads."`. It would be great if AITER MLA kernels with `num_head=8` such that vLLM Kimi K2.5 can achieve the full performance of the ROCm platform on MI355 ``` (Worker_TP1 pid=944525) ERROR 03-01 06:39:51 [multiproc_executor.py:783] self.mla_attn = MultiHeadLatentAttentionWrapper( (Worker_TP1 pid=944525) ERROR 03-01 06:39:51 [multiproc_executor.py:783] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP1 pid=944525) ERROR 03-01 06:39:51 [multiproc_executor.py:783] File "/usr/local/lib/py...

## 现有链接修复摘要

#35064 [ROCm] Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5/Linear) | #35850 [ROCm] Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5/Linear)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: @powderluv @chunfangamd @andyluo7 Today i was trying to test out amd's mxfp4 checkpoint `amd/Kimi-K2.5-MXFP4` using amd's `vllm/vllm-openai-rocm:v0.16.0`. After getting over the inital hump (https://github.com/vllm-proj...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ### Your current environment `vllm/vllm-openai-rocm:v0.16.0` with `pip install amd-quark` inside the container ### 🐛 Describe the bug hi @powderluv @chunfangamd @andyluo7 Today i was trying to test out amd's mxfp4 check...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: ROCm MI355X Kimi K2.5 AITER TP8 MLA kernel Error (num_head=8) bug;performance;rocm ### Your current environment `vllm/vllm-openai-rocm:v0.16.0` with `pip install amd-quark` inside the container ### 🐛 Describe the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: ROCm MI355X Kimi K2.5 AITER TP8 MLA kernel Error (num_head=8) bug;performance;rocm ### Your current environment `vllm/vllm-openai-rocm:v0.16.0` with `pip install amd-quark` inside the container ### 🐛 Describe the...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ization attention;kernel #35064 [ROCm] Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5/Linear) | #35850 [ROCm] Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5/Linear) Your current environme...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35064](https://github.com/vllm-project/vllm/pull/35064) | closes_keyword | 0.95 | [ROCm] Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5/Linear) | Fixes #35641 ## Test plan - [x] Verify `amd/Kimi-K2.5-MXFP4` runs with TP=8, AITER enabled (8 heads/rank, previously crashed with assertion error) - [x] Verify `moonshotai/Kimi-L |
| [#35850](https://github.com/vllm-project/vllm/pull/35850) | closes_keyword | 0.95 | [ROCm] Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5/Linear) | Fixes #35641 ## Test plan - Verify `amd/Kimi-K2.5-MXFP4` runs with TP=8, AITER enabled (8 heads/rank, previously crashed with assertion error) - Verify `moonshotai/Kimi-Linear-48 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
