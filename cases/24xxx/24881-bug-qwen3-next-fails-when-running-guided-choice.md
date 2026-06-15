# vllm-project/vllm#24881: [Bug]: Qwen3-Next Fails when running Guided Choice

| 字段 | 值 |
| --- | --- |
| Issue | [#24881](https://github.com/vllm-project/vllm/issues/24881) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next Fails when running Guided Choice

### Issue 正文摘录

### 🐛 Describe the bug ``` containers: - name: vllm-openai image: vllm/vllm-openai:v0.10.2 imagePullPolicy: IfNotPresent env: - name: VLLM_FLASH_ATTN_VERSION value: "3" - name: VLLM_ALLOW_LONG_MAX_MODEL_LEN value: "1" command: - vllm - serve - /mnt/models/qwen3-next - --host - "0.0.0.0" - --port - "8000" - --uvicorn-log-level - warning - --enable-log-requests - --enable-log-outputs - --served-model-name - qwen3-next - --trust-remote-code - --gpu-memory-utilization - "0.9" - --enable-prefix-caching - --max-model-len - "12288" - --enable-auto-tool-choice - --tool-call-parser - hermes - --tensor-parallel-size - "4" - --speculative-config - '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' ``` When using guided choice, service breaks showing [CUDA] Illegal Memory Access. Client: ``` system_prompt = "You are a helpful assistant. Answer the following question concisely. Give only the final Answer, don't give justifications." user_prompt = f"""Question: "{transcription}" Answer: """ import openai qwen3= openai.AsyncOpenAI(base_url=...,api_key=...) system_prompt = "You are a helpful assistant. Answer the following question concisely. Give only the final Answer, don't give justifica...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: "8000" - --uvicorn-log-level - warning - --enable-log-requests - --enable-log-outputs - --served-model-name - qwen3-next - --trust-remote-code - --gpu-memory-utilization - "0.9" - --enable-prefix-caching - --max-model-l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: imagePullPolicy: IfNotPresent env: - name: VLLM_FLASH_ATTN_VERSION value: "3" - name: VLLM_ALLOW_LONG_MAX_MODEL_LEN value: "1" command: - vllm - serve - /mnt/models/qwen3-next - --host - "0.0.0.0" - --port - "80
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ods: POST (APIServer pid=1) INFO 09-15 04:42:16 [launcher.py:44] Route: /scale_elastic_ep, Methods: POST (APIServer pid=1) INFO 09-15 04:42:16 [launcher.py:44] Route: /is_scaling_elastic_ep, Methods: POST (APIServer pid...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: worker.py:391] Free memory on device (78.6/79.2 GiB) on startup. Desired GPU memory utilization is (0.9, 71.28 GiB). Actual usage is 37.99 GiB for weight, 4.71 GiB for peak activation, 1.84 GiB for non-torch memory, and...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-Next Fails when running Guided Choice bug ### 🐛 Describe the bug ``` containers: - name: vllm-openai image: vllm/vllm-openai:v0.10.2 imagePullPolicy: IfNotPresent env: - name: VLLM_FLASH_ATTN_V

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
