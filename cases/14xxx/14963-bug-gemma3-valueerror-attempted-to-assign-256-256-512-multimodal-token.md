# vllm-project/vllm#14963: [Bug]: Gemma3 ValueError: Attempted to assign 256 + 256 = 512 multimodal tokens to 1536 placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#14963](https://github.com/vllm-project/vllm/issues/14963) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3 ValueError: Attempted to assign 256 + 256 = 512 multimodal tokens to 1536 placeholders

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 ### 🐛 Describe the bug Just refer to this code snippet https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/vision_language_multi_image.py#L87-L114 and run the following script: python tools/nemo_curator/test_vllm.py --model-type gemma3 --method generate And Raising the error: [Bug]: Gemma3 ValueError: Attempted to assign 256 + 256 = 512 multimodal tokens to 1536 placeholders ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: PyTorch version: 2.6.0+cu124 Is debug build: False
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma3 ValueError: Attempted to assign 256 + 256 = 512 multimodal tokens to 1536 placeholders bug ### Your current environment Collecting environment information...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: CUDA used to build PyTorch: 12.4 ROCM used to b
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Is debug build: False CUDA used to build PyTorch: 12.4
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma3 ValueError: Attempted to assign 256 + 256 = 512 multimodal tokens to 1536 placeholders bug ### Your current environment Collecting environment information...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
