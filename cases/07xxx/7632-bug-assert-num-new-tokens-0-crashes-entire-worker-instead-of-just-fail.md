# vllm-project/vllm#7632: [Bug]: assert num_new_tokens > 0 crashes entire worker instead of just failing single API call

| 字段 | 值 |
| --- | --- |
| Issue | [#7632](https://github.com/vllm-project/vllm/issues/7632) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | sampling;triton |
| 症状 | crash |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: assert num_new_tokens > 0 crashes entire worker instead of just failing single API call

### Issue 正文摘录

### Your current environment vllm docker 0.5.4 ``` docker pull vllm/vllm-openai:latest docker stop danube3_mig ; docker remove danube3_mig docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=MIG-a6dbed35-9d05-58da-a0b5-23ae5bf8427e"' \ --shm-size=10.24gb \ -p 5004:5004 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name danube3_mig \ vllm/vllm-openai:latest \ --port=5004 \ --host=0.0.0.0 \ --model=h2oai/h2o-danube3-4b-chat \ --seed 1234 \ --trust-remote-code \ --tensor-parallel-size=1 \ --max-model-len=8192 \ --gpu-memory-utilization=0.99 \ --max-num-batched-tokens=131072 --max-log-len=100 \ --use-v2-block-manager \ --num-speculative-tokens=5 \ --ngram-prompt-lookup-max=4 \ --enable-prefix-caching \ --speculative-model="[ngram]" \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.danube3_migb.txt ``` Unsure if has t...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 31072 --max-log-len=100 \ --use-v2-block-manager \ --num-speculative-tokens=5 \ --ngram-prompt-lookup-max=4 \ --enable-prefix-caching \ --speculative-model="[ngram]" \ --download-dir=$HOME/.cache/huggingface/hub &>> log...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d of just failing single API call bug ### Your current environment vllm docker 0.5.4 ``` docker pull vllm/vllm-openai:latest docker stop danube3_mig ; docker remove danube3_mig docker run -d --restart=always \ --runtime...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name danube3_mig \ vllm/vllm-openai:latest \ --port=5004 \ --host=0.0.0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: .cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name danube3_mig \ vllm/vllm-openai:latest \ --port=5004 \ --host=0.0.0.0 \ --model=h2oai/h2o-danube3-4b-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: --max-num-batched-tokens=131072 --max-log-len=100 \ --use-v2-block-manager \ --num-speculative-tokens=5 \ --ngram-prompt-lookup-max=4 \ --enable-prefix-caching \ --speculative-model="[ngram]" \ --download-dir=$HOME/.cac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
