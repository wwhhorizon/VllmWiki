# vllm-project/vllm#14537: [Bug]: NCCL error when load model to 8*GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#14537](https://github.com/vllm-project/vllm/issues/14537) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NCCL error when load model to 8*GPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Load model successfully when TP=8 on A100. But on H200, load model successfully when TP=2, but failed when TP=8. and it failed to go through the vllm NCCL test on H200 ifollowing: https://docs.vllm.ai/en/latest/getting_started/troubleshooting.html#incorrect-hardware-driver [driver_nccl_test.log](https://github.com/user-attachments/files/19155376/driver_nccl_test.log) ```python from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/data/models/qwen25-72b", tensor_parallel_size=8) ``` [load_model_tp8_error.log](https://github.com/user-attachments/files/19155425/load_model_tp8_error.log) error key point: ``` DistBackendError: Error in model execution (input dumped to [/tmp/err_execute_model_input_20250310-040324.pkl](https://runai.kr1a.coupang.net/tmp/err_execute_model_input_20250310-040324.pkl)): NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:317, unhandled system error (run with NCCL_DEBUG=INFO for details), NCCL version 2.21.5 ncclSystemError: System call (e.g. socket, malloc) or external library call failed or device error. Last error: Error while creatin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: er-attachments/files/19155376/driver_nccl_test.log) ```python from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/data/models/qwen25-72b", tensor_parallel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ronment ### 🐛 Describe the bug Load model successfully when TP=8 on A100. But on H200, load model successfully when TP=2, but failed when TP=8. and it failed to go through the vllm NCCL test on H200 ifollowing: https://...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ents/files/19155425/load_model_tp8_error.log) error key point: ``` DistBackendError: Error in model execution (input dumped to [/tmp/err_execute_model_input_20250310-040324.pkl](https://runai.kr1a.coupang.net/tmp/err_ex...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: NCCL error when load model to 8*GPU bug;stale ### Your current environment ### 🐛 Describe the bug Load model successfully when TP=8 on A100. But on H200, load model successfully when TP=2, but failed when TP=8. a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: NCCL error when load model to 8*GPU bug;stale ### Your current environment ### 🐛 Describe the bug Load model successfully when TP=8 on A100. But on H200, load model successfully when TP=2, but failed when TP=8. a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
