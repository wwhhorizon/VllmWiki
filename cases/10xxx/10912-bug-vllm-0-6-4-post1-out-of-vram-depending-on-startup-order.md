# vllm-project/vllm#10912: [Bug]: vllm 0.6.4.post1 out of VRAM depending on startup order

| 字段 | 值 |
| --- | --- |
| Issue | [#10912](https://github.com/vllm-project/vllm/issues/10912) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.6.4.post1 out of VRAM depending on startup order

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run “shuyuej/gemma-2-27b-it-GPTQ” model with vllm==0.6.4.post1, with below command. `VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 VLLM_ATTENTION_BACKEND=FLASHINFER vllm serve shuyuej/gemma-2-27b-it-GPTQ --dtype auto --port 11000 --gpu-memory-utilization 0.56 --max-model-len 4096 --trust-remote-code --quantization gptq_marlin` When I run vllm first, and then run another process to running whisper model (with faster-whisper backend, ctranslate2) in the same GPU, it run normally. But when I first run whisper model, and then run vllm second, it gives out of vram memory error. In vllm==0.6.2, this problem doesn't appear. After update vllm to 0.6.4.post1, I found this behavior. Why did this change happen? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: t1, with below command. `VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 VLLM_ATTENTION_BACKEND=FLASHINFER vllm serve shuyuej/gemma-2-27b-it-GPTQ --dtype auto --port 11000 --gpu-memory-utilization 0.56 --max-model-len 4096 --trust-remo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: LM_ATTENTION_BACKEND=FLASHINFER vllm serve shuyuej/gemma-2-27b-it-GPTQ --dtype auto --port 11000 --gpu-memory-utilization 0.56 --max-model-len 4096 --trust-remote-code --quantization gptq_marlin` When I run vllm first,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: en? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: VRAM depending on startup order bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run “shuyuej/gemma-2-27b-it-GPTQ” model with vllm==0.6.4.post1, with below command. `VLLM_ALL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
