# vllm-project/vllm#16153: jinaai/jina-reranker-v1-turbo-en not compatible with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16153](https://github.com/vllm-project/vllm/issues/16153) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> jinaai/jina-reranker-v1-turbo-en not compatible with vLLM

### Issue 正文摘录

Command used: docker run -v /home/sdp/vignesh/model_weights/vllm/:/data -it --rm --network=host --name jinaa-reranker-v1-turbo-en_vllm_vignesh vllm-cpu-env --port 8081 --host 0.0.0.0 --task score --model jinaai/jina-reranker-v1-turbo-en --dtype float32 --device cpu Problem Description When attempting to load jinaai/jina-reranker-v1-turbo-en in vLLM, the engine crashes with the following error: ValueError: JinaBertModel has no vLLM implementation and the Transformers implementation is not compatible with vLLM. Try setting VLLM_USE_V1=0. ### 🐛 Describe the bug ValueError: JinaBertModel has no vLLM implementation and the Transformers implementation is not compatible with vLLM. Try setting VLLM_USE_V1=0.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 1 --host 0.0.0.0 --task score --model jinaai/jina-reranker-v1-turbo-en --dtype float32 --device cpu Problem Description When attempting to load jinaai/jina-reranker-v1-turbo-en in vLLM, the engine crashes with the follo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: na-reranker-v1-turbo-en not compatible with vLLM bug;stale Command used: docker run -v /home/sdp/vignesh/model_weights/vllm/:/data -it --rm --network=host --name jinaa-reranker-v1-turbo-en_vllm_vignesh vllm-cpu-env --po...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: atible with vLLM bug;stale Command used: docker run -v /home/sdp/vignesh/model_weights/vllm/:/data -it --rm --network=host --name jinaa-reranker-v1-turbo-en_vllm_vignesh vllm-cpu-env --port 8081 --host 0.0.0.0 --task sc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: jinaai/jina-reranker-v1-turbo-en not compatible with vLLM bug;stale Command used: docker run -v /home/sdp/vignesh/model_weights/vllm/:/data -it --rm --network=host --name jinaa-reranker-v1-turbo-en_vllm_vignesh vllm-cpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
