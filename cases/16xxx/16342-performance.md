# vllm-project/vllm#16342: [Performance]:

| 字段 | 值 |
| --- | --- |
| Issue | [#16342](https://github.com/vllm-project/vllm/issues/16342) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;quantization |
| 症状 | oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]:

### Issue 正文摘录

### Proposal to improve performance When running the vllm Docker container with version v0.8.3, a CUDA out of memory error occurs, while version v0.6.3 runs without issues on an A100 80GB GPU. The error message indicates that the GPU runs out of memory during the warm-up phase, specifically when handling 1024 dummy requests. The model in question is Qwen2.5-14B-Instruct-AWQ, and the Docker command used is as follows: docker run --rm \ --name Qwen2.5-14B-Instruct-AWQ \ --runtime nvidia \ --gpus all \ -v /ai/model/model/:/models \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:v0.8.3 \ --served-model-name Qwen2.5-14B-Instruct-AWQ \ --max-model-len 4096 \ --trust-remote-code \ --gpu-memory-utilization 0.99 \ --model /models/Qwen2.5-14B-Instruct-AWQ The performance of version 0.8.3 is not as good as that of version 0.6.3. reuslt as below： vllm version mdoel ttfs throughput GPU Utilization vllm 0.8.3 Qwen2.5-7B-Instruct 0.062856206 91.79787982 0.85-0.92 vllm 0.6.3 Qwen2.5-7B-Instruct 0.045440826 103.2321574 0.94 env use： ![Image](https://github.com/user-attachments/assets/7427f96d-d173-45d6-9977-6604c19cd8c5) ### Report of performance regression _No response_ ### Misc discussion on perfo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ormance;stale ### Proposal to improve performance When running the vllm Docker container with version v0.8.3, a CUDA out of memory error occurs, while version v0.6.3 runs without issues on an A100 80GB GPU. The error me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rformance When running the vllm Docker container with version v0.8.3, a CUDA out of memory error occurs, while version v0.6.3 runs without issues on an A100 80GB GPU. The error message indicates that the GPU runs out of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: lm version mdoel ttfs throughput GPU Utilization vllm 0.8.3 Qwen2.5-7B-Instruct 0.062856206 91.79787982 0.85-0.92 vllm 0.6.3 Qwen2.5-7B-Instruct 0.045440826 103.2321574 0.94 env use： ![Image](
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g the warm-up phase, specifically when handling 1024 dummy requests. The model in question is Qwen2.5-14B-Instruct-AWQ, and the Docker command used is as follows: docker run --rm \ --name Qwen2.5-14B-Instruct-AWQ \ --ru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: performance;stale ### Proposal to improve performance When running the vllm Docker container with version v0.8.3, a CUDA out of memory error occurs, while version v0.6.3 runs without issues on an A100 80G...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
