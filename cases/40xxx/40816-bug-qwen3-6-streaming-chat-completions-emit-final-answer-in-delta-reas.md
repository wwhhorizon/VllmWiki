# vllm-project/vllm#40816: [Bug]: Qwen3.6 streaming chat completions emit final answer in delta.reasoning and leave delta.content empty even with enable_thinking=false

| 字段 | 值 |
| --- | --- |
| Issue | [#40816](https://github.com/vllm-project/vllm/issues/40816) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.6 streaming chat completions emit final answer in delta.reasoning and leave delta.content empty even with enable_thinking=false

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the OpenAI-compatible `/v1/chat/completions` endpoint with a Qwen3-family model and `--reasoning-parser qwen3`, non-streaming responses behave correctly, but streaming responses may emit the final answer in `choices[0].delta.reasoning` while `choices[0].delta.content` stays empty for the entire stream. I can reproduce this even when explicitly disabling thinking with `chat_template_kwargs.enable_thinking=false`. In other words: - `stream=false` + `enable_thinking=false` -> normal `message.content` - `stream=true` + `enable_thinking=false` -> answer tokens appear in `delta.reasoning`, no `delta.content` This breaks OpenAI-compatible streaming clients that only read `delta.content`, because they see "reasoning only" and never receive the final answer in the content channel. ## Server startup The model I used is Qwen3.6-35B-A3B-NVFP4 (https://huggingface.co/RedHatAI/Qwen3.6-35B-A3B-NVFP4). I am serving the model with: ```bash vllm serve /model \ --served-model-name qwen3.6-35b-nvfp4 \ --max-model-len 262144 \ --gpu-memory-utilization 0.92 \ --max-num-batched-tokens 16384 \ --enable-prefix-caching \ --reasoning-parser qwen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: stays empty for the entire stream. I can reproduce this even when explicitly disabling thinking with `chat_template_kwargs.enable_thinking=false`. In other words: - `stream=false` + `enable_thinking=false` -> normal `me...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: content channel. ## Server startup The model I used is Qwen3.6-35B-A3B-NVFP4 (https://huggingface.co/RedHatAI/Qwen3.6-35B-A3B-NVFP4). I am serving the model with: ```bash vllm serve /model \ --served-model-name qwen3.6-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.6 streaming chat completions emit final answer in delta.reasoning and leave delta.content empty even with enable_thinking=false bug ### Your current environment ### 🐛 Describe the bug When using the OpenAI-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: \ --enable-prefix-caching \ --reasoning-parser qwen3 \ --attention-backend FLASH_ATTN \ --default-chat-template-kwargs '{"enable_thinking": false}' ``` Container image: ```text vllm/vllm-openai:cu130-nightly-aarch64 ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : false}' ``` Container image: ```text vllm/vllm-openai:cu130-nightly-aarch64 ``` ## Minimal reproduction ### Case 1: non-streaming works ```bash curl -sS http://localhost:8000/v1/chat/completions \ -H 'Content-Type: ap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
