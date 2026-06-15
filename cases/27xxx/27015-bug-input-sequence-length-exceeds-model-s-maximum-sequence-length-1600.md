# vllm-project/vllm#27015: [Bug]: Input sequence length exceeds model's maximum sequence length (160004 > 131072)

| 字段 | 值 |
| --- | --- |
| Issue | [#27015](https://github.com/vllm-project/vllm/issues/27015) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Input sequence length exceeds model's maximum sequence length (160004 > 131072)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed the DeepSeek-V3.2-Exp model from https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp I ran performance testing using https://github.com/modelscope/evalscope: ```bash evalscope perf \ --api openai \ --url http://10.172.98.10/v1/chat/completions \ --model deepseek-v3.2-exp \ --api-key "..." \ --stream \ --dataset random \ --prefix-length 160000 \ --min-prompt-length 4 \ --max-prompt-length 4 \ --max-tokens 128 \ --min-tokens 128 \ --tokenizer-path /data1/gpustack/cache/model_scope/deepseek-ai/DeepSeek-V3.2-Exp/ \ --extra-args '{"ignore_eos": true}' \ --number 1 \ --parallel 1 ```` Before running, the following warning appeared: ``` Token indices sequence length is longer than the specified maximum sequence length for this model (160004 > 131072). Running this sequence through the model will result in indexing errors ``` While this may not prevent inference, it seems incorrect because the model's `config.json` specifies `max_position_embeddings` of 163840, not 131072. Discussing with AI, this behavior also seems unreasonable. "The above translation is provided by ChatGPT." ### Before submitting a new issue... - [x] Make...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rning appeared: ``` Token indices sequence length is longer than the specified maximum sequence length for this model (160004 > 131072). Running this sequence through the model will result in indexing errors ``` While t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;fp8;operator;quantization;sampling;triton build_error;crash;mismatch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Input sequence length exceeds model's maximum sequence length (160004 > 131072) bug;stale ### Your current environment ### 🐛 Describe the bug I deployed the DeepSeek-V3.2-Exp model from https://huggingface.co/dee...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: nce length exceeds model's maximum sequence length (160004 > 131072) bug;stale ### Your current environment ### 🐛 Describe the bug I deployed the DeepSeek-V3.2-Exp model from https://huggingface.co/deepseek-ai/DeepSeek-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
