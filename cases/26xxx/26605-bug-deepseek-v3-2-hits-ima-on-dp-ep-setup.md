# vllm-project/vllm#26605: [Bug]: DeepSeek v3.2 hits IMA on DP/EP setup

| 字段 | 值 |
| --- | --- |
| Issue | [#26605](https://github.com/vllm-project/vllm/issues/26605) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek v3.2 hits IMA on DP/EP setup

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running DeepSeek v3.2 with DP/EP leads to IMA in `flash_fwd_mla_combine_kernel`: ```bash vllm serve deepseek-ai/DeepSeek-V3.2-Exp -dp 4 --enable-expert-parallel --hf-overrides.num_hidden_layers=4 --load-format=dummy ``` ```bash vllm bench serve --model deepseek-ai/DeepSeek-V3.2-Exp --dataset-name random --random-input-len 128 --random-output-len 128 ``` leads to: ``` [21:42:21.267000] coredump: Detected an exception of type CUDBG_EXCEPTION_WARP_ILLEGAL_ADDRESS (14) [21:42:21.267066] coredump: - Device: 0 [21:42:21.267072] coredump: - SM: 0 [21:42:21.267078] coredump: - Warp: 12 [21:42:21.267085] coredump: - PC 0x7f49c2e9ca80 [21:42:21.268575] coredump: Stack trace (lane masks: active 0xffffffff, valid 0xffffffff): [21:42:21.268586] coredump: #0 0x7f49c2e9caf0 _Z28flash_fwd_mla_combine_kernelIN7cutlass10bfloat16_tELi512ELi8ELi32ELi256EEv14DecodingParams ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_erro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 21:42:21.267066] coredump: - Device: 0 [21:42:21.267072] coredump: - SM: 0 [21:42:21.267078] coredump: - Warp: 12 [21:42:21.267085] coredump: - PC 0x7f49c2e9ca80 [21:42:21.268575] coredump: Stack trace (lane masks: acti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: llm serve deepseek-ai/DeepSeek-V3.2-Exp -dp 4 --enable-expert-parallel --hf-overrides.num_hidden_layers=4 --load-format=dummy ``` ```bash vllm bench serve --model deepseek-ai/DeepSeek-V3.2-Exp --dataset-name random --ra...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 268586] coredump: #0 0x7f49c2e9caf0 _Z28flash_fwd_mla_combine_kernelIN7cutlass10bfloat16_tELi512ELi8ELi32ELi256EEv14DecodingParams ``` ### Before submitting a new issue... - [x] Make sure you already searched for releva...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: oredump: #0 0x7f49c2e9caf0 _Z28flash_fwd_mla_combine_kernelIN7cutlass10bfloat16_tELi512ELi8ELi32ELi256EEv14DecodingParams ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
