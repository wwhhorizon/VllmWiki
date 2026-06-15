# vllm-project/vllm#16892: [Bug]: Pooling last token differences with Sentence Transformers for embedding models

| 字段 | 值 |
| --- | --- |
| Issue | [#16892](https://github.com/vllm-project/vllm/issues/16892) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Pooling last token differences with Sentence Transformers for embedding models

### Issue 正文摘录

### Your current environment vLLM 0.8.4 ### 🐛 Describe the bug `"pooling_mode_lasttoken": true` outputs dont match between vLLM and sentence transformers for embedding models. See this [model config](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct/blob/main/1_Pooling/config.json). Illustrated example: ```python from vllm import LLM from sentence_transformers import SentenceTransformer import numpy as np model_path = "Alibaba-NLP/gte-Qwen2-1.5B-instruct" queries = [ "how much protein should a female eat", "summit define", ] documents = [ "As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.", "Definition of summit for English Language Learners. : 1 the highest point of a mountain : the top of a mountain. : 2 the highest level. : 3 a meeting or series of meetings between the leaders of two or more governments.", ] # Sentence transformers model = SentenceTransformer(model_path, trust_remote_code=True) query_embeddings = model...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Pooling last token differences with Sentence Transformers for embedding models bug ### Your current environment vLLM 0.8.4 ### 🐛 Describe the bug `"pooling_mode_lasttoken": true` outputs dont match between vLLM and sent...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 3.753040713220344]] ``` Pure transformers/torch implementation gives the same outputs as sentence transformers. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /main/1_Pooling/config.json). Illustrated example: ```python from vllm import LLM from sentence_transformers import SentenceTransformer import numpy as np model_path = "Alibaba-NLP/gte-Qwen2-1.5B-instruct" queries = [ "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
