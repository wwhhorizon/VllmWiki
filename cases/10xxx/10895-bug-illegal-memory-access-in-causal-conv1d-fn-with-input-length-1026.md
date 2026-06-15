# vllm-project/vllm#10895: [Bug]: illegal memory access in `causal_conv1d_fn` with input length 1026

| 字段 | 值 |
| --- | --- |
| Issue | [#10895](https://github.com/vllm-project/vllm/issues/10895) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: illegal memory access in `causal_conv1d_fn` with input length 1026

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I encountered an **illegal memory access** error when using the `causal_conv1d_fn` function with an input tensor shape of [1, dim, 1026]. This issue does not occur with other sequence lengths like 1024 or 1028. ### Reproduction code ```python from vllm.model_executor.layers.mamba.ops.causal_conv1d import causal_conv1d_fn import torch # from causal_conv1d import causal_conv1d_fn dim = 1024 seq_len = 1026 x = ( torch.randn(1, dim, seq_len).to(torch.bfloat16).cuda() ) weight = ( torch.randn(dim, 4).to(torch.bfloat16).cuda() ) activation = "silu" output = causal_conv1d_fn(x, weight, None, activation=activation) print(output) ``` ### Observation The illegal memory access error did not occur when I used the ·causal_conv1d· function from the [causal_conv1d](https://github.com/Dao-AILab/causal-conv1d) repository instead of causal_conv1d_fn. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#10928 [BugFix][Kernel]: fix illegal memory access in causal_conv1d when conv_states is None

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n code ```python from vllm.model_executor.layers.mamba.ops.causal_conv1d import causal_conv1d_fn import torch # from causal_conv1d import causal_conv1d_fn dim = 1024 seq_len = 1026 x = ( torch.randn(1, dim, seq_len).to(...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m = 1024 seq_len = 1026 x = ( torch.randn(1, dim, seq_len).to(torch.bfloat16).cuda() ) weight = ( torch.randn(dim, 4).to(torch.bfloat16).cuda() ) activation = "silu" output = causal_conv1d_fn(x, weight, None, activation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eq_len = 1026 x = ( torch.randn(1, dim, seq_len).to(torch.bfloat16).cuda() ) weight = ( torch.randn(dim, 4).to(torch.bfloat16).cuda() ) activation = "silu" output = causal_conv1d_fn(x, weight, None, activation=activatio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t;sampling_logits;speculative_decoding activation;cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency;shape #10928 [BugFix][Kernel]: fix illegal memory access in causal_conv1d when conv_states is None...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nv1d_fn` with input length 1026 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I encountered an **illegal memory access** error when using the `causal_conv1d_fn` function wit...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#10928](https://github.com/vllm-project/vllm/pull/10928) | closes_keyword | 0.95 | [BugFix][Kernel]: fix illegal memory access in causal_conv1d when conv_states is None | fix #10895 Issue #10895 reports an illegal memory access error on H100 GPUs when calling the `causal_conv1d_fn` function with specific input shapes and when `conv_states` is not |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
