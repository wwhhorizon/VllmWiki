# vllm-project/vllm#7833: [Bug]: AI21-Jamba-1.5-Mini RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#7833](https://github.com/vllm-project/vllm/issues/7833) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | activation;cache;cuda;kernel;moe;operator;quantization;triton |
| 症状 | crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AI21-Jamba-1.5-Mini RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment vllm 0.5.5 H100 80GB Ubuntu. This says that at 100*1024 context one should be able to run this model with vLLM: https://huggingface.co/ai21labs/AI21-Jamba-1.5-Mini Using the quantization mentioned here: https://huggingface.co/ai21labs/AI21-Jamba-1.5-Mini#expertsint8-quantization However, it fails with illegal access. ### 🐛 Describe the bug ``` docker pull vllm/vllm-openai:latest docker stop jamba15mini ; docker remove jamba15mini docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=4"' \ --shm-size=10.24gb \ -p 5000:5000 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name jamba15mini \ vllm/vllm-openai:latest \ --port=5000 \ --host=0.0.0.0 \ --model=ai21labs/AI21-Jamba-1.5-Mini \ --seed 1234 \ --trust-remote-code \ --max-num-batched-tokens 102400 \ --max-model-len=102400 \ --quantization=experts_int8 \...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ion However, it fails with illegal access. ### 🐛 Describe the bug ``` docker pull vllm/vllm-openai:latest docker stop jamba15mini ; docker remove jamba15mini docker run -d --restart=always \ --runtime=nvidia \ --gpus '"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: untu. This says that at 100*1024 context one should be able to run this model with vLLM: https://huggingface.co/ai21labs/AI21-Jamba-1.5-Mini Using the quantization mentioned here: https://huggingface.co/ai21labs/AI21-Ja...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_specu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: th vLLM: https://huggingface.co/ai21labs/AI21-Jamba-1.5-Mini Using the quantization mentioned here: https://huggingface.co/ai21labs/AI21-Jamba-1.5-Mini#expertsint8-quantization However, it fails with illegal access. ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: AI21-Jamba-1.5-Mini RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered bug ### Your current environment vllm 0.5.5 H100 80GB Ubuntu. This says that at 100*1024 context one should be able...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
