# vllm-project/vllm#10439: [Bug]: Unable to run Qwen2.5-0.5B-Instruct model in v0.6.4.post1 version, Error: No available memory for the cache blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#10439](https://github.com/vllm-project/vllm/issues/10439) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to run Qwen2.5-0.5B-Instruct model in v0.6.4.post1 version, Error: No available memory for the cache blocks

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Unique variable When I revert back to the v0.6.3 version image, this model can run successfully. ### GPU info ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA H800 PCIe Off | 00000000:93:00.0 Off | 0 | | N/A 86C P0 128W / 350W | 37789MiB / 81559MiB | 0% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ +-----------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=========================================================================================| | 0 N/A N/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Unable to run Qwen2.5-0.5B-Instruct model in v0.6.4.post1 version, Error: No available memory for the cache blocks bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### U...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Unable to run Qwen2.5-0.5B-Instruct model in v0.6.4.post1 version, Error: No available memory for the cache blocks bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### U...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=512, guided_decoding_backend='outlines', distributed_executor_bac...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: model in v0.6.4.post1 version, Error: No available memory for the cache blocks bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Unique variable When I revert back to the v0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
