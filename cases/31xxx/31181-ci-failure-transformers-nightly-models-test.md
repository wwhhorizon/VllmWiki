# vllm-project/vllm#31181: [CI Failure]: Transformers Nightly Models Test

| 字段 | 值 |
| --- | --- |
| Issue | [#31181](https://github.com/vllm-project/vllm/issues/31181) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Transformers Nightly Models Test

### Issue 正文摘录

### Name of failing test `pytest -v -s tests/models/test_initialization.py -k 'not (Gemma3 or ModernBert or Qwen2_5_VL or Qwen2_5vl or Qwen2VL or TransformersMultiModalEmbeddingModel or TransformersMultiModalForSequenceClassification or Ultravox or Phi4Multimodal or LlavaNextVideo or MiniCPMO or Lfm2Moe or PaliGemma or RobertaForSequenceClassification or Ovis2_5 or Fuyu or DeepseekOCR or KimiVL)'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is an issue with latest transformers version, where the test triggers: ``` ImportError while loading conftest '/vllm-workspace/tests/conftest.py'. tests/conftest.py:48: in from tests.models.utils import TokensTextLogprobs, TokensTextLogprobsPromptLogprobs tests/models/utils.py:13: in from vllm.config.model import ModelConfig, ModelDType, RunnerOption /usr/local/lib/python3.12/dist-packages/vllm/config/__init__.py:18: in from vllm.config.model import ( /usr/local/lib/python3.12/dist-packages/vllm/config/model.py:14: in from transformers.configuration_utils import ALLOWED_LAYER_TYPES E ImportError: cannot import name 'ALLOW...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [CI Failure]: Transformers Nightly Models Test ci-failure ### Name of failing test `pytest -v -s tests/models/test_initialization.py -k 'not (Gemma3 or ModernBert or Qwen2_5_VL or Qwen2_5vl or Qwen2VL or TransformersMul...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: Transformers Nightly Models Test ci-failure ### Name of failing test `pytest -v -s tests/models/test_initialization.py -k 'not (Gemma3 or ModernBert or Qwen2_5_VL or Qwen2_5vl or Qwen2VL or TransformersMult
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: failing test `pytest -v -s tests/models/test_initialization.py -k 'not (Gemma3 or ModernBert or Qwen2_5_VL or Qwen2_5vl or Qwen2VL or TransformersMultiModalEmbeddingModel or TransformersMultiModalForSequenceClassificati...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 981/steps/canvas?sid=019b4751-fd00-4c11-880e-60ab16072fa5#019b4751-fd5a-4fa3-a9cd-fcff5c2d1067/L450 ### CC List. _No response_
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pseekOCR or KimiVL)'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is an issue with latest tran...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
