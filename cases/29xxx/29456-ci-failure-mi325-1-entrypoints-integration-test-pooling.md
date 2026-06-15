# vllm-project/vllm#29456: [CI Failure]: mi325_1: Entrypoints Integration Test (Pooling)

| 字段 | 值 |
| --- | --- |
| Issue | [#29456](https://github.com/vllm-project/vllm/issues/29456) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 | build_error;crash;import_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Entrypoints Integration Test (Pooling)

### Issue 正文摘录

### Name of failing test `pytest -v -s entrypoints/pooling` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test collection fails for `tests/entrypoints/pooling/correctness/test_mteb_embed.py`. **Failure:** ImportError at line 7 during test module import, preventing test collection. Out of 37 collected items, 2 have collection errors and 9 are skipped. The specific import causing the failure is not shown in the truncated traceback. **Test scope:** The command `pytest -v -s entrypoints/pooling` attempts to run all pooling endpoint tests, but fails during the collection phase before any tests execute. **Likely cause:** Missing dependency in the test file. Many pooling tests skip on ROCm with "Encoder self-attention is not implemented on ROCm", suggesting the import may be attempting to load a component not available for the selected attention backend. ### 📝 History of failing test AMD-CI build Buildkite references: - 1041 - 1077 - 1088 - 1109 - 1111 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: mi325_1: Entrypoints Integration Test (Pooling) ci-failure ### Name of failing test `pytest -v -s entrypoints/pooling` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by ex
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: attempting to load a component not available for the selected attention backend. ### 📝 History of failing test AMD-CI build Buildkite references: - 1041 - 1077 - 1088 - 1109 - 1111 ### CC List. _No response_ correctness...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: entrypoints/pooling` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test collection fails for `tests/en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cause:** Missing dependency in the test file. Many pooling tests skip on ROCm with "Encoder self-attention is not implemented on ROCm", suggesting the import may be attempting to load a component not available for the s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ## Name of failing test `pytest -v -s entrypoints/pooling` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
