# vllm-project/vllm#2240: Get weird answer when loading Llama2-7b-chat-hf by using VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#2240](https://github.com/vllm-project/vllm/issues/2240) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Get weird answer when loading Llama2-7b-chat-hf by using VLLM

### Issue 正文摘录

Hi, I got a problem when I load Llama2-7B-Chat-Hf by using VLLM **Config info:** vllm 0.2.6 transformers 4.36.2 LLM Llama2-7B-Chat-Hf Python 3.10.12 Ubuntu 22.04 GPU NVIDIA 4090 24gb **Code** llm = VLLM(model="meta-llama/Llama-2-7b-chat-hf", tensor_parallel_size=1, trust_remote_code=True, temperature=0.6, top_k=5, top_p=0.9, torch_dtype=torch.bfloat16, max_new_tokens=500) llm("hello") **Answer from llm("hello"):** @matthew-mitchell.com [www.matthew-mitchell.com](http://www.matthew-mitchell.com/) Matthew Mitchell is a composer ... I also try another question "explain to me the meaning of 'hi how are you today?' " and get weird answer too. **My questions** 1. Can you please reproduce the answer to check if you get the same problem as me? If yes, please let me know how to fix this problem. 2. Also, Llama2-7b-Chat occupied around 21GB from VRAM. However, previously, I run exactly the same code before but it takes only around 14GB VRAM). Moreover, when I use VLLM to load a LLM-13B model (model size is about 26GB) but it occupied around 23GB for each of my GPU-4090 24GB (I have two GPU-4090 24GB). I think VLLM intends to take more memory from GPUs.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Get weird answer when loading Llama2-7b-chat-hf by using VLLM Hi, I got a problem when I load Llama2-7B-Chat-Hf by using VLLM **Config info:** vllm 0.2.6 transformers 4.36.2 LLM Llama2-7B-Chat-Hf Python 3.10.12 Ubuntu 2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ze=1, trust_remote_code=True, temperature=0.6, top_k=5, top_p=0.9, torch_dtype=torch.bfloat16, max_new_tokens=500) llm("hello") **Answer from llm("hello"):** @matthew-mitchell.com [www.matthew-mitchell.com](http://www.m...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: today?' " and get weird answer too. **My questions** 1. Can you please reproduce the answer to check if you get the same problem as me? If yes, please let me know how to fix this problem. 2. Also, Llama2-7b-Chat occupie...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: from GPUs. performance model_support;sampling_logits sampling dtype;env_dependency Hi,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
