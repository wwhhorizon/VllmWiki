# vllm-project/vllm#29466: [CI Failure]: mi325_1: Language Models Test (Extended Pooling)

| 字段 | 值 |
| --- | --- |
| Issue | [#29466](https://github.com/vllm-project/vllm/issues/29466) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | attention |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Language Models Test (Extended Pooling)

### Issue 正文摘录

### Name of failing test `pytest -v -s models/language/pooling -m 'not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **33 pooling model tests** - Various correctness and functionality tests across multiple pooling tasks #### Failed Test Categories: **1. Prefix caching tests (3 failures)** - `test_auto_prefix_cache_support.py` - `test_non_causal_models` for intfloat/e5-small, Alibaba-NLP/gte-Qwen2-1.5B-instruct, papluca/xlm-roberta-base-language-detection **2. Embedding tests (2 failures)** - `test_embedding.py` - sentence-transformers/all-MiniLM-L12-v2, intfloat/multilingual-e5-small **3. GritLM tests (2 failures)** - `test_gritlm.py` - `test_gritlm_offline_embedding`, `test_gritlm_api_server_embedding` **4. Classification tests (2 failures)** - `test_head_dtype.py`: nie3e/sentiment-polish-gpt2-small - `test_multilabel_classification_support.py`: Rami/multi-label-class-classification-on-github-issues **5. Nomic model configuration tests (6 failures)** - `test_nomic_max_model_len.py` - Various configuration validation tests **6. Pooler config tests (3 fa...

## 现有链接修复摘要

#31084 Fix ROCm attention backend selection for encoder-only models

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [CI Failure]: mi325_1: Language Models Test (Extended Pooling) ci-failure ### Name of failing test `pytest -v -s models/language/pooling -m 'not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce lo...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: -m 'not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **33 pooling model tests** - Variou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: auto_prefix_cache_support.py` - `test_non_causal_models` for intfloat/e5-small, Alibaba-NLP/gte-Qwen2-1.5B-instruct, papluca/xlm-roberta-base-language-detection **2. Embedding tests (2 failures)** - `test_embedding.py`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Language Models Test (Extended Pooling) ci-failure ### Name of failing test `pytest -v -s models/language/pooling -m 'not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce l
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_1: Language Models Test (Extended Pooling) ci-failure ### Name of failing test `pytest -v -s models/language/pooling -m 'not core_model'` ### Basic information - [ ] Flaky test - [x] Can reproduce lo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31084](https://github.com/vllm-project/vllm/pull/31084) | closes_keyword | 0.95 | Fix ROCm attention backend selection for encoder-only models | Fixes #29466 - 33 failing pooling model tests on ROCm This PR fixes the attention backend selection for encoder-only models (embeddings, cross-encoders, classifiers) on ROCm by us |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
