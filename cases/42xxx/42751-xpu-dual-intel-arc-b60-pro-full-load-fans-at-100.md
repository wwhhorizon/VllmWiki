# vllm-project/vllm#42751: [XPU]: Dual Intel ARC B60 Pro -> full load, fans at 100%

| 字段 | 值 |
| --- | --- |
| Issue | [#42751](https://github.com/vllm-project/vllm/issues/42751) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [XPU]: Dual Intel ARC B60 Pro -> full load, fans at 100%

### Issue 正文摘录

### Your current environment I am running vllm in docker on a dual INTEL Arc B60 Pro system. I already tried all the options that I found on the internet. However, I still end up with 100% fan power AFTER a request is finished. Any solution to this? ThanksY ```text collect_env.py 100%[===========================================================================================>] 34.27K --.-KB/s in 0.01s 2026-05-15 15:15:08 (2.96 MB/s) - ‘collect_env.py’ saved [35090/35090] root@ai-server:/workspace/vllm# python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : version 4.3.2 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+xpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A XPU used to build PyTorch : 20250302 ============================== Python Environment ============================== Python version : 3.12.3 (main, Mar 3 2026, 12:15:18) [GCC 13.3.0] (6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: d, fans at 100% usage ### Your current environment I am running vllm in docker on a dual INTEL Arc B60 Pro system. I already tried all the options that I found on the internet. However, I still end up with 100% fan powe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: h version : 2.11.0+xpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A XPU used to build PyTorch : 20250302 ============================== Python Environment ===================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: i-server:/workspace/vllm# python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: und on the internet. However, I still end up with 100% fan power AFTER a request is finished. Any solution to this? ThanksY ```text collect_env.py 100%[===================================================================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx_vnni avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
