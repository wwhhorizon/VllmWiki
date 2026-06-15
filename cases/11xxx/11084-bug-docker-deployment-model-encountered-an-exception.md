# vllm-project/vllm#11084: [Bug]: Docker deployment model encountered an exception

| 字段 | 值 |
| --- | --- |
| Issue | [#11084](https://github.com/vllm-project/vllm/issues/11084) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker deployment model encountered an exception

### Issue 正文摘录

### Your current environment docker vllm imags version: ``` vllm/vllm-openai latest 698668586297 3 weeks ago 10.6GB ``` nvidia-smi: ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.78 Driver Version: 550.78 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA GeForce RTX 4090 Off | 00000000:4B:00.0 Off | Off | | 30% 33C P8 22W / 450W | 7981MiB / 24564MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA GeForce RTX 4090 Off | 00000000:65:00.0 Off | Off | | 30% 28C P8 13W / 450W | 7981MiB / 24564MiB | 0% Default | | | | N/A | ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug docker run: ``` docker run --gpus all --ipc=host -p 8000:8000 -e VLLM_USE_MODELSCOPE=True vllm/vllm-openai --model=Qwen/Qwen2.5-7B-Instruct --tensor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Docker deployment model encountered an exception bug ### Your current environment docker vllm imags version: ``` vllm/vllm-openai latest 698668586297 3 week
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Docker deployment model encountered an exception bug ### Your current environment docker vllm imags version: ``` vllm/vllm-openai latest 698668586297 3 weeks ago 10.6GB `
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 698668586297 3 weeks ago 10.6GB ``` nvidia-smi: ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.78 Driver Version: 550.78 CUDA Version: 12.4 | |----------...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
