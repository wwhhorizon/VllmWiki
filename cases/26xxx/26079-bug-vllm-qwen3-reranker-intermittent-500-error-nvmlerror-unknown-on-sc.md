# vllm-project/vllm#26079: [Bug]: vLLM Qwen3 Reranker intermittent 500 error - NVMLError_Unknown on score endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#26079](https://github.com/vllm-project/vllm/issues/26079) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM Qwen3 Reranker intermittent 500 error - NVMLError_Unknown on score endpoint

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1. start `qwen3-0.6b` reranker ``` docker run --name reranker \ --runtime nvidia --gpus '"device=1"' \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --restart unless-stopped \ -p 8003:8000 \ --shm-size=4g \ --entrypoint /bin/bash \ vllm/vllm-openai:latest \ -c "pip install --force-reinstall --no-deps nvidia-nccl-cu12==2.27.7 && \ VLLM_USE_V1=0 python3 -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-Reranker-0.6B \ --task score \ --hf-overrides '{\"architectures\": [\"Qwen3ForSequenceClassification\"],\"classifier_from_token\": [\"no\", \"yes\"],\"is_original_qwen3_reranker\": true}'" ``` 2. Monitored logs over an extended period. (Does not always occur!) 3. check [this log](https://gist.github.com/Cyp9715/6db9628a1975625e5837f04134802edf). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ironment ### 🐛 Describe the bug 1. start `qwen3-0.6b` reranker ``` docker run --name reranker \ --runtime nvidia --gpus '"device=1"' \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --restart unless-stopped \ -p 800...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM Qwen3 Reranker intermittent 500 error - NVMLError_Unknown on score endpoint bug;stale ### Your current environment ### 🐛 Describe the bug 1. start `qwen3-0.6b` reranker ``` docker run --name reranker \ -
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r-0.6B \ --task score \ --hf-overrides '{\"architectures\": [\"Qwen3ForSequenceClassification\"],\"classifier_from_token\": [\"no\", \"yes\"],\"is_original_qwen3_reranker\": true}'" ``` 2. Monitored logs over an extende...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eranker intermittent 500 error - NVMLError_Unknown on score endpoint bug;stale ### Your current environment ### 🐛 Describe the bug 1. start `qwen3-0.6b` reranker ``` docker run --name reranker \ --runtime nvidia --gpus...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
