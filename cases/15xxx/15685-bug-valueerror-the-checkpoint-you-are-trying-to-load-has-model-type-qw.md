# vllm-project/vllm#15685: [Bug]: ValueError: The checkpoint you are trying to load has model type `qwen2_5_omni` but Transformers does not recognize this architecture.

| 字段 | 值 |
| --- | --- |
| Issue | [#15685](https://github.com/vllm-project/vllm/issues/15685) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;gemm;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: The checkpoint you are trying to load has model type `qwen2_5_omni` but Transformers does not recognize this architecture.

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/42d3756a-4ddf-4ece-bb68-62d44c38ff79) model: [https://github.com/QwenLM/Qwen2.5-Omni](https://github.com/QwenLM/Qwen2.5-Omni) ### 🐛 Describe the bug `(base) root@node15:/disk2/Qwen2.5-Omni-7B# nvidia-smi Fri Mar 28 15:17:15 2025 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 565.57.01 Driver Version: 565.57.01 CUDA Version: 12.7 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA L20 Off | 00000000:02:00.0 Off | 0 | | N/A 41C P0 80W / 350W | 37816MiB / 46068MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA L20 Off | 00000000:03:00.0 Off | 0 | | N/A 28C P8 26W / 350W | 14MiB / 46068MiB | 0% Default | | | | N/A | +-----------------------------------------+-------------------...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: ValueError: The checkpoint you are trying to load has model type `qwen2_5_omni` but Transformers does not recognize this architecture. bug;stale ### Your current environment ![Image](https://github.com/user-attac...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ----------------------------+ | NVIDIA-SMI 565.57.01 Driver Version: 565.57.01 CUDA Version: 12.7 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M |...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: qwen2_5_omni` but Transformers does not recognize this architecture. bug;stale ### Your current environment ![Image](https://github.com/user-attachments/assets/42d3756a-4ddf-4ece-bb68-62d44c38ff79) model: [https://githu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: -Omni-7B --tokenizer_mode="auto" --trust-remote-code --dtype=bfloat16 --max_num_seqs=256 --tensor_parallel_size=1 --gpu-memory-utilization=0.9 --max-model-len=32768 --limit-mm-per-prompt image=2 --served-model-name=Qwen...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
