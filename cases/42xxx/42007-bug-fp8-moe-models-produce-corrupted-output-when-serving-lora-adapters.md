# vllm-project/vllm#42007: [Bug]: FP8 MoE models produce corrupted output when serving LoRA adapters

| 字段 | 值 |
| --- | --- |
| Issue | [#42007](https://github.com/vllm-project/vllm/issues/42007) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 MoE models produce corrupted output when serving LoRA adapters

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Env/model - vLLM version: 0.20.0 - Quantization: FP8 W8A8 - Model architecture: MoE (e.g., Nemotron-H with `FusedMoE` / `TritonExperts`). Specifically, Nemotron 3 Nano - LoRA: enabled via `--enable-lora --lora-modules` ### Description When serving an FP8-quantized MoE model with LoRA adapters, queries directed at the LoRA adapter model produce gibberish / incoherent output. The same adapter served on the same model in vLLM 0.19.0 produces correct output. This affects any FP8 W8A8 MoE model with LoRA adapters. the MoE LoRA kernel receives hidden states that have already been quantized to `torch.float8_e4m3fn` by the MoE layer's `_prepare()` step, but the LoRA computation expects the original bf16/fp16 activations. The LoRA delta is computed on values that are 50-500x smaller than expected (raw FP8 without scale compensation), producing a numerically incorrect correction that corrupts the output. ### Repro 1. Serve an FP8-quantized MoE model with a LoRA adapter: ```bash vllm serve \ --enable-lora \ --lora-modules my_adapter= ``` 2. Send an inference request targeting the LoRA adapter: ```bash curl -s http:// : /v1/chat/completi...

## 现有链接修复摘要

#42120 [Bugfix] Fix corrupt outputs in MoE FP8 LoRA responses and MoE base model responses when LoRAs are loaded

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: FP8 MoE models produce corrupted output when serving LoRA adapters bug ### Your current environment ### 🐛 Describe the bug ### Env/model - vLLM version: 0.20.0 - Quantization: FP8 W8A8 - Model architecture: MoE (...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: smaller than expected (raw FP8 without scale compensation), producing a numerically incorrect correction that corrupts the output. ### Repro 1. Serve an FP8-quantized MoE model with a LoRA adapter: ```bash vllm serve \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ur current environment ### 🐛 Describe the bug ### Env/model - vLLM version: 0.20.0 - Quantization: FP8 W8A8 - Model architecture: MoE (e.g., Nemotron-H with `FusedMoE` / `TritonExperts`). Specifically, Nemotron 3 Nano -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Env/model - vLLM version: 0.20.0 - Quantization: FP8 W8A8 - Model architecture: MoE (e.g., Nemotron-H with `FusedMoE` / `TritonExperts`). Specifically, Nemotron 3 Nano - LoRA: enabled via `--enable-lora --lora-modul...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: FP8 MoE models produce corrupted output when serving LoRA adapters bug ### Your current environment ### 🐛 Describe the bug ### Env/model - vLLM version: 0.20.0 - Quantization: FP8 W8A8 - Model architecture: MoE (...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42120](https://github.com/vllm-project/vllm/pull/42120) | closes_keyword | 0.95 | [Bugfix] Fix corrupt outputs in MoE FP8 LoRA responses and MoE base model responses when LoRAs are loaded | Fixes two bugs: - #42007 - #42008 ## Test Plan Adds two unit/regression tests that catch the two bugs above - `test_lora_kernel_receives_unquantized_hidden_states` ensures |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
