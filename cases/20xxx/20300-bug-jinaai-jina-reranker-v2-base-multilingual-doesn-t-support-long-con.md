# vllm-project/vllm#20300: [Bug]: `jinaai/jina-reranker-v2-base-multilingual` doesn't support long context above 1024 tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#20300](https://github.com/vllm-project/vllm/issues/20300) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `jinaai/jina-reranker-v2-base-multilingual` doesn't support long context above 1024 tokens

### Issue 正文摘录

### Your current environment vLLM Production Stack on Kube with Helm. Helm values: ```yaml servingEngineSpec: runtimeClassName: '' modelSpec: - name: bge-reranker-v2-m3 repository: vllm/vllm-openai tag: v0.9.1 modelURL: BAAI/bge-reranker-v2-m3 replicaCount: 1 requestCPU: 8 requestMemory: 16Gi requestGPU: 1 - name: jina-reranker-v2-base-multilingual repository: vllm/vllm-openai tag: v0.9.1 modelURL: jinaai/jina-reranker-v2-base-multilingual replicaCount: 1 requestCPU: 8 requestMemory: 8Gi requestGPU: 1 vllmConfig: extraArgs: - --trust-remote-code ``` ### 🐛 Describe the bug [`jinaai/jina-reranker-v2-base-multilingual`](https://huggingface.co/jinaai/jina-reranker-v2-base-multilingual) is no supporting long context reranking above 1024 with vLLM while outside vLLM (with Transformers) it will support it. This is the error we get from `/v1/rerank` when invoking the request. We tested with [`BAAI/bge-reranker-v2-m3`](https://huggingface.co/BAAI/bge-reranker-v2-m3) which ends up working nicely without issue with long context (>1024 tokens), it's just long context mode (>1024 tokens) on the jina reranking model that fails. ``` BadRequestError: status_code: 400, body: {'object': 'error', 'm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: values: ```yaml servingEngineSpec: runtimeClassName: '' modelSpec: - name: bge-reranker-v2-m3 repository: vllm/vllm-openai tag: v0.9.1 modelURL: BAAI/bge-reranker-v2-m3 replicaCount: 1 requestCPU: 8 requestMe
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: modelURL: BAAI/bge-reranker-v2-m3 replicaCount: 1 requestCPU: 8 requestMemory: 16Gi requestGPU: 1 - name: jina-reranker-v2-base-multilingual repository: vllm/vllm-openai tag: v0.9.1 modelURL: jinaai/jina-reranker
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: This is the error we get from `/v1/rerank` when invoking the request. We tested with [`BAAI/bge-reranker-v2-m3`](https://huggingface.co/BAAI/bge-reranker-v2-m3) which ends up working nicely without issue with long conte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
