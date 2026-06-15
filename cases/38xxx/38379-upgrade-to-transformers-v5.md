# vllm-project/vllm#38379: Upgrade to Transformers v5

| 字段 | 值 |
| --- | --- |
| Issue | [#38379](https://github.com/vllm-project/vllm/issues/38379) |
| 状态 | open |
| 标签 | help wanted |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm |
| 子分类 | wrong_output |
| Operator 关键词 | attention |
| 症状 | mismatch |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Upgrade to Transformers v5

### Issue 正文摘录

## What is this issue? This issue serves as a living tracker for the current issues preventing us from upgrading vLLM to Transformers v5. We will use sub-issues to track individual failures and PRs should be made against these sub-issues. The solutions to these issues may need to be applied to either: - Transformers in the form of: - Adding missing backward compatibility (usually for custom code models) - General bug fixes/improvements to new features of v5 - vLLM in the form of: - Forward compatibility with how something is now done in v5 - Edge case handling for issues that v4 ignored (such as config validation) Sometimes, the issue is simply with the model checkpoint itself, for example if it: - Contains a malformed `config.json` that cannot be used to instantiate the newly input validated `PreTrainedConfig` class - Custom code* uses deprecated/removed APIs In these situations, the best solution will likely be to skip these tests in vLLM and open a PR to Transformers to contribute this model. This will be faster and more sustainable than waiting for the model vendor to fix their custom model code, sometimes they nevert do. Contributing the new model should be done using the new...

## 现有链接修复摘要

#43514 [Bugfix] Reject non-positive block_size in CacheConfig

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: m of: - Adding missing backward compatibility (usually for custom code models) - General bug fixes/improvements to new features of v5 - vLLM in the form of: - Forward compatibility with how something is now done in v5 -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: le_correctness_*` — "Feature is experimental and uses too much memory in CI" (TODO from hmellor) ## `tests/models/multimodal/generation/test_common.py` — VLMTestInfo entries newly marked `pytest.mark.skip` - [ ] PR: _TB...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: (entire `run_test` block at line 875) — Custom MBart decoder head-count mismatch with transformers v5 GQA-aware cross-attention (8 vs 16 heads) - [ ] PR: _TBD_ — `tests/models/multimodal/generation/test_voxtral.py::test...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: test/test_jina.py::test_embed_models_correctness` (entire `@parametrize` block at line 759, covers all `EMBEDDING_MODELS` x `dtype=half` x `dimensions=[16, 32]`) — `jinaai/jina-embeddings-v3` custom XLMRobertaLoRA model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: to contribute this model. This will be faster and more sustainable than waiting for the model vendor to fix their custom model code, sometimes they nevert do. Contributing the new model should be done using the new [Mod...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43514](https://github.com/vllm-project/vllm/pull/43514) | mentioned | 0.45 | [Bugfix] Reject non-positive block_size in CacheConfig | -4-reasoning-vision-15b`), cap `5.3` — siglip2 internals removed by hf#43514 above v5.4 - [ ] pr: _tbd_ — `tarsier2forconditionalgeneration` (line ~1267), cap `5.3` — `qwen2vlconf… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
