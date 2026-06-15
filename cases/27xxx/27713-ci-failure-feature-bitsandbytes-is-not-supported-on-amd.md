# vllm-project/vllm#27713: [CI Failure][Feature]: BitsAndBytes is not supported on AMD

| 字段 | 值 |
| --- | --- |
| Issue | [#27713](https://github.com/vllm-project/vllm/issues/27713) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure][Feature]: BitsAndBytes is not supported on AMD

### Issue 正文摘录

### Name of failing test models/quantization/test_bitsandbytes.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [BitsAndBytes](https://github.com/bitsandbytes-foundation/bitsandbytes) is not supported on AMD: https://github.com/vllm-project/vllm/blob/main/vllm/platforms/rocm.py#L192 - `ValidationError: bitsandbytes quantization is currently not supported in rocm` https://github.com/vllm-project/vllm/pull/27712 will fix this by skipping the tests ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/36507#019a28fa-2a03-47a9-9604-b64749e6b39a ### CC List. @yeqcharlotte @Alexei-V-Ivanov-AMD @DarkLight1337 @gshtras

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][Feature]: BitsAndBytes is not supported on AMD rocm;ci-failure ### Name of failing test models/quantization/test_bitsandbytes.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Cau
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: dBytes is not supported on AMD rocm;ci-failure ### Name of failing test models/quantization/test_bitsandbytes.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: /test_bitsandbytes.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [BitsAndBytes](https://github.com/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: is not supported on AMD rocm;ci-failure ### Name of failing test models/quantization/test_bitsandbytes.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure][Feature]: BitsAndBytes is not supported on AMD rocm;ci-failure ### Name of failing test models/quantization/test_bitsandbytes.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caus...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
