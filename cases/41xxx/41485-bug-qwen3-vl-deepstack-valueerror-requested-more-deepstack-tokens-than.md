# vllm-project/vllm#41485: [Bug]: Qwen3-VL deepstack ValueError "Requested more deepstack tokens than available in buffer" with chunked prefill + prefix caching

| 字段 | 值 |
| --- | --- |
| Issue | [#41485](https://github.com/vllm-project/vllm/issues/41485) |
| 状态 | open |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;gemm;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL deepstack ValueError "Requested more deepstack tokens than available in buffer" with chunked prefill + prefix caching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug \`Qwen3VLForConditionalGeneration._get_deepstack_input_embeds\` raises \`ValueError\`, EngineCore catches it as fatal, and the engine dies (V1 \`EngineDeadError\`): \`\`\` File \"/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/qwen3_vl.py\", line ~1716, in _get_deepstack_input_embeds raise ValueError( ValueError: Requested more deepstack tokens than available in buffer: num_tokens=16 > self.deepstack_input_embeds_num_tokens=9 \`\`\` The \`num_tokens\` requested is consistently **16** but the buffer's \`deepstack_input_embeds_num_tokens\` varies (we have observed **9, 11, 14**). EngineCore logs \`EngineCore encountered a fatal error\` → systemd has restarted the service **39 times in 3 days**. ### Reproduction signal - **Workload:** OpenAI Chat Completions, single-image multimodal requests with prompts of 1500–2000 tokens. Production safety-monitoring pipeline that issues two-pass calls (primary + a longer \"rescue\" prompt on the same image). - **First crash always happens after the engine has been serving normally for many minutes** — it isn't a startup issue. - **Different \`mm_hash\` and different image cont...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: mage_embeds out-of-bounds, #31404 MM cache AssertionError). - [x] Latest version (v0.20.0). performance attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory cuda;fp8;gemm;q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL deepstack ValueError "Requested more deepstack tokens than available in buffer" with chunked prefill + prefix caching ### Your current environment ### 🐛 Describe the bug \`Qwen3VLForConditionalGeneration...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Qwen3-VL deepstack ValueError "Requested more deepstack tokens than available in buffer" with chunked prefill + prefix caching ### Your current environment ### 🐛 Describe the bug \`Qwen3VLForConditionalGeneration...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ce attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory cuda;fp8;gemm;quantization crash;oom;slowdown dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: hunked-prefill / prefix-cache misalignment: when prefix caching leaves a small residual chunk that lands inside the image's vision-token region, the buffer is sized to the chunk remainder while the language model still...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
