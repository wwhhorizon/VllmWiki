# vllm-project/vllm#41726: [Bug]: Latest Nightly build with TurboQuant KV cache crashes on large chunked continuation prefill after workspace lock ( testing PR #39931 implementing TQ on Hybrid Attention Models e.g Qwen3.5-9B)

| 字段 | 值 |
| --- | --- |
| Issue | [#41726](https://github.com/vllm-project/vllm/issues/41726) |
| 状态 | open |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;kernel;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Latest Nightly build with TurboQuant KV cache crashes on large chunked continuation prefill after workspace lock ( testing PR #39931 implementing TQ on Hybrid Attention Models e.g Qwen3.5-9B)

### Issue 正文摘录

### Your current environment ### Environment - vLLM: `0.20.2rc1.dev35+g4845aee6b` - Python: `3.12.13` - Torch: `2.11.0+cu130` - CUDA driver/runtime: NVIDIA driver `595.71.05`, CUDA `13` - GPU: NVIDIA GeForce RTX 5080 - FlashInfer: `0.6.8.post1` - Transformers: `5.7.0` ### 🐛 Describe the bug ### Summary Testing latest commit #39931 turbo --kv-cache-dtype can crash at runtime when chunked prefill resumes a long prompt. The failure happens in TurboQuant attention’s large continuation-prefill path after the global workspace has already been locked. This appears TurboQuant-specific. ### Model Model: NVFP4 quantization of Qwen3.5-9b Relevant config: architectures: Qwen3_5ForConditionalGeneration model_type: qwen3_5 text_config.hidden_size: 4096 text_config.num_attention_heads: 16 text_config.num_key_value_heads: 4 text_config.head_dim: 256 text_config.num_hidden_layers: 32 text_config.full_attention_interval: 4 quantization_config.quant_method: modelopt quantization_config.quant_algo: NVFP4 Startup logs detect the TurboQuant hybrid layers: TQ hybrid: full-attention layers [3, 7, 11, 15, 19, 23, 27, 31] Using TURBOQUANT attention backend out of potential backends: ['TURBOQUANT']. ### Com...

## 现有链接修复摘要

#39931 [Feature] TurboQuant: support hybrid models and uniform quantization | #43747 [Bugfix][TurboQuant] Fix CUDA graph capture crash with spec-decode + chunked-prefill (#40807)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Latest Nightly build with TurboQuant KV cache crashes on large chunked continuation prefill after workspace lock ( testing PR #39931 implementing TQ on Hybrid Attention Models e.g Qwen3.5-9B) bug ### Your current...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Latest Nightly build with TurboQuant KV cache crashes on large chunked continuation prefill after workspace lock ( testing PR #39931 implementing TQ on Hybrid Attention Models e.g Qwen3.5-9B) bug ### Your current...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: c1.dev35+g4845aee6b` - Python: `3.12.13` - Torch: `2.11.0+cu130` - CUDA driver/runtime: NVIDIA driver `595.71.05`, CUDA `13` - GPU: NVIDIA GeForce RTX 5080 - FlashInfer: `0.6.8.post1` - Transformers: `5.7.0` ### 🐛 Descr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: tly build with TurboQuant KV cache crashes on large chunked continuation prefill after workspace lock ( testing PR #39931 implementing TQ on Hybrid Attention Models e.g Qwen3.5-9B) bug ### Your current environment ### E...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r workspace lock ( testing PR #39931 implementing TQ on Hybrid Attention Models e.g Qwen3.5-9B) bug ### Your current environment ### Environment - vLLM: `0.20.2rc1.dev35+g4845aee6b` - Python: `3.12.13` - Torch: `2.11.0+...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39931](https://github.com/vllm-project/vllm/pull/39931) | mentioned | 0.45 | [Feature] TurboQuant: support hybrid models and uniform quantization | `5.7.0` ### 🐛 describe the bug ### summary testing latest commit #39931 turbo --kv-cache-dtype can crash at runtime when chunked prefill resumes a long prompt. the failure happen |
| [#43747](https://github.com/vllm-project/vllm/pull/43747) | closes_keyword | 0.95 | [Bugfix][TurboQuant] Fix CUDA graph capture crash with spec-decode + chunked-prefill (#40807) | closed) - #42544 — workspace allocation assertion (open, addressed by #42551) - #41726 — large chunked continuation prefill crash (open) - #40069 — TurboQuant/HIGGS tracking issue |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
