# vllm-project/vllm#42008: [Bug]: Base model queries produce corrupt output when LoRA adapters are loaded on MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#42008](https://github.com/vllm-project/vllm/issues/42008) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Base model queries produce corrupt output when LoRA adapters are loaded on MoE models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Env/model - vLLM version: 0.20.0 - Model architecture: MoE (e.g., models using `FusedMoE` / `TritonExperts`). Specifically, Nemotron 3 Nano in this case. - LoRA: enabled via `--enable-lora --lora-modules` ### Description When serving an MoE model with LoRA adapters loaded, queries directed at the **base model** (not the adapter) produce gibberish output. The base model should be completely unaffected by loaded adapters e.g. LoRA computation should be a no-op for base model tokens. This can be verified by comparing: - `--enable-lora` **without** `--lora-modules`: base model output is correct - `--enable-lora` **with** `--lora-modules my_adapter=...`: base model output is gibberish Simply having an adapter loaded corrupts base model inference, even though the request does not reference the adapter. ### Repro 1. Serve an MoE model with a LoRA adapter: ```bash vllm serve \ --enable-lora \ --lora-modules my_adapter= ``` 2. Send an inference request targeting the base model: ```bash curl -s http:// : /v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": " ", "messages": [{"role": "user", "content": "Tell me a...

## 现有链接修复摘要

#42120 [Bugfix] Fix corrupt outputs in MoE FP8 LoRA responses and MoE base model responses when LoRAs are loaded

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ur current environment ### 🐛 Describe the bug ### Env/model - vLLM version: 0.20.0 - Model architecture: MoE (e.g., models using `FusedMoE` / `TritonExperts`). Specifically, Nemotron 3 Nano in this case. - LoRA: enabled...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: . ### Additional context - This is an independent issue from the other FP8 LoRA bug I filed ( #42007 ). it affects MoE models regardless of quantization scheme. - The root cause is in the MoE LoRA kernel dispatch path....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: se model queries produce corrupt output when LoRA adapters are loaded on MoE models bug ### Your current environment ### 🐛 Describe the bug ### Env/model - vLLM version: 0.20.0 - Model architecture: MoE (e.g., models us...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: sion: 0.20.0 - Model architecture: MoE (e.g., models using `FusedMoE` / `TritonExperts`). Specifically, Nemotron 3 Nano in this case. - LoRA: enabled via `--enable-lora --lora-modules` ### Description When serving an Mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### 🐛 Describe the bug ### Env/model - vLLM version: 0.20.0 - Model architecture: MoE (e.g., models using `FusedMoE` / `TritonExperts`). Specifically, Nemotron 3 Nano in this case. - LoRA: enabled via `--enable-lora --l...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42120](https://github.com/vllm-project/vllm/pull/42120) | closes_keyword | 0.95 | [Bugfix] Fix corrupt outputs in MoE FP8 LoRA responses and MoE base model responses when LoRAs are loaded | Fixes two bugs: - #42007 - #42008 ## Test Plan Adds two unit/regression tests that catch the two bugs above - `test_lora_kernel_receives_unquantized_hidden_states` ensures |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
