# vllm-project/vllm#11205: [Bug]: Corrupted output with GPTQ Marlin kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#11205](https://github.com/vllm-project/vllm/issues/11205) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Corrupted output with GPTQ Marlin kernel

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug @dacorvo discovered a potential issue (https://github.com/huggingface/optimum-quanto/issues/332) with the GPTQ Marlin kernel where the outputs become corrupted for certain shape combinations. The corrupted values appear at different indices after each invocation. I took some time to investigate the issue, and found two suspicious race conditions in the kernel with Compute Sanitizer: ``` ========= Error: Race reported between Read access at void marlin::Marlin (const int4 *, const int4 *, int4 *, int4 *, const int4 *, const int4 *, const int *, int, int, int, int, int *, bool)::[lambda(int, int) (instance 2)]::operator ()(int, int) const+0x2df0 in [REDACTED]/vllm/csrc/quantization/gptq_marlin/gptq_marlin.cu:1044 ========= and Write access at marlin::cp_async4(void *, const void *)+0x3380 in [REDACTED]/vllm/csrc/quantization/gptq_marlin/marlin.cuh:73 [1830656 hazards] ========= ========= Error: Race reported between Read access at void marlin::Marlin (const int4 *, const int4 *, int4 *, int4 *, const int4 *, const int4 *, const int *, int, int, int, int, int *, bool)::[lambda(int, int) (instance...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vocation. I took some time to investigate the issue, and found two suspicious race conditions in the kernel with Compute Sanitizer: ``` ========= Error: Race reported between Read access at void marlin::Marlin (const in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rvo discovered a potential issue (https://github.com/huggingface/optimum-quanto/issues/332) with the GPTQ Marlin kernel where the outputs become corrupted for certain shape combinations. The corrupted values appear at d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: == ========= Error: Race reported between Read access at void marlin::ldsm4 (marlin::ScalarType ::FragA &, const void *)+0x5930 in [REDACTED]/vllm/csrc/quantization/gptq_marlin/gptq_marlin.cu:131 ========= and Write acc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: output with GPTQ Marlin kernel bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug @dacorvo discovered a potential issue (https://github.com/huggingface/optimum-quanto/issues/332)...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: g_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency;race_condition;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
