# vllm-project/vllm#43753: [Performance]: DeepSeek-V4-Pro 128K+ timeout on deepseekv4-cu130; nightly aa2b56f completes 1M real-prose checks on 8x B200

| 字段 | 值 |
| --- | --- |
| Issue | [#43753](https://github.com/vllm-project/vllm/issues/43753) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: DeepSeek-V4-Pro 128K+ timeout on deepseekv4-cu130; nightly aa2b56f completes 1M real-prose checks on 8x B200

### Issue 正文摘录

### Summary On a single Nebius 8x NVIDIA B200 SXM6 node, `vllm/vllm-openai:deepseekv4-cu130` timed out at the 3600 s client deadline for coherent real-prose, completion-style DeepSeek-V4-Pro requests at 128K, 512K, and 1M input tokens under the published DeepSeek-V4 launch recipe. As a positive control, `vllm/vllm-openai:nightly` build `0.21.1rc1.dev281+gaa2b56ffb` / commit `aa2b56f` completed the same coherent real-prose checks through 1,042,080 input tokens on the same 8x B200 host. The long-context cells are limited-sample checks: n=1 per context length, plus one `nsys` repeat for the nightly 1M path. This report documents that image-specific delta and provides enough environment/kernel evidence for maintainers to decide whether the cu130 path is stale, missing a fix, or should be replaced in docs or recipes. This is not a claim that V4-Pro is generally production-ready on B200. The passing path is a nightly image plus a one-line local derived layer, and the long-context cells are limited-sample validation. ### Maintainer asks 1. Is `vllm/vllm-openai:deepseekv4-cu130` expected to remain supported for DeepSeek-V4, or should users move to a newer nightly or stable image? 2. Is th...

## 现有链接修复摘要

#27114 [Bugfix] Use PIECEWISE cudagraphs on Blackwell if max_model_len > 131072

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: 128K, 512K, and 1M input tokens under the published DeepSeek-V4 launch recipe. As a positive control, `vllm/vllm-openai:nightly` build `0.21.1rc1.dev281+gaa2b56ffb` / commit `aa2b56f` completed the same coherent real-pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: hon | 3.12.13 | | CUDA / PyTorch | CUDA 13.0, PyTorch `2.11.0+cu130` | | Triton | 3.6.0 | | FlashInfer | 0.6.11.post2 | | Transformers / Accelerate | Transformers 5.9.0, Accelerate 1.13.0 | | NCCL | 2.28.9 via `torch.cu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: -name deepseek-ai/DeepSeek-V4-Pro \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 8 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: n deepseekv4-cu130; nightly aa2b56f completes 1M real-prose checks on 8x B200 ### Summary On a single Nebius 8x NVIDIA B200 SXM6 node, `vllm/vllm-openai:deepseekv4-cu130` timed out at the 3600 s client deadline for cohe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: lient deadline for coherent real-prose, completion-style DeepSeek-V4-Pro requests at 128K, 512K, and 1M input tokens under the published DeepSeek-V4 launch recipe. As a positive control, `vllm/vllm-openai:nightly` build...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27114](https://github.com/vllm-project/vllm/pull/27114) | mentioned | 0.45 | [Bugfix] Use PIECEWISE cudagraphs on Blackwell if max_model_len > 131072 | i can split into separate issues (cu130 cliff, pytest import path, pr #27114 / piecewise on v4-pro) if triage prefers narrower surfaces. ### proof artifacts available on request f… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
