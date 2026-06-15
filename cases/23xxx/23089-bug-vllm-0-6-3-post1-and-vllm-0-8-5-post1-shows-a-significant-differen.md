# vllm-project/vllm#23089: [Bug]: vLLM 0.6.3.post1 and vLLM 0.8.5.post1 shows a significant difference in inference speed when running qwen2-vl-3b and internvl3-1b. What could be the cause of this?"

| 字段 | 值 |
| --- | --- |
| Issue | [#23089](https://github.com/vllm-project/vllm/issues/23089) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: vLLM 0.6.3.post1 and vLLM 0.8.5.post1 shows a significant difference in inference speed when running qwen2-vl-3b and internvl3-1b. What could be the cause of this?"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **startup command and env** The startup command, code, data, and machine platform are all the same; the only difference is the Docker image. The v0.8.5 Docker was upgraded from the v0.6.3 Docker with a new vLLM version. **Startup command:** `CUDA_VISIBLE_DEVICES=1 nohup vllm serve checkpoint-24280 --trust-remote-code --port 8013 --dtype bfloat16 --gpu-memory-utilization 0.8 --max-num-batched-tokens 32768 --max-num-seqs 550 --max-model-len 4096 > log_v10 2>&1 &` **Inference with v0.8.5 takes 769.07 s** `vlm infer, processing: 100%|███████████████████████████████████████████████████| 8670/8670 [12:24<00:00, 11.64it/s] INFO:__main__:VLM infer finished, total time: 769.07 seconds INFO:__main__:time cost per image: 0.09 seconds ` **Inference with v0.6.3 takes 390 s** `vlm infer, processing: 100%|█████████████████████████████████████████████████████████████| 8670/8670 [06:04<00:00, 23.77it/s] INFO:__main__:VLM infer finished, total time: 390.18 seconds INFO:__main__:time cost per image: 0.05 seconds ` With version 0.8.5, the inference metrics are slightly lower, and there are more incorrectly formatted outputs. The inference speed diff...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 8.5.post1 shows a significant difference in inference speed when running qwen2-vl-3b and internvl3-1b. What could be the cause of this?" bug;stale ### Your current environment ### 🐛 Describe the bug **startup command an...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: data, and machine platform are all the same; the only difference is the Docker image. The v0.8.5 Docker was upgraded from the v0.6.3 Docker with a new vLLM version. **Startup command:** `CUDA_VISIBLE_DEVICES=1 nohup vll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ES=1 nohup vllm serve checkpoint-24280 --trust-remote-code --port 8013 --dtype bfloat16 --gpu-memory-utilization 0.8 --max-num-batched-tokens 32768 --max-num-seqs 550 --max-model-len 4096 > log_v10 2>&1 &` **Inference w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d from the v0.6.3 Docker with a new vLLM version. **Startup command:** `CUDA_VISIBLE_DEVICES=1 nohup vllm serve checkpoint-24280 --trust-remote-code --port 8013 --dtype bfloat16 --gpu-memory-utilization 0.8 --max-num-ba...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
