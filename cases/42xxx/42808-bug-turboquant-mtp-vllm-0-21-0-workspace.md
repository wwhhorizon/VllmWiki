# vllm-project/vllm#42808: [Bug]: 这次崩溃的直接原因是 TurboQuant 注意力后端与 MTP 推测解码在 vLLM 0.21.0 版本中的兼容性问题，具体表现为工作区（workspace）预留不足，导致引擎在处理第一个请求时触发断言错误

| 字段 | 值 |
| --- | --- |
| Issue | [#42808](https://github.com/vllm-project/vllm/issues/42808) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;fp8;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 这次崩溃的直接原因是 TurboQuant 注意力后端与 MTP 推测解码在 vLLM 0.21.0 版本中的兼容性问题，具体表现为工作区（workspace）预留不足，导致引擎在处理第一个请求时触发断言错误

### Issue 正文摘录

### Your current environment 🔍 错误定位 核心错误信息是： text AssertionError: Workspace is locked but allocation from 'turboquant_attn.py:879:_decode_attention' requires 0.76 MB, current size is 0.00 MB. Workspace growth is not allowed after locking. vLLM 在 CUDA Graph 捕获完成后会锁定工作区大小，以防止动态重分配带来的性能抖动。但 TurboQuant 的 _decode_attention 在推测解码（MTP）的草稿模型前向传播时，试图额外申请 0.76 MB 的临时空间，而预热阶段并未为这种情况预留空间，导致断言失败，引擎直接死亡。 💡 解决方案 目前有几种可行的调整方法，按推荐程度排列： ✅ 方案一：暂时禁用推测解码（推荐） 这是最简单可靠的方案。TurboQuant 带来的 4-bit KV 缓存压缩本身已经能显著提升长上下文下的并发能力，推测解码并非必需。你可以在启动命令中移除以下参数来关闭 MTP： bash --speculative-config '{"method": "mtp", "num_speculative_tokens": 3}' 修改后的完整启动命令应为： powershell vllm serve Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-GPTQ-Int4 \ --host 0.0.0.0 \ --port 8000 \ --kv-cache-dtype turboquant_4bit_nc \ --max-model-len auto \ --max-num-seqs 3 \ --gpu-memory-utilization 0.96 \ --enable-chunked-prefill \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser qwen3 \ --trust-remote-code \ --enable-prefix-caching \ --max-num-batched-tokens 8192 这样保留了 TurboQuant 的显存优势，同时避开了冲突。 ✅ 方案二：回退到 FP8 KV 缓存 + 推测解码 如果你更看重推测解码的加速效果（而非显存压缩），可以将 --kv-cache-dtype 改回 fp8，并重新启用 MTP。这是你最初成功的配置，稳定性更高： powershell v...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: nError: Workspace is locked but allocation from 'turboquant_attn.py:879:_decode_attention' requires 0.76 MB, current size is 0.00 MB. Workspace growth is not allowed after locking. vLLM 在 CUDA Graph 捕获完成后会锁定工作区大小，以防止动态重...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: 这次崩溃的直接原因是 TurboQuant 注意力后端与 MTP 推测解码在 vLLM 0.21.0 版本中的兼容性问题，具体表现为工作区（workspace）预留不足，导致引擎在处理第一个请求时触发断言错误 bug ### Your current environment 🔍 错误定位 核心错误信息是： text AssertionError: Workspace is locked but allocation fr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=Fal...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: monitor.py:103] Triton kernel JIT compilation during inference: _zero_kv_blocks_kernel. This causes a latency spike; consider extending warmup to cover this shape/config. (EngineCore pid=7972) WARNING 05-16 11:10:19 [ji...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: V 缓存容量，对于 max-num-seqs=3 的并发完全够用，且首 token 延迟会有改善。 无论采用哪种方案，建议继续观察是否还会出现 Triton kernel JIT compilation during inference 的警告。如果频繁出现，可以尝试增加预热批次大小（通过 --max-num-batched-tokens 或调大 --max-num-seqs 的初始请求），或接受初次请求的轻微延迟（后续会缓存）。 (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
