# vllm-project/vllm#14102: [Bug]:  max_model_len setting fail

| 字段 | 值 |
| --- | --- |
| Issue | [#14102](https://github.com/vllm-project/vllm/issues/14102) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cache;cuda;operator;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  max_model_len setting fail

### Issue 正文摘录

### Your current environment ''' Because the limitation of kv memory, I added " max_model_len=10000, enforce_max_model_len=True,". But it didn't work, the error message still showed the original big window size. The model's max seq len (131072) is larger than the maximum number of tokens that can be stored in KV cache (103632). ''' ### 🐛 Describe the bug Because the limitation of kv memory, I added " max_model_len=10000, enforce_max_model_len=True,". But it didn't work, the error message still showed the original big window size. The model's max seq len (131072) is larger than the maximum number of tokens that can be stored in KV cache (103632). The code: from langchain.llms import VLLM from langchain.prompts import PromptTemplate from langchain.chains import ConversationalRetrievalChain from langchain.memory import ConversationBufferMemory model_path = "/root/commonData/DeepSeek-R1-Distill-Qwen-7B" llm_local = VLLM( model=model_path, max_model_len=1000, enforce_max_model_len=True, gpu_memory_utilization=0.9, tensor_parallel_size=1, temperature=0.8, top_p=0.95, max_tokens=512, ) Error messages: ValidationError: 1 validation error for VLLM Value error, The model's max seq len (1310...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: that can be stored in KV cache (103632). The code: from langchain.llms import VLLM from langchain.prompts import PromptTemplate from langchain.chains import ConversationalRetrievalChain from langchain.memory import Conv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: max_model_len setting fail bug;stale ### Your current environment ''' Because the limitation of kv memory, I added " max_model_len=10000, enforce_max_model_len=True,". But it didn't work, the error message still...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ror ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ts import PromptTemplate from langchain.chains import ConversationalRetrievalChain from langchain.memory import ConversationBufferMemory model_path = "/root/commonData/DeepSeek-R1-Distill-Qwen-7B" llm_local = VLLM( mode...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 31072) is larger than the maximum number of tokens that can be stored in KV cache (103632). ''' ### 🐛 Describe the bug Because the limitation of kv memory, I added " max_model_len=10000, enforce_max_model_len=True,". Bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
