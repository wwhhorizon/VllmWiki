# vllm-project/vllm#21681: [Bug]: Qwen3-Reranker issue with score

| 字段 | 值 |
| --- | --- |
| Issue | [#21681](https://github.com/vllm-project/vllm/issues/21681) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Reranker issue with score

### Issue 正文摘录

### Your current environment docker-compose.yml ```docker-compose.yml services: vllm: build: context: . dockerfile: Dockerfile container_name: vllm runtime: nvidia environment: NVIDIA_VISIBLE_DEVICES: all NVIDIA_DRIVER_CAPABILITIES: all HF_TOKEN: ${HF_TOKEN} HUGGING_FACE_HUB_TOKEN: ${HF_TOKEN} volumes: - huggingface-cache:/app/.cache/huggingface ports: - "8000:8000" ipc: host command: [ "--model=Qwen/Qwen3-Reranker-4B", "--trust-remote-code", "--dtype=bfloat16", "--gpu-memory-utilization=0.8", "--max-seq-len-to-capture=8192", "--max-model-len=8192", "--cpu-offload-gb=0", "--tensor-parallel-size=1", "--disable-log-requests", "--hf_overrides={\"architectures\": [\"Qwen3ForSequenceClassification\"],\"classifier_from_token\": [\"no\", \"yes\"],\"is_original_qwen3_reranker\": true}" ] ``` ### 🐛 Describe the bug I launched Qwen/Qwen3-Reranker-4B and found that the output score is incorrect and the ranking is very poor, seemingly random. If I run the same thing with the original Qwen code via transformers, everything works fine. There seems to be an error in your implementation. For example: Request to vllm: ``` { "query": "What types of transistors are there?", "documents": [ "The prima...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Qwen3-Reranker issue with score bug ### Your current environment docker-compose.yml ```docker-compose.yml services: vllm: build: context: . dockerfile: Dockerfile container_name: vllm runtime: nvidia environment:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-Reranker issue with score bug ### Your current environment docker-compose.yml ```docker-compose.yml services: vllm: build: context: . dockerfile: Dockerfile container_name: vllm runtime:
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: "--model=Qwen/Qwen3-Reranker-4B", "--trust-remote-code", "--dtype=bfloat16", "--gpu-memory-utilization=0.8", "--max-seq-len-to-capture=8192", "--max-model-len=8192", "--cpu-offload-gb=0", "--tensor-parallel-size=1", "--...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rallel-size=1", "--disable-log-requests", "--hf_overrides={\"architectures\": [\"Qwen3ForSequenceClassification\"],\"classifier_from_token\": [\"no\", \"yes\"],\"is_original_qwen3_reranker\": true}" ] ``` ### 🐛 Describe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: "Qwen/Qwen3-Reranker-4B", torch_dtype=torch.bfloat16 ).to(device).eval() token_false_id = tokenizer.convert_tokens_to_ids("no") token_true_id = tokenizer.convert_tokens_to_ids("yes") max_length = 8192 prefix = " system\...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
