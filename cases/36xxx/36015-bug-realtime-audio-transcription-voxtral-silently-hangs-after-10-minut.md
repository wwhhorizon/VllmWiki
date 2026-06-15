# vllm-project/vllm#36015: [Bug]: Realtime audio transcription (Voxtral) silently hangs after ~10 minutes due to unhandled TimeoutError in background task

| 字段 | 值 |
| --- | --- |
| Issue | [#36015](https://github.com/vllm-project/vllm/issues/36015) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cache |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Realtime audio transcription (Voxtral) silently hangs after ~10 minutes due to unhandled TimeoutError in background task

### Issue 正文摘录

### 🐛 Describe the bug When streaming audio chunks to a realtime model (Voxtral) using the `vllm/vllm-openai:nightly` Docker image, the server completely stops sending transcription results after about 10 minutes of continuous streaming. The connection remains open, the client keeps sending audio, but no output tokens are received and no errors are logged on the server side. It results in a silent deadlock. ### Steps to Reproduce **1. Build the custom Docker image:** Create a `Dockerfile` to add the necessary audio dependencies: ```dockerfile FROM vllm/vllm-openai:nightly RUN pip install "mistral-common[soundfile]" soundfile ``` Build the image: ```bash docker build -t vllm-voxtral-audio . ``` **2. Run the vLLM server:** Start the container with the `mistralai/Voxtral-Mini-4B-Realtime-2602` model on an RTX 5090: ```bash docker run --rm --gpus all \ --shm-size=4g \ -p 8000:8000 \ -v ~/.cache/huggingface:/hf \ -e HF_HUB_OFFLINE=1 \ -e VLLM_DISABLE_COMPILE_CACHE=1 \ -e HF_HOME=/hf \ vllm-voxtral-audio \ --model mistralai/Voxtral-Mini-4B-Realtime-2602 \ --tokenizer-mode mistral \ --config-format mistral \ --load-format mistral \ --trust-remote-code \ --compilation-config '{"cudagraph_...

## 现有链接修复摘要

#36089 [Bugfix] Handle TimeoutError in Voxtral buffer_realtime_audio to prevent silent hang

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: hunks to a realtime model (Voxtral) using the `vllm/vllm-openai:nightly` Docker image, the server completely stops sending transcription results after about 10 minutes of continuous streaming. The connection remains ope...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: sk bug ### 🐛 Describe the bug When streaming audio chunks to a realtime model (Voxtral) using the `vllm/vllm-openai:nightly` Docker image, the server completely stops sending transcription results after about 10 minutes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ived and no errors are logged on the server side. It results in a silent deadlock. ### Steps to Reproduce **1. Build the custom Docker image:** Create a `Dockerfile` to add the necessary audio dependencies: ```dockerfil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: container with the `mistralai/Voxtral-Mini-4B-Realtime-2602` model on an RTX 5090: ```bash docker run --rm --gpus all \ --shm-size=4g \ -p 8000:8000 \ -v ~/.cache/huggingface:/hf \ -e HF_HUB_OFFLINE=1 \ -e VLLM_DISABLE_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: oposed Solution: Wrap the `input_stream.get()` call in a `try...except` block to gracefully handle the `TimeoutError` and other potential exceptions, allowing the task to either continue waiting or cleanly abort the ses...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36089](https://github.com/vllm-project/vllm/pull/36089) | closes_keyword | 0.95 | [Bugfix] Handle TimeoutError in Voxtral buffer_realtime_audio to prevent silent hang | Fixes #36015 The `feed_tokens` background task in `buffer_realtime_audio` uses `asyncio.wait_for` with a timeout to fetch output tokens from the engine. When the engine iteration |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
