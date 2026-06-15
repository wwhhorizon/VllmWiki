# vllm-project/vllm#28467: [Bug]: Persistent CPU RAM Growth and Container Restarts with QWEN2-2B on SageMaker, Unaffected by Cache Settings

| 字段 | 值 |
| --- | --- |
| Issue | [#28467](https://github.com/vllm-project/vllm/issues/28467) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Persistent CPU RAM Growth and Container Restarts with QWEN2-2B on SageMaker, Unaffected by Cache Settings

### Issue 正文摘录

### Your current environment We are using [this](https://gallery.ecr.aws/deep-learning-containers/vllm) image with 0.11.0 vLLM version and 1.7 sagemaker version: Image URI: public.ecr.aws/deep-learning-containers/vllm:0.11.0-gpu-py312-cu128-ubuntu22.04-sagemaker-v1.7 [Release](https://github.com/aws/deep-learning-containers/releases/tag/v1.7-vllm-sagemaker-0.11.0-gpu-py312) We are using the default ENV values but we are also using the following: - name: "SM_VLLM_MAX_MODEL_LEN" value: "12000" - name: "SM_VLLM_LIMIT_MM_PER_PROMPT" value: '{"image":6, "video":0}' - name: "SM_VLLM_MODEL" value: "/opt/ml/model/qwen2_W4A16" - name: "SM_VLLM_MM_PROCESSOR_CACHE_GB" value: "0" ### 🐛 Describe the bug When serving QWEN2-2B with vLLM on AWS SageMaker (g6e.xlarge, 32GB RAM), we see persistent CPU RAM growth leading to container restarts during normal inference workloads. This occurs regardless of cache configuration (--mm-processor-cache-type SHM/LRU, with default or custom --mm-processor-cache-gb, and with cache entirely disabled). * RAM Usage: Memory usage increases steadily with requests (seen with both 4GB and 8GB cache values) and RAM is not freed post-inference. * Container Restarts: End...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Persistent CPU RAM Growth and Container Restarts with QWEN2-2B on SageMaker, Unaffected by Cache Settings bug;unstale ### Your current environment We are using [this](https://gallery.ecr.aws/deep-learning-contain...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ing the default ENV values but we are also using the following: - name: "SM_VLLM_MAX_MODEL_LEN" value: "12000" - name: "SM_VLLM_LIMIT_MM_PER_PROMPT" value: '{"image":6, "video":0}' - name: "SM_VLLM_MODEL" value: "/opt/m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Restarts with QWEN2-2B on SageMaker, Unaffected by Cache Settings bug;unstale ### Your current environment We are using [this](https://gallery.ecr.aws/deep-learning-containers/vllm) image with 0.11.0 vLLM version and 1....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: dpoint server restarts around 60–65% total RAM consumed. * Model Choice: Reproduced with QWEN2-2B (multimodal enabled) and text-only pipelines. * vLLM Version: We are using the latest stable release. Expected: RAM usage...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ://gallery.ecr.aws/deep-learning-containers/vllm) image with 0.11.0 vLLM version and 1.7 sagemaker version: Image URI: public.ecr.aws/deep-learning-containers/vllm:0.11.0-gpu-py312-cu128-ubuntu22.04-sagemaker-v1.7 [Rele...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
