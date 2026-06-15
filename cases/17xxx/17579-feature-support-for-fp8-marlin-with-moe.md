# vllm-project/vllm#17579: [Feature]: support for fp8 marlin with MoE

| 字段 | 值 |
| --- | --- |
| Issue | [#17579](https://github.com/vllm-project/vllm/issues/17579) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;hardware_porting;moe;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: support for fp8 marlin with MoE

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I wanna run Qwen3-235B-A22B on Ampere (A100) in fp8. I quantized it to w8a16 using llm-compressor https://huggingface.co/cognitivecomputations/Qwen3-235B-A22B-FP8-W8A16 but when I run it, I get the error ERROR 05-02 03:16:53 [multiproc_executor.py:435] AssertionError: float16 is required for MoE compressed models. Set dtype=torch.float16 Please support FP8 with MoE in Marlin kernel ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: support for fp8 marlin with MoE feature request ### 🚀 The feature, motivation and pitch I wanna run Qwen3-235B-A22B on Ampere (A100) in fp8. I quantized it to w8a16 using llm-compressor https://huggingface.co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### 🚀 The feature, motivation and pitch I wanna run Qwen3-235B-A22B on Ampere (A100) in fp8. I quantized it to w8a16 using llm-compressor https://huggingface.co/cognitivecomputations/Qwen3-235B-A22B-FP8-W8A16 but when I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: MoE feature request ### 🚀 The feature, motivation and pitch I wanna run Qwen3-235B-A22B on Ampere (A100) in fp8. I quantized it to w8a16 using llm-compressor https://huggingface.co/cognitivecomputations/Qwen3-235B-A22B-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ;hardware_porting;moe;quantization fp8;kernel;moe;quantization dtype;env_dependency 🚀 The feature, motivation and pitch
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: support for fp8 marlin with MoE feature request ### 🚀 The feature, motivation and pitch I wanna run Qwen3-235B-A22B on Ampere (A100) in fp8. I quantized it to w8a16 using llm-compressor https://huggingface.co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
