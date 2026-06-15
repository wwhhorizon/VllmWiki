# vllm-project/vllm#17832: [Bug]: Inconsistent Output: First API call differs from subsequent identical calls with temperature=0 on Qwen models

| 字段 | 值 |
| --- | --- |
| Issue | [#17832](https://github.com/vllm-project/vllm/issues/17832) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;sampling |
| 症状 | nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inconsistent Output: First API call differs from subsequent identical calls with temperature=0 on Qwen models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are observing inconsistent output behavior when using vLLM (v0.8.1 via vllm/vllm-openai:v0.8.1 Docker image) to serve Qwen-based models (specifically tested with DeepSeek-R1-Distill-Qwen-32B and Qwen2.5-72B-Instruct). When sending multiple identical API requests with temperature: 0, the response from the very first request differs from the responses of subsequent requests (2nd, 3rd, etc.). The responses from the 2nd request onwards are consistent with each other. This behavior is unexpected, especially with temperature: 0, which should ideally lead to deterministic outputs for identical inputs. Environment: vLLM Version: v0.8.1 (from Docker image vllm/vllm-openai:v0.8.1) Model(s) Affected: DeepSeek-R1-Distill-Qwen-32B Qwen2.5-72B-Instruct (exhibits the same issue) Deployment Method: Docker GPU Configuration: 2 H100 GPUs (e.g., "device=4,5") Tensor Parallel Size: 2 Operating System: Ubuntu 11.4.0-1ubuntu1~22.04 NVIDIA Driver Version: 570.124.06 CUDA Version (inside Docker): 12.8 Steps to Reproduce: Deploy the model using vLLM. For example, with DeepSeek-R1-Distill-Qwen-32B: Bash sudo docker run -d \ --runtime nvidia \ --gpus '"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: tent output behavior when using vLLM (v0.8.1 via vllm/vllm-openai:v0.8.1 Docker image) to serve Qwen-based models (specifically tested with DeepSeek-R1-Distill-Qwen-32B and Qwen2.5-72B-Instruct). When sending multiple i...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: unexpected, especially with temperature: 0, which should ideally lead to deterministic outputs for identical inputs. Environment: vLLM Version: v0.8.1 (from Docker image vllm/vllm-openai:v0.8.1) Model(s) Affected: DeepS...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: (exhibits the same issue) Deployment Method: Docker GPU Configuration: 2 H100 GPUs (e.g., "device=4,5") Tensor Parallel Size: 2 Operating System: Ubuntu 11.4.0-1ubuntu1~22.04 NVIDIA Driver Version: 570.124.06 CUDA Versi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t API call differs from subsequent identical calls with temperature=0 on Qwen models bug;stale ### Your current environment ### 🐛 Describe the bug We are observing inconsistent output behavior when using vLLM (v0.8.1 vi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rs from subsequent identical calls with temperature=0 on Qwen models bug;stale ### Your current environment ### 🐛 Describe the bug We are observing inconsistent output behavior when using vLLM (v0.8.1 via vllm/vllm-open...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
