# vllm-project/vllm#29543: [CI Failure]: mi325_2: Distributed Model Tests (2 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#29543](https://github.com/vllm-project/vllm/issues/29543) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_2: Distributed Model Tests (2 GPUs)

### Issue 正文摘录

### Name of failing test `TARGET_TEST_SUITE=L4 pytest basic_correctness/ -v -s -m 'distributed(num_gpus=2)' && CUDA_VISIBLE_DEVICES=0,1 pytest -v -s model_executor/model_loader/test_sharded_state_loader.py && pytest models/test_transformers.py -v -s -m 'distributed(num_gpus=2)' && pytest models/language -v -s -m 'distributed(num_gpus=2)' && pytest models/multimodal -v -s -m 'distributed(num_gpus=2)' --ignore models/multimodal/generation/test_whisper.py && VLLM_WORKER_MULTIPROC_METHOD=spawn pytest models/multimodal/generation/test_whisper.py -v -s -m 'distributed(num_gpus=2)'` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests:** All 11 test files in `tests/models/language/pooling_mteb_test/`: - test_baai.py - test_bge_reranker_v2_gemma.py - test_cross_encoder.py - test_gte.py - test_intfloat.py - test_jina.py - test_mxbai_rerank.py - test_nomic.py - test_qwen3_reranker.py - test_snowflake_arctic_embed.py - test_st_projector.py **Failure:** Collection errors during pytest discovery - tests never executed **Configuration:** Embedding/reranking model MTEB be...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [CI Failure]: mi325_2: Distributed Model Tests (2 GPUs) ci-failure ### Name of failing test `TARGET_TEST_SUITE=L4 pytest basic_correctness/ -v -s -m 'distributed(num_gpus=2)' && CUDA_VISIBLE_DEVICES=0,1 pytest -v -s mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [CI Failure]: mi325_2: Distributed Model Tests (2 GPUs) ci-failure ### Name of failing test `TARGET_TEST_SUITE=L4 pytest basic_correctness/ -v -s -m 'distributed(num_gpus=2)' && CUDA_VISIBLE_DEVICES=0,1 pytest -v -s mode
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_2: Distributed Model Tests (2 GPUs) ci-failure ### Name of failing test `TARGET_TEST_SUITE=L4 pytest basic_correctness/ -v -s -m 'distributed(num_gpus=2)' && CUDA_VISIBLE_DEVICES=0,1 pytest -v -s mod...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ributed(num_gpus=2)'` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests:** All 11 test fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: SUITE=L4 pytest basic_correctness/ -v -s -m 'distributed(num_gpus=2)' && CUDA_VISIBLE_DEVICES=0,1 pytest -v -s model_executor/model_loader/test_sharded_state_loader.py && pytest models/test_transformers.py -v -s -m 'dis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
