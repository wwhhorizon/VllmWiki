# vllm-project/vllm#42860: [Bug]: integer overflow in activation_kernels.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#42860](https://github.com/vllm-project/vllm/issues/42860) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: integer overflow in activation_kernels.cu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There appears to be a potential integer overflow in activation_kernels.cu when handling long sequences. The expression: ```blockIdx.x * 2 * d``` can exceed ```2^32-1 ``` for sufficiently large values of blockIdx.x and hidden dimension d. https://github.com/vllm-project/vllm/blob/ff712f6447093d07747c88680b9d006b119f5890/csrc/activation_kernels.cu#L78-L82 For example, for model "royokong/e5-v", `d = 14336`, when `seq_len=7890` and `batch_size=19`, `blockIdx.x * 2 * d` overflows. log: ``` silu_and_mul out 123997786210304 shape torch.Size([149910, 14336]) dtype torch.float16 x 124002114732032 shape torch.Size([149910, 28672]) dtype torch.float16 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#42861 [Bug] Fix integer overflow in activation_kernels.cu pointer arithmetic | #44026 [Bugfix] Fix integer overflow in libtorch_stable/activation_kernels.cu pointer arithmetic

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e expression: ```blockIdx.x * 2 * d``` can exceed ```2^32-1 ``` for sufficiently large values of blockIdx.x and hidden dimension d. https://github.com/vllm-project/vllm/blob/ff712f6447093d07747c88680b9d006b119f5890/csrc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: : ``` silu_and_mul out 123997786210304 shape torch.Size([149910, 14336]) dtype torch.float16 x 124002114732032 shape torch.Size([149910, 28672]) dtype torch.float16 ``` ### Before submitting a new issue... - [x] Make su...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency;shape #42861 [Bug] Fix integer overflow in activation_kernels.cu pointer arithmetic | #44026 [Bugf...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: n activation_kernels.cu when handling long sequences. The expression: ```blockIdx.x * 2 * d``` can exceed ```2^32-1 ``` for sufficiently large values of blockIdx.x and hidden dimension d. https://github.com/vllm-project...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42861](https://github.com/vllm-project/vllm/pull/42861) | closes_keyword | 0.95 | [Bug] Fix integer overflow in activation_kernels.cu pointer arithmetic | Fixes #42860. --- ### AI assistance disclosure This PR was prepared with the assistance of an AI coding tool (Claude). The bug diagnosis, the fix, the static audit of all `block |
| [#44026](https://github.com/vllm-project/vllm/pull/44026) | closes_keyword | 0.95 | [Bugfix] Fix integer overflow in libtorch_stable/activation_kernels.cu pointer arithmetic | Closes #42860 ## Test Plan - [ ] Build + activation tests via CI. ## Duplicate-work check `gh pr list --repo vllm-project/vllm --state open --search "libtorch_stable activation |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
