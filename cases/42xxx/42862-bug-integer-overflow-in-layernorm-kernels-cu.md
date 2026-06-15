# vllm-project/vllm#42862: [Bug]: integer overflow in layernorm_kernels.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#42862](https://github.com/vllm-project/vllm/issues/42862) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: integer overflow in layernorm_kernels.cu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There is a potential integer overflow in layernorm_kernels.cu when handling long sequences. The expression: `blockIdx.x * hidden_size` can exceed `2^32-1` for sufficiently large values of `blockIdx.x` and `hidden_size`. https://github.com/vllm-project/vllm/blob/ff712f6447093d07747c88680b9d006b119f5890/csrc/layernorm_kernels.cu#L69-L72 For example, for model "royokong/e5-v", `hidden_size` is 4096, when `seq_len=8129` and `batch_size=129`, `blockIdx.x * hidden_size` overflows. log: ``` rms_norm out shape torch.Size([1048641, 4096]) dtype torch.float16 x shape torch.Size([1048641, 4096]) dtype torch.float16 weight shape torch.Size([4096]) dtype torch.float16 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#42863 [Bug] Fix integer overflow in layernorm_kernels.cu pointer arithmetic | #43166 [Bug] Fix fused_qk_norm_rope 32-bit QKV offset overflow | #44027 [Bugfix] Fix integer overflow in libtorch_stable/layernorm_kernels.cu pointer arithmetic

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: The expression: `blockIdx.x * hidden_size` can exceed `2^32-1` for sufficiently large values of `blockIdx.x` and `hidden_size`. https://github.com/vllm-project/vllm/blob/ff712f6447093d07747c88680b9d006b119f5890/csrc/lay...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: size` overflows. log: ``` rms_norm out shape torch.Size([1048641, 4096]) dtype torch.float16 x shape torch.Size([1048641, 4096]) dtype torch.float16 weight shape torch.Size([4096]) dtype torch.float16 ``` ### Before sub...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency;shape #42863 [Bug] Fix integer overflow in layernorm_kernels.cu pointer arithmetic | #43166 [Bug]...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: w in layernorm_kernels.cu when handling long sequences. The expression: `blockIdx.x * hidden_size` can exceed `2^32-1` for sufficiently large values of `blockIdx.x` and `hidden_size`. https://github.com/vllm-project/vll...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42863](https://github.com/vllm-project/vllm/pull/42863) | closes_keyword | 0.95 | [Bug] Fix integer overflow in layernorm_kernels.cu pointer arithmetic | Fixes #42862. --- ### AI assistance disclosure This PR was prepared with the assistance of an AI coding tool (Claude). The bug diagnosis, the per-site classification into buggy |
| [#43166](https://github.com/vllm-project/vllm/pull/43166) | closes_keyword | 0.95 | [Bug] Fix fused_qk_norm_rope 32-bit QKV offset overflow | fixes the same overflow class in `activation_kernels.cu` and lists `fused_qknorm_rope` as out of scope. - #42862 tracks `layernorm_kernels.cu`; this PR is for `fused_qknorm_rope_ke |
| [#44027](https://github.com/vllm-project/vllm/pull/44027) | closes_keyword | 0.95 | [Bugfix] Fix integer overflow in libtorch_stable/layernorm_kernels.cu pointer arithmetic | Closes #42862 ## Test Plan - [ ] Build + relevant layernorm tests via CI. ## Duplicate-work check `gh pr list --repo vllm-project/vllm --state open --search "libtorch_stable la |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
