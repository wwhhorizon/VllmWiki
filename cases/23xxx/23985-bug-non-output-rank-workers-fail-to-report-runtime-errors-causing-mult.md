# vllm-project/vllm#23985: [Bug]: Non-output-rank Workers Fail to Report Runtime Errors, Causing MultiProcExecutor to Wait for RPC Timeout

| 字段 | 值 |
| --- | --- |
| Issue | [#23985](https://github.com/vllm-project/vllm/issues/23985) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Non-output-rank Workers Fail to Report Runtime Errors, Causing MultiProcExecutor to Wait for RPC Timeout

### Issue 正文摘录

### Your current environment npu environment Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] pyzmq==27.0.2 [pip3] torch==2.7.1+cpu [pip3] torch_npu==2.7.1.dev20250724 [pip3] torchvision==0.22.1 [pip3] transformers==4.55.3 [conda] Could not collect vLLM Version: 0.10.1.1 vLLM Ascend Version: 0.1.dev1+gb0403f8d8 (git sha: b0403f8d8) ### 🐛 Describe the bug When using MultiProcExecutor in a distributed vLLM setup, runtime errors (e.g., GPU/XPU failures) in non-output-rank workers are not properly reported to the executor. The current implementation only allows the output_rank worker to enqueue exceptions into the communication queue (worker_response_mq). For non-output-rank workers, if an error occurs during execute_model execution, the exception is not propagated to the queue. Additionally, other workers may get stuck in communication kernels (due to the failed non-output-rank worker) and do not throw exceptions either. This forces MultiProcExecutor to wait for the full RPC timeout (controlled by VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS) before detecting the failure—leading to long, unnecessary hangs and degraded service reliability. ### Before submitting a new issue... - [x] M...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rt Runtime Errors, Causing MultiProcExecutor to Wait for RPC Timeout bug;stale ### Your current environment npu environment Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] pyzmq==27.0.2 [pip3] torch==2.7.1+c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: for RPC Timeout bug;stale ### Your current environment npu environment Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] pyzmq==27.0.2 [pip3] torch==2.7.1+cpu [pip3] torch_npu==2.7.1.dev20250724 [pip3] torchvi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ty. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: onse_mq). For non-output-rank workers, if an error occurs during execute_model execution, the exception is not propagated to the queue. Additionally, other workers may get stuck in communication kernels (due to the fail...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
