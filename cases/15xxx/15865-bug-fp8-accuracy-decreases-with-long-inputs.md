# vllm-project/vllm#15865: [Bug]: FP8 accuracy decreases with long inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#15865](https://github.com/vllm-project/vllm/issues/15865) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 accuracy decreases with long inputs

### Issue 正文摘录

### Your current environment H100 NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 vllm0.7.2 ### 🐛 Describe the bug It is currently found that when the data length exceeds 8096, the accuracy will decrease, and when it is lower than this value, the accuracy is normal. Is there any way to optimize the effect of FP8? service startup script: ``` vllm serve ${MODEL_PATH} \ --host 0.0.0.0 \ --port 8081 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.85 \ --max-seq-len-to-capture 16384\ --max-num-seqs 512 \ --max-model-len 32768 \ --enable-chunked-prefill true \ --served-model-name llama_3_1_8b \ --device cuda \ --num_scheduler_steps 10 \ --quantization fp8 \ ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: uracy decreases with long inputs bug;stale ### Your current environment H100 NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 vllm0.7.2 ### 🐛 Describe the bug It is currently found that when the data le...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 accuracy decreases with long inputs bug;stale ### Your current environment H100 NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 vllm0.7.2 ### 🐛 Describe the bug It is cu
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: FP8 accuracy decreases with long inputs bug;stale ### Your current environment H100 NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 vllm0.7.2 ### 🐛 Describe the bug It is currently found that wh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Your current environment H100 NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 vllm0.7.2 ### 🐛 Describe the bug It is currently found that when the data length exceeds 8096, the accuracy will decrease,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: to optimize the effect of FP8? service startup script: ``` vllm serve ${MODEL_PATH} \ --host 0.0.0.0 \ --port 8081 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.85 \ --max-seq-len-to-capture 16384\ --max-num-s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
