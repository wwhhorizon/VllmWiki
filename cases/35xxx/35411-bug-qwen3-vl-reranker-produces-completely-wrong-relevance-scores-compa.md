# vllm-project/vllm#35411: [Bug]:Qwen3-VL-Reranker produces completely wrong relevance scores compared to native Transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#35411](https://github.com/vllm-project/vllm/issues/35411) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Qwen3-VL-Reranker produces completely wrong relevance scores compared to native Transformers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug Description The `Qwen/Qwen3-VL-Reranker-2B` model produces severely incorrect relevance scores when running under VLLM compared to native Transformers inference. The ranking results are almost completely reversed - making the model practically unusable for reranking tasks. ## Reproduction Steps ### Environment - VLLM version: 0.16.0 (also tested on 0.15.x) - Model: `Qwen/Qwen3-VL-Reranker-2B` - GPU: CUDA 12.x - Python: 3.12 ### Launch Command ```bash CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /home/kongkong/.cache/modelscope/hub/models/Qwen/Qwen3-VL-Reranker-2B \ --runner pooling \ --port 8001 \ --host 0.0.0.0 \ --dtype float16 \ --max-model-len 4096 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 64 \ --max-num-batched-tokens 4096 \ --hf-overrides '{"architectures": ["Qwen3VLForSequenceClassification"], "classifier_from_token": ["no", "yes"], "is_original_qwen3_reranker": true}' \ --allowed-local-media-path /home/kongkong/下载/测试 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [doc...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 16.0 (also tested on 0.15.x) - Model: `Qwen/Qwen3-VL-Reranker-2B` - GPU: CUDA 12.x - Python: 3.12 ### Launch Command ```bash CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /home/kongkong/....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]:Qwen3-VL-Reranker produces completely wrong relevance scores compared to native Transformers bug ### Your current environment ### 🐛 Describe the bug ## Bug Description The `Qwen/Qwen3-VL-Reranker-2B` model produces
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: able for reranking tasks. ## Reproduction Steps ### Environment - VLLM version: 0.16.0 (also tested on 0.15.x) - Model: `Qwen/Qwen3-VL-Reranker-2B` - GPU: CUDA 12.x - Python: 3.12 ### Launch Command ```bash CUDA_VISIBLE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ker-2B \ --runner pooling \ --port 8001 \ --host 0.0.0.0 \ --dtype float16 \ --max-model-len 4096 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 64 \ --max-num-batched-tokens 4096 \ --hf-overrides '{"architectures": ["...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nswer lots of frequently asked questions. correctness model_support cuda mismatch dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
