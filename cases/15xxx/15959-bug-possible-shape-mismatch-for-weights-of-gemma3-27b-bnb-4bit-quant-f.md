# vllm-project/vllm#15959: [Bug]: Possible shape mismatch for weights of gemma3 27b bnb 4bit quant from Unsloth

| 字段 | 值 |
| --- | --- |
| Issue | [#15959](https://github.com/vllm-project/vllm/issues/15959) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Possible shape mismatch for weights of gemma3 27b bnb 4bit quant from Unsloth

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Apparently it looks like for the Unsloth 4bit quantized model using bitsandbytes the model shape is mismatched? or the weights? can't really tell much from the error messsage here ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Possible shape mismatch for weights of gemma3 27b bnb 4bit quant from Unsloth bug ### Your current environment ### 🐛 Describe the bug Apparently it looks like for the Unsloth 4bit quantized model using bitsandbyt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Possible shape mismatch for weights of gemma3 27b bnb 4bit quant from Unsloth bug ### Your current environment ### 🐛 Describe the bug Apparently it looks like for the Unsloth 4bit quantized model using bitsandbyt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Possible shape mismatch for weights of gemma3 27b bnb 4bit quant from Unsloth bug ### Your current environment ### 🐛 Describe the bug Apparently it looks like for the Unsloth 4bit quantized model using bitsandbyt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rdware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;gemm;operator;quantization;sampling;triton build_error;crash;mismatch;nan_inf;slowdown dtype;...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
