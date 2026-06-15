# vllm-project/vllm#39631: [Bug]: Abnormal Scores in Batch Processing of Image-Text Pairs with qwen3-VL-reranker Model

| 字段 | 值 |
| --- | --- |
| Issue | [#39631](https://github.com/vllm-project/vllm/issues/39631) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Abnormal Scores in Batch Processing of Image-Text Pairs with qwen3-VL-reranker Model

### Issue 正文摘录

### Your current environment Description: When using qwen3-VL-reranker, the returned scores are normal when processing each image-text pair individually. However, when using the format of one text corresponding to multiple images (batch processing), although scores are returned normally, there is a significant deviation in the scores. The results of these two approaches are completely different. Environment: GPU: NVIDIA V100 VLLM version: 0.18 OS: Ubuntu 24.04 Model: Qwen3-VL-Reranker-2B CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /home/kongkong/.cache/modelscope/hub/models/Qwen/Qwen3-VL-Reranker-2B \ --runner pooling \ --port 8001 \ --host 0.0.0.0 \ --dtype float16 \ --max-model-len 4096 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 32 \ --max-num-batched-tokens 2048 \ --hf-overrides '{"architectures": ["Qwen3VLForSequenceClassification"], "classifier_from_token": ["no", "yes"], "is_original_qwen3_reranker": true}' \ --allowed-local-media-path /home/kongkong/下载/测试 \ --chat-template /home/kongkong/下载/qwen3_vl_reranker.jinja ### 🐛 Describe the bug Reproduction Steps: Submit a batch request with one text query against ~100 images Compare the score...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Abnormal Scores in Batch Processing of Image-Text Pairs with qwen3-VL-reranker Model bug ### Your current environment Description: When using qwen3-VL-reranker, the returned scores are normal when processing each...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 2B \ --runner pooling \ --port 8001 \ --host 0.0.0.0 \ --dtype float16 \ --max-model-len 4096 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 32 \ --max-num-batched-tokens 2048 \ --hf-overrides '{"architectures": ["Qwen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: VLLM version: 0.18 OS: Ubuntu 24.04 Model: Qwen3-VL-Reranker-2B CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /home/kongkong/.cache/modelscope/hub/models/Qwen/Qwen3-VL-Reranker-2B \ --run...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: es are completely different. Environment: GPU: NVIDIA V100 VLLM version: 0.18 OS: Ubuntu 24.04 Model: Qwen3-VL-Reranker-2B CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /home/kongkong/.ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: r.jinja ### 🐛 Describe the bug Reproduction Steps: Submit a batch request with one text query against ~100 images Compare the scores with individual single-pair processing curl http://localhost:8001/rerank \ -H "Content...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
