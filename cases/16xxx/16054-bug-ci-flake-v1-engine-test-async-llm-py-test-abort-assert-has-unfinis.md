# vllm-project/vllm#16054: [Bug]: CI flake - v1/engine/test_async_llm.py::test_abort - assert has_unfinished_requests()

| 字段 | 值 |
| --- | --- |
| Issue | [#16054](https://github.com/vllm-project/vllm/issues/16054) |
| 状态 | closed |
| 标签 | bug;ci/build;stale;v1 |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CI flake - v1/engine/test_async_llm.py::test_abort - assert has_unfinished_requests()

### Issue 正文摘录

### Your current environment ... ### 🐛 Describe the bug main commit 51d7c6a2b23e100cd9e7d85b8e7c0eea656b331e Seen in https://github.com/vllm-project/vllm/pull/15894 https://buildkite.com/organizations/vllm/pipelines/ci/builds/16742/jobs/0195f24d-e81a-46a3-ad08-6a51983d65d6/log ``` =================================== FAILURES =================================== [2025-04-01T17:38:12Z] _ test_abort[engine_args0-Hello my name is Robert and-RequestOutputKind.DELTA] _ [2025-04-01T17:38:12Z] [2025-04-01T17:38:12Z] monkeypatch = [2025-04-01T17:38:12Z] output_kind = [2025-04-01T17:38:12Z] engine_args = AsyncEngineArgs(model='meta-llama/Llama-3.2-1B-Instruct', served_model_name=None, tokenizer='meta-llama/Llama-3.2-1B-I...additional_config=None, enable_reasoning=None, reasoning_parser=None, use_tqdm_on_load=True, disable_log_requests=True) [2025-04-01T17:38:12Z] prompt = 'Hello my name is Robert and' [2025-04-01T17:38:12Z] [2025-04-01T17:38:12Z] @pytest.mark.parametrize( [2025-04-01T17:38:12Z] "output_kind", [RequestOutputKind.DELTA, RequestOutputKind.FINAL_ONLY]) [2025-04-01T17:38:12Z] @pytest.mark.parametrize("engine_args,prompt", [2025-04-01T17:38:12Z] [(TEXT_ENGINE_ARGS, TEXT_PROMPT), [...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 2Z] output_kind = [2025-04-01T17:38:12Z] engine_args = AsyncEngineArgs(model='meta-llama/Llama-3.2-1B-Instruct', served_model_name=None, tokenizer='meta-llama/Llama-3.2-1B-I...additional_config=None, enable_reasoning=No...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: flake - v1/engine/test_async_llm.py::test_abort - assert has_unfinished_requests() bug;ci/build;stale;v1 ### Your current environment ... ### 🐛 Describe the bug main commit 51d7c6a2b23e100cd9e7d85b8e7c0eea656b331e Seen...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: CI flake - v1/engine/test_async_llm.py::test_abort - assert has_unfinished_requests() bug;ci/build;stale;v1 ### Your current environment ... ### 🐛 Describe the bug main commit 51d7c6a2b23e100cd9e7d85b8e7c0eea656b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [2025-04-01T17:38:12Z] idx in REQUEST_IDS_TO_ABORT) else NUM_EXPECTED_TOKENS [2025-04-01T17:38:12Z] n = 3 if idx in PARALLEL_SAMPLE_REQ_IDS else 1 [2025-04-01T17:38:12Z] tasks.append( [2025-04-01T17:38:12Z] asyncio.crea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
