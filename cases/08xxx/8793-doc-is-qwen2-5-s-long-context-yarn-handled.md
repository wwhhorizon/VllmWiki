# vllm-project/vllm#8793: [Doc]: Is Qwen2.5's long context YARN handled?

| 字段 | 值 |
| --- | --- |
| Issue | [#8793](https://github.com/vllm-project/vllm/issues/8793) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | race_cond |
| Operator 关键词 | cuda;triton |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: Is Qwen2.5's long context YARN handled?

### Issue 正文摘录

### 📚 The doc issue https://huggingface.co/Qwen/Qwen2.5-72B-Instruct#processing-long-texts But when starting like this: ``` docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=4,5,6,7"' \ --shm-size=10.24gb \ -p 5001:5001 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name qwen25_72b \ vllm/vllm-openai:latest \ --port=5001 \ --host=0.0.0.0 \ --model=Qwen/Qwen2.5-72B-Instruct \ --tensor-parallel-size=4 \ --seed 1234 \ --trust-remote-code \ --max-model-len=131072 \ --max-num-batched-tokens 131072 \ --max-log-len=100 \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.qwen25_72b.txt ``` I get failure: ``` ValueError: User-specified max_model_len (131072) is greater than the derived max_model_len (max_position_embeddings=32768 or model_max_length=None in model's config.json). This may lead to incorrect model outputs or CUDA errors. To allow overriding this maximum, set the env var VLLM_ALLOW_LONG_MAX_MODEL_ LE...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Doc]: Is Qwen2.5's long context YARN handled? documentation;stale ### 📚 The doc issue https://huggingface.co/Qwen/Qwen2.5-72B-Instruct#processing-long-texts But when starting like this: ``` docker run -d --restart=alwa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: .5-72B-Instruct#processing-long-texts But when starting like this: ``` docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=4,5,6,7"' \ --shm-size=10.24gb \ -p 5001:5001 \ -e NCCL_IGNORE_DISABLED_P2P=1 \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: one in model's config.json). This may lead to incorrect model outputs or CUDA errors. To allow overriding this maximum, set the env var VLLM_ALLOW_LONG_MAX_MODEL_ LEN=1 ``` ### Suggest a potential alternative/fix Unsure...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name qwen25_72b \ vllm/vllm-openai:latest \ --port=5001 \ --host=0.0.0.0 \ --model=Qwen/Qwen2.5-72B-Instr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ons. correctness ci_build;distributed_parallel;model_support cuda;triton mismatch 📚 The doc issue

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
