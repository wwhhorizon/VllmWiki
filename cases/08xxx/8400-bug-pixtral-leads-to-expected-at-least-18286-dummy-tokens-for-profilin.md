# vllm-project/vllm#8400: [Bug]: Pixtral leads to Expected at least 18286 dummy tokens for profiling, but found 16640 tokens instead or seq_len 25254 should be equal to N_txt + N_img (806, 12224, 24448)

| 字段 | 值 |
| --- | --- |
| Issue | [#8400](https://github.com/vllm-project/vllm/issues/8400) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pixtral leads to Expected at least 18286 dummy tokens for profiling, but found 16640 tokens instead or seq_len 25254 should be equal to N_txt + N_img (806, 12224, 24448)

### Issue 正文摘录

### Your current environment H100 40GB ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=MIG-2ea01c20-8e9b-54a7-a91b-f308cd216a95"' \ --shm-size=10.24gb \ -p 5000:5000 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ \ -v "${HOME}"/.cache/huggingface:$HOME/.cache/huggingface \ -v "${HOME}"/.cache/huggingface/hub:$HOME/.cache/huggingface/hub \ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name pixtral \ vllm/vllm-openai:latest \ --port=5000 \ --host=0.0.0.0 \ --model=mistralai/Pixtral-12B-2409 \ --seed 1234 \ --tensor-parallel-size=1 \ --max-model-len=128000 \ --max-num-batched-tokens=512 \ --gpu-memory-utilization 0.98 \ --enable_chunked_prefill=True \ --enable-chunked-prefill=True \ --enforce-eager \ --tokenizer_mode mistral \ --limit_mm_per_prompt 'image=4' \ --max_num_batched_tokens 128000 --max-log-len=100 \ -...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: img (806, 12224, 24448) bug ### Your current environment H100 40GB ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=MIG-2ea01c20-8e9b-54a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 40GB ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=MIG-2ea01c20-8e9b-54a7-a91b-f308cd216a95"' \ --shm-size=10.24gb \ -p 5000:5000 \ -e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: s=512 \ --gpu-memory-utilization 0.98 \ --enable_chunked_prefill=True \ --enable-chunked-prefill=True \ --enforce-eager \ --tokenizer_mode mistral \ --limit_mm_per_prompt 'image=4' \ --max_num_batched_tokens 128000 --ma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: code=False, download_dir=None, load_format='auto', config_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=128000, guided_decoding_backend='outlines', distributed_executor_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: l to N_txt + N_img (806, 12224, 24448) bug ### Your current environment H100 40GB ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=MIG-2e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
