# vllm-project/vllm#12539: [Bug]: Deepseek models for L4 GPU not working

| 字段 | 值 |
| --- | --- |
| Issue | [#12539](https://github.com/vllm-project/vllm/issues/12539) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek models for L4 GPU not working

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug First of all, thanks a lot for adding supports of these new models so quickly. It is a great community and thanks a lot to all the maintainers and contributors. I have searched through the discussion and issues but couldn't find anything similar. So here I am creating a new issue. I am trying to run the DeepSeek's distilled models into my L4 GPU (96 GB). I am always facing `torch.OutOfMemoryError: CUDA out of memory.` error. Here is my docker-compose.yml file: ```yml services: llm-server: container_name: deepseek image: vllm/vllm-openai:v0.7.0 runtime: nvidia deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [ gpu ] ports: - "4200:8000" volumes: - hf_cache:/root/.cache/huggingface environment: - HUGGING_FACE_HUB_TOKEN=${HF_TOKEN} - NCCL_SHM_DISABLE=1 entrypoint: [ "vllm", "serve", "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", "--tensor-parallel-size", "4", "--max-model-len", "32768", "--enforce-eager" ] restart: always volumes: hf_cache: ``` Here is the detailed error I got: As far as I am able to understand, for some reason the vLLM [engine.py](https://github.c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Deepseek models for L4 GPU not working bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug First of all, thanks a lot for adding supports of these new models so quickly. It...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: un the DeepSeek's distilled models into my L4 GPU (96 GB). I am always facing `torch.OutOfMemoryError: CUDA out of memory.` error. Here is my docker-compose.yml file: ```yml services: llm-server: container_name: deepsee...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;na...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nity and thanks a lot to all the maintainers and contributors. I have searched through the discussion and issues but couldn't find anything similar. So here I am creating a new issue. I am trying to run the DeepSeek's d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e.py#L375) file is not using all the GPUs for `MQLLMEngine`. Is anybody else facing the same issue? I have tried this yaml file for all the different distilled models but none of them are working but this configuration...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
