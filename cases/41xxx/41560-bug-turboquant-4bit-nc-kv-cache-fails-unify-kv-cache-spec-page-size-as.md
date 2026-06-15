# vllm-project/vllm#41560: [Bug] turboquant_4bit_nc KV cache fails unify_kv_cache_spec_page_size assertion on hybrid Qwen3_5 (GDN + attention) architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#41560](https://github.com/vllm-project/vllm/issues/41560) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;quantization |
| 症状 | build_error;crash;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] turboquant_4bit_nc KV cache fails unify_kv_cache_spec_page_size assertion on hybrid Qwen3_5 (GDN + attention) architecture

### Issue 正文摘录

## Summary `--kv-cache-dtype turboquant_4bit_nc` causes a deterministic `AssertionError` at engine init when used with hybrid `Qwen3_5ForConditionalGeneration` models (Qwen3.6 27B family). The turboquant page-size bytes do not satisfy the mamba/GDN-aligned max page-size constraint after vLLM's internal padding step in `unify_kv_cache_spec_page_size`. The crash is consistent and unrecoverable — no combination of `--max-model-len`, `--gpu-memory-utilization`, or `--max-num-seqs` resolves it. The vLLM build used is `v0.20.0-tq-hybrid-v3`, which specifically targets hybrid architectures. ## Reproduction ```bash python -m vllm.entrypoints.openai.api_server \ --model Intel/Qwen3.6-27B-int4-AutoRound \ --quantization auto_round \ --kv-cache-dtype turboquant_4bit_nc \ --max-model-len 96000 \ --gpu-memory-utilization 0.97 \ --compilation-config '{"cudagraph_mode":"PIECEWISE","cudagraph_capture_sizes":[1]}' \ --no-scheduler-reserve-full-isl \ --language-model-only \ --skip-mm-profiling \ --trust-remote-code ``` **Crash:** ``` AssertionError File "vllm/v1/core/kv_cache_utils.py", line 1030, in unify_kv_cache_spec_page_size ``` **Stack context:** Model weights load successfully (~16.6 GiB / 1...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug] turboquant_4bit_nc KV cache fails unify_kv_cache_spec_page_size assertion on hybrid Qwen3_5 (GDN + attention) architecture ## Summary `--kv-cache-dtype turboquant_4bit_nc` causes a deterministic `AssertionError` a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: fy_kv_cache_spec_page_size assertion on hybrid Qwen3_5 (GDN + attention) architecture ## Summary `--kv-cache-dtype turboquant_4bit_nc` causes a deterministic `AssertionError` at engine init when used with hybrid `Qwen3_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: `, `--gpu-memory-utilization`, or `--max-num-seqs` resolves it. The vLLM build used is `v0.20.0-tq-hybrid-v3`, which specifically targets hybrid architectures. ## Reproduction ```bash python -m vllm.entrypoints.openai.a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug] turboquant_4bit_nc KV cache fails unify_kv_cache_spec_page_size assertion on hybrid Qwen3_5 (GDN + attention) architecture ## Summary `--kv-cache-dtype turboquant_4bit_nc` causes a deterministic `AssertionError` a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 4bit_nc KV cache fails unify_kv_cache_spec_page_size assertion on hybrid Qwen3_5 (GDN + attention) architecture ## Summary `--kv-cache-dtype turboquant_4bit_nc` causes a deterministic `AssertionError` at engine init whe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
