# vllm-project/vllm#33911: [Bug]: Gemma-3 multimodal models (4b/12b/27b) fail with torch.compile assertion error

| 字段 | 值 |
| --- | --- |
| Issue | [#33911](https://github.com/vllm-project/vllm/issues/33911) |
| 状态 | closed |
| 标签 | torch.compile |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support;multimodal_vlm |
| 子分类 | edge_case |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma-3 multimodal models (4b/12b/27b) fail with torch.compile assertion error

### Issue 正文摘录

Gemma-3 multimodal models fail during initialization with a torch.compile assertion error. Text-only Gemma-3 models (270m, 1b) work fine. **Reproduce:** ```bash vllm serve google/gemma-3-4b-it --max-model-len 4096 ``` **Error:** ``` AssertionError: expected size 1048576==131072, stride 256==256 at dim=0 This error most often comes from a incorrect fake (aka meta) kernel for a custom op. ``` **Affected models:** google/gemma-3-4b-it, google/gemma-3-12b-it, google/gemma-3-27b-it (all use `Gemma3ForConditionalGeneration`) **Working models:** google/gemma-3-270m-it, google/gemma-3-1b-it (use `Gemma3ForCausalLM`) The size mismatch ratio (1048576 / 131072 = 8) matches the `rope_scaling.factor` of 8.0 in the multimodal model configs. **Environment:** vLLM main (4403e3ed4), PyTorch 2.9.1, CUDA 12.8

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma-3 multimodal models (4b/12b/27b) fail with torch.compile assertion error torch.compile Gemma-3 multimodal models fail during initialization with a torch.compile assertion error. Text-only Gemma-3 models (27...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Gemma-3 multimodal models (4b/12b/27b) fail with torch.compile assertion error torch.compile Gemma-3 multimodal models fail during initialization with a torch.compile assertion error. Text-only Gemma-3 models (27...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: mpile assertion error. Text-only Gemma-3 models (270m, 1b) work fine. **Reproduce:** ```bash vllm serve google/gemma-3-4b-it --max-model-len 4096 ``` **Error:** ``` AssertionError: expected size 1048576==131072, stride...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ma-3-270m-it, google/gemma-3-1b-it (use `Gemma3ForCausalLM`) The size mismatch ratio (1048576 / 131072 = 8) matches the `rope_scaling.factor` of 8.0 in the multimodal model configs. **Environment:** vLLM main (4403e3ed4...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 4096 ``` **Error:** ``` AssertionError: expected size 1048576==131072, stride 256==256 at dim=0 This error most often comes from a incorrect fake (aka meta) kernel for a custom op. ``` **Affected models:** google/gemma-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
