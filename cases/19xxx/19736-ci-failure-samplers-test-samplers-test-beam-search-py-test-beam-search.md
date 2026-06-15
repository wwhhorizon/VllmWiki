# vllm-project/vllm#19736: [CI Failure]: Samplers Test - samplers/test_beam_search.py::test_beam_search_passes_multimodal_data

| 字段 | 值 |
| --- | --- |
| Issue | [#19736](https://github.com/vllm-project/vllm/issues/19736) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;gemm;quantization;sampling |
| 症状 | oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Samplers Test - samplers/test_beam_search.py::test_beam_search_passes_multimodal_data

### Issue 正文摘录

### Name of failing test `samplers/test_beam_search.py::test_beam_search_passes_multimodal_data[False-2-64-half]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test It seems the issue is because we are now passing empty lists to _flatten_embeddings ``` FAILED samplers/test_beam_search.py::test_beam_search_passes_multimodal_data[False-2-64-half] - RuntimeError: torch.cat(): expected a non-empty list of Tensors ``` Full output: ``` pytest -s -v "samplers/test_beam_search.py::test_beam_search_passes_multimodal_data[False-2-64-half]" INFO 06-17 09:19:56 [__init__.py:244] Automatically detected platform cuda. /home/mgoin/venvs/vllm/lib/python3.12/site-packages/pytest_asyncio/plugin.py:208: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset. The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: ]: Samplers Test - samplers/test_beam_search.py::test_beam_search_passes_multimodal_data ci-failure ### Name of failing test `samplers/test_beam_search.py::test_beam_search_passes_multimodal_data[False-2-64-half]` ### B...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [CI Failure]: Samplers Test - samplers/test_beam_search.py::test_beam_search_passes_multimodal_data ci-failure ### Name of failing test `samplers/test_beam_search.py::test_beam_search_passes_multimodal_data[False-2-64-ha
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: a[False-2-64-half] WARNING 06-17 09:19:58 [config.py:3273] Casting torch.bfloat16 to torch.float16. Loading checkpoint shards: 100%|███████████████████████████████████████████████████████████████████████████████████████...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: Samplers Test - samplers/test_beam_search.py::test_beam_search_passes_multimodal_data ci-failure ### Name of failing test `samplers/test_beam_search.py::test_beam_search_passes_multimodal_data[False-2-64-h...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: `samplers/test_beam_search.py::test_beam_search_passes_multimodal_data[False-2-64-half]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`)...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
