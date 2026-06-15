# vllm-project/vllm#16777: [Bug]:  Could't deploy c4ai-command-a-03-2025 with VLLM docker

| 字段 | 值 |
| --- | --- |
| Issue | [#16777](https://github.com/vllm-project/vllm/issues/16777) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Could't deploy c4ai-command-a-03-2025 with VLLM docker

### Issue 正文摘录

### Your current environment - cuda 12.4 - works for other model like internVL, whisper and so on - the environment should be fine ### 🐛 Describe the bug - Use vllm 0.8.4 and 0.8.2. neither of them could deploy c4ai-command-a-03-2025 model (downloaded from hf) - deploy command for simple test `NVIDIA_VISIBLE_DEVICES=2,3 docker run --runtime nvidia -v /mnt/disk2/modelHub:/root/ -p 8099:8000 --ipc=host vllm/vllm-openai:v0.8.2 --model /root/llm/cohere/c4ai-command-a-03-2025 --enable-chunked-prefill --max-num-batched-tokens=2048 --max-num-seqs=128 -tp=2 --gpu-memory-utilization=0.95 --max-model-len=128000` ---- --- ERROR message ```shell NVIDIA_VISIBLE_DEVICES=2,3 docker run --runtime nvidia -v /mnt/disk2/modelHub:/root/ -p 8099:8000 --ipc=host vllm/vllm-openai:v0.8.2 --model /root/llm/cohere/c4ai-command-a-03-2025 --enable-chunked-prefill --max-num-batched-tokens=2048 --max-num-seqs=128 -tp=2 --gpu-memory-utilization=0.95 --max-model-len=128000 INFO 04-17 03:13:23 [__init__.py:239] Automatically detected platform cuda. INFO 04-17 03:13:25 [api_server.py:981] vLLM API server version 0.8.2 INFO 04-17 03:13:25 [api_server.py:982] args: Namespace(host=None, port=8000, uvicorn_log_level='...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: docker bug ### Your current environment - cuda 12.4 - works for other model like internVL, whisper and so on - the environment should be fine ### 🐛 Describe the bug - Use vllm 0.8.4 and 0.8.2. neither of them could depl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Could't deploy c4ai-command-a-03-2025 with VLLM docker bug ### Your current environment - cuda 12.4 - works for other model like internVL, whisper and so on - the environment should be fine ### 🐛 Describe the bug...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 8.2 --model /root/llm/cohere/c4ai-command-a-03-2025 --enable-chunked-prefill --max-num-batched-tokens=2048 --max-num-seqs=128 -tp=2 --gpu-memory-utilization=0.95 --max-model-len=128000` ---- --- ERROR message ```shell N...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=128000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: i-command-a-03-2025 with VLLM docker bug ### Your current environment - cuda 12.4 - works for other model like internVL, whisper and so on - the environment should be fine ### 🐛 Describe the bug - Use vllm 0.8.4 and 0.8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
