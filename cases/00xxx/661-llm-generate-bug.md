# vllm-project/vllm#661: llm.generate BUG

| 字段 | 值 |
| --- | --- |
| Issue | [#661](https://github.com/vllm-project/vllm/issues/661) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | nan_inf |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> llm.generate BUG

### Issue 正文摘录

I loaded the GPT-NEOX-20B model on a RTX8000 with 48G of memory, then modified the offline_inference.py file in the example directory, changed max_tokens to 512, and expanded the prompts to 78 sentences, and set a string as the stop condition. Then when I executed llm.generate, it got stuck at the progress bar, with no error or hint, the progress bar was always 0, but the graphics card was no longer loaded at this time. I tried to put only one question, and other conditions remained unchanged, and sometimes it could run normally. Then I observed the status of the graphics card and found that the model occupied 39G of the graphics card, and the graphics card occupied less than 42G at most when generating. In normal cases of 512 tokens inference, it should occupy more cuda memory. It was fully loaded at first, and then suddenly it was empty. This looks a bit like cuda memory overflow, but because there is no error or hint information, it just stopped there, I am not sure. Here is a screenshot of the running stuck: ![image](https://github.com/vllm-project/vllm/assets/35474337/0b3fb3d6-cad5-481d-a410-b993930feed5) ![image](https://github.com/vllm-project/vllm/assets/35474337/5d971ff6-...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: llm.generate BUG I loaded the GPT-NEOX-20B model on a RTX8000 with 48G of memory, then modified the offline_inference.py file in the example directory, changed max_tokens to 512, and expanded the prompts to 78 sentences...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llm.generate BUG I loaded the GPT-NEOX-20B model on a RTX8000 with 48G of memory, then modified the offline_inference.py file in the example directory, changed max_tokens to 512, and expanded the prompts to 78 sentences...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
