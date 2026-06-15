# vllm-project/vllm#18984: [Usage]: How to Retrieve Model Parameters (e.g., Supported Embedding Dimensions) for an Embedding Model (Online Service)

| 字段 | 值 |
| --- | --- |
| Issue | [#18984](https://github.com/vllm-project/vllm/issues/18984) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to Retrieve Model Parameters (e.g., Supported Embedding Dimensions) for an Embedding Model (Online Service)

### Issue 正文摘录

### Your current environment ## Description: The scenario we are considering for a RAG application involves the following setup: 1. Deploying **VLLM** as an **OpenAI-compatible service** on a GPU server, serving an embedding model as its `task`. 2. A local machine requests the parameters of the serving model from the server. Examples of the parameters are: - The **maximum number of tokens** allowed for each input text to be embedded. - The **maximum length** of the target embedding supported by the model. - The types of task supported by the model. 3. The machine uses these parameters to determine subsequent actions, such as: - The **chunking strategy** for input text. - The **number of dimensions** to use for the embedding. ## Example: With `sentence_transformers` package, the following code retrieves the **maximum sequence length (in tokens)** for a model: ```python from sentence_transformers import SentenceTransformer # Initialize torch settings for device-agnostic code. N_GPU = torch.cuda.device_count() DEVICE = torch.device('cuda:N_GPU' if torch.cuda.is_available() else 'cpu') # Download the model from the Hugging Face model hub. model_name = "BAAI/bge-large-en-v1.5" encoder...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: gth (in tokens)** for a model: ```python from sentence_transformers import SentenceTransformer # Initialize torch settings for device-agnostic code. N_GPU = torch.cuda.device_count() DEVICE = torch.device('cuda:N_GPU' i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: # Initialize torch settings for device-agnostic code. N_GPU = torch.cuda.device_count() DEVICE = torch.device('cuda:N_GPU' if torch.cuda.is_available() else 'cpu') # Download the model from the Hugging Face model hub. m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rted Embedding Dimensions) for an Embedding Model (Online Service) usage;stale ### Your current environment ## Description: The scenario we are considering for a RAG application involves the following setup: 1. Deployin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: count() DEVICE = torch.device('cuda:N_GPU' if torch.cuda.is_available() else 'cpu') # Download the model from the Hugging Face model hub. model_name = "BAAI/bge-large-en-v1.5" encoder = SentenceTransformer(model_name, d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How to Retrieve Model Parameters (e.g., Supported Embedding Dimensions) for an Embedding Model (Online Service) usage;stale ### Your current environment ## Description: The scenario we are considering for a RAG...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
