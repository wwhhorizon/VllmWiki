# vllm-project/vllm#41871: [Bug]: Stale Triton kernel cache on DGX Spark (sm_121) produces silently garbled outputs — wiping ~/.triton/cache restores correctness

| 字段 | 值 |
| --- | --- |
| Issue | [#41871](https://github.com/vllm-project/vllm/issues/41871) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | attention;cuda;kernel;triton |
| 症状 | crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Stale Triton kernel cache on DGX Spark (sm_121) produces silently garbled outputs — wiping ~/.triton/cache restores correctness

### Issue 正文摘录

### Summary On NVIDIA DGX Spark (GB10, sm_121) running torch 2.11.0+cu130 + triton 3.6.0, gpt-oss-20b returned semantically corrupted outputs — foreign-script glyphs mixed into otherwise English text, malformed Harmony tool-call headers (e.g. ` 1` instead of ` json`), and intermittent 500s in the responses parser. Wiping `~/.triton/cache` and restarting restored fully clean, well-formed outputs with zero garbled-token warnings. ### Environment - Hardware: NVIDIA GB10 (Blackwell, compute capability 12.1 / sm_121) - Arch: aarch64 Linux - torch: 2.11.0+cu130 (`torch.cuda.get_arch_list()` = `[..., 'sm_120']` — sm_121 not present, falls back to sm_120 PTX → JIT) - triton: 3.6.0 - vLLM: 0.16.0rc1.dev2814+ge151cd6a6 - Model: `openai/gpt-oss-20b` ### Reproducer 1. On a GB10 host with stale `~/.triton/cache` (entries built by an older torch/triton combo), run gpt-oss-20b. 2. Send any chat completion or `/v1/responses` request. 3. Observe: outputs contain mixed-script garble; tool-call headers are malformed enough to trip the Harmony parser. 4. Stop server, `rm -rf ~/.triton/cache`, restart. 5. Outputs are clean and well-formed; zero garbled-token warnings in the same code paths. ### Likely...

## 现有链接修复摘要

#42859 [Platform][CUDA] Warn on PTX fallback and optionally invalidate Triton cache (sm_121)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Stale Triton kernel cache on DGX Spark (sm_121) produces silently garbled outputs — wiping ~/.triton/cache restores correctness ### Summary On NVIDIA DGX Spark (GB10, sm_121) running torch 2.11.0+cu130 + triton 3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Stale Triton kernel cache on DGX Spark (sm_121) produces silently garbled outputs — wiping ~/.triton/cache restores correctness ### Summary On NVIDIA DGX Spark (GB10, sm_121) running torch 2.11.0+cu130 + triton 3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Stale Triton kernel cache on DGX Spark (sm_121) produces silently garbled outputs — wiping ~/.triton/cache restores correctness ### Summary On NVIDIA DGX Spark (GB10, sm_121) running torch 2.11.0+cu130 + triton 3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: /JIT cache key does not reflect every variable that actually changes the compiled PTX → SASS path on sm_121 fallback. Artifacts compiled under one (torch, triton, driver, arch-fallback) combination get reused later unde...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: anded in the output. After ruling out attention backend swaps (gpt-oss + mxfp4 only exposes `TRITON_ATTN`), we wiped `~/.triton/cache`. Next run: clean Harmony stream, valid tool calls, no parser recovery warnings. ###...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42859](https://github.com/vllm-project/vllm/pull/42859) | closes_keyword | 0.95 | [Platform][CUDA] Warn on PTX fallback and optionally invalidate Triton cache (sm_121) | fix the issue also proposes is out of scope here — that has to happen upstream in Triton. ### Not a duplicate - #41871 has no open PR (`gh pr list --search "41871 in:body"` is emp |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
