# vllm-project/vllm#12379: [Usage]: How to run vllm with regression task, just like classify task

| 字段 | 值 |
| --- | --- |
| Issue | [#12379](https://github.com/vllm-project/vllm/issues/12379) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to run vllm with regression task, just like classify task

### Issue 正文摘录

### Your current environment I have trained qwen2.5 with regression task, below is inference code : from transformers import AutoTokenizer, AutoModelForSequenceClassification import torch tokenizer = AutoTokenizer.from_pretrained("qwen3_score_0123", trust_remote_code=True) model = AutoModelForSequenceClassification.from_pretrained( "qwen3_score_0123", num_labels=1, problem_type="regression", trust_remote_code=True ).to(torch.bfloat16) device = torch.device("cuda:2" if torch.cuda.is_available() else "cpu") model.to(device) model.eval() text = """ hello """ inputs = tokenizer( text, truncation=True, padding='max_length', max_length=512, return_tensors="pt" ) inputs = {key: value.to(device) for key, value in inputs.items()} with torch.no_grad(): outputs = model(**inputs) predicted_score = outputs.logits.item() ### How would you like to use vllm I want to inference the qwen llm regression model with vllm, need help ,thanks ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: =1, problem_type="regression", trust_remote_code=True ).to(torch.bfloat16) device = torch.device("cuda:2" if torch.cuda.is_available() else "cpu") model.to(device) model.eval() text = """ hello """ inputs = tokenizer( t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: How to run vllm with regression task, just like classify task usage;stale ### Your current environment I have trained qwen2.5 with regression task, below is inference code : from transformers import AutoTokeniz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 2.5 with regression task, below is inference code : from transformers import AutoTokenizer, AutoModelForSequenceClassification import torch tokenizer = AutoTokenizer.from_pretrained("qwen3_score_0123", trust_remote_code...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: trust_remote_code=True ).to(torch.bfloat16) device = torch.device("cuda:2" if torch.cuda.is_available() else "cpu") model.to(device) model.eval() text = """ hello """ inputs = tokenizer( text, truncation=True, padding='...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e classify task usage;stale ### Your current environment I have trained qwen2.5 with regression task, below is inference code : from transformers import AutoTokenizer, AutoModelForSequenceClassification import torch tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
