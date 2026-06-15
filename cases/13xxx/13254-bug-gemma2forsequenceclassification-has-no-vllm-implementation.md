# vllm-project/vllm#13254: [Bug]: Gemma2ForSequenceClassification has no vLLM implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#13254](https://github.com/vllm-project/vllm/issues/13254) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma2ForSequenceClassification has no vLLM implementation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Getting this error while using Skywork-Reward-Gemma. ``` WARNING 02-14 02:49:29 utils.py:69] Gemma2ForSequenceClassification has no vLLM implementation, falling back to Transformers implementation. Some features may not be supported and performance may not be optimal. ``` reference code ```python import torch from vllm import LLM from transformers import AutoTokenizer model_name = "Skywork/Skywork-Reward-Gemma-2-27B" llm = LLM(model=model_name, task="reward") rm_tokenizer = AutoTokenizer.from_pretrained(model_name) prompt = "Jane has 12 apples. She gives 4 apples to her friend Mark, then buys 1 more apple, and finally splits all her apples equally among herself and her 2 siblings. How many apples does each person get?" response1 = "1. Jane starts with 12 apples and gives 4 to Mark. 12 - 4 = 8. Jane now has 8 apples.\n2. Jane buys 1 more apple. 8 + 1 = 9. Jane now has 9 apples.\n3. Jane splits the 9 apples equally among herself and her 2 siblings (3 people in total). 9 \u00f7 3 = 3 apples each. Each person gets 3 apples." response2 = "1. Jane starts with 12 apples and gives 4 to Mark. 12 - 4 = 8. Jane now has 8 apples.\n2. Jane bu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rted and performance may not be optimal. ``` reference code ```python import torch from vllm import LLM from transformers import AutoTokenizer model_name = "Skywork/Skywork-Reward-Gemma-2-27B" llm = LLM(model=model_name...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma2ForSequenceClassification has no vLLM implementation bug;stale ### Your current environment ### 🐛 Describe the bug Getting this error while using Skywork-Reward-Gemma. ``` WARNING 02-14 02:49:29 utils.py:69]
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: }] conv1_formatted = rm_tokenizer.apply_chat_template(conv1, tokenize=False) conv2_formatted = rm_tokenizer.apply_chat_template(conv2, tokenize=False) score1 = llm.encode(conv1_formatted)[0] # Extract the scalar reward...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
