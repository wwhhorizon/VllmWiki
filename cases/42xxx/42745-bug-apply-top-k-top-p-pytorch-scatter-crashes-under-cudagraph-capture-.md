# vllm-project/vllm#42745: [Bug]: `apply_top_k_top_p_pytorch` `scatter_` crashes under cudagraph capture on sm_121a (Blackwell GB10)

| 字段 | 值 |
| --- | --- |
| Issue | [#42745](https://github.com/vllm-project/vllm/issues/42745) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `apply_top_k_top_p_pytorch` `scatter_` crashes under cudagraph capture on sm_121a (Blackwell GB10)

### Issue 正文摘录

On a DGX Spark (GB10, sm_121a) running vLLM 0.20.0 with speculative decoding enabled and the FlashInfer sampler unavailable, the PyTorch-native fallback `apply_top_k_top_p_pytorch` crashes the engine on any request with `top_p > 0` or `top_k > 0`: ``` torch.AcceleratorError: CUDA error: operation not permitted File "vllm/v1/sample/ops/topk_topp_sampler.py", line 427 (main) / line 299 (v0.20.0), in apply_top_k_top_p_pytorch logits.scatter_(dim=-1, index=logits_idx, src=logits_sort) ``` The truncated text is the standard "operation not permitted when stream is capturing" — see pytorch/pytorch#87794. `cudagraph_mode` is already being downgraded to PIECEWISE under spec at startup (separate well-documented interaction), but the `scatter_` still ends up inside a captured region and faults. `EngineCoreError` cascades to 500s on subsequent requests, container exits. Why we hit the PyTorch-native fallback at all: FlashInfer's JIT-time arch detection rejects `sm_121a` (12.1a), so vLLM falls back. The Avarok-Cybersecurity/dgx-vllm fork patches FlashInfer for sm_121 in other modules but not in the sampler. ## Repro ``` docker run -e MODEL= ... \ vllm/vllm-openai \ ... --speculative-config '{"...

## 现有链接修复摘要

#42866 [Bugfix] v1/sample: use out-of-place scatter in apply_top_k_top_p_pytorch

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Infer for sm_121 in other modules but not in the sampler. ## Repro ``` docker run -e MODEL= ... \ vllm/vllm-openai \ ... --speculative-config '{"method":"ngram","num_speculative_tokens":8}' # Send any request with top_p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: `apply_top_k_top_p_pytorch` `scatter_` crashes under cudagraph capture on sm_121a (Blackwell GB10) On a DGX Spark (GB10, sm_121a) running vLLM 0.20.0 with speculative decoding enabled and the FlashInfer sampler u...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: , sm_121a) running vLLM 0.20.0 with speculative decoding enabled and the FlashInfer sampler unavailable, the PyTorch-native fallback `apply_top_k_top_p_pytorch` crashes the engine on any request with `top_p > 0` or `top...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 21 in other modules but not in the sampler. ## Repro ``` docker run -e MODEL= ... \ vllm/vllm-openai \ ... --speculative-config '{"method":"ngram","num_speculative_tokens":8}' # Send any request with top_p: 0.8, top_k:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: (Blackwell GB10) On a DGX Spark (GB10, sm_121a) running vLLM 0.20.0 with speculative decoding enabled and the FlashInfer sampler unavailable, the PyTorch-native fallback `apply_top_k_top_p_pytorch` crashes the engine on...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42866](https://github.com/vllm-project/vllm/pull/42866) | closes_keyword | 0.95 | [Bugfix] v1/sample: use out-of-place scatter in apply_top_k_top_p_pytorch | Fixes #42745. `apply_top_k_top_p_pytorch` uses an in-place `scatter_` to restore sorted logits to their original positions: ```python return logits.scatter_(dim=-1, index=logits_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
