# vllm-project/vllm#27649: [Usage]: Qwen3-32B on RTX PRO 6000 (55s First Token Delay and 15t/s)

| 字段 | 值 |
| --- | --- |
| Issue | [#27649](https://github.com/vllm-project/vllm/issues/27649) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Qwen3-32B on RTX PRO 6000 (55s First Token Delay and 15t/s)

### Issue 正文摘录

Why does the Qwen3-32B model take 55 seconds before producing the first token, and why is the generation speed only 15t/s? My vLLM configuration: Device: GB202GL [RTX PRO 6000 Blackwell Server Edition] Nvidia Driver Version：580.95.05 CUDA Version：13.0 Docker configuration: ```sh PORT=8085 MODEL_PATH=Qwen/Qwen3-32B SERVED_MODEL_NAME=vLLM-Qwen3-32B docker run -d \ --runtime nvidia \ --gpus all \ -v /data/projects/docker/vllm/.cache/huggingface:/root/.cache/huggingface \ -p $PORT:8000 \ --env "HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN" \ --name $SERVED_MODEL_NAME \ --restart unless-stopped \ --ipc=host \ vllm/vllm-openai:v0.11.0 \ --model /root/.cache/huggingface/$MODEL_PATH \ --served-model-name $SERVED_MODEL_NAME \ --dtype bfloat16 \ --gpu-memory-utilization 0.92 \ --max-model-len 32768 \ --max-num-seqs 64 \ --tensor-parallel-size 1 \ --api-key sk-vx023nmlrtTmlC ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: /s) usage;stale Why does the Qwen3-32B model take 55 seconds before producing the first token, and why is the generation speed only 15t/s? My vLLM configuration: Device: GB202GL [RTX PRO 6000 Blackwell Server Edition] N...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Qwen3-32B on RTX PRO 6000 (55s First Token Delay and 15t/s) usage;stale Why does the Qwen3-32B model take 55 seconds before producing the first token, and why is the generation speed only 15t/s? My vLLM configu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: huggingface/$MODEL_PATH \ --served-model-name $SERVED_MODEL_NAME \ --dtype bfloat16 \ --gpu-memory-utilization 0.92 \ --max-model-len 32768 \ --max-num-seqs 64 \ --tensor-parallel-size 1 \ --api-key sk-vx023nmlrtTmlC ``...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: Qwen3-32B on RTX PRO 6000 (55s First Token Delay and 15t/s) usage;stale Why does the Qwen3-32B model take 55 seconds before producing the first token, and why is the generation speed only 15t/s? My vLLM configu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sage]: Qwen3-32B on RTX PRO 6000 (55s First Token Delay and 15t/s) usage;stale Why does the Qwen3-32B model take 55 seconds before producing the first token, and why is the generation speed only 15t/s? My vLLM configura...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
