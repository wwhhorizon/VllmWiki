# vllm-project/vllm#10738: [Bug]: use /v1/score to do Rerank and get RuntimeError: torch.cat(): expected a non-empty list of Tensors

| 字段 | 值 |
| --- | --- |
| Issue | [#10738](https://github.com/vllm-project/vllm/issues/10738) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: use /v1/score to do Rerank and get RuntimeError: torch.cat(): expected a non-empty list of Tensors

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run vllm rerank functon with docker in following steps: ## Build docker git clone https://github.com/vllm-project/vllm.git cd ./vllm/ docker build -f Dockerfile.cpu -t vllm-cpu:latest --shm-size=128g . --build-arg https_proxy=$https_proxy --build-arg http_proxy=$http_proxy ## Launch docker container docker run -it --rm \ --name="vllm-service" \ -p 8003:80 \ --ipc=host \ -e HTTPS_PROXY=$https_proxy \ -e HTTP_PROXY=$https_proxy \ -e HF_TOKEN=${HF_TOKEN}\ -e VLLM_CPU_KVCACHE_SPACE=40 \ vllm-cpu:latest \ --model BAAI/bge-reranker-v2-m3 --host 0.0.0.0 --port 80 ## query refer to https://github.com/vllm-project/vllm/blob/main/docs/source/serving/openai_compatible_server.md#score-api-for-cross-encoder-models curl -X 'POST' \ 'http://0.0.0.0:8003/v1/score' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "model": "BAAI/bge-reranker-v2-m3", "text_1": "What is the capital of France?", "text_2": [ "The capital of Brazil is Brasilia.", "The capital of France is Paris." ] }' ## Then get following error log and container exit INFO: Started server process [1] INFO: Waiting for a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s _No response_ ### 🐛 Describe the bug I run vllm rerank functon with docker in following steps: ## Build docker git clone https://github.com/vllm-project/vllm.git cd ./vllm/ docker build -f Dockerfile.cpu -t vllm-cpu:l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: or log and container exit INFO: Started server process [1] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit) INFO 11-28 06:55:49...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [1] ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ted a non-empty list of Tensors bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run vllm rerank functon with docker in following steps: ## Build docker git clone https://git...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e? The capital of Brazil is Brasilia.', params: PoolingParams(additional_metadata=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None. INFO 11-28 06:55:49 logger.py:37] Received request score...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
