# vllm-project/vllm#37406: [Bug]: GPU hang on MI325/300 when serving MiniMax-M2.1-MXFP4 with TP=1

| 字段 | 值 |
| --- | --- |
| Issue | [#37406](https://github.com/vllm-project/vllm/issues/37406) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU hang on MI325/300 when serving MiniMax-M2.1-MXFP4 with TP=1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Community user [reported ](https://huggingface.co/amd/MiniMax-M2.1-MXFP4/discussions/1) GPU hang issue for model amd/MiniMax-M2.1-MXFP4 with TP=1 on MI300. However, using TP>1 (e.g., 2) can successfully make the server launched. This is because MI300 has no native MXFP4, therefore Quark uses the emulative (QDQ) path, dequantizing MXFP4 to BF16 (~4× memory). With a ~230 GB FP16-equivalent model, a single 192 GB MI300 is under heavy memory pressure, which can lead to hang or invalid access. To help users pass "good" serving CLI args, Quark can emit relevant infos or warnings at an early stage before GPU hang happens, particularly for emulation cases, cc @BowenBao @fxmarty-amd ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions./

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: GPU hang on MI325/300 when serving MiniMax-M2.1-MXFP4 with TP=1 bug;rocm ### Your current environment ### 🐛 Describe the bug Community user [reported ](https://huggingface.co/amd/MiniMax-M2.1-MXFP4/discussions/1)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ug]: GPU hang on MI325/300 when serving MiniMax-M2.1-MXFP4 with TP=1 bug;rocm ### Your current environment ### 🐛 Describe the bug Community user [reported ](https://huggingface.co/amd/MiniMax-M2.1-MXFP4/discussions/1) G...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: est/), which can answer lots of frequently asked questions./ correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;kernel;operator;s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vironment ### 🐛 Describe the bug Community user [reported ](https://huggingface.co/amd/MiniMax-M2.1-MXFP4/discussions/1) GPU hang issue for model amd/MiniMax-M2.1-MXFP4 with TP=1 on MI300. However, using TP>1 (e.g., 2)...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ation;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
