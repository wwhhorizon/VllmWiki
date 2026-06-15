# vllm-project/vllm#29468: [CI Failure]: mi325_1: Basic Models Tests (Other)

| 字段 | 值 |
| --- | --- |
| Issue | [#29468](https://github.com/vllm-project/vllm/issues/29468) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Basic Models Tests (Other)

### Issue 正文摘录

### Name of failing test `pytest -v -s models/test_transformers.py models/test_registry.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **4 model tests** - Quantization and model registry import failures #### Failed Tests: **1. Quantization test (1 failure)** - `test_transformers.py` - `test_quantization[5-32-TheBloke/TinyLlama-1.1B-Chat-v0.3-GPTQ-quantization_kwargs1]` - GPTQ quantization with Transformers backend **2. Model registry import tests (3 failures)** - `test_registry.py` - `test_registry_imports[PrithviGeoSpatialMAE]` - `test_registry_imports[Terratorch]` - `test_registry_imports[MiDashengLMModel]` **Configuration:** - Test duration: ~305 seconds (5 minutes) - 230 tests passed, 26 skipped, 4 failed - Tests verify model class imports and quantization compatibility **Likely cause:** 1. **GPTQ quantization failure**: GPTQ quantization with Transformers backend produces different outputs on ROCm compared to native vLLM implementation, causing the logprobs comparison to fail. 2. **Model registry import failures**: Three specialized model architectures (Prit...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: mi325_1: Basic Models Tests (Other) ci-failure ### Name of failing test `pytest -v -s models/test_transformers.py models/test_registry.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: Basic Models Tests (Other) ci-failure ### Name of failing test `pytest -v -s models/test_transformers.py models/test_registry.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locall
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: els/test_registry.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **4 model tests** - Quantization a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: PTQ quantization with Transformers backend produces different outputs on ROCm compared to native vLLM implementation, causing the logprobs comparison to fail. 2. **Model registry import failures**: Three specialized mod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t-v0.3-GPTQ-quantization_kwargs1]` - GPTQ quantization with Transformers backend **2. Model registry import tests (3 failures)** - `test_registry.py` - `test_registry_imports[PrithviGeoSpatialMAE]` - `test_registry_impo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
