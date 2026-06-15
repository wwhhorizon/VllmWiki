# vllm-project/vllm#40740: [Bug]: assert is_mixture_of_experts fails on vllm serve with --enable-eplb

| 字段 | 值 |
| --- | --- |
| Issue | [#40740](https://github.com/vllm-project/vllm/issues/40740) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: assert is_mixture_of_experts fails on vllm serve with --enable-eplb

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to initialize vllm for online serving of an MoE model (for example, microsoft/Phi-mini-MoE-instruct ) with expert parallel load balancing enabled I encounter the following error: (Worker_TP0_EP0 pid=890654) ERROR 04-23 21:17:35 [multiproc_executor.py:949] File "/home/dylan/.local/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", line 3093, in eplb_step (Worker_TP0_EP0 pid=890654) ERROR 04-23 21:17:35 [multiproc_executor.py:949] assert is_mixture_of_experts(model) (Worker_TP0_EP0 pid=890654) ERROR 04-23 21:17:35 [multiproc_executor.py:949] AssertionError [vllmtrace_moeassertfail.txt](https://github.com/user-attachments/files/27027800/vllmtrace_moeassertfail.txt) digging into the code base, it seems that this is failing because the type PhiMoEForCausalLM is not implemented in a way which is compatible with EPLB. Everything works as intended when `--enable-eplb` is not included. In addition to microsoft/Phi-mini-MoE-instruct, I repeated these tests with Qwen/Qwen1.5-MoE-A2.7B-Chat and ModelCloud/DeepSeek-V2-Lite-gptq-4bit (using `--quantization aqw` for the latter) with the same results. The issue can be...

## 现有链接修复摘要

#41096 [Bugfix] Raise clear error when --enable-eplb on non-EPLB model | #41097 [Bugfix] Raise clear error when --enable-eplb on non-EPLB model

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: xample, microsoft/Phi-mini-MoE-instruct ) with expert parallel load balancing enabled I encounter the following error: (Worker_TP0_EP0 pid=890654) ERROR 04-23 21:17:35 [multiproc_executor.py:949] File "/home/dylan/.loca...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: assert is_mixture_of_experts fails on vllm serve with --enable-eplb bug ### Your current environment ### 🐛 Describe the bug When trying to initialize vllm for online serving of an MoE model (for example, microsof...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lb` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ibe the bug When trying to initialize vllm for online serving of an MoE model (for example, microsoft/Phi-mini-MoE-instruct ) with expert parallel load balancing enabled I encounter the following error: (Worker_TP0_EP0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;moe;operator;quantization;sampling;triton build_error;nan_inf env_dependency #41096 [Bugfix] Raise clear error when --enable-eplb on non-EPLB model | #41097 [Bugfix] Raise clear err...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41096](https://github.com/vllm-project/vllm/pull/41096) | closes_keyword | 0.95 | [Bugfix] Raise clear error when --enable-eplb on non-EPLB model | Fixes #40740. ## Summary When users pass `--enable-eplb` with a model whose vLLM implementation does not implement the `MixtureOfExperts` interface, the worker silently registers |
| [#41097](https://github.com/vllm-project/vllm/pull/41097) | closes_keyword | 0.95 | [Bugfix] Raise clear error when --enable-eplb on non-EPLB model | Fixes #40740. ## Summary When users pass `--enable-eplb` with a model whose vLLM implementation does not implement the `MixtureOfExperts` interface, the worker silently registers |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
