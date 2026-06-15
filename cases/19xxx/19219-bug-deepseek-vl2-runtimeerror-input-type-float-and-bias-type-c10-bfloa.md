# vllm-project/vllm#19219: [Bug]: deepseek-vl2 `RuntimeError: Input type (float) and bias type (c10::BFloat16) should be the same`

| 字段 | 值 |
| --- | --- |
| Issue | [#19219](https://github.com/vllm-project/vllm/issues/19219) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;quantization;sampling |
| 症状 | crash;import_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepseek-vl2 `RuntimeError: Input type (float) and bias type (c10::BFloat16) should be the same`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Just a quick guess, perhaps related to the dtype resolution change? @DarkLight1337 ``` vllm serve deepseek-ai/deepseek-vl2-small --trust_remote_code --hf_overrides '{"architectures": ["DeepseekVLV2ForCausalLM"]}' INFO 06-05 16:06:04 [__init__.py:244] Automatically detected platform cuda. INFO 06-05 16:06:08 [api_server.py:1289] vLLM API server version 0.9.1.dev70+g8f8900cee INFO 06-05 16:06:09 [cli_args.py:309] non-default args: {'model': 'deepseek-ai/deepseek-vl2-small', 'trust_remote_code': True, 'hf_overrides': {'architectures': ['DeepseekVLV2ForCausalLM']}} INFO 06-05 16:06:09 [config.py:532] Overriding HF config with {'architectures': ['DeepseekVLV2ForCausalLM']} INFO 06-05 16:06:15 [config.py:822] This model supports multiple tasks: {'score', 'classify', 'reward', 'embed', 'generate'}. Defaulting to 'generate'. INFO 06-05 16:06:15 [config.py:2176] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 06-05 16:06:15 [cuda.py:154] Forcing kv cache block size to 64 for FlashMLA backend. WARNING 06-05 16:06:17 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead wi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 06-05 16:06:08 [api_server.py:1289] vLLM API server version 0.9.1.dev70+g8f8900cee INFO 06-05 16:06:09 [cli_args.py:309] non-default args: {'model': 'deepseek-ai/deepseek-vl2-small', 'trust_remote_co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 337 ``` vllm serve deepseek-ai/deepseek-vl2-small --trust_remote_code --hf_overrides '{"architectures": ["DeepseekVLV2ForCausalLM"]}' INFO 06-05 16:06:04 [__init__.py:244] Automatically detected platform cuda. INFO 06-0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Bug]: deepseek-vl2 `RuntimeError: Input type (float) and bias type (c10::BFloat16) should be the same` bug ### Your current environment ### 🐛 Describe the bug Just a quick guess, perhaps related to the dtype resolution...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: olution change? @DarkLight1337 ``` vllm serve deepseek-ai/deepseek-vl2-small --trust_remote_code --hf_overrides '{"architectures": ["DeepseekVLV2ForCausalLM"]}' INFO 06-05 16:06:04 [__init__.py:244] Automatically detect...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: . Defaulting to 'generate'. INFO 06-05 16:06:15 [config.py:2176] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 06-05 16:06:15 [cuda.py:154] Forcing kv cache block size to 64 for FlashMLA backend. WAR...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
