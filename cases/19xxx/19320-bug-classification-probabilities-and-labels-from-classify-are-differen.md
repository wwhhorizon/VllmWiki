# vllm-project/vllm#19320: [Bug]: Classification probabilities and labels from `/classify` are different from using HF's `transformers` pipeline

| 字段 | 值 |
| --- | --- |
| Issue | [#19320](https://github.com/vllm-project/vllm/issues/19320) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Classification probabilities and labels from `/classify` are different from using HF's `transformers` pipeline

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I try to deploy a fine-tuned `Qwen2.5-Coder-1.5B-Instruct` for a sequence classification task and use it via [the `/classify` endpoint](https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html#classification-api_1), I see the probability outputs are entirely different and for a lot of instances, the predicted classes are flipped compare to inference with `transformers`'s pipeline. ```python from transformers import pipeline MODEL_NAME = 'Qwen/Qwen2.5-Coder-1.5B-Instruct' # Placeholder for fine-tuned model classifier = pipeline("text-classification", model=MODEL_NAME, tokenizer=tokenizer) preds = classifier(prompts, return_all_scores=True) ``` I have checked to make sure the prompt sent to both are the same. I'm not super sure whether this is expected or a bug, and if this is expected, is there any way to make the two outputs the same? I assume when fine-tuning with `Qwen2ForSequenceClassification`, the HF's `transformers` pipeline implementation should be the correct way to use the model (i.e., the training and inference will match). Thanks! ### Before submitting a new issue... - [x] Make sure you already searche...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: o inference with `transformers`'s pipeline. ```python from transformers import pipeline MODEL_NAME = 'Qwen/Qwen2.5-Coder-1.5B-Instruct' # Placeholder for fine-tuned model classifier = pipeline("text-classification", mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ation probabilities and labels from `/classify` are different from using HF's `transformers` pipeline bug ### Your current environment ### 🐛 Describe the bug When I try to deploy a fine-tuned `Qwen2.5-Coder-1.5B-Instruc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting;model_support cuda build_error env...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
