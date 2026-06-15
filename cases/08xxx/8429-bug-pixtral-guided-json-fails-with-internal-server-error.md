# vllm-project/vllm#8429: [Bug]: Pixtral + guided_json fails with Internal Server Error

| 字段 | 值 |
| --- | --- |
| Issue | [#8429](https://github.com/vllm-project/vllm/issues/8429) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | kernel_eff |
| Operator 关键词 | triton |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pixtral + guided_json fails with Internal Server Error

### Issue 正文摘录

### Your current environment ``` docker pull vllm/vllm-openai:latest docker stop pixtral ; docker remove pixtral docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=MIG-2ea01c20-8e9b-54a7-a91b-f308cd216a95"' \ --shm-size=10.24gb \ -p 5001:5001 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ \ -v "${HOME}"/.cache/huggingface:$HOME/.cache/huggingface \ -v "${HOME}"/.cache/huggingface/hub:$HOME/.cache/huggingface/hub \ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name pixtral \ vllm/vllm-openai:latest \ --port=5001 \ --host=0.0.0.0 \ --model=mistralai/Pixtral-12B-2409 \ --seed 1234 \ --tensor-parallel-size=1 \ --gpu-memory-utilization 0.98 \ --enforce-eager \ --tokenizer_mode mistral \ --limit_mm_per_prompt 'image=8' \ --max-model-len=32768 \ --max-num-batched-tokens=32768 \ --max-log-len=100 \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.pixtral.txt ``` All...

## 现有链接修复摘要

#8521 [Misc][Bugfix] Disable guided decoding for mistral tokenizer

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ \ -v "${HOME}"/.cache/huggingface:$HOME/.cache/huggingface \ -v "${HOME}"/.cache/huggingface/hub:$HOME/.cache/huggingface/hub \ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n fails with Internal Server Error bug ### Your current environment ``` docker pull vllm/vllm-openai:latest docker stop pixtral ; docker remove pixtral docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uggingface/hub \ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name pixtral \ vllm/vllm-openai:latest \ --port=5001 \ --host=0.0.0.0 \ --model=mistralai/Pixtral-12B-2409 \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ve. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: } } messages = [{'role': 'user', 'content': prompt}] stream = False client_kwargs = dict(model='mistralai/Pixtral-12B-2409', max_tokens=2048, stream=stream, messages=messages, response_format=dict(type='json_object'), e...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8521](https://github.com/vllm-project/vllm/pull/8521) | closes_keyword | 0.95 | [Misc][Bugfix] Disable guided decoding for mistral tokenizer | FIX #8429 cc @patrickvonplaten --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
