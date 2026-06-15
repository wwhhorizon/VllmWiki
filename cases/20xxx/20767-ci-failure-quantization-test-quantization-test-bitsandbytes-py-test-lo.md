# vllm-project/vllm#20767: [CI Failure]: Quantization Test - quantization/test_bitsandbytes.py::test_load_4bit_bnb_model

| 字段 | 值 |
| --- | --- |
| Issue | [#20767](https://github.com/vllm-project/vllm/issues/20767) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Quantization Test - quantization/test_bitsandbytes.py::test_load_4bit_bnb_model

### Issue 正文摘录

### Name of failing test `quantization/test_bitsandbytes.py::test_load_4bit_bnb_model[facebook/opt-125m-quantize opt model inflight]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There are quite a few failing bnb tests https://buildkite.com/vllm/ci/builds/23559/steps/canvas?sid=0197f23d-c9e5-45de-b07a-5e290ae4a6ce ``` [2025-07-10T04:47:11Z] FAILED quantization/test_bitsandbytes.py::test_load_4bit_bnb_model[facebook/opt-125m-quantize opt model inflight] - AssertionError: function failed when called with args () and kwargs {'hf_runner': , 'vllm_runner': , 'example_prompts': ['vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs.\n', 'Briefly describe the major milestones in the development of artificial intelligence from 1950 to 2020.\n', 'Compare and contrast artificial intelligence with human intelligence in terms of processing information.\n', 'Describe the basic components of a neural network and how it can be trained.\n', 'Write a short story about a robot that dreams for the first time.\n', 'Analyze the impact of the COVID-19 pan...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: uantization Test - quantization/test_bitsandbytes.py::test_load_4bit_bnb_model stale;ci-failure ### Name of failing test `quantization/test_bitsandbytes.py::test_load_4bit_bnb_model[facebook/opt-125m-quantize opt model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [CI Failure]: Quantization Test - quantization/test_bitsandbytes.py::test_load_4bit_bnb_model stale;ci-failure ### Name of failing test `quantization/test_bitsandbytes.py::test_load_4bit_bnb_model[facebook/opt-125m-quan...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Quantization Test - quantization/test_bitsandbytes.py::test_load_4bit_bnb_model stale;ci-failure ### Name of failing test `quantization/test_bitsandbytes.py::test_load_4bit_bnb_model[facebook/opt-125m-quant
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: Quantization Test - quantization/test_bitsandbytes.py::test_load_4bit_bnb_model stale;ci-failure ### Name of failing test `quantization/test_bitsandbytes.py::test_load_4bit_bnb_model[facebook/opt-125m-quan...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: opt model inflight]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There are quite a few failing bnb t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
