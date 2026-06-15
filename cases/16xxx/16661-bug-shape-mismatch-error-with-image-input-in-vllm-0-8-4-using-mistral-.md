# vllm-project/vllm#16661: [Bug]: Shape Mismatch Error with Image Input in vLLM 0.8.4 using Mistral-Small-3.1-24B-Instruct-2503

| 字段 | 值 |
| --- | --- |
| Issue | [#16661](https://github.com/vllm-project/vllm/issues/16661) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;model_support;multimodal_vlm |
| 子分类 | shape_align |
| Operator 关键词 | gemm |
| 症状 | mismatch |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Shape Mismatch Error with Image Input in vLLM 0.8.4 using Mistral-Small-3.1-24B-Instruct-2503

### Issue 正文摘录

### Docker Command ``` docker run --runtime nvidia --gpus all --shm-size 1g -v /mnt/models/:/mnt/models/ -p 8080:8080 --ipc=host vllm/vllm-openai:v0.8.4 --port 8080 --model /mnt/models/mistralai/Mistral-Small-3.1-24B-Instruct-2503 --served-model-name test --limit_mm_per_prompt 'image=10' --tensor-parallel-size 2 --max-model-len 16384 --disable-mm-preprocessor-cache ``` ### 🐛 Describe the bug I am encountering a `RuntimeError` related to a shape mismatch when using the Mistral-Small-3.1-24B-Instruct-2503 model with image inputs in vLLM 0.8.4. **The error does not occur in vLLM 0.8.3**, indicating a potential regression in the latest version. ### Error Message ``` RuntimeError: shape mismatch: value tensor of shape [4, 5120] cannot be broadcast to indexing result of shape [16, 5120] ``` ### Expected Behavior The model should process the image input without any shape mismatch errors, as it does in vLLM 0.8.3. ### Actual Behavior A RuntimeError occurs due to a shape mismatch between the value tensor and the indexing result. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ut in vLLM 0.8.4 using Mistral-Small-3.1-24B-Instruct-2503 bug;stale ### Docker Command ``` docker run --runtime nvidia --gpus all --shm-size 1g -v /mnt/models/:/mnt/models/ -p 8080:8080 --ipc=host vllm/vllm-openai:v0.8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ommand ``` docker run --runtime nvidia --gpus all --shm-size 1g -v /mnt/models/:/mnt/models/ -p 8080:8080 --ipc=host vllm/vllm-openai:v0.8.4 --port 8080 --model /mnt/models/mistralai/Mistral-Small-3.1-24B-Instruct-2503...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Shape Mismatch Error with Image Input in vLLM 0.8.4 using Mistral-Small-3.1-24B-Instruct-2503 bug;stale ### Docker Command ``` docker run --runtime nvidia --gpus all --shm-size 1g -v /mnt/models/:/mnt/models/ -p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: models/mistralai/Mistral-Small-3.1-24B-Instruct-2503 --served-model-name test --limit_mm_per_prompt 'image=10' --tensor-parallel-size 2 --max-model-len 16384 --disable-mm-preprocessor-cache ``` ### 🐛 Describe the bug I...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Shape Mismatch Error with Image Input in vLLM 0.8.4 using Mistral-Small-3.1-24B-Instruct-2503 bug;stale ### Docker Command ``` docker run --runtime nvidia --gpus all --shm-size 1g -v /mnt/models/:/mnt/models/ -p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
