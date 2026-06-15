# vllm-project/vllm#36112: [Bug]: bge-large-en-v1.5 embedding model can not be use when I use vllm to deploy the embedding model.

| 字段 | 值 |
| --- | --- |
| Issue | [#36112](https://github.com/vllm-project/vllm/issues/36112) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: bge-large-en-v1.5 embedding model can not be use when I use vllm to deploy the embedding model.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use the following comand to deploy the bge embedding model: 1. modelscope download --model BAAI/bge-large-en-v1.5 --local_dir ./bge_model 2. CUDA_VISIBLE_DEVICE=6 vllm serve ./bge_model \ --host 0.0.0.0 --port 13003 --block-size 16 \ --api-key 123456 --dtype auto \ --trust-remote-code \ --served-model-name embed \ --enable-prefix-caching \ --gpu-memory-utilization 0.9 \ --task embed --disable-log-requests 3. And then I use the langchain embedding module to embed text like this: ```python from langchain_openai import ChatOpenAI, OpenAIEmbeddings # 初始化嵌入模型 embed_model = OpenAIEmbeddings( api_key=embedding_api_key, base_url=embedding_base_url, model=embedding_model_name, ) # 测试嵌入模型 test_text = "This is a test sentence for embedding." embedding_result = embed_model.embed_query(test_text) ``` we would get the next error in vllm backend: ```text Traceback (most recent call last): File "/home/zhujiajian/survey/milvus/exps/models.py", line 41, in embedding_result = embed_model.embed_query(test_text) File "/home/zhujiajian/survey/.venv/lib/python3.13/site-packages/langchain_openai/embeddings/base.py", line 801, in embed_query return sel...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: scope download --model BAAI/bge-large-en-v1.5 --local_dir ./bge_model 2. CUDA_VISIBLE_DEVICE=6 vllm serve ./bge_model \ --host 0.0.0.0 --port 13003 --block-size 16 \ --api-key 123456 --dtype auto \ -
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: bed_model.embed_query(test_text) ``` we would get the next error in vllm backend: ```text Traceback (most recent call last): File "/home/zhujiajian/survey/milvus/exps/models.py", line 41, in embedding_result = embed_mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mbedding module to embed text like this: ```python from langchain_openai import ChatOpenAI, OpenAIEmbeddings # 初始化嵌入模型 embed_model = OpenAIEmbeddings( api_key=embedding_api_key, base_url=embedding_base_url, model=embedd...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 13003 --block-size 16 \ --api-key 123456 --dtype auto \ --trust-remote-code \ --served-model-name embed \ --enable-prefi
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: serve ./bge_model \ --host 0.0.0.0 --port 13003 --block-size 16 \ --api-key 123456 --dtype auto \ --trust-remote-code \ --served-model-name embed

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
