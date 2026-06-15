# vllm-project/vllm#7382: [Bug]: LLaMa 3.1 8B/70B/405B all behave poorly and differently using completions API as compared to good chat API

| 字段 | 值 |
| --- | --- |
| Issue | [#7382](https://github.com/vllm-project/vllm/issues/7382) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | triton |
| 症状 | nondeterministic |
| 根因提示 | race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLaMa 3.1 8B/70B/405B all behave poorly and differently using completions API as compared to good chat API

### Issue 正文摘录

### Your current environment Docker latest 0.5.4 ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=0"' \ --shm-size=10.24gb \ -p 5000:5000 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ \ -v "${HOME}"/.cache/huggingface:$HOME/.cache/huggingface \ -v "${HOME}"/.cache/huggingface/hub:$HOME/.cache/huggingface/hub \ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name llama31_8b \ vllm/vllm-openai:latest \ --port=5000 \ --host=0.0.0.0 \ --model=meta-llama/Meta-Llama-3.1-8B-Instruct \ --seed 1234 \ --tensor-parallel-size=1 \ --max-model-len=131072 \ --max-num-batched-tokens=131072 --max-log-len=100 \ --served-model-name meta-llama/Meta-Llama-3.1-8B-Instruct meta-llama/Meta-Llama-3-8B-Instruct \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.llama3-8b.txt ``` ### 🐛 Describe the bug I cannot reproduce HuggingFace transformers...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: LLaMa 3.1 8B/70B/405B all behave poorly and differently using completions API as compared to good chat API bug;stale ### Your current environment Docker latest 0.5.4 ``` docker pull vllm/vllm-openai:latest docker...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: API as compared to good chat API bug;stale ### Your current environment Docker latest 0.5.4 ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=0"' \ --shm-size=10...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: &>> logs.vllm_server.llama3-8b.txt ``` ### 🐛 Describe the bug I cannot reproduce HuggingFace transformers (works) or Chat API with vLLM (works) against Completions API (fails). Both streaming and non-streaming completio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: mpared to good chat API bug;stale ### Your current environment Docker latest 0.5.4 ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=0"' \ --shm-size=10.24gb \ -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uggingface/hub \ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name llama31_8b \ vllm/vllm-openai:latest \ --port=5000 \ --host=0.0.0.0 \ --model=meta-llama/Meta-Llama-3.1-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
