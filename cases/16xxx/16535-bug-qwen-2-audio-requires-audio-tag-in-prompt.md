# vllm-project/vllm#16535: [Bug]: Qwen-2-audio requires <|AUDIO|> tag in prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#16535](https://github.com/vllm-project/vllm/issues/16535) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen-2-audio requires <\|AUDIO\|> tag in prompt

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to prompt qwen-2-audio with an audio file, the textual prompt requires ` ` in it, otherwise the server throws a 500 error. Seems potentially related to [this issue](https://github.com/vllm-project/vllm/issues/14209#issuecomment-2711963097), or it's the closest I could find. Here are the logs when including the tag in the request I'm seving the model with the following params ``` md = [ "vllm", "serve", "--uvicorn-log-level=info", MODEL_NAME, "--revision", MODEL_REVISION, "--host", "0.0.0.0", "--port", str(VLLM_PORT), "--enforce-eager", "--max-num-seqs", "16", "--max-model-len", "8192", "--api-key", API_KEY, ] ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen-2-audio requires <|AUDIO|> tag in prompt bug;stale ### Your current environment ### 🐛 Describe the bug When trying to prompt qwen-2-audio with an audio file, the textual prompt requires ` ` in it, otherwise...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. performance activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory attention;c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Qwen-2-audio requires <|AUDIO|> tag in prompt bug;stale ### Your current environment ### 🐛 Describe the bug When trying to prompt qwen-2-audio with an audio file, the textual prompt requires ` ` in it, otherwise...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: uted_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory attention;cache;cuda;operator;quantization;sampling;triton build_error;slowdown dtype;env_dependency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
