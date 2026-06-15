# vllm-project/vllm#34910: [Bug]: the embeddings from vllm does not match hugging face sentence-transformer

| 字段 | 值 |
| --- | --- |
| Issue | [#34910](https://github.com/vllm-project/vllm/issues/34910) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: the embeddings from vllm does not match hugging face sentence-transformer

### Issue 正文摘录

### Your current environment Name: vllm Version: 0.15.1 ### 🐛 Describe the bug ```python from sentence_transformers import SentenceTransformer from vllm import LLM vllm_model = LLM(model="Qwen/Qwen3-Embedding-0.6B", gpu_memory_utilization=0.35, tensor_parallel_size=1,) hug_model = torch.compile(SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")) query_total = ''.join(__import__('random').choices('abcdefghijklmnopqrstuvwxyz ', k=10000)) for i in range(100, len(query_total), 100): query = query_total[:i] # Huggingface embeddings embeddings_huggingface = hug_model.encode([query]) # vllm embeddings outputs = llm_vllm.embed([query], truncate_prompt_tokens=None) vllm_embeddings = [o.outputs.embedding for o in outputs] diff = np.sum(np.abs(np.sign(embeddings_huggingface[0])-np.sign(vllm_embeddings))>0) print(f"Length: {i}, Sign differences: {diff}") ``` Length, Sign differences 100,10 200,7 300,9 400,6 500,5 600,4 700,5 800,12 900,7 1000,4 1100,4 1200,10 1300,5 1400,8 1500,8 1600,6 1700,20 1800,7 1900,6 2000,6 2100,10 2200,7 2300,9 2400,9 2500,8 2600,4 2700,9 2800,10 2900,6 3000,5 3100,5 3200,8 3300,6 3400,22 3500,5 3600,6 3700,20 3800,4 3900,5 4000,10 4100,5 4200,15 4300,4 4400,4 4500,16...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: g face sentence-transformer bug ### Your current environment Name: vllm Version: 0.15.1 ### 🐛 Describe the bug ```python from sentence_transformers import SentenceTransformer from vllm import LLM vllm_model = LLM(model=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ntence_transformers import SentenceTransformer from vllm import LLM vllm_model = LLM(model="Qwen/Qwen3-Embedding-0.6B", gpu_memory_utilization=0.35, tensor_parallel_size=1,) hug_model = torch.compile(SentenceTransformer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
