# vllm-project/vllm#29208: [Bug]: enable-log-requests has stopped logging requests between 11.0 and 11.2

| 字段 | 值 |
| --- | --- |
| Issue | [#29208](https://github.com/vllm-project/vllm/issues/29208) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: enable-log-requests has stopped logging requests between 11.0 and 11.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Im using the production releases from docker hub, no modifications, in 11.0 with a docker compose like this > version: '3.8' > > services: > vllm-openai: > image: vllm/vllm-openai:v0.11.0 > runtime: nvidia > environment: > - HUGGING_FACE_HUB_TOKEN=xxx > volumes: > - VLLMcache:/root/.cache/huggingface > ports: > - "8001:8000" > ipc: host > command: > > --model unsloth/granite-4.0-h-tiny-FP8-Dynamic > --served-model-name gpt-4o-mini > --gpu-memory-utilization 0.78 > --max_model_len 32768 > --max_num_seqs 2 > --tool-call-parser hermes > --enable-auto-tool-choice > --enable-prefix-caching > --enable-log-requests > --enable-log-outputs i get an output like this > (APIServer pid=1) INFO: Application startup complete. (APIServer pid=1) INFO 11-21 14:04:13 [chat_utils.py:560] Detected the chat template content format to be 'openai'. You can set `--chat-template-content-format` to override this. (APIServer pid=1) INFO 11-21 14:04:13 [logger.py:40] Received request chatcmpl-0f424b063d494ec2899cc58944aa79d7: prompt: ' system I want you to act as … if i change the > image: vllm/vllm-openai:v0.11.1 to > image: vllm/vllm-openai:v0.11.2 then th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: onment ### 🐛 Describe the bug Im using the production releases from docker hub, no modifications, in 11.0 with a docker compose like this > version: '3.8' > > services: > vllm-openai: > image: vllm/vllm-openai:v0.11.0 >...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ipc: host > command: > > --model unsloth/granite-4.0-h-tiny-FP8-Dynamic > --served-model-name gpt-4o-mini > --gpu-memory-utilization 0.78 > --max_model_len 32768 > --max_num_seqs 2 > --tool-call-parser hermes > --enable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 8af349e880656a715f4ebd4a: output: 'Hello! How can I assist you with your smart home today? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: GGING_FACE_HUB_TOKEN=xxx > volumes: > - VLLMcache:/root/.cache/huggingface > ports: > - "8001:8000" > ipc: host > command: > > --model unsloth/granite-4.0-h-tiny-FP8-Dynamic > --served-model-name gpt-4o-mini > --gpu-mem...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: > - "8001:8000" > ipc: host > command: > > --model unsloth/granite-4.0-h-tiny-FP8-Dynamic > --served-model-name gpt-4o-mini > --gpu-memory-utilization 0.78 > --max_model_len 32768 > --max_num_seqs 2 > --tool-call-parser...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
