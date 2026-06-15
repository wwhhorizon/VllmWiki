# vllm-project/vllm#39093: [Bug] WSL2: Ctrl+C shows shutdown complete but requires pkill -9 (lingering processes)

| 字段 | 值 |
| --- | --- |
| Issue | [#39093](https://github.com/vllm-project/vllm/issues/39093) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] WSL2: Ctrl+C shows shutdown complete but requires pkill -9 (lingering processes)

### Issue 正文摘录

### Environment - OS: Windows 11 with WSL2 - WSL kernel: linux 6.6.87.2-microsoft-standard-WSL2 - vLLM version: 0.19.0 (from logs) - Model: Qwen/Qwen3.5-27B-FP8 - Python: 3.12 (virtualenv) - NCCL: nccl==2.27.5 (from logs) - Launch method: bash script (start_vllm_FP8.sh) running vLLM OpenAI-compatible API server ### Description On WSL2, pressing Ctrl+C triggers a seemingly clean shutdown (EngineCore reports \"Shutdown complete\" and FastAPI reports \"Application shutdown complete\"), but vLLM-related processes sometimes remain alive afterwards. To fully stop vLLM and return to a clean state, I have to manually run `pkill -9` on the remaining processes. This suggests SIGINT shutdown is not reliably tearing down all child/worker/distributed processes on WSL2, even though the high-level shutdown logs indicate success. ### Steps to Reproduce 1. Start vLLM API server on WSL2 (example model: `Qwen/Qwen3.5-27B-FP8`). 2. Wait for startup to complete (FastAPI prints `Application startup complete`). 3. Press Ctrl+C in the same terminal. 4. Observe shutdown logs claim completion. 5. Check running processes — some vLLM-related processes remain; I then manually kill them with `pkill -9`. ### Ex...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ux 6.6.87.2-microsoft-standard-WSL2 - vLLM version: 0.19.0 (from logs) - Model: Qwen/Qwen3.5-27B-FP8 - Python: 3.12 (virtualenv) - NCCL: nccl==2.27.5 (from logs) - Launch method: bash script (start_vllm_FP8.sh) running...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: even though the high-level shutdown logs indicate success. ### Steps to Reproduce 1. Start vLLM API server on WSL2 (example model: `Qwen/Qwen3.5-27B-FP8`). 2. Wait for startup to complete (FastAPI prints `Application st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 11 with WSL2 - WSL kernel: linux 6.6.87.2-microsoft-standard-WSL2 - vLLM version: 0.19.0 (from logs) - Model: Qwen/Qwen3.5-27B-FP8 - Python: 3.12 (virtualenv) - NCCL: nccl==2.27.5 (from logs) - Launch method: bash scrip...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: andard-WSL2 - vLLM version: 0.19.0 (from logs) - Model: Qwen/Qwen3.5-27B-FP8 - Python: 3.12 (virtualenv) - NCCL: nccl==2.27.5 (from logs) - Launch method: bash script (start_vllm_FP8.sh) running vLLM OpenAI-compatible A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: INFO: Started server process [13250] (APIServer pid=13250) INFO: Waiting for application startup. (APIServer pid=13250) INFO: Application startup complete. ^C(Worker_TP1 pid=15694) WARNING 04-06 17:17:54 [multiproc_exec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
