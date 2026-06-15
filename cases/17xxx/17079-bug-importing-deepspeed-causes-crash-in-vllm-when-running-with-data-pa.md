# vllm-project/vllm#17079: [Bug]: Importing DeepSpeed causes crash in vLLM when running with data parallelism and TP=1

| 字段 | 值 |
| --- | --- |
| Issue | [#17079](https://github.com/vllm-project/vllm/issues/17079) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Importing DeepSpeed causes crash in vLLM when running with data parallelism and TP=1

### Issue 正文摘录

### Your current environment - DeepSpeed: v0.16.7 ### 🐛 Describe the bug When using vLLM with DeepSpeed imported, a crash occurs only when `tensor_parallel_size=1` and `data_parallel_size>1`. This does not happen in other configurations. Below is a minimal, reproducible example. It is a simplified version of [your DP example](https://docs.vllm.ai/en/stable/getting_started/examples/data_parallel.html). ```python import os from time import sleep from vllm import LLM from vllm.utils import get_open_port from multiprocessing import Process import deepspeed os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn" # seems necessary when importing deepspeed def main(dp_size, dp_rank, dp_master_port): os.environ["VLLM_DP_RANK"] = str(dp_rank) os.environ["VLLM_DP_RANK_LOCAL"] = str(dp_rank) os.environ["VLLM_DP_SIZE"] = str(dp_size) os.environ["VLLM_DP_MASTER_IP"] = "127.0.0.1" os.environ["VLLM_DP_MASTER_PORT"] = str(dp_master_port) LLM(model="ibm-research/PowerMoE-3b", tensor_parallel_size=1, enforce_eager=True, enable_expert_parallel=True) sleep(5) if __name__ == "__main__": dp_size = 2 dp_master_port = get_open_port() procs = [] for dp_rank in range(dp_size): proc = Process(target=main, args...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Importing DeepSpeed causes crash in vLLM when running with data parallelism and TP=1 bug;stale ### Your current environment - DeepSpeed: v0.16.7 ### 🐛 Describe the bug When using vLLM with DeepSpeed imported, a c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: uda (auto detect) INFO 04-23 21:31:08 [config.py:2832] Downcasting torch.float32 to torch.float16. INFO 04-23 21:31:09 [config.py:2832] Downcasting torch.float32 to torch.float16. INFO 04-23 21:31:21 [config.py:689] Thi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: eed causes crash in vLLM when running with data parallelism and TP=1 bug;stale ### Your current environment - DeepSpeed: v0.16.7 ### 🐛 Describe the bug When using vLLM with DeepSpeed imported, a crash occurs only when `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Importing DeepSpeed causes crash in vLLM when running with data parallelism and TP=1 bug;stale ### Your current environment - DeepSpeed: v0.16.7 ### 🐛 Describe the bug When using vLLM with DeepSpeed imported, a crash oc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rallel_size=1` and `data_parallel_size>1`. This does not happen in other configurations. Below is a minimal, reproducible example. It is a simplified version of [your DP example](https://docs.vllm.ai/en/stable/getting_s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
