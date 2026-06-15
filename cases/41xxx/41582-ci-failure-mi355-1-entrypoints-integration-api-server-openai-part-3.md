# vllm-project/vllm#41582: [CI Failure]:  mi355_1: Entrypoints Integration (API Server openai - Part 3)

| 字段 | 值 |
| --- | --- |
| Issue | [#41582](https://github.com/vllm-project/vllm/issues/41582) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Entrypoints Integration (API Server openai - Part 3)

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-entrypoints-integration-api-server-openai---part-3 && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && export VLLM_WORKER_MULTIPROC_METHOD=spawn && pytest -v -s entrypoints/openai --ignore=entrypoints/openai/chat_completion/test_audio.py --ignore=entrypoints/openai/completion/test_shutdown.py --ignore=entrypoints/openai/test_completion.py --ignore=entrypoints/openai/models/test_models.py --ignore=entrypoints/openai/test_return_tokens_as_ids.py --ignore=entrypoints/openai/chat_completion/test_root_path.py --ignore=entrypoints/openai/completion/test_prompt_validation.py --ignore=entrypoints/openai/chat_completion --ignore=entrypoints/openai/completion --ignore=entrypoints/openai/speech_to_text/ --ignore=entrypoints/openai/correctness/ --ignore=entrypoints/openai/tool_parsers/ --ignore=entrypoints/openai/responses --ignore=entrypoints/openai/test_multi_api_servers.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED entrypoints/openai/realtime/te...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: I Server openai - Part 3) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-entrypoints-integration-api-server-openai---part-3 && export VLLM_ALLOW_DEPRECATED_BEAM_SE...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Entrypoints Integration (API Server openai - Part 3) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-entrypoints-integration-api-server-opena
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: re=entrypoints/openai/test_completion.py --ignore=entrypoints/openai/models/test_models.py --ignore=entrypoints/openai/test_return_tokens_as_ids.py --ignore=entrypoints/openai/chat_completion/test_root_path.py --ignore=...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: multi_api_servers.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED entrypoints/openai/real...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Integration (API Server openai - Part 3) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-entrypoints-integration-api-server-openai---part-3 && export VLLM_ALLOW_DEP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
