# vllm-project/vllm#22982: [Bug]: vllm0.8.5.post1相比0.6.3.post1推理qwen2-vl-3b和internvl3-1b速度差异大，推理指标也有一定降低，可能是哪方面问题？

| 字段 | 值 |
| --- | --- |
| Issue | [#22982](https://github.com/vllm-project/vllm/issues/22982) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.8.5.post1相比0.6.3.post1推理qwen2-vl-3b和internvl3-1b速度差异大，推理指标也有一定降低，可能是哪方面问题？

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1. 启动命令一样、代码一样、数据一样、机器平台一样，差异只是不同docker，v0.8.5的docker是在v0.6.3的docker上升级了vllm。 `CUDA_VISIBLE_DEVICES=1 nohup vllm serve checkpoint-24280 --trust-remote-code --port 8013 --dtype bfloat16 --gpu-memory-utilization 0.8 --max-num-batched-tokens 32768 --max-num-seqs 550 --max-model-len 4096 > log_v10 2>&1 &` 2. v0.8.5推理需要769.07 s `vlm infer, processing: 100%|███████████████████████████████████████████████████| 8670/8670 [12:24<00:00, 11.64it/s] INFO:__main__:VLM infer finished, total time: 769.07 seconds INFO:__main__:time cost per image: 0.09 seconds` 3. v0.6.3推理需要390s `vlm infer, processing: 100%|█████████████████████████████████████████████████████████████| 8670/8670 [06:04<00:00, 23.77it/s] INFO:__main__:VLM infer finished, total time: 390.18 seconds INFO:__main__:time cost per image: 0.05 seconds` 4. 0.8.5版本推理时，模型输出的指标低一些，错误格式也会多一些。 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vllm0.8.5.post1相比0.6.3.post1推理qwen2-vl-3b和internvl3-1b速度差异大，推理指标也有一定降低，可能是哪方面问题？ bug ### Your current environment ### 🐛 Describe the bug 1. 启动命令一样、代码一样、数据一样、机器平台一样，差异只是不同docker，v0.8.5的docker是在v0.6.3的docker上升级了vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: environment ### 🐛 Describe the bug 1. 启动命令一样、代码一样、数据一样、机器平台一样，差异只是不同docker，v0.8.5的docker是在v0.6.3的docker上升级了vllm。 `CUDA_VISIBLE_DEVICES=1 nohup vllm serve checkpoint-24280 --trust-remote-code --port 8013 --dtype bfloat16...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ES=1 nohup vllm serve checkpoint-24280 --trust-remote-code --port 8013 --dtype bfloat16 --gpu-memory-utilization 0.8 --max-num-batched-tokens 32768 --max-num-seqs 550 --max-model-len 4096 > log_v10 2>&1 &` 2. v0.8.5推理需要...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 令一样、代码一样、数据一样、机器平台一样，差异只是不同docker，v0.8.5的docker是在v0.6.3的docker上升级了vllm。 `CUDA_VISIBLE_DEVICES=1 nohup vllm serve checkpoint-24280 --trust-remote-code --port 8013 --dtype bfloat16 --gpu-memory-utilization 0.8 --max-num-b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
