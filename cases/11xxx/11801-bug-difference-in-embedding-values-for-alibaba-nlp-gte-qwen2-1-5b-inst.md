# vllm-project/vllm#11801: [Bug]: Difference in embedding values for Alibaba-NLP/gte-Qwen2-1.5B-instruct between vLLM and huggingface methods

| 字段 | 值 |
| --- | --- |
| Issue | [#11801](https://github.com/vllm-project/vllm/issues/11801) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Difference in embedding values for Alibaba-NLP/gte-Qwen2-1.5B-instruct between vLLM and huggingface methods

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I serve the Alibaba-NLP/gte-Qwen2-1.5B-instruct model using vllm and compare the embedding values with HuggingFace, the resulting similarity scores seem to be very different. First I serve the model using: `python -m vllm.entrypoints.openai.api_server --dtype auto --tensor-parallel-size 1 --enforce-eager --model gte-Qwen2-1.5B-instruct/snapshots/c6c1b92f4a3e1b92b326ad29dd3c8433457df8dd --gpu-memory-utilization 0.85 --task embed` Then on the client side, after initializing, I do the following: ``` responses = client.embeddings.create( input=[ "how much protein should a female eat", "summit define", ], model=model, ) query_embeddings = np.array([data.embedding for data in responses.data]) # QUERY EMBEDDINGS responses = client.embeddings.create( input=[ "As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 is 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or training for a marathon. Check out the chart below to see how much protein you should be eating each day.", "Definition of summit for English Lan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: entence Transformers, it looks like this: ``` from sentence_transformers import SentenceTransformer model = SentenceTransformer("gte-qwen2-1.5b-instruct/snapshots/ca1f7d7fda484a8024027bbc1769db97789034ff", trust_remote_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Difference in embedding values for Alibaba-NLP/gte-Qwen2-1.5B-instruct between vLLM and huggingface methods bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I serve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: :) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: I serve the model using: `python -m vllm.entrypoints.openai.api_server --dtype auto --tensor-parallel-size 1 --enforce-eager --model gte-Qwen2-1.5B-instruct/snapshots/c6c1b92f4a3e1b92b326ad29dd3c8433457df8dd --gpu-memor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
