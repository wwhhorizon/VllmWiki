# vllm-project/vllm#37732: [Bug] Garbage output for long prompts after #35216

| 字段 | 值 |
| --- | --- |
| Issue | [#37732](https://github.com/vllm-project/vllm/issues/37732) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cache;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Garbage output for long prompts after #35216

### Issue 正文摘录

## Summary Commit `12fd17eb5` (#35216, "[compile] Initialize passes at VllmBackend init") causes garbage logits for prompts exceeding ~2048 tokens when using `-O3` compilation level. The regression was identified via `git bisect` across 33 commits. ## Environment - **vLLM version**: 0.17.2rc1.dev195 (commit c57d38d60) - **Model**: `nvidia/Kimi-K2.5-NVFP4` (MLA architecture, kv_lora_rank=512) - **Hardware**: NVIDIA GB200 - **Launch flags**: `-O3 --compilation_config.pass_config.enable_qk_norm_rope_fusion true` ## Reproduction ```bash # Start vLLM with -O3 vllm serve nvidia/Kimi-K2.5-NVFP4 -O3 # Works (short prompt, ~1500 tokens): curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "nvidia/Kimi-K2.5-NVFP4", "messages": [{"role": "system", "content": "You are helpful."}, {"role": "user", "content": "What is 2+2?"}], "max_tokens": 50 }' # → Coherent response ✅ # Fails (long prompt, ~2500+ tokens): python3 -c " import json, requests body = { 'model': 'nvidia/Kimi-K2.5-NVFP4', 'messages': [ {'role': 'system', 'content': 'You are a helpful assistant. ' * 400}, {'role': 'user', 'content': 'What is 2+2?'} ], 'max_tokens': 50, 'temperature': 0 }...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: long prompts after #35216 bug ## Summary Commit `12fd17eb5` (#35216, "[compile] Initialize passes at VllmBackend init") causes garbage logits for prompts exceeding ~2048 tokens when using `-O3` compilation level. The re...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: on**: 0.17.2rc1.dev195 (commit c57d38d60) - **Model**: `nvidia/Kimi-K2.5-NVFP4` (MLA architecture, kv_lora_rank=512) - **Hardware**: NVIDIA GB200 - **Launch flags**: `-O3 --compilation_config.pass_config.enable_qk_norm_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: r prompts exceeding ~2048 tokens when using `-O3` compilation level. The regression was identified via `git bisect` across 33 commits. ## Environment - **vLLM version**: 0.17.2rc1.dev195 (commit c57d38d60) - **Model**:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Summary Commit `12fd17eb5` (#35216, "[compile] Initialize passes at VllmBackend init") causes garbage logits for prompts exceeding ~2048 tokens when using `-O3` compilation level. The regression was identified via `git...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rc1.dev195 (commit c57d38d60) - **Model**: `nvidia/Kimi-K2.5-NVFP4` (MLA architecture, kv_lora_rank=512) - **Hardware**: NVIDIA GB200 - **Launch flags**: `-O3 --compilation_config.pass_config.enable_qk_norm_rope_fusion...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
