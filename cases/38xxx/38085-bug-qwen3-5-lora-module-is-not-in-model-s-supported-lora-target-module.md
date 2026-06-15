# vllm-project/vllm#38085: [Bug]: Qwen3.5 LoRA module is not in model's supported LoRA target modules

| 字段 | 值 |
| --- | --- |
| Issue | [#38085](https://github.com/vllm-project/vllm/issues/38085) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 LoRA module is not in model's supported LoRA target modules

### Issue 正文摘录

### Your current environment Env: Driver Version: 590.48.01 CUDA Version: 13.1 vllm: 0.18.1rc0+cu131 transformers: 4.57.6 torch: 2.10.0 ### 🐛 Describe the bug when I use vllm with multi-lora, I got "LoRA module xxx is not in the model's supported LoRA target modules". Why vllm can not support "in_proj_a, in_proj_b, gate_proj, up_proj, k_proj, q_proj, v_proj". my vllm script is: ``` vllm serve /home/xxx/Qwen3.5-27B \ --tensor-parallel-size 1 \ --reasoning-parser qwen3 \ --max-model-len 262144 \ --enable-prefix-caching \ --gpu-memory-utilization 0.9 \ --block-size 16 \ --port 8002 \ --enable-log-requests \ --enable-prompt-tokens-details \ --max-num-seqs 256 \ --max_log_len 128 \ --default-chat-template-kwargs '{"enable_thinking": false}' \ --served-model-name Qwen3.5-27B \ --enable-lora \ --max-lora-rank 64 \ --lora-modules /home/xxx/Q35-27B_lora ``` the vllm warning is: ``` (EngineCore pid=731496) WARNING 03-25 10:45:34 [worker_manager.py:153] LoRA module 'language_model.model.layers.0.linear_attn.in_proj_a' in adapter '/home/xxx/Qwen3.5-27B-lora/Q35-27B_lora_xxx' is not in the model's supported LoRA target modules [conv1d, down_proj, gate_up_proj, in_proj_ba, in_proj_qkv, in_proj_...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: -len 262144 \ --enable-prefix-caching \ --gpu-memory-utilization 0.9 \ --block-size 16 \ --port 8002 \ --enable-log-requests \ --enable-prompt-tokens-details \ --max-num-seqs 256 \ --max_log_len 128 \ --default-chat-tem...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ported LoRA target modules bug ### Your current environment Env: Driver Version: 590.48.01 CUDA Version: 13.1 vllm: 0.18.1rc0+cu131 transformers: 4.57.6 torch: 2.10.0 ### 🐛 Describe the bug when I use vllm with multi-lo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: modules bug ### Your current environment Env: Driver Version: 590.48.01 CUDA Version: 13.1 vllm: 0.18.1rc0+cu131 transformers: 4.57.6 torch: 2.10.0 ### 🐛 Describe the bug when I use vllm with multi-lora, I got "LoRA mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3.5 LoRA module is not in model's supported LoRA target modules bug ### Your current environment Env: Driver Version: 590.48.01 CUDA Version: 13.1 vllm: 0.18.1rc0+cu131 transformers: 4.57.6 torch: 2.10.0 ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pu-memory-utilization 0.9 \ --block-size 16 \ --port 8002 \ --enable-log-requests \ --enable-prompt-tokens-details \ --max-num-seqs 256 \ --max_log_len 128 \ --default-chat-template-kwargs '{"enable_thinking": false}' \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
