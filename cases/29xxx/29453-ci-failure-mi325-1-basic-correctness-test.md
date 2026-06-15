# vllm-project/vllm#29453: [CI Failure]: mi325_1: Basic Correctness Test

| 字段 | 值 |
| --- | --- |
| Issue | [#29453](https://github.com/vllm-project/vllm/issues/29453) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | sampling |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Basic Correctness Test

### Issue 正文摘录

### Name of failing test `pytest -v -s basic_correctness/test_cumem.py && pytest -v -s basic_correctness/test_basic_correctness.py && pytest -v -s basic_correctness/test_cpu_offload.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Summary The `test_models` test compares the output correctness between HuggingFace (HF) and vLLM implementations when using greedy sampling. Specifically, it: 1. Generates outputs using HF's model implementation 2. Generates outputs using vLLM's implementation with various configurations 3. Compares the outputs to ensure they match #### Failed Test Configurations All failures involve the `FLASH_ATTN` backend with these parameter combinations: - **Models tested:** - `hmellor/tiny-random-Gemma2ForCausalLM` - `meta-llama/Llama-3.2-1B-Instruct` - **Parameter variations that failed:** - `enable_prompt_embeds`: True and False - `model_executor`: "uni" and "mp" (uniprocessor and multiprocessor) - `async_scheduling`: True and False - `enforce_eager`: False - `max_tokens`: 5 #### Root Cause Indication The RuntimeError occurring at line 964 in `...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: s.py && pytest -v -s basic_correctness/test_cpu_offload.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: #### Failed Test Configurations All failures involve the `FLASH_ATTN` backend with these parameter combinations: - **Models tested:** - `hmellor/tiny-random-Gemma2ForCausalLM` - `meta-llama/Llama-3.2-1B-Instruct` - **Pa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Basic Correctness Test ci-failure ### Name of failing test `pytest -v -s basic_correctness/test_cumem.py && pytest -v -s basic_correctness/test_basic_correctness.py && pytest -v -s basic_correctnes
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: /test_cpu_offload.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Summary The `test_models` test...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /utils.py` suggests an issue with: - The V1 engine implementation on AMD/ROCm hardware - Potential missing AITER activation for the FLASH_ATTN backend to be correctly activated on ROCm ### 📝 History of failing test **Te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
