# vllm-project/vllm#27949: [Usage]: How do I deploy GGUF models with vLLM via Docker correct?

| 字段 | 值 |
| --- | --- |
| Issue | [#27949](https://github.com/vllm-project/vllm/issues/27949) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;import_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How do I deploy GGUF models with vLLM via Docker correct?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Here is the output from `sudo python3 collect_env.py` ``` Traceback (most recent call last): File "/export/nvme/vllm/collect_env.py", line 18, in import regex as re ModuleNotFoundError: No module named 'regex' ``` ### How would you like to use vllm I am using an Ubuntu 22.04 LTS LXC in Proxmox. I have Docker installed. I downloaded `https://huggingface.co/unsloth/DeepSeek-R1-Distill-Llama-70B-GGUF/resolve/main/DeepSeek-R1-Distill-Llama-70B-Q4_K_M.gguf?download=true` to `/export/nvme/huggingface/DeepSeek-R1-Distill-Llama-70B-GGUF/DeepSeek-R1-Distill-Llama-70B-Q4_K_M.gguf` via `wget`. The command that I am trying to use to start said Docker container is: ``` sudo docker run --runtime nvidia --gpus all \ --name vllm \ -v /export/nvme/huggingface/DeepSeek-R1-Distill-Llama-70B-Q4_K_M-GGUF:/root/.cache/huggingface/DeepSeek-R1-Distill-Llama-70B-Q4_K_M-GGUF \ -v /export/nvme/vllm:/export/nvme/vllm \ -e TRANSFORMERS_OFFLINE=1 \ --shm-size=16G \ -v /dev/shm:/dev/shm \ -p 0.0.0.0:8000:8000 \ --security-opt apparmor:unconfined \ vllm/vllm-openai:v0.8.5 \ --model /root/.cache/huggingface/DeepSeek-R1-Distill-Llama-70...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Usage]: How do I deploy GGUF models with vLLM via Docker correct? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` Here is the output from `sudo python3 collect_env.py` ``` Tra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: How do I deploy GGUF models with vLLM via Docker correct? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` Here is the output from `sudo python3 collect_env.py` ``` Tra...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=32768, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distri...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Usage]: How do I deploy GGUF models with vLLM via Docker correct? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` Here is the output from `sudo python3 collect_env.py` ``` Tra...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: oxmox. I have Docker installed. I downloaded `https://huggingface.co/unsloth/DeepSeek-R1-Distill-Llama-70B-GGUF/resolve/main/DeepSeek-R1-Distill-Llama-70B-Q4_K_M.gguf?download=true` to `/export/nvme/huggingface/DeepSeek...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
