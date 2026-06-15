# vllm-project/vllm#36315: [Bug]: AttributeError: 'Qwen3_5TextConfig' object has no attribute 'max_window_layers'

| 字段 | 值 |
| --- | --- |
| Issue | [#36315](https://github.com/vllm-project/vllm/issues/36315) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Qwen3_5TextConfig' object has no attribute 'max_window_layers'

### Issue 正文摘录

### Your current environment vllm 0.17.0 lastest. ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=1,2 vllm serve /home/ub3960x/model_data/Qwen3.5-9B \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.80 \ --port 30005 \ --served-model-name qwen3.5-9b \ --max-model-len 16384 \ --reasoning-parser qwen3 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --trust-remote-code (APIServer pid=31946) INFO 03-07 14:45:02 [utils.py:302] (APIServer pid=31946) INFO 03-07 14:45:02 [utils.py:302] █ █ █▄ ▄█ (APIServer pid=31946) INFO 03-07 14:45:02 [utils.py:302] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.0 (APIServer pid=31946) INFO 03-07 14:45:02 [utils.py:302] █▄█▀ █ █ █ █ model /home/ub3960x/model_data/Qwen3.5-9B (APIServer pid=31946) INFO 03-07 14:45:02 [utils.py:302] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=31946) INFO 03-07 14:45:02 [utils.py:302] (APIServer pid=31946) INFO 03-07 14:45:02 [utils.py:238] non-default args: {'model_tag': '/home/ub3960x/model_data/Qwen3.5-9B', 'enable_auto_tool_choice': True, 'tool_call_parser': 'hermes', 'port': 30005, 'model': '/home/ub3960x/model_data/Qwen3.5-9B', 'trust_remote_code': True, 'max_model_len': 16384, 'served_model_name': ['qwen3.5-9b'], 'reasoning_parser...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: id=31946) INFO 03-07 14:45:02 [utils.py:302] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.0 (APIServer pid=31946) INFO 03-07 14:45:02 [utils.py:302] █▄█▀ █ █ █ █ model /home/ub3960x/model_data/Qwen3.5-9B (APIServer pid=31946) INFO 03...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Your current environment vllm 0.17.0 lastest. ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=1,2 vllm serve /home/ub3960x/model_data/Qwen3.5-9B \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.80 \ --port 30005 \ --...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: AttributeError: 'Qwen3_5TextConfig' object has no attribute 'max_window_layers' bug ### Your current environment vllm 0.17.0 lastest. ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=1,2 vllm serve /home/ub3960x/model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 54] Using max model len 16384 (APIServer pid=31946) INFO 03-07 14:45:02 [scheduler.py:231] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=31946) INFO 03-07 14:45:02 [vllm.py:747] Asynchronou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
