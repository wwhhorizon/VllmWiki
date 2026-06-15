# vllm-project/vllm#15340: [Bug][V0][Trition MLA][GGUF]: Deepseek R1 GGUF starts producing gibberish towards the end of a longer generation

| 字段 | 值 |
| --- | --- |
| Issue | [#15340](https://github.com/vllm-project/vllm/issues/15340) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][V0][Trition MLA][GGUF]: Deepseek R1 GGUF starts producing gibberish towards the end of a longer generation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When inferencing with DeepSeek R1 `Q3_K_M` gguf quant it starts to produce gibberish towards the end of a longer generation. I have followed direction in https://github.com/vllm-project/vllm/pull/13167#issue-2848824985 in terms of the `--tokenizer and ---hf-config-path` configuration. I have tested various different images with nightly, and most recent `0.8.1` release, the issue persists. I would appreciate some direction on this, as vLLM is by far the fastest inference engine for GGUF on my 16x3090 config, but this bug (which @SzymonOzog had said he experienced a similar issue with model overflowing and producing NaNs, but that got fixed - ref here https://github.com/vllm-project/vllm/pull/13167#issuecomment-2728111595). Unfortunately I'm at a bit of a loss to fix this myself. Run command: ``` networks: vllm-dev: external: true name: br1 services: vllm-dev: image: vllm/vllm-openai:v0.8.1 runtime: nvidia restart: unless-stopped networks: vllm-dev: ipv4_address: 192.168.x.x environment: - HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN} - NVIDIA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 - VLLM_RPC_TIMEOUT=180000 - VLLM...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug][V0][Trition MLA][GGUF]: Deepseek R1 GGUF starts producing gibberish towards the end of a longer generation bug;stale ### Your current environment ### 🐛 Describe the bug When inferencing with DeepSeek R1 `Q3_K_M` g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ect/vllm/pull/13167#issue-2848824985 in terms of the `--tokenizer and ---hf-config-path` configuration. I have tested various different images with nightly, and most recent `0.8.1` release, the issue persists. I would a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: UF starts producing gibberish towards the end of a longer generation bug;stale ### Your current environment ### 🐛 Describe the bug When inferencing with DeepSeek R1 `Q3_K_M` gguf quant it starts to produce gibberish tow...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ### 🐛 Describe the bug When inferencing with DeepSeek R1 `Q3_K_M` gguf quant it starts to produce gibberish towards the end of a longer generation. I have followed direction in https://github.com/vllm-project/vllm/pull/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
