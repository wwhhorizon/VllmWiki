# vllm-project/vllm#41719: [Bug]: TokenizersBackend fallback returns tokenizer without `max_chars_per_token`

| 字段 | 值 |
| --- | --- |
| Issue | [#41719](https://github.com/vllm-project/vllm/issues/41719) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TokenizersBackend fallback returns tokenizer without `max_chars_per_token`

### Issue 正文摘录

## Your current environment ## 🐛 Describe the bug ### Summary vLLM has a fallback for models with incorrect Hub tokenizer_class metadata: ```python _MODEL_TYPES_WITH_INCORRECT_TOKENIZER_CLASS = {"step3_vl"} ``` `model_type="step3_vl"` is used by `stepfun-ai/step3`. This fallback returns a bare Transformers TokenizersBackend. Unlike the normal HF tokenizer path, it is not wrapped with get_cached_tokenizer(), so it misses vLLM-required properties such as max_chars_per_token. ### Repro ```python from transformers import PretrainedConfig import vllm.tokenizers.registry as registry from vllm.renderers.params import TokenizeParams registry.get_config = lambda *args, **kwargs: PretrainedConfig(model_type="step3_vl") tok = registry.get_tokenizer("gpt2") params = TokenizeParams(max_total_tokens=10, max_output_tokens=1) print(params._text_len_check(tok, "hello")) ``` ### Actual ```python AttributeError: TokenizersBackend has no attribute max_chars_per_token ``` ### Expected The fallback tokenizer should expose the same cached properties as normal HF tokenizers in vLLM. ### Suggested Fix Wrap the `TokenizersBackend` fallback with `get_cached_tokenizer()`, for example by adding a `CachedToken...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ies such as max_chars_per_token. ### Repro ```python from transformers import PretrainedConfig import vllm.tokenizers.registry as registry from vllm.renderers.params import TokenizeParams registry.get_config = lambda *a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: TokenizersBackend fallback returns tokenizer without `max_chars_per_token` bug ## Your current environment ## 🐛 Describe the bug ### Summary vLLM has a fallback for models with incorrect Hub tokenizer_class metad...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: der. ## Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vironment ## 🐛 Describe the bug ### Summary vLLM has a fallback for models with incorrect Hub tokenizer_class metadata: ```python _MODEL_TYPES_WITH_INCORRECT_TOKENIZER_CLASS = {"step3_vl"} ``` `model_type="step3_vl"` is...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ;model_support;sampling_logits cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
