# vllm-project/vllm#7265: [Feature]: Custom Embedding function for vector databases (Chroma & Quadrant)

| 字段 | 值 |
| --- | --- |
| Issue | [#7265](https://github.com/vllm-project/vllm/issues/7265) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Custom Embedding function for vector databases (Chroma & Quadrant)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### 🚀 The feature, motivation and pitch I served an open-source embedding model via VLLM (as a stand alone server). The issue is that I cannot directly use vllm's open-ai wrapper with chroma or quadrant for custom embedding function. Usually it throws some internal function parameter errors or some time throws memory errors on vllm server logs (despite setting up all arguments correctly). Since I am using Langchain , I have written a wrapper for custom embedding function which utilises vllm open-ai wrapper and is also tested out with large number of requests (load testing). ``` from openai import OpenAI from langchain_core.embeddings import Embeddings from typing import List from app.main import logger class VllmEmbeddingFunction(Embeddings): def __init__(self) -> None: super().__init__() self.openai_client = OpenAI(api_key="EMPTY",base_url="http://1.2.3.4:3000/v1") # base url is of vllm server self.model = "MODEL_NAME" def embed_documents(self, texts: List[str]) -> List[List[float]]: embeddings = [] try: responses = self.openai_client.embeddings.create( input=texts, model=self.model, encoding_format="float", ) # Extracting the embeddings fr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # 🚀 The feature, motivation and pitch I served an open-source embedding model via VLLM (as a stand alone server). The issue is that I cannot directly use vllm's open-ai wrapper with chroma or quadrant for custom embeddi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ested out with large number of requests (load testing). ``` from openai import OpenAI from langchain_core.embeddings import Embeddings from typing import List from app.main import logger class VllmEmbeddingFunction(Embe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: generated successfully") return embeddings else: logger.warning("Warning: 'data' not found in response.") return [] except Exception as e: logger.error(f"Error in VllmEmbeddingFunction: {e}") return [
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: stom Embedding function for vector databases (Chroma & Quadrant) feature request ### 🚀 The feature, motivation and pitch ### 🚀 The feature, motivation and pitch I served an open-source embedding model via VLLM (as a sta...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ustom embedding function which utilises vllm open-ai wrapper and is also tested out with large number of requests (load testing). ``` from openai import OpenAI from langchain_core.embeddings import Embeddings from typin...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
