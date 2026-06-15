# vllm-project/vllm#8866: [Performance]: Slowdown compared to Gradio

| 字段 | 值 |
| --- | --- |
| Issue | [#8866](https://github.com/vllm-project/vllm/issues/8866) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Slowdown compared to Gradio

### Issue 正文摘录

### Proposal to improve performance vLLM is amazingly fast However, when running below prompt, with meta-llama/Meta-Llama-3-8B-Instruct, Gradio takes ~4sec per prompt (one by one) while vLLM takes ~12sec by def. When setting --quantization fp8 times reduced to ~8s Overall vLLM is much faster since it allows to process in parallel while Gradio doesn't Tested with AWS L4, Gradio 4.43.0 What am I missing? `prompt = """You are a knowledgeable, efficient, and direct Al assistant. Provide concise answers up to 100 words` `without explainations or extra notes, focusing on the key information needed. Answer in question: answer JSON format` `**User:**I like the color red. Our website is www.nba.com. My age is 18.` `**Assistant:**Great. Write 3 things for me to answer.` `**User:**What is our website? What is my age? What kind of drink do I like to drink?` `**Assistant**:` `"""` ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: c per prompt (one by one) while vLLM takes ~12sec by def. When setting --quantization fp8 times reduced to ~8s Overall vLLM is much faster since it allows to process in parallel while Gradio doesn't Tested with AWS L4,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: dio 4.43.0 What am I missing? `prompt = """You are a knowledgeable, efficient, and direct Al assistant. Provide concise answers up to 100 words` `without explainations or extra notes, focusing on the key information nee...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ce vLLM is amazingly fast However, when running below prompt, with meta-llama/Meta-Llama-3-8B-Instruct, Gradio takes ~4sec per prompt (one by one) while vLLM takes ~12sec by def. When setting --quantization fp8 times re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: much faster since it allows to process in parallel while Gradio doesn't Tested with AWS L4, Gradio 4.43.0 What am I missing? `prompt = """You are a knowledgeable, efficient, and direct Al assistant. Provide concise answ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
