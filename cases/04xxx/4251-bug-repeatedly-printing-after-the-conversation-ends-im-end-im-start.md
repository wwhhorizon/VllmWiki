# vllm-project/vllm#4251: [Bug]: Repeatedly printing after the conversation ends<| im_end |><| im_start |>

| 字段 | 值 |
| --- | --- |
| Issue | [#4251](https://github.com/vllm-project/vllm/issues/4251) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Repeatedly printing after the conversation ends<\| im_end \|><\| im_start \|>

### Issue 正文摘录

### Your current environment ```text docker run --rm --runtime nvidia --gpus all --name vllm-qwen72b -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /data1/Download/models/Qwen-72B-Chat-Int4:/data/shared/Qwen/Qwen-Chat -p 8901:8000 --ipc=host \ vllm/vllm-openai:latest --model /data/shared/Qwen/Qwen-Chat --max-model-len 6400 --trust-remote-code --tensor-parallel-size 2 \ --gpu-memory-utilization 0.9 --served-model-name qwen72b --api-key "xxxx" ``` ### 🐛 Describe the bug I encountered an issue while running the model in Docker environment. The model is Qwen-72B and the conversation cannot end properly ![image](https://github.com/vllm-project/vllm/assets/70123250/15ef5a33-b5c8-4d5a-989e-ba0e3c773a7f)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: im_end |><| im_start |> bug;stale ### Your current environment ```text docker run --rm --runtime nvidia --gpus all --name vllm-qwen72b -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /data1/Download/models/Qwen-72...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /root/.cache/huggingface \ -v /data1/Download/models/Qwen-72B-Chat-Int4:/data/shared/Qwen/Qwen-Chat -p 8901:8000 --ipc=host \ vllm/vllm-openai:latest --model /data/shared/Qwen/Qwen-Chat --max-model-len 6400 --trust-remo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nment ```text docker run --rm --runtime nvidia --gpus all --name vllm-qwen72b -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /data1/Download/models/Qwen-72B-Chat-Int4:/data/shared/Qwen/Qwen-Chat -p 8901:8000 --ip...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tedly printing after the conversation ends<| im_end |><| im_start |> bug;stale ### Your current environment ```text docker run --rm --runtime nvidia --gpus all --name vllm-qwen72b -v ~/.cache/huggingface:/root/.cache/hu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: /Qwen/Qwen-Chat -p 8901:8000 --ipc=host \ vllm/vllm-openai:latest --model /data/shared/Qwen/Qwen-Chat --max-model-len 6400 --trust-remote-code --tensor-parallel-size 2 \ --gpu-memory-utilization 0.9 --served-model-name...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
