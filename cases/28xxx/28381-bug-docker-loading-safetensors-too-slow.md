# vllm-project/vllm#28381: [Bug]: docker  Loading safetensors  too slow

| 字段 | 值 |
| --- | --- |
| Issue | [#28381](https://github.com/vllm-project/vllm/issues/28381) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8;gemm |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: docker  Loading safetensors  too slow

### Issue 正文摘录

Loading safetensors checkpoint shards: 0% Completed | 0/2 [00:00<?, ?it/s] ssd loads 20M/s, while comfyui loads 1G/s ![Image](https://github.com/user-attachments/assets/7e325462-5aab-423d-acf7-b577887c025c) ``` docker run --rm --name q1 ` --runtime nvidia ` --gpus "device=0" ` --ipc=host ` -v "m:\ComfyUI\ComfyUI\models\LLM\Qwen-VL\Qwen3-VL-4B-Instruct-FP8:/app/models/Qwen3-VL-4B-Instruct-FP8" ` -p 8000:8000 ` vllm/vllm-openai:latest ` --model /app/models/Qwen3-VL-4B-Instruct-FP8 ` --tensor-parallel-size 1 ` --swap-space 2 ` --limit-mm-per-prompt.video 0 ` --async-scheduling ` --gpu-memory-utilization 0.85 ` --max-num-seqs 128 ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e nvidia ` --gpus "device=0" ` --ipc=host ` -v "m:\ComfyUI\ComfyUI\models\LLM\Qwen-VL\Qwen3-VL-4B-Instruct-FP8:/app/models/Qwen3-VL-4B-Instruct-FP8" ` -p 8000:8000 ` vllm/vllm-openai:latest ` --model /app/models/Qwen3-V...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: docker Loading safetensors too slow bug;stale Loading safetensors checkpoint shards: 0% Completed | 0/2 [00:00<?, ?it/s] ssd loads 20M/s, while comfyui loads 1G/s ![Image](https://github.com/user-attachments/asse...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: =host ` -v "m:\ComfyUI\ComfyUI\models\LLM\Qwen-VL\Qwen3-VL-4B-Instruct-FP8:/app/models/Qwen3-VL-4B-Instruct-FP8" ` -p 8000:8000 ` vllm/vllm-openai:latest ` --model /app/models/Qwen3-VL-4B-Instruct-FP8 ` --tensor-paralle...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: docker Loading safetensors too slow bug;stale Loading safetensors checkpoint shards: 0% Completed | 0/2 [00:00<?, ?it/s] ssd loads 20M/s, while comfyui loads 1G/s ![Image](https://github.com/user-attachments/asse...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: _parallel;model_support;multimodal_vlm;quantization;scheduler_memory fp8;gemm slowdown dtype Loading safetensors checkpoint shards: 0% Completed | 0/2 [00:00<?, ?it/s]

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
