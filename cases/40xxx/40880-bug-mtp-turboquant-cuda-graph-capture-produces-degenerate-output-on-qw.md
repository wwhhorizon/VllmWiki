# vllm-project/vllm#40880: [Bug]: MTP × TurboQuant × CUDA graph capture produces degenerate output on Qwen3-Next hybrid (not closed by v7.13 ngram fix tree)

| 字段 | 值 |
| --- | --- |
| Issue | [#40880](https://github.com/vllm-project/vllm/issues/40880) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: MTP × TurboQuant × CUDA graph capture produces degenerate output on Qwen3-Next hybrid (not closed by v7.13 ngram fix tree)

### Issue 正文摘录

### Summary **MTP speculative decoding × TurboQuant KV cache × CUDA graph capture produces degenerate output on Qwen3-Next hybrid models.** The four upstream PRs that fixed the ngram path (#40738 + #36138 + #40783 + #39055, plus the `prompt_lookup_min=8` config trick from #40875) do **not** close this for MTP — the MTP forward path goes through a different proposer (`EagleProposer` configured with `method="mtp"`) that the ngram-scoped fixes don't cover. Filed at @Sandermage's [explicit suggestion](https://github.com/vllm-project/vllm/issues/40831#issuecomment-4319965017): *"we did not test MTP at all in the v7.13 cycle... your data shows that assumption is wrong."* ### Reproducer Image: `vllm/vllm-openai@sha256:9bba4628a3b943e0dd33caefb94b811569ba1e97bdf23bee19a265c31b947ccb` (`v0.19.2rc1.dev21+g893611813`). Hardware: 1× RTX 3090 (Ampere SM 8.6). Model: `Lorbus/Qwen3.6-27B-int4-AutoRound`. Genesis v7.13 backports applied via [Sandermage/genesis-vllm-patches@852b73f](https://github.com/Sandermage/genesis-vllm-patches/tree/852b73f) — log confirms `Genesis Results: 25 applied, 16 skipped, 0 failed` including P60 (#40738 Phase 1) + P60b (#40738 Phase 2 Triton kernel offset). ```bash v...

## 现有链接修复摘要

#40738 [Bugfix] Fix GDN conv + SSM state corruption with ngram spec decode | #40914 [Bugfix][Spec-Decode] TurboQuant K+1 spec-verify routing (fixes #40880) | #43747 [Bugfix][TurboQuant] Fix CUDA graph capture crash with spec-decode + chunked-prefill (#40807)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ) that the ngram-scoped fixes don't cover. Filed at @Sandermage's [explicit suggestion](https://github.com/vllm-project/vllm/issues/40831#issuecomment-4319965017): *"we did not test MTP at all in the v7.13 cycle... your...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: MTP × TurboQuant × CUDA graph capture produces degenerate output on Qwen3-Next hybrid (not closed by v7.13 ngram fix tree) ### Summary **MTP speculative decoding × TurboQuant KV cache × CUDA graph capture produce...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: wen3-Next hybrid (not closed by v7.13 ngram fix tree) ### Summary **MTP speculative decoding × TurboQuant KV cache × CUDA graph capture produces degenerate output on Qwen3-Next hybrid models.** The four upstream PRs tha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: MTP × TurboQuant × CUDA graph capture produces degenerate output on Qwen3-Next hybrid (not closed by v7.13 ngram fix tree) ### Summary **MTP speculative decoding × TurboQuant KV cache × CUDA graph capture produce...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: "auto", "max_tokens": 256, "chat_template_kwargs": {"enable_thinking": False}, } r = urllib.request.urlopen(urllib.request.Request( "http://localhost:8020/v1/chat/completions", data=json.dumps(body).encode(), headers={"...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40738](https://github.com/vllm-project/vllm/pull/40738) | mentioned | 0.45 | [Bugfix] Fix GDN conv + SSM state corruption with ngram spec decode | t/vllm/issues/40875) — ngram `prompt_lookup_min=8` config-only fix - [#40738](https://github.com/vllm-project/vllm/pull/40738) — @tdoublep's gdn+ngram state recovery (scope-limite… |
| [#40914](https://github.com/vllm-project/vllm/pull/40914) | closes_keyword | 0.95 | [Bugfix][Spec-Decode] TurboQuant K+1 spec-verify routing (fixes #40880) | fix. ## Stakeholders / for awareness - @noonghunna — reported #40880, multi-rig confirmation. Their `patch_tolist_cudagraph.py` was the first capture-guard prototype in the wild. |
| [#43747](https://github.com/vllm-project/vllm/pull/43747) | closes_keyword | 0.95 | [Bugfix][TurboQuant] Fix CUDA graph capture crash with spec-decode + chunked-prefill (#40807) | fixes Layer 1 (the `.tolist()` crash) which had **no open PR**. ## Related Issues - #40807 — primary issue (this PR) - #40880 — MTP × TurboQuant × CUDA graph degenerate output (c |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
