# vllm-project/vllm#2925: Unintended memory, clear or clean the memory

| 字段 | 值 |
| --- | --- |
| Issue | [#2925](https://github.com/vllm-project/vllm/issues/2925) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Unintended memory, clear or clean the memory

### Issue 正文摘录

I don't expect the model to remember the last prompt. Not directly, though, I might want to implement a history by sending a list of messages, but if runed with out merign the prompt I don't expect it to return different results: Running the following basic example: ```python from langchain_community.llms import VLLM from src.models.literals_types_constants import VLLM_DOWNLOAD_PATH llm = VLLM( model="mosaicml/mpt-7b", trust_remote_code=True, # mandatory for hf models download_dir=VLLM_DOWNLOAD_PATH, max_new_tokens=128, top_k=10, top_p=0.95, temperature=0.8, ) print(llm.invoke("What is the capital of France ?")) print(llm.invoke("What is the capital of France ?")) print(llm.invoke("What is the capital of France ?")) ``` I expected the same-ish result for each questions, but I got extreamelly different ones. ``` Processed prompts: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 3.04it/s] What is the capital of France ? The capital of France is Paris. Processed prompts: 100%|████████████████████████████████████████████████████████████████████████████...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ng the following basic example: ```python from langchain_community.llms import VLLM from src.models.literals_types_constants import VLLM_DOWNLOAD_PATH llm = VLLM( model="mosaicml/mpt-7b", trust_remote_code=True, # manda...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Unintended memory, clear or clean the memory I don't expect the model to remember the last prompt. Not directly, though, I might want to implement a history by sending a list of messages, but if runed with out merign th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
