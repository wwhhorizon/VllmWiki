# vllm-project/vllm#41638: [Bug]: Batch invariant mode does not work for Kimi K2.6

| 字段 | 值 |
| --- | --- |
| Issue | [#41638](https://github.com/vllm-project/vllm/issues/41638) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Batch invariant mode does not work for Kimi K2.6

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Worker failures when running Kimi-K2.6 with `VLLM_BATCH_INVARIANT=1` on the vLLM 0.20.1 image. Setup: - Model: Kimi-K2.6 - vLLM image/version: 0.20.1 - TP: 8 - `--mm-encoder-tp-mode=data` - `--trust-remote-code` - Tool parser + reasoning parser enabled With default dtype / `--dtype=auto`, startup or inference fails with: Error encountered ```text RuntimeError: Worker failed with error 'expected scalar type Float but found BFloat16', please check the stack trace above for the root cause ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ANT=1` on the vLLM 0.20.1 image. Setup: - Model: Kimi-K2.6 - vLLM image/version: 0.20.1 - TP: 8 - `--mm-encoder-tp-mode=data` - `--trust-remote-code` - Tool parser + reasoning parser enabled With default dtype / `--dtyp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rust-remote-code` - Tool parser + reasoning parser enabled With default dtype / `--dtype=auto`, startup or inference fails with: Error encountered ```text RuntimeError: Worker failed with error 'expected scalar type Flo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf dtype;env_dependency;shape Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: i-K2.6 with `VLLM_BATCH_INVARIANT=1` on the vLLM 0.20.1 image. Setup: - Model: Kimi-K2.6 - vLLM image/version: 0.20.1 - TP: 8 - `--mm-encoder-tp-mode=data` - `--trust-remote-code` - Tool parser + reasoning parser enable...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
