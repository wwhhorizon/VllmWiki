# vllm-project/vllm#39595: [Bug]: Gemma 4 26B MoE NVFP4 fails under tensor-parallel-size 2 across all available MoE backends

| 字段 | 值 |
| --- | --- |
| Issue | [#39595](https://github.com/vllm-project/vllm/issues/39595) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | kernel;moe |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 26B MoE NVFP4 fails under tensor-parallel-size 2 across all available MoE backends

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug All community NVFP4 quantizations of `google/gemma-4-26B-A4B-it` fail to initialize under `--tensor-parallel-size 2`, each hitting a different unsupported kernel path. The official `nvidia/Gemma-4-31B-IT-NVFP4` works correctly under TP=2, confirming this is specific to the 26B MoE architecture's expert dimensions when split across two GPUs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Gemma 4 26B MoE NVFP4 fails under tensor-parallel-size 2 across all available MoE backends bug ### Your current environment ### 🐛 Describe the bug All community NVFP4 quantizations of `google/gemma-4-26B-A4B-it`...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Gemma 4 26B MoE NVFP4 fails under tensor-parallel-size 2 across all available MoE backends bug ### Your current environment ### 🐛 Describe the bug All community NVFP4 quantizations of `google/gemma-4-26B-A4B-it`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma 4 26B MoE NVFP4 fails under tensor-parallel-size 2 across all available MoE backends bug ### Your current environment ### 🐛 Describe the bug All community NVFP4 quantizations of `google/gemma-4-26B-A4B-it`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 6B MoE NVFP4 fails under tensor-parallel-size 2 across all available MoE backends bug ### Your current environment ### 🐛 Describe the bug All community NVFP4 quantizations of `google/gemma-4-26B-A4B-it` fail to initiali...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: allel-size 2`, each hitting a different unsupported kernel path. The official `nvidia/Gemma-4-31B-IT-NVFP4` works correctly under TP=2, confirming this is specific to the 26B MoE architecture's expert dimensions when sp...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
