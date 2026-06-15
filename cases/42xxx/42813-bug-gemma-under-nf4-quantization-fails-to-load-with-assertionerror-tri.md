# vllm-project/vllm#42813: [Bug]: Gemma under NF4 quantization fails to load with AssertionError: Tried to load weights of size torch.Size([3096576, 1])to a parameter of size torch.Size([5376, 1152])

| 字段 | 值 |
| --- | --- |
| Issue | [#42813](https://github.com/vllm-project/vllm/issues/42813) |
| 状态 | open |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma under NF4 quantization fails to load with AssertionError: Tried to load weights of size torch.Size([3096576, 1])to a parameter of size torch.Size([5376, 1152])

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I quantized google/gemma-4-31B-it under NF4 using bitsandbytes, and loaded with this minimal script: ```py MODEL_ID="vody-am/gemma-4-31B-it-bnb-nf4" vllm serve $MODEL_ID \ --quantization bitsandbytes \ --gpu-memory-utilization 0.5 \ --max-model-len 4096 \ --max-num-seqs 1 \ --tensor-parallel-size 1 \ --enable-prefix-caching \ --attention-backend TRITON_ATTN \ --default-chat-template-kwargs '{"enable_thinking": false}' ``` Which results in the error: ``` AssertionError: Tried to load weights of size torch.Size([3096576, 1])to a parameter of size torch.Size([5376, 1152]) ``` Full trace: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#42825 [Bugfix] Fix Gemma4 BNB prequantized multimodal weight loading

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma under NF4 quantization fails to load with AssertionError: Tried to load weights of size torch.Size([3096576, 1])to a parameter of size torch.Size([5376, 1152]) bug ### Your current environment ### 🐛 Describ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_me...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --tensor-parallel-size 1 \ --enable-prefix-caching \ --attention-backend TRITON_ATTN \ --default-chat-template-kwargs '{"enable_thinking": false}' ``` Which results in the error: ``` AssertionError: Tried to load weight...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Gemma under NF4 quantization fails to load with AssertionError: Tried to load weights of size torch.Size([3096576, 1])to a parameter of size torch.Size([5376, 1152]) bug ### Your current environment ### 🐛 Describ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42825](https://github.com/vllm-project/vllm/pull/42825) | closes_keyword | 0.95 | [Bugfix] Fix Gemma4 BNB prequantized multimodal weight loading | Fixes #42813. This PR fixes loading of pre-quantized BitsAndBytes 4-bit Gemma4 checkpoints where checkpoint weights are stored as packed uint8 tensors with BNB `quant_state`. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
